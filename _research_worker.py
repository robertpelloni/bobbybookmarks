#!/usr/bin/env python3
"""Borg Research Worker v2.1 — Process new atlas entries through LLM enrichment"""
import os, re, json, sqlite3, requests, time, logging, sys
from datetime import datetime, timezone
from bs4 import BeautifulSoup, Comment
from urllib.parse import urlparse
sys.stdout.reconfigure(encoding='utf-8')

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.FileHandler('logs/borg_research.log', mode='a'), logging.StreamHandler()])
logger = logging.getLogger(__name__)

ATLAS_DB = 'atlas.db'
BORG_TAXONOMY = [
    "Agent Orchestration & Workflow",
    "Context Engineering & Isolation",
    "Memory & Persistence Architecture",
    "Interface & Developer UX",
    "Connectivity / MCP / A2A",
    "Infrastructure & Proxy Layers",
    "Guides & Industry Trends",
    "Coding Harness Tools",
    "AI Agents & Frameworks",
    "Search & Discovery",
    "Coding Tools & IDEs",
    "Developer Workflow & Tools",
    "Vector Databases & Embeddings",
    "Security & Red Teaming",
]

def call_llm(prompt, url_hint=""):
    """Call LM Studio with fallback"""
    models_url = "http://localhost:1234/v1/chat/completions"
    
    # Try models in order of capability
    # Start with smallest/fastest model for bulk processing
    models = ["liquid/lfm2.5-1.2b", "gemma-4-e2b-uncensored-hauhaucs-aggressive",
              "gemma-4-e4b-uncensored-hauhaucs-aggressive",
              "gemma-4-26b-a4b-it-heretic-ara", "qwen3.6-27b-uncensored-hauhaucs-aggressive"]
    
    for model in models:
        try:
            resp = requests.post(models_url, json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
                "max_tokens": 600,
            }, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                text = data.get('choices', [{}])[0].get('message', {}).get('content', '')
                if text and len(text) > 50:
                    return text, model
        except Exception as e:
            logger.warning(f"Model {model} failed: {e}")
        time.sleep(1)
    return None, None

def fetch_content(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        resp = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        if resp.status_code == 200:
            return resp.text
    except Exception:
        pass
    return None

def extract_fit_markdown(html, url=""):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(['script','style','nav','footer','header','aside','iframe','noscript','svg','button','form']):
        tag.decompose()
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()
    main = None
    for sel in ['main','article','[role="main"]','.content','#content','.post-body','.markdown-body','.readme','#readme','.entry-content']:
        main = soup.select_one(sel)
        if main: break
    if not main: main = soup.find('body') or soup
    text = main.get_text(separator='\n', strip=True)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    text = '\n'.join(lines)
    return text[:6000]

def extract_gh_meta(url, html):
    meta = {}
    soup = BeautifulSoup(html, 'html.parser')
    about = soup.find('p', class_='f4 my-3')
    if about: meta['desc'] = about.get_text(strip=True)
    topics = soup.find_all('a', class_='topic-tag')
    if topics: meta['topics'] = [t.get_text(strip=True) for t in topics]
    stars = soup.find('span', id='repo-stars-counter-star')
    if stars: meta['stars'] = stars.get_text(strip=True)
    readme = soup.find('div', class_='markdown-body')
    if readme: meta['readme'] = readme.get_text(separator='\n', strip=True)[:3000]
    return meta

def build_prompt(url, fit_text, gh_meta=None):
    prompt = "Analyze this technical resource for the Borg Intelligence database.\n\nURL: " + url + "\n"
    if gh_meta:
        if 'desc' in gh_meta: prompt += "\nRepo: " + gh_meta['desc'] + "\n"
        if 'topics' in gh_meta: prompt += "Topics: " + ", ".join(gh_meta['topics']) + "\n"
    prompt += "\nContent:\n" + fit_text + "\n\n"
    prompt += "Categorize into EXACTLY ONE: " + ", ".join(BORG_TAXONOMY) + "\n\n"
    prompt += """Return strict JSON:
- CATEGORY: one of the above categories
- SHORT_DESCRIPTION: 1 specific sentence about what this DOES
- LONG_DESCRIPTION: detailed technical breakdown (2-3 sentences)
- MAIN_FEATURES: 3-5 SPECIFIC concrete features (comma separated)
- INNOVATION_SCORE: 1-10 uniqueness rating
- TAGS: 8-12 lowercase hyphenated technical tags (comma separated)

CRITICAL: MAIN_FEATURES must be SPECIFIC capabilities, NOT generic phrases."""
    return prompt

def stringify(v):
    if v is None: return ''
    if isinstance(v, str): return v
    if isinstance(v, (list, tuple)): return ', '.join(str(x) for x in v)
    return str(v)

def is_garbage(rdata):
    desc = stringify(rdata.get('SHORT_DESCRIPTION','')).lower().strip()
    feats = stringify(rdata.get('MAIN_FEATURES','')).lower().strip()
    if not feats or len(feats) < 10: return True, "empty_features"
    if not desc or len(desc) < 15: return True, "empty_description"
    for p in ['automated discovery', 'heuristic mapping', 'unable to determine']:
        if p in feats: return True, f"boilerplate:{p[:30]}"
    for p in ['sign in to continue', 'a comprehensive resource detailing']:
        if p in desc: return True, f"generic_desc:{p[:30]}"
    try:
        innov = int(rdata.get('INNOVATION_SCORE', 0))
        if innov <= 2 and len(feats) < 50: return True, f"low_innov:{innov}"
    except: pass
    return False, None

def main():
    atl = sqlite3.connect(ATLAS_DB)
    a = atl.cursor()
    
    # Find entries that need enrichment (no long_description or placeholder)
    a.execute("""SELECT e.id, e.url, e.short_description, e.long_description, e.is_github, e.innovation
        FROM entries e 
        WHERE (e.long_description = e.short_description OR LENGTH(e.long_description) < 50)
        AND e.is_github = 1
        ORDER BY e.id DESC""")
    github_entries = a.fetchall()
    
    # Also process non-GitHub entries with placeholder descriptions
    a.execute("""SELECT e.id, e.url, e.short_description, e.long_description, e.is_github, e.innovation
        FROM entries e 
        WHERE LENGTH(e.long_description) < 30
        AND e.is_github = 0
        ORDER BY e.id DESC""")
    web_entries = a.fetchall()
    
    all_entries = list(github_entries) + list(web_entries)
    logger.info(f"Entries to research: {len(github_entries)} GitHub + {len(web_entries)} web = {len(all_entries)} total")
    
    accepted = 0
    rejected = 0
    failed = 0
    skipped = 0
    
    for idx, (eid, url, sd, ld, is_gh, innov) in enumerate(all_entries):
        logger.info(f"[{idx+1}/{len(all_entries)}] Researching: {url[:80]}")
        
        content = fetch_content(url)
        if not content:
            logger.warning(f"  Fetch failed: {url[:80]}")
            failed += 1
            continue
        
        fit_text = extract_fit_markdown(content, url)
        if len(fit_text) < 50:
            logger.warning(f"  Content too thin: {url[:80]}")
            skipped += 1
            continue
        
        gh_meta = None
        if is_gh:
            gh_meta = extract_gh_meta(url, content)
        
        prompt = build_prompt(url, fit_text, gh_meta)
        raw, model = call_llm(prompt, url)
        
        if not raw:
            logger.warning(f"  LLM failed: {url[:80]}")
            failed += 1
            continue
        
        # Parse JSON response
        try:
            text = raw.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()
            
            json_match = re.search(r'\{[^{}]*\}', text, re.DOTALL)
            if json_match:
                rdata = json.loads(json_match.group(0))
            else:
                rdata = json.loads(text)
        except (json.JSONDecodeError, ValueError) as e:
            logger.warning(f"  JSON decode error: {e}")
            failed += 1
            continue
        
        # Garbage check
        garbage, reason = is_garbage(rdata)
        if garbage:
            logger.warning(f"  Garbage rejected ({reason}): {url[:60]}")
            rejected += 1
            continue
        
        # Extract data
        category = stringify(rdata.get('CATEGORY') or '').strip()
        short_desc = stringify(rdata.get('SHORT_DESCRIPTION') or '').strip()
        long_desc = stringify(rdata.get('LONG_DESCRIPTION') or '').strip() or short_desc
        features = stringify(rdata.get('MAIN_FEATURES') or '').strip()
        tags_str = stringify(rdata.get('TAGS') or '').strip()
        innovation = rdata.get('INNOVATION_SCORE', 8)
        try: innovation = int(innovation)
        except: innovation = 8
        innovation = max(1, min(10, innovation))
        
        # Normalize tags
        tags = [t.strip().lower().replace(' ','-').replace('_','-') for t in tags_str.split(',') if t.strip()]
        # Remove duplicates while preserving order
        seen_tags = set()
        clean_tags = []
        for t in tags:
            if t not in seen_tags:
                seen_tags.add(t)
                clean_tags.append(t)
        
        # Recompute quality and signal
        score = 0.0
        ld_len = len(long_desc)
        if ld_len > 500: score += 30
        elif ld_len > 300: score += 25
        elif ld_len > 150: score += 20
        elif ld_len > 50: score += 12
        elif ld_len > 10: score += 6
        
        feat_count = len([x.strip() for x in features.split(',') if x.strip() and len(x.strip())>3])
        if feat_count >= 5: score += 25
        elif feat_count >= 4: score += 22
        elif feat_count >= 3: score += 18
        elif feat_count >= 2: score += 12
        elif feat_count >= 1: score += 6
        
        tag_count = len(clean_tags)
        if tag_count >= 6: score += 15
        elif tag_count >= 4: score += 12
        elif tag_count >= 2: score += 8
        elif tag_count >= 1: score += 4
        
        # Check page_title
        a.execute("SELECT page_title FROM entries WHERE id=?", (eid,))
        pt = a.fetchone()[0] or ''
        if pt and len(pt) > 5: score += 10
        
        owner = None
        a.execute("SELECT owner FROM entries WHERE id=?", (eid,))
        row = a.fetchone()
        if row: owner = row[0]
        if owner and len(owner) > 1: score += 10
        
        quality = min(1.0, score / 100)
        
        # Recompute innovation with LLM score
        old_innov = innov
        new_innov = max(old_innov, innovation)  # Take the higher score
        
        # Signal
        feat_score = min(15, feat_count * 3)
        desc_score = min(10, len(long_desc) / 50.0)
        gh_bonus = 5 if is_gh else 0
        signal = min(100, max(0, int(round((new_innov * 4) + (quality * 30) + feat_score + desc_score + gh_bonus))))
        is_standout = 1 if new_innov >= 9 and quality >= 0.8 else 0
        
        # Update entry
        a.execute("""UPDATE entries SET 
            short_description=?, long_description=?, main_features=?, 
            tags=?, innovation=?, quality=?, signal=?, is_standout=?, verdict=?
            WHERE id=?""",
            (short_desc or sd, long_desc, features, json.dumps(clean_tags),
             new_innov, quality, signal, is_standout, '', eid))
        
        # Reclassify if LLM category matches a known layer
        if category:
            # Map old category names to atlas layers
            CAT_MAP = {
                'Connectivity & Interoperability (MCP/A2A)': 'Connectivity / MCP / A2A',
                'Connectivity & Interoperability': 'Connectivity / MCP / A2A',
                'Development Tools & Libraries': 'Coding Tools & IDEs',
                'Vector Databases & Search': 'Vector Databases & Embeddings',
                'Developer Workflow': 'Developer Workflow & Tools',
                'Guides & Articles': 'Guides & Industry Trends',
                'Infrastructure': 'Infrastructure & Proxy Layers',
                'Other': None,
            }
            mapped = CAT_MAP.get(category, category)
            if mapped and mapped in BORG_TAXONOMY:
                # Check if current layer is different
                a.execute("SELECT layer FROM layer_membership WHERE entry_id=? AND is_primary=1", (eid,))
                current = a.fetchone()
                if current and current[0] != mapped:
                    # Check if entry already exists in target layer
                    a.execute("SELECT COUNT(*) FROM layer_membership WHERE entry_id=? AND layer=?", (eid, mapped))
                    if a.fetchone()[0] > 0:
                        a.execute("DELETE FROM layer_membership WHERE entry_id=? AND is_primary=1", (eid,))
                        a.execute("UPDATE layer_membership SET is_primary=1 WHERE entry_id=? AND layer=?", (eid, mapped))
                    else:
                        a.execute("UPDATE layer_membership SET layer=? WHERE entry_id=? AND is_primary=1", (mapped, eid))
                    logger.info("  Reclassified: " + current[0] + " -> " + mapped)
        
        atl.commit()
        accepted += 1
        logger.info(f"  ✅ Enriched (I{new_innov} Q{quality:.2f} ⚡{signal}): {short_desc[:60]}")
        
        time.sleep(1)  # Rate limit
    
    logger.info("=" * 60)
    logger.info(f"Research complete: {accepted} enriched, {rejected} rejected, {failed} failed, {skipped} skipped")
    logger.info("=" * 60)
    
    # Final counts
    a.execute("SELECT COUNT(*) FROM entries")
    total = a.fetchone()[0]
    a.execute("SELECT COUNT(*) FROM entries WHERE is_standout=1")
    standout = a.fetchone()[0]
    logger.info(f"Atlas: {total:,} entries, {standout:,} standout")
    
    atl.close()

if __name__ == "__main__":
    main()
