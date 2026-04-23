import os
import re
import requests
import sqlite3
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import logging
import queue
import threading

# Configure logging to BOTH file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fast_process.log', mode='a'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# File paths
BOOKMARKS_FILE = 'bookmarks.txt'
DB_PATH = 'bookmarks.db'
FAILED_FILE = 'failed_bookmarks.txt'

# EXPANDED KNOWLEDGE BASE
KEYWORDS = {
    'mcp': ('MCP', ['mcp', 'protocol', 'context', 'anthropic', 'model-context-protocol']),
    'letta': ('AI Agents & Frameworks', ['letta', 'memgpt', 'memory', 'agent-os']),
    'memgpt': ('AI Agents & Frameworks', ['memgpt', 'long-term-memory', 'agent']),
    'cursor': ('Coding Tools', ['cursor', 'ide', 'ai-editor', 'productivity']),
    'aider': ('Coding Tools', ['aider', 'cli', 'git-integration', 'llm-coding']),
    'roo-code': ('Coding Tools', ['roo-code', 'agentic-ide', 'vs-code']),
    'windsurf': ('Coding Tools', ['windsurf', 'ide', 'next-gen-coding']),
    'agent': ('AI Agents & Frameworks', ['agent', 'autonomous', 'workflow', 'orchestration', 'swarm']),
    'claude': ('AI Agents & Frameworks', ['claude', 'anthropic', 'sdk', 'bedrock']),
    'gemini': ('AI Agents & Frameworks', ['gemini', 'google', 'router', 'vertex-ai']),
    'openai': ('AI Agents & Frameworks', ['openai', 'gpt', 'llm', 'codex']),
    'pinecone': ('Vector Databases', ['pinecone', 'vector-db', 'rag', 'semantic-search']),
    'weaviate': ('Vector Databases', ['weaviate', 'vector-search', 'knowledge-graph']),
    'qdrant': ('Vector Databases', ['qdrant', 'vector-engine', 'similarity-search']),
    'milvus': ('Vector Databases', ['milvus', 'vector-database', 'high-scale']),
    'supabase': ('Infrastructure', ['supabase', 'backend-as-a-service', 'postgres', 'auth']),
    'neon': ('Infrastructure', ['neon', 'serverless-postgres', 'database']),
    'github': ('Development Tools & Libraries', ['github', 'repository', 'code', 'open-source']),
    'docs': ('Guides & Articles', ['documentation', 'guide', 'tutorial', 'learn']),
    'search': ('Search & Discovery', ['search', 'crawler', 'tavily', 'exa', 'web-search']),
    'proxy': ('Infrastructure', ['proxy', 'router', 'api', 'gateway']),
    'langgraph': ('AI Agents & Frameworks', ['langgraph', 'langchain', 'state-machine', 'cycles']),
    'crewai': ('AI Agents & Frameworks', ['crewai', 'multi-agent', 'collaboration', 'task-management']),
}

class DatabaseWorker(threading.Thread):
    def __init__(self, db_path, q):
        super().__init__(daemon=True)
        self.db_path = db_path
        self.q = q

    def run(self):
        logger.info("DB Worker started.")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        while True:
            item = self.q.get()
            if item is None: break
            try:
                cursor.execute('''
                    INSERT OR IGNORE INTO bookmarks (url, category, short_description, long_description, tags, main_features)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', item)
                conn.commit()
            except Exception as e:
                logger.error(f"DB insert error: {e}")
            self.q.task_done()
        conn.close()

def normalize_url(url):
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip('/'), '', '', '')).rstrip('/')

def heuristic_analyze(url, title, description):
    combined = f"{url} {title} {description}".lower()
    category = "Other"
    tags = []
    for kw, (cat, t) in KEYWORDS.items():
        if kw in combined:
            category = cat
            tags.extend(t)
    tags = list(set(tags))[:5]
    return {
        'CATEGORY': category,
        'SHORT_DESCRIPTION': title[:100] if title else "Project Reference",
        'LONG_DESCRIPTION': description[:500] if description else f"Link to {urlparse(url).netloc}",
        'TAGS': ', '.join(tags),
        'MAIN_FEATURES': 'Automated Discovery'
    }

def process_url(url, q):
    try:
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=8, allow_redirects=True)
        if resp.status_code != 200:
            with open(FAILED_FILE, 'a', encoding='utf-8') as f: f.write(f"{url}\n")
            return False
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else ""
        desc_tag = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', property='og:description')
        description = desc_tag.get('content', '').strip() if desc_tag else ""
        data = heuristic_analyze(url, title, description)
        q.put((url, data['CATEGORY'], data['SHORT_DESCRIPTION'], data['LONG_DESCRIPTION'], data['TAGS'], data['MAIN_FEATURES']))
        return True
    except Exception:
        with open(FAILED_FILE, 'a', encoding='utf-8') as f: f.write(f"{url}\n")
        return False

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS bookmarks (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT UNIQUE, category TEXT, short_description TEXT, long_description TEXT, tags TEXT, main_features TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)')
    cursor.execute('SELECT url FROM bookmarks')
    processed = {normalize_url(row[0]) for row in cursor.fetchall()}
    conn.close()

    failed = set()
    if os.path.exists(FAILED_FILE):
        with open(FAILED_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                u = line.strip()
                if u.startswith('http'): failed.add(normalize_url(u))

    urls = []
    with open(BOOKMARKS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            u = line.strip()
            if u.startswith('http'):
                norm = normalize_url(u)
                if norm not in processed and norm not in failed:
                    urls.append(u)

    logger.info(f"Resuming research. Live links to process: {len(urls)} (Skipping {len(processed)} existing, {len(failed)} broken)")
    if not urls: return

    db_queue = queue.Queue()
    db_worker = DatabaseWorker(DB_PATH, db_queue)
    db_worker.start()

    batch_size = 50
    success_count = 0

    for i in range(0, len(urls), batch_size):
        batch = urls[i:i+batch_size]
        with ThreadPoolExecutor(max_workers=15) as executor:
            results = list(as_completed({executor.submit(process_url, url, db_queue): url for url in batch}))
            for r in results:
                if r.result(): success_count += 1

        logger.info(f"Processed batch {i//batch_size + 1}. Total successes: {success_count}. Queue size: {db_queue.qsize()}")
        time.sleep(1)

    db_queue.put(None)
    db_worker.join()

if __name__ == "__main__":
    main()
