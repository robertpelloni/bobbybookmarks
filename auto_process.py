import os
import re
import json
import logging
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
from concurrent.futures import ThreadPoolExecutor, as_completed

from gemini_pool import GeminiModelPool, stringify_field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='auto_process.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

# Also log to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

# File paths
BOOKMARKS_FILE = 'bookmarks.txt'
PROCESSED_FILE = 'processed.txt'
FAILED_FILE = 'failed_bookmarks.txt'

gemini_pool = GeminiModelPool(logger=logger)
GEMINI_MODELS = gemini_pool.models

def normalize_url(url):
    parsed = urlparse(url)
    if "google.com/search" in url: return url
    if "github.com" in parsed.netloc:
        path_parts = [part for part in parsed.path.split('/') if part]
        if len(path_parts) >= 2:
            normalized_path = f"/{path_parts[0]}/{path_parts[1]}"
        else:
            normalized_path = parsed.path
        return urlunparse((parsed.scheme, parsed.netloc, normalized_path, '', '', '')).rstrip('/')
    normalized_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip('/'), '', '', '')).rstrip('/')
    return normalized_url

def load_processed():
    processed = set()
    for file_path in [PROCESSED_FILE, FAILED_FILE]:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    if line.startswith('http'):
                        url = line.split(',')[0].strip()
                        processed.add(normalize_url(url))
                    else:
                        match = re.search(r'https?://[^\s,]+', line)
                        if match:
                            processed.add(normalize_url(match.group(0)))
    return processed

def fetch_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        resp.raise_for_status()
        return resp.text
    except Exception:
        return None

def process_url(url):
    content = fetch_url(url)
    if not content:
        with open(FAILED_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{url}\n")
        return None

    soup = BeautifulSoup(content, 'html.parser')
    text_content = soup.get_text(separator=' ', strip=True)
    text_content = re.sub(r'\s+', ' ', text_content)[:8000]

    prompt = f"URL: {url}\nContent: {text_content}\n\nReturn JSON: CATEGORY, SHORT_DESCRIPTION, LONG_DESCRIPTION, TAGS, MAIN_FEATURES."

    try:
        response, _ = gemini_pool.generate_content(prompt, f"processing {url}")
        if response is None:
            return None
        res_text = response.text.strip()
        if "```json" in res_text:
            res_text = res_text.split("```json")[1].split("```")[0].strip()
        elif "```" in res_text:
            res_text = res_text.split("```")[1].split("```")[0].strip()

        data = json.loads(res_text)

        csv_line = (
            f"{url}, "
            f"{stringify_field(data.get('CATEGORY', 'Other')).replace(',', ';')}, "
            f"{stringify_field(data.get('SHORT_DESCRIPTION', 'N/A')).replace(',', ';')}, "
            f"{stringify_field(data.get('LONG_DESCRIPTION', 'N/A')).replace(',', ';')}, "
            f"{stringify_field(data.get('TAGS', '')).replace(',', ';')}, "
            f"{stringify_field(data.get('MAIN_FEATURES', '')).replace(',', ';')}\n"
        )
        with open(PROCESSED_FILE, 'a', encoding='utf-8') as f:
            f.write(csv_line)

        logger.info(f"Processed: {url}")
        return True
    except Exception as e:
        logger.error(f"Failed {url}: {e}")
        return None

def main():
    logger.info(f"Using Gemini models: {', '.join(GEMINI_MODELS)}")
    processed = load_processed()
    urls_to_process = []
    if os.path.exists(BOOKMARKS_FILE):
        with open(BOOKMARKS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line.startswith('http'):
                    if normalize_url(line) not in processed:
                        urls_to_process.append(line)

    logger.info(f"Found {len(urls_to_process)} URLs to process.")

    # Single worker, slower but avoid rate limit instant kill
    for url in urls_to_process:
        process_url(url)
        time.sleep(2) # Be very nice to the free tier

if __name__ == "__main__":
    main()
