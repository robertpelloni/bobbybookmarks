import os
import re
import json
import requests
import time
from bs4 import BeautifulSoup
import google.generativeai as genai

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def process(url):
    try:
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if resp.status_code != 200: 
            print(f"Skipping {url} (status {resp.status_code})")
            return
        soup = BeautifulSoup(resp.text, 'html.parser')
        txt = re.sub(r'\s+', ' ', soup.get_text())[:5000]
        prompt = f"Analyze URL: {url}\nContent: {txt}\nReturn strict JSON: CATEGORY, SHORT_DESCRIPTION, LONG_DESCRIPTION, TAGS, MAIN_FEATURES."
        res_text = model.generate_content(prompt).text
        
        # Strip markdown
        if "```json" in res_text:
            res_text = res_text.split("```json")[1].split("```")[0].strip()
        elif "```" in res_text:
            res_text = res_text.split("```")[1].split("```")[0].strip()
            
        data = json.loads(res_text)
        
        # Clean commas for CSV
        c = data.get('CATEGORY','Other').replace(',', ';')
        sd = data.get('SHORT_DESCRIPTION','').replace(',', ';')
        ld = data.get('LONG_DESCRIPTION','').replace(',', ';')
        t = data.get('TAGS','').replace(',', ';')
        mf = data.get('MAIN_FEATURES','').replace(',', ';')
        
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
