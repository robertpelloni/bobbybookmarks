from datetime import datetime

from models import Bookmark, Cluster, db


def seed_analytics_data():
    Bookmark.query.delete()
    Cluster.query.delete()
    db.session.commit()

    cluster = Cluster(name="AI Agents", tags=["ai", "agents"], bookmark_count=2)
    db.session.add(cluster)
    db.session.flush()

    alpha = Bookmark(
        url="https://github.com/acme/alpha",
        normalized_url="https://github.com/acme/alpha",
        title="Alpha Agents",
        tags=["ai", "agents"],
        source="text",
        research_status="done",
        imported_at=datetime(2026, 3, 1, 12, 0, 0),
        researched_at=datetime(2026, 3, 2, 12, 0, 0),
        cluster_id=cluster.id,
    )
    db.session.add(alpha)
    db.session.flush()

    bookmarks = [
        Bookmark(
            url="https://github.com/acme/beta",
            normalized_url="https://github.com/acme/beta",
            title="Beta Tools",
            tags=["ai", "tools"],
            source="text",
            research_status="failed",
            imported_at=datetime(2026, 3, 3, 12, 0, 0),
            researched_at=datetime(2026, 3, 4, 12, 0, 0),
        ),
        Bookmark(
            url="https://docs.python.org/3/library/sqlite3.html",
            normalized_url="https://docs.python.org/3/library/sqlite3.html",
            title="SQLite Docs",
            tags=[],
            source="chrome_json",
            research_status="pending",
            imported_at=datetime(2026, 3, 5, 12, 0, 0),
        ),
        Bookmark(
            url="https://news.ycombinator.com/item?id=1",
            normalized_url="https://news.ycombinator.com/item?id=1",
            title="Gamma Thread",
            tags=["agents", "python"],
            source="firefox_json",
            research_status="done",
            imported_at=datetime(2026, 3, 6, 12, 0, 0),
            researched_at=datetime(2026, 3, 7, 12, 0, 0),
            cluster_id=cluster.id,
        ),
        Bookmark(
            url="https://github.com/acme/alpha?utm_source=test",
            normalized_url="https://github.com/acme/alpha",
            title="Alpha Agents Duplicate",
            tags=["ai"],
            source="text",
            is_duplicate=True,
            duplicate_of=alpha.id,
            research_status="skipped",
            imported_at=datetime(2026, 3, 8, 12, 0, 0),
        ),
    ]
    db.session.add_all(bookmarks)
    db.session.commit()


def test_api_analytics_returns_pattern_breakdowns(client, app):
    with app.app_context():
        seed_analytics_data()

    response = client.get("/api/analytics")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["summary"]["unique_bookmarks"] == 4
    assert payload["summary"]["duplicate_bookmarks"] == 1
    assert payload["summary"]["untagged_bookmarks"] == 1
    assert payload["summary"]["uncategorized_bookmarks"] == 2
    assert payload["summary"]["unique_domains"] == 3
    assert payload["top_domains"][0]["domain"] == "github.com"
    assert payload["top_domains"][0]["count"] == 2
    assert any(item["tag"] == "ai" and item["count"] == 2 for item in payload["top_tags"])
    assert payload["top_clusters"][0]["name"] == "AI Agents"
    assert payload["top_clusters"][0]["count"] == 2
    assert payload["top_tag_pairs"][0]["label"] == "agents + ai"
    assert payload["import_timeline"][-1]["day"] == "2026-03-06"
    assert any(item["label"] == "Untagged bookmarks" and item["count"] == 1 for item in payload["opportunities"])


def test_api_bookmarks_supports_new_filters_and_sorting(client, app):
    with app.app_context():
        seed_analytics_data()

    response = client.get("/api/bookmarks?source=text&domain=github.com&sort=title&dir=asc")
    payload = response.get_json()

    assert response.status_code == 200
    assert [item["title"] for item in payload["bookmarks"]] == ["Alpha Agents", "Beta Tools"]

    response = client.get("/api/bookmarks?tags=__empty__")
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["total"] == 1
    assert payload["bookmarks"][0]["title"] == "SQLite Docs"

    response = client.get("/api/bookmarks?cluster_id=none")
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["total"] == 2

    response = client.get("/api/bookmarks?duplicate_mode=only")
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["total"] == 1
    assert payload["bookmarks"][0]["is_duplicate"] is True
