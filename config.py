import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'bookmarks.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # LLM settings
    LLM_BACKEND = os.environ.get("LLM_BACKEND", "mock")  # openai | anthropic | ollama | mock
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
    ANTHROPIC_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
    OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3")

    # Research queue settings
    RESEARCH_CONCURRENCY = int(os.environ.get("RESEARCH_CONCURRENCY", "4"))
    RESEARCH_TIMEOUT = int(os.environ.get("RESEARCH_TIMEOUT", "10"))
    RESEARCH_AUTO_START = os.environ.get("RESEARCH_AUTO_START", "false").lower() == "true"

    # Dedup settings
    DEDUP_ON_IMPORT = os.environ.get("DEDUP_ON_IMPORT", "true").lower() == "true"


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    LLM_BACKEND = "mock"
    RESEARCH_AUTO_START = False
    WTF_CSRF_ENABLED = False
