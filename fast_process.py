import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='fast_process.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

# File paths
BOOKMARKS_FILE = 'bookmarks.txt'
PROCESSED_FILE = 'processed.txt'
FAILED_FILE = 'failed_bookmarks.txt'

KEYWORDS = {
    'mcp': ('MCP', ['mcp', 'protocol', 'context', 'anthropic']),
    'agent': ('AI Agents & Frameworks', ['agent', 'autonomous', 'workflow', 'orchestration']),
    'claude': ('AI Agents & Frameworks', ['claude', 'anthropic', 'sdk']),
    'gemini': ('AI Agents & Frameworks', ['gemini', 'google', 'router']),
    'openai': ('AI Agents & Frameworks', ['openai', 'gpt', 'llm']),
    'github': ('Development Tools & Libraries', ['github', 'repository', 'code', 'open-source']),
    'docs': ('Guides & Articles', ['documentation', 'guide', 'tutorial', 'learn']),
    'search': ('Search & Discovery', ['search', 'crawler', 'tavily', 'exa']),
    'proxy': ('Infrastructure', ['proxy', 'router', 'api', 'gateway']),
    'mcp-server': ('MCP', ['mcp', 'server', 'integration']),
}

def normalize_url(url):
    parsed = urlparse(url)
    normalized_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip('/'), '', '', '')).rstrip('/')
    return normalized_url

def load_processed():
    processed = set()
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if line.strip().startswith('http'):
                    processed.add(normalize_url(line.split(',')[0].strip()))
    return processed

def heuristic_analyze(url, title, description):
    combined = f"{url} {title} {description}".lower()
    category = "Other"
    tags = []
    
    for kw, (cat, t) in KEYWORDS.items():
        if kw in combined:
            category = cat
            tags.extend(t)
    
    tags = list(set(tags))[:5]
    short_desc = title[:50] if title else "Project Reference"
    long_desc = description[:150] if description else f"Link to {urlparse(url).netloc}"
    
    return {
        'CATEGORY': category,
        'SHORT_DESCRIPTION': short_desc,
        'LONG_DESCRIPTION': long_desc,
        'TAGS': ', '.join(tags),
        'MAIN_FEATURES': 'Heuristic detection'
    }

def process_url(url):
    try:
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10, allow_redirects=True)
        if resp.status_code != 200:
            return None
            
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else ""
        
        desc_tag = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', property='og:description')
        description = desc_tag.get('content', '').strip() if desc_tag else ""
        
        data = heuristic_analyze(url, title, description)
        
        # Clean for CSV
        c = data['CATEGORY'].replace(',', ';')
        sd = data['SHORT_DESCRIPTION'].replace(',', ';').replace('\n', ' ')
        ld = data['LONG_DESCRIPTION'].replace(',', ';').replace('\n', ' ')
        t = data['TAGS'].replace(',', ';')
        mf = data['MAIN_FEATURES'].replace(',', ';')
        
        line = f"{url}, {c}, {sd}, {ld}, {t}, {mf}\n"
        with open(PROCESSED_FILE, 'a', encoding='utf-8') as f:
            f.write(line)
        return True
    except Exception as e:
        logger.error(f"Error processing {url}: {e}")
        return None

def main():
    processed = load_processed()
    urls = []
    with open(BOOKMARKS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            u = line.strip()
            if u.startswith('http') and normalize_url(u) not in processed:
                urls.append(u)
    
    logger.info(f"Starting fast process for {len(urls)} URLs...")
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(process_url, url): url for url in urls}
        count = 0
        for future in as_completed(futures):
            count += 1
            if count % 100 == 0:
                logger.info(f"Processed {count}/{len(urls)}...")

if __name__ == "__main__":
    main()
