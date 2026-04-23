import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import json
import pytest
from unittest.mock import MagicMock, patch

from tagger import LLMTagger
from config import TestConfig


@pytest.fixture
def mock_tagger():
    return LLMTagger(TestConfig)


class TestMockTagger:
    def test_mock_tagger_returns_tags(self, mock_tagger):
        tags = mock_tagger.get_tags(
            title="Introduction to Python",
            description="Learn Python programming",
            url="https://python.org/tutorial"
        )
        assert isinstance(tags, list)
        assert len(tags) > 0

    def test_mock_tagger_returns_strings(self, mock_tagger):
        tags = mock_tagger.get_tags("Flask web framework", "Build web apps", "https://flask.palletsprojects.com/")
        for tag in tags:
            assert isinstance(tag, str)
            assert tag == tag.lower()

    def test_mock_tagger_github_url(self, mock_tagger):
        tags = mock_tagger.get_tags("My GitHub Repo", "Source code", "https://github.com/user/project")
        assert any("github" in t for t in tags)

    def test_mock_tagger_fallback_on_empty(self, mock_tagger):
        tags = mock_tagger.get_tags("", "", "https://some-obscure-site.xyz/")
        assert isinstance(tags, list)

    def test_mock_tagger_max_tags(self, mock_tagger):
        tags = mock_tagger.get_tags(
            "Python Flask Django React Vue TypeScript Docker Kubernetes AWS Cloud",
            "Full stack development tutorial",
            "https://fullstack.dev/tutorial"
        )
        assert len(tags) <= 10


class TestTaggerParseJsonResponse:
    def test_parse_valid_json_array(self, mock_tagger):
        response = '["python", "web", "tutorial", "flask"]'
        tags = mock_tagger._parse_response(response)
        assert tags == ["python", "web", "tutorial", "flask"]

    def test_parse_json_embedded_in_text(self, mock_tagger):
        response = 'Here are the tags: ["python", "programming", "tutorial"] for this page.'
        tags = mock_tagger._parse_response(response)
        assert "python" in tags
        assert "programming" in tags

    def test_parse_empty_array(self, mock_tagger):
        tags = mock_tagger._parse_response("[]")
        assert tags == []

    def test_parse_empty_string(self, mock_tagger):
        tags = mock_tagger._parse_response("")
        assert tags == []

    def test_tagger_handles_malformed_response(self, mock_tagger):
        tags = mock_tagger._parse_response("This is not JSON at all, no array here!")
        assert tags == []

    def test_parse_lowercases_tags(self, mock_tagger):
        response = '["Python", "WEB", "Tutorial"]'
        tags = mock_tagger._parse_response(response)
        assert "python" in tags
        assert "web" in tags
        assert "tutorial" in tags

    def test_parse_multiline_json(self, mock_tagger):
        response = '[\n  "python",\n  "flask",\n  "web"\n]'
        tags = mock_tagger._parse_response(response)
        assert "python" in tags
        assert "flask" in tags


class TestTaggerErrorHandling:
    def test_tagger_returns_empty_on_openai_failure(self):
        config = MagicMock()
        config.LLM_BACKEND = "openai"
        config.OPENAI_API_KEY = "fake-key"
        config.OPENAI_MODEL = "gpt-4o-mini"
        tagger = LLMTagger(config)
        # Should not raise, returns [] on failure
        with patch("openai.OpenAI") as mock_client:
            mock_client.return_value.chat.completions.create.side_effect = Exception("API error")
            tags = tagger.get_tags("title", "desc", "https://example.com")
        assert tags == []

    def test_tagger_uses_mock_when_configured(self):
        config = MagicMock()
        config.LLM_BACKEND = "mock"
        tagger = LLMTagger(config)
        tags = tagger.get_tags("Python tutorial", "Learn Python", "https://python.org")
        assert isinstance(tags, list)

    def test_tagger_unknown_backend_uses_mock(self):
        config = MagicMock()
        config.LLM_BACKEND = "nonexistent_backend"
        tagger = LLMTagger(config)
        tags = tagger.get_tags("test", "test", "https://example.com")
        assert isinstance(tags, list)
