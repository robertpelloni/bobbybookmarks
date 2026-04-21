"""
Resume Research Pipeline v2 - Memory-Efficient Multi-Provider Borg Processor

Key improvements over v1:
- Streams URLs one at a time instead of building giant in-memory lists
- Releases HTML/text memory immediately after processing each URL
- Smaller BeautifulSoup footprint (lxml parser, smaller text slice)
- Explicit gc.collect() every 100 URLs
- Chunked DB commits
"""

import os
import re
import gc
import json
import sqlite3
import requests
import time
import logging
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from deduplicator import normalize_url

# ─── Configuration ───────────────────────────────────────────────────────────

BOOKMARKS_FILE = 'bookmarks.txt'
DB_PATH = 'bookmarks.db'
STATUS_PATH = 'deep_research_status.json'
FAILED_FILE = 'failed_bookmarks.txt'

LLM_CALL_INTERVAL = 4
MAX_RETRIES = 2
FETCH_TIMEOUT = 12
MAX_CONTENT_CHARS = 4000  # reduced from 8000 to save memory/bandwidth
GC_EVERY = 100  # force garbage collection interval

BORG_TAXONOMY = [
    "Agent Orchestration & Workflow",
    "Context Engineering & Isolation",
    "Memory & Persistence Architecture",
    "Interface & Developer UX",
    "Connectivity & Interoperability (MCP/A2A)",
    "Infrastructure & Proxy Layers",
    "Guides & Industry Trends",
    "Vector Databases & Search",
    "Coding Tools & IDEs",
    "Development Tools & Libraries",
    "AI Agents & Frameworks",
    "Search & Discovery",
    "Infrastructure",
    "Other",
]

# ─── Logging ─────────────────────────────────────────────────────────────────

os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join('logs', 'resume_research.log'), mode='a'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ─── Multi-Provider LLM Pool ─────────────────────────────────────────────────

class MultiProviderPool:
    def __init__(self):
        self.providers = []
        self.cooldowns = {}
        self.error_counts = {}
        self.active_index = 0
        self.last_provider = None
        self.total_calls = 0
        self.total_errors = 0
        self._init_providers()

    def _init_providers(self):
        # 1. LM Studio (Local First)
        lm_url = os.environ.get('LMSTUDIO_URL', 'http://localhost:1234/v1/chat/completions')
        self.providers.append({
            'name': 'lmstudio-local',
            'endpoint': lm_url,
            'key': 'not-needed',
            'model': 'local-model'
        })

        # 2. OpenRouter (Free/Preferred)
        or_key = os.environ.get('OPENROUTER_API_KEY')
        if or_key:
            # Try free/low-cost models first
            free_models = [
                'google/gemini-2.0-flash-exp:free',
                'mistralai/mistral-7b-instruct:free',
                'meta-llama/llama-3-8b-instruct:free',
                'microsoft/phi-3-mini-128k-instruct:free',
                'openchat/openchat-7b:free'
            ]
            for m in free_models:
                self.providers.append({
                    'name': f'openrouter-{m.split("/")[1].split(":")[0]}',
                    'endpoint': 'https://openrouter.ai/api/v1/chat/completions',
                    'key': or_key,
                    'model': m
                })

        # 3. Other potential free services (Placeholder for integration)
        # cline/free, zen/free, kilo/free etc usually require specific endpoints/keys
        # We can add them as environment-configurable OpenRouter custom models or direct endpoints

        # 4. Specialized Free Tiers
        groq_key = os.environ.get('GROQ_API_KEY')
        if groq_key:
            self.providers.append({
                'name': 'groq-llama3-8b',
                'endpoint': 'https://api.groq.com/openai/v1/chat/completions',
                'key': groq_key,
                'model': 'llama3-8b-8192'
            })

        # 5. Last Resort: Gemini Flash (paid/standard)
        if or_key:
            self.providers.append({
                'name': 'openrouter-gemini-flash',
                'endpoint': 'https://openrouter.ai/api/v1/chat/completions',
                'key': or_key,
                'model': 'google/gemini-2.0-flash-001'
            })

        logger.info(f"LLM providers (ordered by priority): {[p['name'] for p in self.providers]}")

    def generate(self, prompt):
        self.total_calls += 1
        for offset in range(len(self.providers)):
            idx = (self.active_index + offset) % len(self.providers)
            p = self.providers[idx]
            until = self.cooldowns.get(p['name'])
            if until and time.time() < until:
                continue
            self.cooldowns.pop(p['name'], None)
            try:
                resp = requests.post(
                    p['endpoint'],
                    headers={'Authorization': f"Bearer {p['key']}", 'Content-Type': 'application/json'},
                    json={'model': p['model'], 'messages': [{'role': 'user', 'content': prompt}], 'max_tokens': 800, 'temperature': 0.3},
                    timeout=30,
                )
                if resp.status_code == 200:
                    text = resp.json().get('choices', [{}])[0].get('message', {}).get('content', '')
                    if text:
                        self.error_counts.pop(p['name'], None)
                        self.active_index = idx
                        self.last_provider = p['name']
                        return text, p['name']
                elif resp.status_code == 429:
                    wait = min(60 * (2 ** self.error_counts.get(p['name'], 0)), 300)
                    self.error_counts[p['name']] = self.error_counts.get(p['name'], 0) + 1
                    self.cooldowns[p['name']] = time.time() + wait
                    logger.warning(f"Rate limited {p['name']}, cooldown {wait}s")
                elif resp.status_code == 402:
                    self.cooldowns[p['name']] = time.time() + 3600
                    logger.warning(f"Balance exhausted: {p['name']}")
                else:
                    logger.error(f"{p['name']}: {resp.status_code}")
            except Exception as e:
                logger.error(f"{p['name']} error: {e}")
        self.total_errors += 1
        return None, None


# ─── Helpers ─────────────────────────────────────────────────────────────────

FETCH_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_and_extract(url):
    """Fetch URL and return (title, clean_text) or (None, None). Memory-efficient."""
    try:
        resp = requests.get(url, headers=FETCH_HEADERS, timeout=FETCH_TIMEOUT, allow_redirects=True)
        if resp.status_code != 200:
            return None, None
        html = resp.text
        # Use 'lxml' if available (faster, less memory), fallback to html.parser
        try:
            soup = BeautifulSoup(html, 'lxml')
        except:
            soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string.strip()[:200] if soup.title and soup.title.string else ""
        for s in soup(['script', 'style', 'nav', 'footer', 'header']):
            s.decompose()
        text = re.sub(r'\s+', ' ', soup.get_text(separator=' ', strip=True))[:MAX_CONTENT_CHARS]
        del soup, html  # release memory immediately
        return title, text
    except Exception:
        return None, None

def heuristic_fallback(url, title, text):
    combined = f"{url} {title} {text[:2000]}".lower()
    category = "Other"
    tags = []
    kw_map = {
        'mcp': ('Connectivity & Interoperability (MCP/A2A)', ['mcp', 'protocol']),
        'agent': ('AI Agents & Frameworks', ['agent', 'autonomous']),
        'llm': ('AI Agents & Frameworks', ['llm', 'gpt', 'claude']),
        'vector': ('Vector Databases & Search', ['vector', 'embedding']),
        'rag': ('Vector Databases & Search', ['rag', 'retrieval']),
        'search': ('Search & Discovery', ['search', 'crawler']),
        'proxy': ('Infrastructure & Proxy Layers', ['proxy', 'router']),
        'github': ('Development Tools & Libraries', ['github', 'open-source']),
    }
    for kw, (cat, t) in kw_map.items():
        if kw in combined:
            category = cat
            tags.extend(t)
    parsed = urlparse(url)
    return {
        'CATEGORY': category,
        'SHORT_DESCRIPTION': title or f"Resource at {parsed.netloc}",
        'LONG_DESCRIPTION': text[:500] if text else f"Link to {parsed.netloc}",
        'TAGS': ', '.join(list(set(tags))[:8]),
        'MAIN_FEATURES': 'Automated Discovery (heuristic)',
        'INNOVATION_SCORE': 3,
    }

def build_prompt(url, text):
    return f"""Analyze this technical resource for the Borg intelligence database.
URL: {url}
Content: {text}
Categories: {', '.join(BORG_TAXONOMY)}
Return JSON only: CATEGORY, SHORT_DESCRIPTION, LONG_DESCRIPTION, MAIN_FEATURES, INNOVATION_SCORE(1-10), TAGS(8-12 lowercase)."""

def parse_response(text):
    if not text: return None
    text = text.strip()
    if "```json" in text: text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text: text = text.split("```")[1].split("```")[0].strip()
    return json.loads(text)

def iso_now():
    return datetime.now(timezone.utc).isoformat()

def write_status(status):
    payload = dict(status)
    payload['updated_at'] = iso_now()
    try:
        with open(f"{STATUS_PATH}.tmp", 'w') as f:
            json.dump(payload, f, indent=2, sort_keys=True)
        os.replace(f"{STATUS_PATH}.tmp", STATUS_PATH)
    except: pass

def write_feed(message, type="info"):
    feed_path = os.path.join('logs', 'live_feed.json')
    try:
        entries = []
        if os.path.exists(feed_path):
            with open(feed_path, 'r') as f:
                entries = json.load(f)
        entries.append({"timestamp": iso_now(), "type": type, "message": message})
        with open(feed_path, 'w') as f:
            json.dump(entries[-200:], f, indent=2)
    except: pass


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    logger.info("=" * 60)
    logger.info("BobbyBookmarks Resume Research Pipeline v2")
    logger.info("=" * 60)

    pool = MultiProviderPool()
    if not pool.providers:
        logger.error("No LLM providers available!")
        return

    # Load already-processed URLs from DB (streaming, don't hold conn open)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT url FROM bookmarks')
    processed = {normalize_url(row[0]) for row in c.fetchall()}
    conn.close()
    logger.info(f"Already in DB: {len(processed)}")

    # Load failed URLs
    failed = set()
    if os.path.exists(FAILED_FILE):
        with open(FAILED_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                u = line.strip()
                if u.startswith('http'):
                    failed.add(normalize_url(u))
    logger.info(f"Previously failed: {len(failed)}")

    # Count total URLs for progress tracking
    with open(BOOKMARKS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        total_urls = sum(1 for line in f if line.strip().startswith('http'))

    status = {
        'worker_pid': os.getpid(),
        'models': [p['name'] for p in pool.providers],
        'state': 'starting',
        'active_url': None,
        'last_extracted_url': None,
        'last_error': None,
        'remaining_urls': 0,
        'borg_rows': len(processed),
        'session_processed': 0,
        'session_failed': 0,
        'session_heuristic': 0,
    }

    # Open DB for writing (single connection, commit periodically)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    session_count = 0
    session_failed = 0
    session_heuristic = 0
    url_index = 0
    skipped = 0

    # Stream through bookmarks.txt line by line - never load all into memory
    with open(BOOKMARKS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        for raw_line in f:
            url = raw_line.strip()
            if not url.startswith('http'):
                continue

            url_index += 1
            norm = normalize_url(url)

            if norm in processed or norm in failed:
                skipped += 1
                continue

            status.update({
                'state': 'fetching',
                'active_url': url,
                'remaining_urls': total_urls - url_index,
            })
            write_status(status)

            # Fetch and extract
            title, text = fetch_and_extract(url)
            if title is None and text is None:
                session_failed += 1
                with open(FAILED_FILE, 'a', encoding='utf-8') as ff:
                    ff.write(f"{url}\n")
                failed.add(norm)
                status.update({'state': 'fetch_failed', 'session_failed': session_failed})
                write_status(status)
                continue

            # LLM research
            rdata = None
            for attempt in range(MAX_RETRIES):
                prompt = build_prompt(url, text)
                resp_text, provider = pool.generate(prompt)
                if resp_text:
                    try:
                        rdata = parse_response(resp_text)
                        if rdata and 'CATEGORY' in rdata:
                            break
                        rdata = None
                    except: rdata = None
                if attempt < MAX_RETRIES - 1:
                    time.sleep(2)

            if not rdata:
                rdata = heuristic_fallback(url, title, text)
                session_heuristic += 1

            # Insert into DB
            try:
                c.execute('''INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level, innovation_score)
                    VALUES (?, ?, ?, ?, ?, ?, 'borg', ?)
                    ON CONFLICT(url) DO UPDATE SET
                    category=excluded.category, short_description=excluded.short_description,
                    long_description=excluded.long_description, tags=excluded.tags,
                    main_features=excluded.main_features, research_level='borg',
                    innovation_score=excluded.innovation_score''',
                    (url, str(rdata.get('CATEGORY', 'Other')), str(rdata.get('SHORT_DESCRIPTION', '')),
                     str(rdata.get('LONG_DESCRIPTION', '')), str(rdata.get('TAGS', '')),
                     str(rdata.get('MAIN_FEATURES', '')), int(rdata.get('INNOVATION_SCORE', 0))))
                conn.commit()
                session_count += 1
                processed.add(norm)
                logger.info(f"[{session_count}] {url} ({pool.last_provider})")
            except Exception as e:
                logger.error(f"DB error: {e}")
                session_failed += 1

            status.update({
                'state': 'processing',
                'last_extracted_url': url,
                'borg_rows': len(processed),
                'session_processed': session_count,
                'session_failed': session_failed,
                'session_heuristic': session_heuristic,
                'last_provider': pool.last_provider,
            })
            write_status(status)

            # Rate limit
            time.sleep(LLM_CALL_INTERVAL)

            # Garbage collect periodically
            if url_index % GC_EVERY == 0:
                gc.collect()
                logger.info(f"Progress: {session_count} done, {session_failed} failed, "
                           f"{session_heuristic} heuristic, skipped {skipped}, "
                           f"{url_index}/{total_urls} scanned ({url_index/total_urls*100:.1f}%)")

    # Final
    status.update({
        'state': 'completed',
        'active_url': None,
        'session_processed': session_count,
        'session_failed': session_failed,
        'session_heuristic': session_heuristic,
    })
    write_status(status)

    logger.info("=" * 60)
    logger.info(f"DONE: {session_count} processed, {session_failed} failed, {session_heuristic} heuristic")
    logger.info(f"LLM calls: {pool.total_calls}, errors: {pool.total_errors}")
    logger.info("=" * 60)

    conn.close()


if __name__ == "__main__":
    main()
