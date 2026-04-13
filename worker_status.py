import json
import re
import sqlite3
import subprocess
import sys
from collections import deque
from pathlib import Path
from urllib.parse import urlparse, urlunparse


BASE_DIR = Path(__file__).resolve().parent
BOOKMARKS_FILE = BASE_DIR / "bookmarks.txt"
DB_PATH = BASE_DIR / "bookmarks.db"
LOG_PATH = BASE_DIR / "borg_research.log"
HEARTBEAT_PATH = BASE_DIR / "deep_research_status.json"


def normalize_url(url):
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", "")).rstrip("/")


def clean_url(url):
    return url.rstrip(".,);]")


def get_worker_process():
    if sys.platform != "win32":
        return None
    command = r"""
$processes = Get-CimInstance Win32_Process |
    Where-Object { $_.CommandLine -match 'deep_research\.py' } |
    Select-Object ProcessId, Name, CommandLine
if ($processes) {
    $processes | ConvertTo-Json -Compress
}
"""
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", command],
            capture_output=True,
            text=True,
            check=True,
            cwd=str(BASE_DIR),
        )
    except Exception:
        return None

    output = result.stdout.strip()
    if not output:
        return None

    parsed = json.loads(output)
    if isinstance(parsed, list):
        parsed = parsed[0]

    return {
        "pid": parsed.get("ProcessId"),
        "name": parsed.get("Name"),
        "command_line": parsed.get("CommandLine", "").strip(),
    }


def get_progress():
    try:
        conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
        cur = conn.cursor()
        cur.execute("SELECT url FROM bookmarks WHERE research_level = 'borg'")
        processed = {normalize_url(row[0]) for row in cur.fetchall()}
        cur.execute("SELECT COUNT(*) FROM bookmarks WHERE research_level = 'borg'")
        borg_rows = cur.fetchone()[0]
        conn.close()
    except sqlite3.OperationalError:
        # Fallback if even RO mode fails or DB doesn't exist yet
        processed = set()
        borg_rows = 0

    total_urls = 0
    remaining_urls = 0
    if BOOKMARKS_FILE.exists():
        for line in BOOKMARKS_FILE.read_text(encoding="utf-8", errors="ignore").splitlines():
            url = line.strip()
            if not url.startswith("http"):
                continue
            total_urls += 1
            if normalize_url(url) not in processed:
                remaining_urls += 1

    return {
        "borg_rows": borg_rows,
        "total_urls": total_urls,
        "remaining_urls": remaining_urls,
    }


def get_recent_log_state():
    if not LOG_PATH.exists():
        return parse_log_lines([])

    lines = deque(LOG_PATH.read_text(encoding="utf-8", errors="ignore").splitlines(), maxlen=100)
    return parse_log_lines(lines)


def get_worker_heartbeat():
    if not HEARTBEAT_PATH.exists():
        return None
    try:
        return json.loads(HEARTBEAT_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None


def parse_log_lines(lines):
    last_timestamp = None
    last_message = None
    active_url = None
    last_extracted_url = None
    sleep_seconds = None

    for line in reversed(lines):
        timestamp_match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (.+)$", line)
        if timestamp_match and last_timestamp is None:
            last_timestamp = timestamp_match.group(1)
            last_message = timestamp_match.group(2)

        if active_url is None:
            url_match = re.search(r"researching (https?://\S+)", line)
            if url_match:
                active_url = clean_url(url_match.group(1))

        if last_extracted_url is None:
            extracted_match = re.search(r"Borg Intelligence Extracted: (https?://\S+)", line)
            if extracted_match:
                last_extracted_url = clean_url(extracted_match.group(1))

        if sleep_seconds is None:
            sleep_match = re.search(r"Sleeping (\d+)s before retry", line)
            if sleep_match:
                sleep_seconds = int(sleep_match.group(1))

        if last_timestamp and active_url and last_extracted_url and sleep_seconds is not None:
            break

    return {
        "last_timestamp": last_timestamp,
        "last_message": last_message,
        "active_url": active_url,
        "last_extracted_url": last_extracted_url,
        "sleep_seconds": sleep_seconds,
    }


def build_status():
    process = get_worker_process()
    progress = get_progress()
    log_state = get_recent_log_state()
    heartbeat = get_worker_heartbeat()
    state = "idle"
    message = log_state["last_message"] or ""
    if heartbeat and heartbeat.get("state"):
        state = heartbeat["state"]
    elif "Sleeping" in message:
        state = "backing_off"
    elif "Extracted" in message or "Switching Gemini model" in message or "Quota hit" in message:
        state = "processing"

    if heartbeat:
        log_state["active_url"] = heartbeat.get("active_url") or log_state["active_url"]
        log_state["last_extracted_url"] = heartbeat.get("last_extracted_url") or log_state["last_extracted_url"]
        log_state["sleep_seconds"] = heartbeat.get("sleep_seconds", log_state["sleep_seconds"])

    return {
        "worker_running": process is not None,
        "state": state if process else "stopped",
        "process": process,
        "progress": progress,
        "log_state": log_state,
        "heartbeat": heartbeat,
    }


def print_text_status(status):
    process = status["process"]
    progress = status["progress"]
    log_state = status["log_state"]

    print(f"worker_running: {status['worker_running']}")
    print(f"state: {status['state']}")
    print(f"worker_pid: {process['pid'] if process else 'n/a'}")
    print(f"borg_rows: {progress['borg_rows']}")
    print(f"total_urls: {progress['total_urls']}")
    print(f"remaining_urls: {progress['remaining_urls']}")
    print(f"last_timestamp: {log_state['last_timestamp'] or 'n/a'}")
    print(f"heartbeat_updated_at: {status['heartbeat']['updated_at'] if status['heartbeat'] else 'n/a'}")
    print(f"active_url: {log_state['active_url'] or 'n/a'}")
    print(f"last_extracted_url: {log_state['last_extracted_url'] or 'n/a'}")
    print(f"sleep_seconds: {log_state['sleep_seconds'] if log_state['sleep_seconds'] is not None else 'n/a'}")
    print(f"last_message: {log_state['last_message'] or 'n/a'}")


def main():
    status = build_status()
    if "--json" in sys.argv[1:]:
        print(json.dumps(status, indent=2))
        return
    print_text_status(status)


if __name__ == "__main__":
    main()
