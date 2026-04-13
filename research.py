import threading
import queue
import logging
import time
from datetime import datetime, timezone
from typing import Optional

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


class ResearchWorker:
    def __init__(self):
        self._threads: list[threading.Thread] = []
        self._stop_event = threading.Event()
        self._app = None
        self._tagger = None
        self._concurrency = 4
        self._timeout = 10
        self._stats = {
            "pending": 0,
            "running": 0,
            "done": 0,
            "failed": 0,
            "total_processed": 0,
        }
        self._stats_lock = threading.Lock()
        self._running = False

    def start(self, app):
        """Start background worker threads."""
        if self._running:
            logger.info("Research worker already running")
            return
        self._app = app
        self._stop_event.clear()
        self._running = True

        from tagger import LLMTagger
        self._tagger = LLMTagger(app.config)
        self._concurrency = app.config.get("RESEARCH_CONCURRENCY", 4)
        self._timeout = app.config.get("RESEARCH_TIMEOUT", 10)

        for i in range(self._concurrency):
            t = threading.Thread(
                target=self._worker_loop,
                name=f"research-worker-{i}",
                daemon=True,
            )
            t.start()
            self._threads.append(t)
        logger.info("Started %d research worker threads", self._concurrency)

    def stop(self):
        """Signal workers to stop gracefully."""
        self._stop_event.set()
        self._running = False
        # Wait for threads to finish (with timeout)
        for t in self._threads:
            t.join(timeout=5)
        self._threads.clear()
        logger.info("Research workers stopped")

    def get_status(self) -> dict:
        """Return current queue statistics."""
        if not self._app:
            return {"running": False, "pending": 0, "done": 0, "failed": 0, "total_processed": 0}
        with self._app.app_context():
            from models import Bookmark, db
            try:
                pending = Bookmark.query.filter_by(research_status="pending", is_duplicate=False).count()
                running = Bookmark.query.filter_by(research_status="running").count()
                done = Bookmark.query.filter_by(research_status="done").count()
                failed = Bookmark.query.filter_by(research_status="failed").count()
                return {
                    "running": self._running,
                    "pending": pending,
                    "running_count": running,
                    "done": done,
                    "failed": failed,
                    "total_processed": done + failed,
                }
            except Exception as exc:
                logger.error("Error getting research status: %s", exc)
                return {"running": self._running, "error": str(exc)}

    def _worker_loop(self):
        """Main loop for each worker thread."""
        while not self._stop_event.is_set():
            bookmark_id = self._claim_next()
            if bookmark_id is None:
                # Nothing to do; wait a bit
                time.sleep(2)
                continue
            self._process(bookmark_id)

    def _claim_next(self) -> Optional[int]:
        """Atomically claim the next pending bookmark for processing."""
        if not self._app:
            return None
        with self._app.app_context():
            from models import Bookmark, db
            try:
                bm = (
                    Bookmark.query
                    .filter_by(research_status="pending", is_duplicate=False)
                    .with_for_update(skip_locked=True)
                    .first()
                )
                if bm is None:
                    return None
                bm.research_status = "running"
                db.session.commit()
                return bm.id
            except Exception as exc:
                logger.debug("Claim next failed (may be DB locking): %s", exc)
                try:
                    db.session.rollback()
                except Exception:
                    pass
                return None

    def _process(self, bookmark_id: int):
        """Fetch URL, extract metadata, run tagger, save results."""
        with self._app.app_context():
            from models import Bookmark, db
            bm = db.session.get(Bookmark, bookmark_id)
            if not bm:
                return

            url = bm.url
            logger.debug("Researching: %s", url)

            http_status = None
            page_title = ""
            page_description = ""
            tags = []
            status = "failed"

            try:
                resp = requests.get(
                    url,
                    headers=HEADERS,
                    timeout=self._timeout,
                    allow_redirects=True,
                )
                http_status = resp.status_code

                if 200 <= resp.status_code < 300:
                    soup = BeautifulSoup(resp.text, "lxml")
                    page_title = _extract_title(soup)
                    page_description = _extract_description(soup)
                    favicon_url = _extract_favicon(soup, url)
                    bm.favicon_url = favicon_url

                    if self._tagger:
                        tags = self._tagger.get_tags(page_title, page_description, url)

                    status = "done"
                else:
                    status = "failed"

            except requests.exceptions.Timeout:
                logger.warning("Timeout fetching %s", url)
                status = "failed"
            except requests.exceptions.ConnectionError:
                logger.warning("Connection error fetching %s", url)
                status = "failed"
            except requests.exceptions.TooManyRedirects:
                logger.warning("Too many redirects for %s", url)
                status = "failed"
            except Exception as exc:
                logger.warning("Unexpected error fetching %s: %s", url, exc)
                status = "failed"

            # Merge new tags with existing tags
            existing_tags = bm.tags or []
            merged_tags = list(dict.fromkeys(existing_tags + tags))

            bm.research_status = status
            bm.http_status = http_status
            bm.page_title = page_title
            bm.page_description = page_description
            bm.tags = merged_tags
            bm.researched_at = datetime.now(timezone.utc).replace(tzinfo=None)

            try:
                db.session.commit()
            except Exception as exc:
                logger.error("Failed to save research results for %s: %s", url, exc)
                db.session.rollback()
                # If DB is locked, retry once after a short delay
                if "database is locked" in str(exc).lower():
                    time.sleep(2)
                    try:
                        db.session.commit()
                        logger.info("Saved research results for %s after retry", url)
                    except Exception as exc_retry:
                        logger.error("Retry also failed for %s: %s", url, exc_retry)
                        db.session.rollback()


def _extract_title(soup: BeautifulSoup) -> str:
    og = soup.find("meta", property="og:title")
    if og and og.get("content"):
        return og["content"].strip()
    twitter = soup.find("meta", attrs={"name": "twitter:title"})
    if twitter and twitter.get("content"):
        return twitter["content"].strip()
    title_tag = soup.find("title")
    if title_tag:
        return title_tag.get_text(strip=True)
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)
    return ""


def _extract_description(soup: BeautifulSoup) -> str:
    og = soup.find("meta", property="og:description")
    if og and og.get("content"):
        return og["content"].strip()
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        return meta_desc["content"].strip()
    twitter = soup.find("meta", attrs={"name": "twitter:description"})
    if twitter and twitter.get("content"):
        return twitter["content"].strip()
    return ""


def _extract_favicon(soup: BeautifulSoup, base_url: str) -> str:
    from urllib.parse import urljoin, urlparse
    # Try standard link rel=icon tags
    for rel in ("icon", "shortcut icon", "apple-touch-icon"):
        link = soup.find("link", rel=lambda r: r and rel in r)
        if link and link.get("href"):
            return urljoin(base_url, link["href"])
    # Fallback to /favicon.ico
    parsed = urlparse(base_url)
    return f"{parsed.scheme}://{parsed.netloc}/favicon.ico"


# Module-level singleton
_worker = ResearchWorker()


def get_worker() -> ResearchWorker:
    return _worker
