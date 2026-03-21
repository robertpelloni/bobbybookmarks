import os
import re
import json
import logging
import requests
import time
from bs4 import BeautifulSoup

from gemini_pool import GeminiModelPool, stringify_field

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

gemini_pool = GeminiModelPool(logger=logger)

def process(url):
    try:
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if resp.status_code != 200: 
            print(f"Skipping {url} (status {resp.status_code})")
            return
        soup = BeautifulSoup(resp.text, 'html.parser')
        txt = re.sub(r'\s+', ' ', soup.get_text())[:5000]
        prompt = f"Analyze URL: {url}\nContent: {txt}\nReturn strict JSON: CATEGORY, SHORT_DESCRIPTION, LONG_DESCRIPTION, TAGS, MAIN_FEATURES."
        response, _ = gemini_pool.generate_content(prompt, f"processing {url}")
        if response is None:
            return
        res_text = response.text
        
        # Strip markdown
        if "```json" in res_text:
            res_text = res_text.split("```json")[1].split("```")[0].strip()
        elif "```" in res_text:
            res_text = res_text.split("```")[1].split("```")[0].strip()
            
        data = json.loads(res_text)
        
        # Clean commas for CSV
        c = stringify_field(data.get('CATEGORY', 'Other')).replace(',', ';')
        sd = stringify_field(data.get('SHORT_DESCRIPTION', '')).replace(',', ';')
        ld = stringify_field(data.get('LONG_DESCRIPTION', '')).replace(',', ';')
        t = stringify_field(data.get('TAGS', '')).replace(',', ';')
        mf = stringify_field(data.get('MAIN_FEATURES', '')).replace(',', ';')
        
        line = f"{url}, {c}, {sd}, {ld}, {t}, {mf}\n"
        with open('processed.txt', 'a', encoding='utf-8') as f:
            f.write(line)
        print(f"Done: {url}")
    except Exception as e:
        print(f"Fail: {url} - {str(e)[:100]}")

def main():
    processed = set()
    if os.path.exists('processed.txt'):
        with open('processed.txt', 'r', encoding='utf-8', errors='ignore') as f:
            for l in f:
                if l.strip().startswith('http'):
                    processed.add(l.split(',')[0].strip())

    urls = []
    with open('bookmarks.txt', 'r', encoding='utf-8', errors='ignore') as f:
        for l in f:
            u = l.strip()
            if u.startswith('http') and u not in processed:
                urls.append(u)
                if len(urls) >= 30: break

    for u in urls:
        process(u)
        time.sleep(3) # Slow and steady

if __name__ == "__main__":
    main()
