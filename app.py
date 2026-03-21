import os
import logging
from collections import Counter, defaultdict
from itertools import combinations
from urllib.parse import urlparse
from flask import Flask, request, jsonify, render_template, abort
from flask_sqlalchemy import SQLAlchemy

from config import Config
from models import db, Bookmark, ImportSession, Cluster
from deduplicator import normalize_url, deduplicate_bookmarks
from importer import detect_and_import
from categorizer import cluster_bookmarks
from research import get_worker

logger = logging.getLogger(__name__)


BOOKMARK_SORT_FIELDS = {
    "imported_at": Bookmark.imported_at,
    "created_at": Bookmark.created_at,
    "researched_at": Bookmark.researched_at,
    "title": Bookmark.title,
    "page_title": Bookmark.page_title,
    "url": Bookmark.url,
    "source": Bookmark.source,
    "research_status": Bookmark.research_status,
    "http_status": Bookmark.http_status,
}


def extract_domain(url):
    try:
        hostname = (urlparse(url).hostname or "").lower()
    except Exception:
        return ""
    if hostname.startswith("www."):
        hostname = hostname[4:]
    return hostname


def normalize_tag(tag):
    return str(tag or "").strip().lower()


def bookmark_tag_list(bookmark):
    return [tag for tag in (normalize_tag(tag) for tag in (bookmark.tags or [])) if tag]


def build_timeline(bookmarks, attr_name, limit=14):
    counts = Counter()
    for bookmark in bookmarks:
        stamp = getattr(bookmark, attr_name)
        if stamp:
            counts[stamp.date().isoformat()] += 1
    if not counts:
        return []
    return [{"day": day, "count": counts[day]} for day in sorted(counts)[-limit:]]


def build_analytics_payload(bookmarks, clusters):
    unique_bookmarks = [bookmark for bookmark in bookmarks if not bookmark.is_duplicate]
    domain_stats = defaultdict(lambda: {
        "count": 0,
        "done": 0,
        "failed": 0,
        "pending": 0,
        "running": 0,
        "skipped": 0,
        "sources": Counter(),
        "tags": Counter(),
    })
    tag_counter = Counter()
    source_counter = Counter()
    tag_pair_counter = Counter()
    cluster_counter = Counter()

    for bookmark in unique_bookmarks:
        domain = extract_domain(bookmark.url)
        if domain:
            domain_stats[domain]["count"] += 1
            status = bookmark.research_status or "pending"
            if status in {"done", "failed", "pending", "running", "skipped"}:
                domain_stats[domain][status] += 1
            if bookmark.source:
                domain_stats[domain]["sources"][bookmark.source] += 1

        tags = sorted(set(bookmark_tag_list(bookmark)))
        for tag in tags:
            tag_counter[tag] += 1
            if domain:
                domain_stats[domain]["tags"][tag] += 1
        for tag_a, tag_b in combinations(tags, 2):
            tag_pair_counter[(tag_a, tag_b)] += 1

        if bookmark.source:
            source_counter[bookmark.source] += 1
        if bookmark.cluster_id:
            cluster_counter[bookmark.cluster_id] += 1

    top_domains = []
    for domain, stats in sorted(domain_stats.items(), key=lambda item: (-item[1]["count"], item[0]))[:12]:
        top_domains.append({
            "domain": domain,
            "count": stats["count"],
            "done": stats["done"],
            "failed": stats["failed"],
            "pending": stats["pending"],
            "running": stats["running"],
            "top_source": stats["sources"].most_common(1)[0][0] if stats["sources"] else "",
            "top_tags": [tag for tag, _ in stats["tags"].most_common(3)],
        })

    top_tags = [{"tag": tag, "count": count} for tag, count in tag_counter.most_common(20)]
    top_sources = [{"source": source or "unknown", "count": count} for source, count in source_counter.most_common(12)]
    top_tag_pairs = [
        {"pair": [tag_a, tag_b], "label": f"{tag_a} + {tag_b}", "count": count}
        for (tag_a, tag_b), count in tag_pair_counter.most_common(12)
    ]
    top_clusters = []
    for cluster in sorted(clusters, key=lambda item: (-cluster_counter[item.id], item.name.lower()))[:12]:
        count = cluster_counter[cluster.id]
        if count:
            top_clusters.append({
                "id": cluster.id,
                "name": cluster.name,
                "count": count,
                "tags": cluster.tags or [],
            })

    untagged_count = sum(1 for bookmark in unique_bookmarks if not bookmark_tag_list(bookmark))
    uncategorized_count = sum(1 for bookmark in unique_bookmarks if bookmark.cluster_id is None)
    researched_count = sum(1 for bookmark in unique_bookmarks if bookmark.research_status == "done")
    duplicate_count = sum(1 for bookmark in bookmarks if bookmark.is_duplicate)
    failed_count = sum(1 for bookmark in unique_bookmarks if bookmark.research_status == "failed")

    opportunities = [
        {
            "label": "Untagged bookmarks",
            "count": untagged_count,
            "description": "Bookmarks without tags are harder to search and cluster.",
            "filters": {"tags": "__empty__"},
        },
        {
            "label": "Uncategorized bookmarks",
            "count": uncategorized_count,
            "description": "Bookmarks without a category cluster are good candidates for organization.",
            "filters": {"cluster_id": "none"},
        },
        {
            "label": "Failed research",
            "count": failed_count,
            "description": "These bookmarks need another research pass or manual cleanup.",
            "filters": {"research_status": "failed"},
        },
        {
            "label": "Duplicates",
            "count": duplicate_count,
            "description": "Duplicate URLs can be hidden or reviewed together.",
            "filters": {"duplicate_mode": "only"},
        },
    ]

    summary = {
        "unique_bookmarks": len(unique_bookmarks),
        "unique_domains": len(domain_stats),
        "tagged_bookmarks": len(unique_bookmarks) - untagged_count,
        "untagged_bookmarks": untagged_count,
        "categorized_bookmarks": len(unique_bookmarks) - uncategorized_count,
        "uncategorized_bookmarks": uncategorized_count,
        "researched_bookmarks": researched_count,
        "failed_bookmarks": failed_count,
        "duplicate_bookmarks": duplicate_count,
        "avg_tags_per_bookmark": round(sum(len(bookmark_tag_list(bookmark)) for bookmark in unique_bookmarks) / len(unique_bookmarks), 2) if unique_bookmarks else 0,
    }

    return {
        "summary": summary,
        "top_domains": top_domains,
        "top_tags": top_tags,
        "top_sources": top_sources,
        "top_clusters": top_clusters,
        "top_tag_pairs": top_tag_pairs,
        "import_timeline": build_timeline(unique_bookmarks, "imported_at"),
        "research_timeline": build_timeline(unique_bookmarks, "researched_at"),
        "opportunities": opportunities,
    }


def create_app(config_object=None):
    app = Flask(__name__)

    if config_object is None:
        app.config.from_object(Config)
    elif isinstance(config_object, dict):
        app.config.update(config_object)
    else:
        app.config.from_object(config_object)

    # Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # ------------------------------------------------------------------ #
    # Main page
    # ------------------------------------------------------------------ #
    @app.route("/")
    def index():
        return render_template("index.html")

    # ------------------------------------------------------------------ #
    # Import
    # ------------------------------------------------------------------ #
    @app.route("/api/import", methods=["POST"])
    def api_import():
        content = None
        filename = None
        source_type = None

        if request.content_type and "multipart/form-data" in request.content_type:
            f = request.files.get("file")
            if f:
                filename = f.filename
                try:
                    content = f.read().decode("utf-8", errors="replace")
                except Exception as exc:
                    return jsonify({"error": f"Could not read file: {exc}"}), 400
            else:
                content = request.form.get("content", "")
                filename = request.form.get("filename")
                source_type = request.form.get("source_type")
        else:
            data = request.get_json(silent=True) or {}
            content = data.get("content", "")
            filename = data.get("filename")
            source_type = data.get("source_type")

        if not content:
            return jsonify({"error": "No content provided"}), 400

        try:
            detected_format, raw_bookmarks = detect_and_import(content, filename=filename)
        except Exception as exc:
            return jsonify({"error": f"Import failed: {exc}"}), 400

        if source_type:
            detected_format = source_type

        # Deduplicate against themselves
        unique_bms, dup_bms = deduplicate_bookmarks(raw_bookmarks)

        # Check against DB for existing normalized URLs
        session_imported = 0
        session_duplicates = len(dup_bms)
        new_bookmark_objects = []

        # Gather all normalized URLs from unique candidates in one query
        norm_urls = [bm["normalized_url"] for bm in unique_bms]
        existing = {}
        if norm_urls:
            rows = Bookmark.query.filter(Bookmark.normalized_url.in_(norm_urls)).all()
            for row in rows:
                existing[row.normalized_url] = row.id

        for bm_data in unique_bms:
            norm = bm_data["normalized_url"]
            if norm in existing:
                session_duplicates += 1
            else:
                bm = Bookmark(
                    url=bm_data.get("url", ""),
                    normalized_url=norm,
                    title=bm_data.get("title", ""),
                    description=bm_data.get("description", ""),
                    tags=bm_data.get("tags") or [],
                    source=detected_format,
                    created_at=bm_data.get("created_at"),
                    is_duplicate=False,
                    research_status="pending",
                )
                db.session.add(bm)
                new_bookmark_objects.append(bm)
                existing[norm] = None  # Mark as seen to avoid same-batch dups
                session_imported += 1

        # Also record DB-level duplicates from raw
        for bm_data in dup_bms:
            norm = bm_data["normalized_url"]
            orig_id = existing.get(norm)
            bm = Bookmark(
                url=bm_data.get("url", ""),
                normalized_url=norm,
                title=bm_data.get("title", ""),
                description=bm_data.get("description", ""),
                tags=bm_data.get("tags") or [],
                source=detected_format,
                created_at=bm_data.get("created_at"),
                is_duplicate=True,
                duplicate_of=orig_id if isinstance(orig_id, int) else None,
                research_status="skipped",
            )
            db.session.add(bm)

        import_session = ImportSession(
            source_type=detected_format,
            source_name=filename or "",
            total_count=len(raw_bookmarks),
            imported_count=session_imported,
            duplicate_count=session_duplicates,
        )
        db.session.add(import_session)
        db.session.commit()

        return jsonify({
            "session_id": import_session.id,
            "total": len(raw_bookmarks),
            "imported": session_imported,
            "duplicates": session_duplicates,
            "format": detected_format,
        }), 201

    # ------------------------------------------------------------------ #
    # Bookmarks
    # ------------------------------------------------------------------ #
    @app.route("/api/bookmarks", methods=["GET"])
    def api_list_bookmarks():
        page = request.args.get("page", 1, type=int)
        per_page = min(request.args.get("per_page", 50, type=int), 200)
        q = request.args.get("q", "").strip()
        tags_filter = request.args.get("tags", "").strip()
        source_filter = request.args.get("source", "").strip()
        domain_filter = request.args.get("domain", "").strip().lower()
        cluster_id_raw = request.args.get("cluster_id", "").strip()
        research_status = request.args.get("research_status", "").strip()
        duplicate_mode = request.args.get("duplicate_mode", "").strip().lower()
        if not duplicate_mode:
            duplicate_mode = "include" if request.args.get("show_duplicates", "false").lower() == "true" else "hide"
        sort_by = request.args.get("sort", "imported_at")
        sort_dir = request.args.get("dir", "desc")

        query = Bookmark.query

        if duplicate_mode == "hide":
            query = query.filter_by(is_duplicate=False)
        elif duplicate_mode == "only":
            query = query.filter_by(is_duplicate=True)

        if q:
            like = f"%{q}%"
            query = query.filter(
                db.or_(
                    Bookmark.title.ilike(like),
                    Bookmark.url.ilike(like),
                    Bookmark.page_title.ilike(like),
                    Bookmark.page_description.ilike(like),
                )
            )

        if tags_filter:
            tag_values = [t.strip() for t in tags_filter.split(",") if t.strip()]
            if "__empty__" in tag_values:
                query = query.filter(db.or_(Bookmark.tags.is_(None), Bookmark.tags == [], Bookmark.tags == "[]"))
            else:
                for tag in tag_values:
                    query = query.filter(Bookmark.tags.contains([tag]))

        if source_filter:
            query = query.filter_by(source=source_filter)

        if domain_filter:
            like = f"%{domain_filter}%"
            query = query.filter(Bookmark.url.ilike(like))

        if cluster_id_raw:
            if cluster_id_raw.lower() == "none":
                query = query.filter(Bookmark.cluster_id.is_(None))
            else:
                try:
                    query = query.filter_by(cluster_id=int(cluster_id_raw))
                except ValueError:
                    return jsonify({"error": "Invalid cluster_id"}), 400

        if research_status:
            query = query.filter_by(research_status=research_status)

        sort_col = BOOKMARK_SORT_FIELDS.get(sort_by, Bookmark.imported_at)
        if sort_dir == "asc":
            query = query.order_by(sort_col.asc().nullslast(), Bookmark.id.asc())
        else:
            query = query.order_by(sort_col.desc().nullslast(), Bookmark.id.desc())

        pagination = query.paginate(page=page, per_page=per_page, error_out=False)

        return jsonify({
            "bookmarks": [bm.to_dict() for bm in pagination.items],
            "total": pagination.total,
            "page": page,
            "per_page": per_page,
            "pages": pagination.pages,
        })

    @app.route("/api/bookmarks/<int:bookmark_id>", methods=["GET"])
    def api_get_bookmark(bookmark_id):
        bm = db.session.get(Bookmark, bookmark_id)
        if not bm:
            return jsonify({"error": "Bookmark not found"}), 404
        return jsonify(bm.to_dict())

    @app.route("/api/bookmarks/<int:bookmark_id>", methods=["DELETE"])
    def api_delete_bookmark(bookmark_id):
        bm = db.session.get(Bookmark, bookmark_id)
        if not bm:
            return jsonify({"error": "Bookmark not found"}), 404
        db.session.delete(bm)
        db.session.commit()
        return jsonify({"deleted": True, "id": bookmark_id})

    @app.route("/api/bookmarks/<int:bookmark_id>", methods=["PATCH"])
    def api_update_bookmark(bookmark_id):
        bm = db.session.get(Bookmark, bookmark_id)
        if not bm:
            return jsonify({"error": "Bookmark not found"}), 404
        data = request.get_json(silent=True) or {}
        for field in ("title", "description", "tags", "research_status", "cluster_id"):
            if field in data:
                setattr(bm, field, data[field])
        db.session.commit()
        return jsonify(bm.to_dict())

    @app.route("/api/bookmarks/deduplicate", methods=["POST"])
    def api_deduplicate():
        """Scan all bookmarks and mark duplicates."""
        all_bms = Bookmark.query.order_by(Bookmark.id.asc()).all()
        seen: dict[str, int] = {}
        duplicates_found = 0
        for bm in all_bms:
            norm = bm.normalized_url or normalize_url(bm.url)
            bm.normalized_url = norm
            if norm in seen:
                if not bm.is_duplicate:
                    bm.is_duplicate = True
                    bm.duplicate_of = seen[norm]
                    bm.research_status = "skipped"
                    duplicates_found += 1
            else:
                seen[norm] = bm.id
                bm.is_duplicate = False
        db.session.commit()
        return jsonify({"duplicates_found": duplicates_found, "merged": duplicates_found})

    # ------------------------------------------------------------------ #
    # Research queue
    # ------------------------------------------------------------------ #
    @app.route("/api/research/status", methods=["GET"])
    def api_research_status():
        worker = get_worker()
        # Always query DB for accurate counts; worker only provides running state
        pending = Bookmark.query.filter_by(research_status="pending", is_duplicate=False).count()
        running_count = Bookmark.query.filter_by(research_status="running").count()
        done = Bookmark.query.filter_by(research_status="done").count()
        failed = Bookmark.query.filter_by(research_status="failed").count()
        return jsonify({
            "running": worker._running,
            "pending": pending,
            "running_count": running_count,
            "done": done,
            "failed": failed,
            "total_processed": done + failed,
        })

    @app.route("/api/research/start", methods=["POST"])
    def api_research_start():
        worker = get_worker()
        if not worker._running:
            worker.start(app)
        return jsonify({"started": True, **worker.get_status()})

    @app.route("/api/research/stop", methods=["POST"])
    def api_research_stop():
        worker = get_worker()
        worker.stop()
        return jsonify({"stopped": True})

    @app.route("/api/research/reset", methods=["POST"])
    def api_research_reset():
        count = Bookmark.query.filter_by(research_status="failed").update(
            {"research_status": "pending"}, synchronize_session=False
        )
        db.session.commit()
        return jsonify({"reset": count})

    # ------------------------------------------------------------------ #
    # Categories / clusters
    # ------------------------------------------------------------------ #
    @app.route("/api/categories", methods=["GET"])
    def api_get_categories():
        clusters = Cluster.query.order_by(Cluster.id.asc()).all()
        return jsonify([c.to_dict() for c in clusters])

    @app.route("/api/categories/refresh", methods=["POST"])
    def api_refresh_categories():
        bookmarks = Bookmark.query.filter_by(is_duplicate=False).all()
        clusters = cluster_bookmarks(bookmarks)

        if not clusters:
            return jsonify({"clusters": 0, "message": "Not enough tagged bookmarks to cluster"})

        # Clear existing cluster assignments
        Bookmark.query.update({"cluster_id": None}, synchronize_session=False)
        Cluster.query.delete(synchronize_session=False)
        db.session.flush()

        cluster_objs = []
        for cl in clusters:
            top_tags = cl.get("top_tags", [])
            name = cl.get("name", f"Cluster {cl['id'] + 1}")
            c_obj = Cluster(
                name=name,
                tags=top_tags,
                bookmark_count=len(cl["bookmark_ids"]),
            )
            db.session.add(c_obj)
            db.session.flush()  # get id
            for bm_id in cl["bookmark_ids"]:
                bm = db.session.get(Bookmark, bm_id)
                if bm:
                    bm.cluster_id = c_obj.id
            cluster_objs.append(c_obj)

        db.session.commit()
        return jsonify({"clusters": len(cluster_objs), "details": [c.to_dict() for c in cluster_objs]})

    # ------------------------------------------------------------------ #
    # Stats
    # ------------------------------------------------------------------ #
    @app.route("/api/stats", methods=["GET"])
    def api_stats():
        total = Bookmark.query.count()
        unique = Bookmark.query.filter_by(is_duplicate=False).count()
        duplicates = Bookmark.query.filter_by(is_duplicate=True).count()
        pending = Bookmark.query.filter_by(research_status="pending").count()
        done = Bookmark.query.filter_by(research_status="done").count()
        failed = Bookmark.query.filter_by(research_status="failed").count()
        running = Bookmark.query.filter_by(research_status="running").count()
        skipped = Bookmark.query.filter_by(research_status="skipped").count()
        clusters = Cluster.query.count()
        sessions = ImportSession.query.count()
        return jsonify({
            "total": total,
            "unique": unique,
            "duplicates": duplicates,
            "research": {
                "pending": pending,
                "running": running,
                "done": done,
                "failed": failed,
                "skipped": skipped,
            },
            "clusters": clusters,
            "import_sessions": sessions,
        })

    @app.route("/api/analytics", methods=["GET"])
    def api_analytics():
        bookmarks = Bookmark.query.order_by(Bookmark.id.asc()).all()
        clusters = Cluster.query.order_by(Cluster.name.asc()).all()
        return jsonify(build_analytics_payload(bookmarks, clusters))

    # ------------------------------------------------------------------ #
    # Import sessions
    # ------------------------------------------------------------------ #
    @app.route("/api/import/sessions", methods=["GET"])
    def api_import_sessions():
        sessions = ImportSession.query.order_by(ImportSession.created_at.desc()).limit(50).all()
        return jsonify([s.to_dict() for s in sessions])

    # ------------------------------------------------------------------ #
    # Auto-start research worker if configured
    # ------------------------------------------------------------------ #
    if app.config.get("RESEARCH_AUTO_START", False):
        worker = get_worker()
        worker.start(app)

    return app


if __name__ == "__main__":
    application = create_app()
    debug = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    application.run(debug=debug, port=5000)
