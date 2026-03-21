import os
import re
import json
import sqlite3
import requests
import time
import logging
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

from gemini_pool import GeminiModelPool, stringify_field

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('borg_research.log', mode='a'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# File paths
BOOKMARKS_FILE = 'bookmarks.txt'
DB_PATH = 'bookmarks.db'
STATUS_PATH = 'deep_research_status.json'

gemini_pool = GeminiModelPool(logger=logger)
GEMINI_MODELS = gemini_pool.models

BORG_TAXONOMY = [
    "Agent Orchestration & Workflow",
    "Context Engineering & Isolation",
    "Memory & Persistence Architecture",
    "Interface & Developer UX",
    "Connectivity & Interoperability (MCP/A2A)",
    "Infrastructure & Proxy Layers",
    "Guides & Industry Trends"
]

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            category TEXT,
            short_description TEXT,
            long_description TEXT,
            tags TEXT,
            main_features TEXT,
            research_level TEXT,
            innovation_score INTEGER,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    try:
        cursor.execute("ALTER TABLE bookmarks ADD COLUMN research_level TEXT DEFAULT 'heuristic'")
        cursor.execute("ALTER TABLE bookmarks ADD COLUMN innovation_score INTEGER DEFAULT 0")
    except sqlite3.OperationalError: pass 
    conn.commit()
    return conn

def normalize_url(url):
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip('/'), '', '', '')).rstrip('/')

def fetch_content(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    try:
        resp = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        if resp.status_code == 200: return resp.text
    except Exception: pass
    return None

def iso_now():
    return datetime.now(timezone.utc).isoformat()

def write_status(status):
    payload = dict(status)
    payload['updated_at'] = iso_now()
    temp_path = f"{STATUS_PATH}.tmp"
    with open(temp_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2, sort_keys=True)
    os.replace(temp_path, STATUS_PATH)

def borg_research_url(url, content, status):
    soup = BeautifulSoup(content, 'html.parser')
    for s in soup(['script', 'style']): s.decompose()
    text = re.sub(r'\s+', ' ', soup.get_text())[:10000] 
    
    prompt = f"""
    Analyze the following technical resource for inclusion in the 'Borg' Project intelligence database.
    URL: {url}
    Content: {text}
    
    Categorize this into EXACTLY ONE of these Borg Categories: {', '.join(BORG_TAXONOMY)}.
    
    Return a strict JSON object:
    - CATEGORY: The chosen category.
    - SHORT_DESCRIPTION: 1 sentence.
    - LONG_DESCRIPTION: Detailed breakdown of the technical approach.
    - MAIN_FEATURES: List of features that Borg should consider implementing (comma separated).
    - INNOVATION_SCORE: 1-10 rating of how unique this project's approach is.
    - TAGS: 8-12 technical tags (lowercase).
    """
    
    while True:
        try:
            status.update({
                'state': 'researching',
                'active_url': url,
                'sleep_seconds': None,
                'last_error': None,
            })
            write_status(status)
            response, _ = gemini_pool.generate_content(prompt, f"researching {url}")
            if response is None:
                status.update({
                    'state': 'backing_off',
                    'active_url': url,
                    'sleep_seconds': gemini_pool.last_backoff_seconds,
                    'last_error': gemini_pool.last_error_summary,
                    'last_model': gemini_pool.last_model_name,
                })
                write_status(status)
                continue
            res_text = response.text.strip()
            if "```json" in res_text: res_text = res_text.split("```json")[1].split("```")[0].strip()
            elif "```" in res_text: res_text = res_text.split("```")[1].split("```")[0].strip()
            return json.loads(res_text)
        except Exception as e:
            logger.error(f"Failed to decode Gemini response for {url}: {e}")
            status.update({
                'state': 'decode_error',
                'active_url': url,
                'last_error': str(e),
            })
            write_status(status)
            return None

def main():
    logger.info(f"Using Gemini models: {', '.join(GEMINI_MODELS)}")
    conn = init_db()
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM bookmarks WHERE research_level = 'borg'")
    processed = {normalize_url(row[0]) for row in cursor.fetchall()}
    cursor.execute("SELECT COUNT(*) FROM bookmarks WHERE research_level = 'borg'")
    existing_borg_rows = cursor.fetchone()[0]
    
    urls = []
    with open(BOOKMARKS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            u = line.strip()
            if u.startswith('http') and normalize_url(u) not in processed:
                urls.append(u)

    status = {
        'worker_pid': os.getpid(),
        'models': GEMINI_MODELS,
        'state': 'starting',
        'active_url': None,
        'last_extracted_url': None,
        'last_error': None,
        'sleep_seconds': None,
        'remaining_urls': len(urls),
        'borg_rows': existing_borg_rows,
    }
    write_status(status)
    logger.info(f"Borg Intelligence Phase: {len(urls)} links remaining.")
    
    for index, url in enumerate(urls):
        status.update({
            'worker_pid': os.getpid(),
            'state': 'fetching',
            'active_url': url,
            'sleep_seconds': None,
            'remaining_urls': len(urls) - index,
        })
        write_status(status)
        content = fetch_content(url)
        if not content:
            status.update({
                'state': 'fetch_failed',
                'active_url': url,
                'last_error': 'fetch_failed',
            })
            write_status(status)
            continue
        
        rdata = borg_research_url(url, content, status)
        if rdata:
            try:
                cursor.execute('''
                    INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level, innovation_score)
                    VALUES (?, ?, ?, ?, ?, ?, 'borg', ?)
                    ON CONFLICT(url) DO UPDATE SET
                        category=excluded.category,
                        short_description=excluded.short_description,
                        long_description=excluded.long_description,
                        tags=excluded.tags,
                        main_features=excluded.main_features,
                        research_level='borg',
                        innovation_score=excluded.innovation_score
                ''', (
                    url,
                    stringify_field(rdata.get('CATEGORY')) or "Other",
                    stringify_field(rdata.get('SHORT_DESCRIPTION')),
                    stringify_field(rdata.get('LONG_DESCRIPTION')),
                    stringify_field(rdata.get('TAGS')),
                    stringify_field(rdata.get('MAIN_FEATURES')),
                    rdata.get('INNOVATION_SCORE', 0),
                ))
                conn.commit()
                logger.info(f"Borg Intelligence Extracted: {url}")
                status.update({
                    'state': 'processing',
                    'active_url': url,
                    'last_extracted_url': url,
                    'last_error': None,
                    'sleep_seconds': None,
                    'remaining_urls': len(urls) - index - 1,
                    'borg_rows': status.get('borg_rows', len(processed)) + 1,
                    'last_model': gemini_pool.last_model_name,
                })
                write_status(status)
            except Exception as e:
                logger.error(f"DB Error: {e}")
                status.update({
                    'state': 'db_error',
                    'active_url': url,
                    'last_error': str(e),
                })
                write_status(status)
        
        time.sleep(15) # Steady state

if __name__ == "__main__":
    main()
