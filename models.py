from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def utcnow():
    return datetime.now(timezone.utc).replace(tzinfo=None)


class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    normalized_url = db.Column(db.Text, nullable=False, index=True)
    title = db.Column(db.Text, default="")
    description = db.Column(db.Text, default="")
    tags = db.Column(db.JSON, default=list)
    source = db.Column(db.String(100), default="")
    created_at = db.Column(db.DateTime, default=utcnow)
    imported_at = db.Column(db.DateTime, default=utcnow)
    is_duplicate = db.Column(db.Boolean, default=False, index=True)
    duplicate_of = db.Column(db.Integer, db.ForeignKey("bookmarks.id"), nullable=True)
    research_status = db.Column(
        db.String(20), default="pending", index=True
    )  # pending|running|done|failed|skipped
    http_status = db.Column(db.Integer, nullable=True)
    page_title = db.Column(db.Text, default="")
    page_description = db.Column(db.Text, default="")
    researched_at = db.Column(db.DateTime, nullable=True)
    cluster_id = db.Column(db.Integer, db.ForeignKey("clusters.id"), nullable=True, index=True)
    favicon_url = db.Column(db.Text, default="")

    cluster = db.relationship("Cluster", back_populates="bookmarks")
    duplicates = db.relationship(
        "Bookmark", backref=db.backref("original", remote_side=[id]), foreign_keys=[duplicate_of]
    )

    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "normalized_url": self.normalized_url,
            "title": self.title or self.page_title or "",
            "description": self.description or self.page_description or "",
            "tags": self.tags or [],
            "source": self.source,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "imported_at": self.imported_at.isoformat() if self.imported_at else None,
            "is_duplicate": self.is_duplicate,
            "duplicate_of": self.duplicate_of,
            "research_status": self.research_status,
            "http_status": self.http_status,
            "page_title": self.page_title or "",
            "page_description": self.page_description or "",
            "researched_at": self.researched_at.isoformat() if self.researched_at else None,
            "cluster_id": self.cluster_id,
            "favicon_url": self.favicon_url or "",
        }


class ImportSession(db.Model):
    __tablename__ = "import_sessions"

    id = db.Column(db.Integer, primary_key=True)
    source_type = db.Column(db.String(50), default="")  # text|netscape_html|chrome_json|firefox_json
    source_name = db.Column(db.String(255), default="")
    created_at = db.Column(db.DateTime, default=utcnow)
    total_count = db.Column(db.Integer, default=0)
    imported_count = db.Column(db.Integer, default=0)
    duplicate_count = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "source_type": self.source_type,
            "source_name": self.source_name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "total_count": self.total_count,
            "imported_count": self.imported_count,
            "duplicate_count": self.duplicate_count,
        }


class Cluster(db.Model):
    __tablename__ = "clusters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), default="")
    tags = db.Column(db.JSON, default=list)
    bookmark_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=utcnow)

    bookmarks = db.relationship("Bookmark", back_populates="cluster")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tags": self.tags or [],
            "bookmark_count": self.bookmark_count,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
