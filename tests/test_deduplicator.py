import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from deduplicator import normalize_url, deduplicate_bookmarks


class TestNormalizeUrl:
    def test_normalize_removes_trailing_slash(self):
        assert normalize_url("https://example.com/page/") == "https://example.com/page"

    def test_normalize_keeps_root_slash(self):
        result = normalize_url("https://example.com/")
        assert result == "https://example.com/"

    def test_normalize_removes_utm_params(self):
        url = "https://example.com/page?utm_source=twitter&utm_medium=social"
        result = normalize_url(url)
        assert "utm_source" not in result
        assert "utm_medium" not in result

    def test_normalize_removes_all_tracking_params(self):
        url = "https://example.com/?fbclid=abc123&gclid=def456"
        result = normalize_url(url)
        assert "fbclid" not in result
        assert "gclid" not in result

    def test_normalize_keeps_search_params(self):
        url = "https://google.com/search?q=python+tutorial"
        result = normalize_url(url)
        assert "q=python" in result

    def test_normalize_keeps_query_param(self):
        url = "https://example.com/results?query=flask"
        result = normalize_url(url)
        assert "query=flask" in result

    def test_normalize_lowercases_domain(self):
        result = normalize_url("HTTPS://WWW.EXAMPLE.COM/Page")
        from urllib.parse import urlparse
        parsed = urlparse(result)
        # hostname is lowercased; www.example.com is preserved as-is
        assert parsed.hostname == "www.example.com"
        assert result == result.lower() or "EXAMPLE" not in result

    def test_normalize_removes_default_port_http(self):
        result = normalize_url("http://example.com:80/page")
        assert ":80" not in result

    def test_normalize_removes_default_port_https(self):
        result = normalize_url("https://example.com:443/page")
        assert ":443" not in result

    def test_normalize_keeps_non_default_port(self):
        result = normalize_url("https://example.com:8080/page")
        assert ":8080" in result

    def test_normalize_removes_fragment(self):
        result = normalize_url("https://example.com/page#section-1")
        assert "#" not in result

    def test_normalize_strips_utm_but_keeps_other(self):
        url = "https://example.com/page?id=42&utm_campaign=test"
        result = normalize_url(url)
        assert "utm_campaign" not in result
        assert "id=42" in result

    def test_normalize_sorts_query_params(self):
        url1 = normalize_url("https://example.com/?b=2&a=1")
        url2 = normalize_url("https://example.com/?a=1&b=2")
        assert url1 == url2

    def test_normalize_adds_scheme_if_missing(self):
        result = normalize_url("example.com/page")
        assert result.startswith("https://")

    def test_normalize_strips_all_when_only_tracking(self):
        url = "https://example.com/?utm_source=a&utm_medium=b&fbclid=c"
        result = normalize_url(url)
        assert "?" not in result


class TestDeduplicateBookmarks:
    def test_deduplicate_finds_duplicates(self):
        bms = [
            {"url": "https://example.com/page/", "title": "A"},
            {"url": "https://example.com/page", "title": "B"},  # duplicate (trailing slash)
        ]
        unique, dups = deduplicate_bookmarks(bms)
        assert len(unique) == 1
        assert len(dups) == 1

    def test_deduplicate_finds_utm_duplicates(self):
        bms = [
            {"url": "https://example.com/post", "title": "A"},
            {"url": "https://example.com/post?utm_source=email", "title": "B"},
        ]
        unique, dups = deduplicate_bookmarks(bms)
        assert len(unique) == 1
        assert len(dups) == 1

    def test_deduplicate_preserves_unique(self):
        bms = [
            {"url": "https://site1.com/", "title": "Site 1"},
            {"url": "https://site2.com/", "title": "Site 2"},
            {"url": "https://site3.com/", "title": "Site 3"},
        ]
        unique, dups = deduplicate_bookmarks(bms)
        assert len(unique) == 3
        assert len(dups) == 0

    def test_deduplicate_adds_normalized_url(self):
        bms = [{"url": "https://example.com/page/", "title": "A"}]
        unique, _ = deduplicate_bookmarks(bms)
        assert "normalized_url" in unique[0]
        assert unique[0]["normalized_url"] == "https://example.com/page"

    def test_deduplicate_first_occurrence_wins(self):
        bms = [
            {"url": "https://example.com/page", "title": "First"},
            {"url": "https://example.com/page/", "title": "Second"},
        ]
        unique, dups = deduplicate_bookmarks(bms)
        assert unique[0]["title"] == "First"
        assert dups[0]["title"] == "Second"

    def test_deduplicate_empty_list(self):
        unique, dups = deduplicate_bookmarks([])
        assert unique == []
        assert dups == []
