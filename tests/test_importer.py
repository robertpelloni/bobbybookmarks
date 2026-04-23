import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import json
import pytest
from importer import (
    import_from_text,
    import_from_netscape_html,
    import_from_chrome_json,
    import_from_firefox_json,
    detect_and_import,
)

NETSCAPE_HTML = """\
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks Menu</H1>
<DL><p>
    <DT><A HREF="https://example.com/" ADD_DATE="1609459200" TAGS="example,test">Example Site</A>
    <DT><A HREF="https://github.com/user/repo" ADD_DATE="1609459201">GitHub Repo</A>
    <DT><H3>Programming</H3>
    <DL><p>
        <DT><A HREF="https://python.org/" ADD_DATE="1609459202" TAGS="python">Python</A>
    </DL><p>
</DL>
"""

CHROME_JSON = json.dumps({
    "checksum": "abc",
    "roots": {
        "bookmark_bar": {
            "children": [
                {
                    "date_added": "13300000000000000",
                    "name": "Google",
                    "type": "url",
                    "url": "https://www.google.com/"
                },
                {
                    "children": [
                        {
                            "date_added": "13300000000000001",
                            "name": "Flask Docs",
                            "type": "url",
                            "url": "https://flask.palletsprojects.com/"
                        }
                    ],
                    "date_added": "13300000000000002",
                    "name": "Dev",
                    "type": "folder"
                }
            ],
            "name": "Bookmarks bar",
            "type": "folder"
        },
        "other": {"children": [], "name": "Other bookmarks", "type": "folder"},
        "synced": {"children": [], "name": "Mobile bookmarks", "type": "folder"}
    },
    "version": 1
})

FIREFOX_JSON = json.dumps({
    "guid": "root________",
    "title": "",
    "id": 1,
    "dateAdded": 1609459200000000,
    "children": [
        {
            "guid": "menu________",
            "title": "Bookmarks Menu",
            "id": 2,
            "dateAdded": 1609459200000000,
            "children": [
                {
                    "guid": "bm1_________",
                    "title": "Mozilla",
                    "id": 3,
                    "uri": "https://www.mozilla.org/",
                    "dateAdded": 1609459200000000,
                    "tags": "mozilla,browser"
                },
                {
                    "guid": "bm2_________",
                    "title": "MDN Docs",
                    "id": 4,
                    "uri": "https://developer.mozilla.org/",
                    "dateAdded": 1609459201000000,
                    "tags": ""
                }
            ]
        }
    ]
})


class TestImportFromText:
    def test_import_from_text_urls(self):
        text = "Check out https://example.com and https://github.com/user/repo for more."
        bms = import_from_text(text)
        urls = set(b["url"] for b in bms)
        assert urls == {"https://example.com", "https://github.com/user/repo"}

    def test_import_from_text_single_url_per_line(self):
        text = "https://example.com\nhttps://python.org\nhttps://flask.palletsprojects.com"
        bms = import_from_text(text)
        assert len(bms) == 3

    def test_import_from_text_deduplicates(self):
        text = "https://example.com https://example.com"
        bms = import_from_text(text)
        assert len(bms) == 1

    def test_import_from_text_ignores_non_urls(self):
        text = "This is just plain text with no URLs."
        bms = import_from_text(text)
        assert bms == []

    def test_import_from_text_sets_source(self):
        bms = import_from_text("https://example.com")
        assert bms[0]["source"] == "text"


class TestImportFromNetscapeHtml:
    def test_import_from_netscape_html(self):
        bms = import_from_netscape_html(NETSCAPE_HTML)
        urls = set(b["url"] for b in bms)
        assert urls == {"https://example.com/", "https://github.com/user/repo", "https://python.org/"}

    def test_netscape_html_extracts_titles(self):
        bms = import_from_netscape_html(NETSCAPE_HTML)
        titles = {b["url"]: b["title"] for b in bms}
        assert titles.get("https://example.com/") == "Example Site"

    def test_netscape_html_extracts_tags(self):
        bms = import_from_netscape_html(NETSCAPE_HTML)
        bm = next(b for b in bms if b["url"] == "https://example.com/")
        assert "example" in bm["tags"]
        assert "test" in bm["tags"]

    def test_netscape_html_folder_as_tag(self):
        bms = import_from_netscape_html(NETSCAPE_HTML)
        bm = next(b for b in bms if b["url"] == "https://python.org/")
        assert "programming" in bm["tags"]

    def test_netscape_html_sets_source(self):
        bms = import_from_netscape_html(NETSCAPE_HTML)
        for bm in bms:
            assert bm["source"] == "netscape_html"

    def test_netscape_html_malformed_returns_empty(self):
        bms = import_from_netscape_html("<html><body>No bookmarks here</body></html>")
        assert isinstance(bms, list)


class TestImportFromChromeJson:
    def test_import_from_chrome_json(self):
        bms = import_from_chrome_json(CHROME_JSON)
        urls = set(b["url"] for b in bms)
        expected = {"https://www.google.com/", "https://flask.palletsprojects.com/"}
        assert expected.issubset(urls)

    def test_chrome_json_extracts_titles(self):
        bms = import_from_chrome_json(CHROME_JSON)
        bm = next(b for b in bms if b["url"] == "https://www.google.com/")
        assert bm["title"] == "Google"

    def test_chrome_json_folder_as_tag(self):
        bms = import_from_chrome_json(CHROME_JSON)
        bm = next(b for b in bms if b["url"] == "https://flask.palletsprojects.com/")
        assert "dev" in bm["tags"]

    def test_chrome_json_invalid_raises(self):
        with pytest.raises(ValueError):
            import_from_chrome_json("{not valid json")

    def test_chrome_json_sets_source(self):
        bms = import_from_chrome_json(CHROME_JSON)
        for bm in bms:
            assert bm["source"] == "chrome_json"


class TestImportFromFirefoxJson:
    def test_import_from_firefox_json(self):
        bms = import_from_firefox_json(FIREFOX_JSON)
        urls = set(b["url"] for b in bms)
        expected = {"https://www.mozilla.org/", "https://developer.mozilla.org/"}
        assert expected.issubset(urls)

    def test_firefox_json_extracts_titles(self):
        bms = import_from_firefox_json(FIREFOX_JSON)
        bm = next(b for b in bms if b["url"] == "https://www.mozilla.org/")
        assert bm["title"] == "Mozilla"

    def test_firefox_json_extracts_tags(self):
        bms = import_from_firefox_json(FIREFOX_JSON)
        bm = next(b for b in bms if b["url"] == "https://www.mozilla.org/")
        assert "mozilla" in bm["tags"]

    def test_firefox_json_sets_source(self):
        bms = import_from_firefox_json(FIREFOX_JSON)
        for bm in bms:
            assert bm["source"] == "firefox_json"


class TestDetectAndImport:
    def test_detect_format_html(self):
        fmt, bms = detect_and_import(NETSCAPE_HTML, filename="bookmarks.html")
        assert fmt == "netscape_html"
        assert len(bms) > 0

    def test_detect_format_html_by_content(self):
        fmt, bms = detect_and_import(NETSCAPE_HTML)
        assert fmt == "netscape_html"

    def test_detect_format_chrome_json(self):
        fmt, bms = detect_and_import(CHROME_JSON, filename="Bookmarks.json")
        assert fmt == "chrome_json"
        assert len(bms) > 0

    def test_detect_format_firefox_json(self):
        fmt, bms = detect_and_import(FIREFOX_JSON, filename="bookmarks.json")
        assert fmt == "firefox_json"
        assert len(bms) > 0

    def test_detect_format_text(self):
        text = "https://example.com\nhttps://python.org"
        fmt, bms = detect_and_import(text)
        assert fmt == "text"
        assert len(bms) == 2

    def test_detect_format_empty(self):
        fmt, bms = detect_and_import("")
        assert bms == []
