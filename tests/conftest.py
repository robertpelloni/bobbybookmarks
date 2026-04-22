import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import create_app
from models import db as _db
from config import TestConfig


@pytest.fixture(scope="session")
def app():
    """Create a Flask application configured for testing."""
    application = create_app(TestConfig)
    return application


@pytest.fixture(scope="session")
def _db_session(app):
    """Create all tables once per session."""
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()


@pytest.fixture(scope="function")
def db(app, _db_session):
    """Provide a clean DB for each test (rolls back after)."""
    with app.app_context():
        connection = _db_session.engine.connect()
        transaction = connection.begin()
        yield _db_session
        transaction.rollback()
        connection.close()


@pytest.fixture(scope="function")
def client(app, db):
    """Test client with an active DB session."""
    return app.test_client()


@pytest.fixture
def sample_bookmarks():
    return [
        {"url": "https://example.com/page/", "title": "Example"},
        {"url": "https://example.com/page", "title": "Example (no slash)"},
        {"url": "https://github.com/user/repo?utm_source=newsletter", "title": "GitHub Repo"},
        {"url": "https://google.com/search?q=python", "title": "Google Search"},
        {"url": "https://unique1.com/article", "title": "Unique Article 1"},
        {"url": "https://unique2.com/article", "title": "Unique Article 2"},
    ]
