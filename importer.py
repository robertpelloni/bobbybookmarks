import re
import json
from datetime import datetime, timezone
from html.parser import HTMLParser
from bs4 import BeautifulSoup

URL_RE = re.compile(
    r"https?://"
    r"(?:[A-Za-z0-9\-]+\.)+[A-Za-z]{2,}"
    r"(?::\d+)?"
    r"(?:/[^\s\"'<>]*)?"
    r"(?:\?[^\s\"'<>]*)?"
    r"(?:#[^\s\"'<>]*)?",
    re.IGNORECASE,
)


def _chrome_timestamp_to_dt(ts_str: str):
    """Convert Chrome's microseconds-since-1601 to a datetime."""
    try:
        ts = int(ts_str)
        # Chrome epoch: Jan 1, 1601; Unix epoch: Jan 1, 1970 => diff in microseconds
        EPOCH_DIFF_MICROSECONDS = 11644473600 * 1_000_000
        unix_us = ts - EPOCH_DIFF_MICROSECONDS
        return datetime.fromtimestamp(unix_us / 1_000_000, tz=timezone.utc).replace(tzinfo=None)
    except Exception:
        return None


def import_from_text(text: str) -> list[dict]:
    """Extract URLs from plain text. Each line may contain one or more URLs."""
    results = []
    seen = set()
    for url in URL_RE.findall(text):
        url = url.strip().rstrip(".,;)")
        if url and url not in seen:
            seen.add(url)
            results.append({"url": url, "title": "", "tags": [], "source": "text"})
    return results


def import_from_netscape_html(html_content: str) -> list[dict]:
    """
    Parse a Netscape Bookmark Format HTML file.

    Standard HTML parsers mangle the Netscape format (DT is not self-closing in
    HTML5, so parsers nest them). We work around this by doing a flat
    document-order walk of ALL elements, maintaining a folder stack ourselves.
    """
    try:
        soup = BeautifulSoup(html_content, "lxml")
    except Exception:
        soup = BeautifulSoup(html_content, "html.parser")

    results = []
    # folder_stack holds (folder_name, dl_element) pairs
    folder_stack: list[str] = []

    # Walk every element in document order
    all_elements = list(soup.descendants)

    # We track which <DL> depths correspond to which folder names.
    # Use a stack of (dl_tag, folder_name) to know when we exit a folder.
    dl_stack: list[tuple] = []  # list of (dl_obj, folder_name)

    # We need to detect DL open/close events. We scan elements and
    # maintain depth by checking when we enter/exit a <DL>.
    # Use the parent chain to determine folder context at any <A> tag.

    def _folder_path_for(element) -> list[str]:
        """Walk up ancestors collecting H3 folder names from containing DLs."""
        path = []
        node = element.parent
        while node:
            if getattr(node, "name", "") and node.name.lower() == "dl":
                # Find the preceding H3 sibling (which is typically a DT sibling of this DL)
                prev = node.find_previous_sibling()
                while prev:
                    if getattr(prev, "name", "") and prev.name.lower() == "dt":
                        h3 = prev.find("h3")
                        if h3:
                            path.insert(0, h3.get_text(strip=True))
                            break
                    prev = prev.find_previous_sibling()
                # Also try the direct previous sibling that is a DT containing H3
            node = node.parent
        return path

    for elem in all_elements:
        if not hasattr(elem, "name") or not elem.name:
            continue
        tag_name = elem.name.lower()

        if tag_name == "a" and elem.get("href"):
            href = elem["href"].strip()
            if not href or href.startswith("javascript:"):
                continue
            title = elem.get_text(strip=True)
            add_date = elem.get("add_date") or elem.get("last_modified")
            raw_tags = elem.get("tags", "")
            tag_list = [t.strip() for t in raw_tags.split(",") if t.strip()]

            # Get folder path from DOM ancestry
            fp = _folder_path_for(elem)
            tag_list += [f.lower().replace(" ", "_") for f in fp if f]

            created_at = None
            if add_date:
                try:
                    created_at = datetime.fromtimestamp(int(add_date), tz=timezone.utc).replace(tzinfo=None)
                except Exception:
                    pass

            results.append({
                "url": href,
                "title": title,
                "tags": list(dict.fromkeys(tag_list)),  # dedupe preserving order
                "created_at": created_at,
                "folder_path": "/".join(fp),
                "source": "netscape_html",
            })

    return results


def _parse_chrome_node(node: dict, folder_path: list[str]) -> list[dict]:
    """Recursively walk a Chrome bookmark node."""
    results = []
    node_type = node.get("type", "")
    if node_type == "url":
        url = node.get("url", "").strip()
        if not url:
            return results
        title = node.get("name", "")
        date_added = node.get("date_added", "")
        created_at = _chrome_timestamp_to_dt(date_added)
        results.append({
            "url": url,
            "title": title,
            "tags": [f.lower().replace(" ", "_") for f in folder_path if f],
            "created_at": created_at,
            "folder_path": "/".join(folder_path),
            "source": "chrome_json",
        })
    elif node_type == "folder":
        folder_name = node.get("name", "")
        for child in node.get("children", []):
            results.extend(_parse_chrome_node(child, folder_path + [folder_name]))
    return results


def import_from_chrome_json(json_content: str) -> list[dict]:
    """Parse Chrome bookmarks JSON export."""
    try:
        data = json.loads(json_content)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {exc}") from exc

    results = []
    roots = data.get("roots", {})
    for root_key in ("bookmark_bar", "other", "synced"):
        root = roots.get(root_key)
        if root:
            results.extend(_parse_chrome_node(root, []))
    return results


def _parse_firefox_node(node: dict, folder_path: list[str]) -> list[dict]:
    """Recursively walk a Firefox bookmark node."""
    results = []
    node_type = node.get("typeCode", node.get("type", ""))
    # typeCode 1 = bookmark, 2 = folder, 3 = separator
    uri = node.get("uri", "")
    if uri:
        title = node.get("title", "") or ""
        date_added = node.get("dateAdded")
        created_at = None
        if date_added:
            try:
                created_at = datetime.fromtimestamp(int(date_added) / 1_000_000, tz=timezone.utc).replace(tzinfo=None)
            except Exception:
                pass
        tags = node.get("tags", "")
        tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []
        tag_list += [f.lower().replace(" ", "_") for f in folder_path if f]
        results.append({
            "url": uri,
            "title": title,
            "tags": tag_list,
            "created_at": created_at,
            "folder_path": "/".join(folder_path),
            "source": "firefox_json",
        })
    for child in node.get("children", []):
        folder_name = node.get("title", "") if not uri else ""
        results.extend(_parse_firefox_node(child, folder_path + ([folder_name] if folder_name else [])))
    return results


def import_from_firefox_json(json_content: str) -> list[dict]:
    """Parse Firefox places JSON export."""
    try:
        data = json.loads(json_content)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {exc}") from exc

    return _parse_firefox_node(data, [])


def _looks_like_netscape_html(content: str) -> bool:
    snippet = content[:2000].upper()
    return "NETSCAPE-BOOKMARK-FILE" in snippet or ("<DL" in snippet and "<DT" in snippet and "<A HREF" in snippet)


def _looks_like_chrome_json(data: dict) -> bool:
    return "roots" in data and any(k in data["roots"] for k in ("bookmark_bar", "other", "synced"))


def _looks_like_firefox_json(data: dict) -> bool:
    # Firefox exports typically have 'children' at the root and 'typeCode' or 'uri'
    return "children" in data and ("title" in data or "guid" in data)


def detect_and_import(content: str, filename: str = None) -> tuple[str, list[dict]]:
    """
    Auto-detect bookmark format from content/filename.
    Returns (format_name, bookmarks_list).
    """
    content = content.strip()
    if not content:
        return "text", []

    ext = ""
    if filename:
        ext = filename.lower().rsplit(".", 1)[-1] if "." in filename else ""

    # Try HTML detection first
    if ext in ("html", "htm") or _looks_like_netscape_html(content):
        try:
            bms = import_from_netscape_html(content)
            if bms:
                return "netscape_html", bms
        except Exception:
            pass

    # Try JSON detection
    if ext == "json" or content.startswith("{") or content.startswith("["):
        try:
            data = json.loads(content)
            if isinstance(data, dict):
                if _looks_like_chrome_json(data):
                    return "chrome_json", import_from_chrome_json(content)
                if _looks_like_firefox_json(data):
                    return "firefox_json", import_from_firefox_json(content)
        except json.JSONDecodeError:
            pass

    # Fallback: plain text URL extraction
    bms = import_from_text(content)
    return "text", bms
