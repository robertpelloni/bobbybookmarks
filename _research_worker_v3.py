#!/usr/bin/env python3
"""Borg Research Worker v2.3 - Optimized enrichment with adaptive model selection"""
import os, re, json, sqlite3, requests, time, logging, sys
from datetime import datetime
from bs4 import BeautifulSoup, Comment
from urllib.parse import urlparse
sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler('logs/research_run.log', mode='a', encoding='utf-8'),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

ATLAS_DB = 'atlas.db'
LMSTUDIO_URL = "http://localhost:1234/v1/chat/completions"

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

# Model tiers - ordered by speed
TIER_FAST = "liquid/lfm2.5-1.2b"           # ~2-3s, 1.2B params
TIER_MEDIUM = "gemma-4-e2b-uncensored-hauhaucs-aggressive"  # ~5-8s, 2B active
TIER_LARGE = "gemma-4-26b-a4b-it-heretic-ara"  # ~15-20s, 26B params


def stringify(v):
    if v is None: return ''
    if isinstance(v, str): return v
    if isinstance(v, (list, tuple)): return ', '.join(str(x) for x in v)
    return str(v)


def call_llm(prompt, model=TIER_FAST, timeout=30):
    """Call a specific LM Studio model."""
    try:
        resp = requests.post(LMSTUDIO_URL, json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 500,
        }, timeout=timeout)
        if resp.status_code == 200:
            data = resp.json()
            text = data.get('choices', [{}])[0].get('message', {}).get('content', '')
            if text and len(text) > 30:
                return text, model
    except requests.exceptions.Timeout:
        logger.warning(f"  Timeout ({timeout}s) on {model}")
    except Exception as e:
        logger.warning(f"  Error on {model}: {str(e)[:80]}")
    return None, None


def call_llm_with_fallback(prompt, preferred_model=TIER_FAST, timeout=40):
    """Try preferred model, then ONE fallback. Don't burn time on triple-timeout."""
    # Try preferred (fast)
    result, model = call_llm(prompt, preferred_model, timeout)
    if result:
        return result, model

    # Single fallback to medium model only
    result, model = call_llm(prompt, TIER_MEDIUM, timeout=60)
    if result:
        return result, model

    return None, None


def fetch_content(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        resp = requests.get(url, headers=headers, timeout=12, allow_redirects=True)
        if resp.status_code == 200:
            return resp.text
    except Exception:
        pass
    return None


def extract_fit_markdown(html, url=""):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(['script', 'style', 'nav', 'footer', 'header', 'aside',
                               'iframe', 'noscript', 'svg', 'button', 'form']):
        tag.decompose()
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()
    main = None
    for sel in ['main', 'article', '[role="main"]', '.content', '#content',
                '.post-body', '.markdown-body', '.readme', '#readme', '.entry-content']:
        main = soup.select_one(sel)
        if main: break
    if not main: main = soup.find('body') or soup
    text = main.get_text(separator='\n', strip=True)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    text = '\n'.join(lines)
    return text[:3000]  # Reduced from 5000 to speed up LLM calls


def extract_gh_meta(url, html):
    meta = {}
    soup = BeautifulSoup(html, 'html.parser')
    about = soup.find('p', class_='f4 my-3')
    if about: meta['desc'] = about.get_text(strip=True)
    topics = soup.find_all('a', class_='topic-tag')
    if topics: meta['topics'] = [t.get_text(strip=True) for t in topics]
    readme = soup.find('div', class_='markdown-body')
    if readme: meta['readme'] = readme.get_text(separator='\n', strip=True)[:2000]
    return meta


def build_prompt(url, fit_text, gh_meta=None, compact=False):
    if compact:
        # Ultra-compact prompt for maximum speed
        prompt = f"Classify: {url}\n"
        if gh_meta:
            if 'desc' in gh_meta: prompt += f"Repo: {gh_meta['desc']}\n"
            if 'topics' in gh_meta: prompt += f"Topics: {', '.join(gh_meta['topics'][:5])}\n"
        prompt += f"Content: {fit_text[:1500]}\n\n"
        prompt += "Cats: " + ", ".join(BORG_TAXONOMY) + "\n"
        prompt += ('JSON: {"CATEGORY":"","SHORT_DESCRIPTION":"1 sentence","LONG_DESCRIPTION":"2-3 sentences",'
                   '"MAIN_FEATURES":"3-5 comma separated","INNOVATION_SCORE":8,"TAGS":"tag1,tag2,tag3"}\n')
    else:
        # Standard prompt
        prompt = "Classify this resource. URL: " + url + "\n"
        if gh_meta:
            if 'desc' in gh_meta: prompt += "\nRepo: " + gh_meta['desc'] + "\n"
            if 'topics' in gh_meta: prompt += "Topics: " + ", ".join(gh_meta['topics'][:5]) + "\n"
        prompt += "\nContent:\n" + fit_text + "\n\n"
        prompt += "Category (pick one): " + ", ".join(BORG_TAXONOMY) + "\n\n"
        prompt += ('Return JSON:\n'
                   '- CATEGORY: one category above\n'
                   '- SHORT_DESCRIPTION: 1 specific sentence\n'
                   '- LONG_DESCRIPTION: 2-3 sentences\n'
                   '- MAIN_FEATURES: 3-5 specific features (comma separated)\n'
                   '- INNOVATION_SCORE: 1-10\n'
                   '- TAGS: 8-12 lowercase hyphenated tags (comma separated)\n')
    return prompt


def is_garbage(rdata):
    desc = stringify(rdata.get('SHORT_DESCRIPTION', '')).lower().strip()
    feats = stringify(rdata.get('MAIN_FEATURES', '')).lower().strip()
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


def reclassify_entry(a, eid, mapped):
    a.execute("SELECT layer FROM layer_membership WHERE entry_id=? AND is_primary=1", (eid,))
    current = a.fetchone()
    if not current or current[0] == mapped:
        return
    old_layer = current[0]
    a.execute("SELECT COUNT(*) FROM layer_membership WHERE entry_id=? AND layer=?", (eid, mapped))
    if a.fetchone()[0] > 0:
        a.execute("DELETE FROM layer_membership WHERE entry_id=? AND is_primary=1", (eid,))
        a.execute("UPDATE layer_membership SET is_primary=1 WHERE entry_id=? AND layer=?", (eid, mapped))
    else:
        a.execute("UPDATE layer_membership SET layer=? WHERE entry_id=? AND is_primary=1", (mapped, eid))
    logger.info(f"  Reclassified: {old_layer} -> {mapped}")


def main():
    atl = sqlite3.connect(ATLAS_DB)
    a = atl.cursor()

    # Find entries that need enrichment
    a.execute("""SELECT e.id, e.url, e.short_description, e.is_github, e.innovation
        FROM entries e
        WHERE (e.long_description = e.short_description OR LENGTH(e.long_description) < 50)
        ORDER BY e.is_github DESC, e.id DESC""")
    all_entries = a.fetchall()

    logger.info(f"Borg Research Worker v2.3 starting")
    logger.info(f"Entries to research: {len(all_entries):,}")

    accepted = 0
    rejected = 0
    failed = 0
    skipped = 0
    model_stats = {}

    for idx, (eid, url, sd, is_gh, innov) in enumerate(all_entries):
        logger.info(f"[{idx+1}/{len(all_entries)}] Researching: {url[:80]}")

        # Fetch content
        content = fetch_content(url)
        if not content:
            logger.warning(f"  Fetch failed")
            failed += 1
            continue

        fit_text = extract_fit_markdown(content, url)
        if len(fit_text) < 50:
            logger.warning(f"  Content too thin ({len(fit_text)}ch)")
            skipped += 1
            continue

        # Extract GitHub metadata if applicable
        gh_meta = None
        if is_gh:
            gh_meta = extract_gh_meta(url, content)

        # Choose model based on content complexity
        content_len = len(fit_text)
        has_gh_meta = gh_meta and ('desc' in gh_meta or 'topics' in gh_meta)

        # Always use fast model first - it's reliable and fast
        # The larger models keep timing out on complex prompts
        preferred = TIER_FAST
        compact = False  # Use full prompt format for quality

        prompt = build_prompt(url, fit_text, gh_meta, compact=compact)
        raw, model = call_llm_with_fallback(prompt, preferred)

        if not raw:
            logger.warning(f"  LLM failed (all models)")
            failed += 1
            continue

        model_stats[model] = model_stats.get(model, 0) + 1

        # Parse JSON response
        try:
            text = raw.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()

            # Try direct parse first
            try:
                rdata = json.loads(text)
            except json.JSONDecodeError:
                # Extract JSON with balanced braces (handles nested objects)
                start = text.find('{')
                if start >= 0:
                    depth = 0
                    end = start
                    for i in range(start, len(text)):
                        if text[i] == '{': depth += 1
                        elif text[i] == '}': depth -= 1
                        if depth == 0:
                            end = i + 1
                            break
                    if end > start:
                        rdata = json.loads(text[start:end])
                    else:
                        raise
                else:
                    raise
        except (json.JSONDecodeError, ValueError) as e:
            logger.warning(f"  JSON decode error: {str(e)[:60]}")
            failed += 1
            continue

        # Garbage check
        garbage, reason = is_garbage(rdata)
        if garbage:
            logger.warning(f"  Garbage ({reason})")
            rejected += 1
            continue

        # Extract and normalize
        category = stringify(rdata.get('CATEGORY', '')).strip()
        short_desc = stringify(rdata.get('SHORT_DESCRIPTION', '')).strip()
        long_desc = stringify(rdata.get('LONG_DESCRIPTION', '')).strip() or short_desc
        features = stringify(rdata.get('MAIN_FEATURES', '')).strip()
        tags_str = stringify(rdata.get('TAGS', '')).strip()
        innovation = rdata.get('INNOVATION_SCORE', 8)
        try: innovation = int(innovation)
        except: innovation = 8
        innovation = max(1, min(10, innovation))

        # Normalize tags
        tags = [t.strip().lower().replace(' ', '-').replace('_', '-') for t in tags_str.split(',') if t.strip()]
        seen_tags = set()
        clean_tags = []
        for t in tags:
            if t not in seen_tags:
                seen_tags.add(t)
                clean_tags.append(t)

        # Compute quality score
        score = 0.0
        ld_len = len(long_desc)
        if ld_len > 500: score += 30
        elif ld_len > 300: score += 25
        elif ld_len > 150: score += 20
        elif ld_len > 50: score += 12
        elif ld_len > 10: score += 6

        feat_count = len([x.strip() for x in features.split(',') if x.strip() and len(x.strip()) > 3])
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

        a.execute("SELECT page_title FROM entries WHERE id=?", (eid,))
        row = a.fetchone()
        pt = row[0] if row else ''
        if pt and len(pt) > 5: score += 10

        a.execute("SELECT owner FROM entries WHERE id=?", (eid,))
        row = a.fetchone()
        owner = row[0] if row else None
        if owner and len(owner) > 1: score += 10

        quality = min(1.0, score / 100)
        new_innov = max(innov, innovation)

        feat_score = min(15, feat_count * 3)
        desc_score = min(10, len(long_desc) / 50.0)
        gh_bonus = 5 if is_gh else 0
        signal = min(100, max(0, int(round(
            (new_innov * 4) + (quality * 30) + feat_score + desc_score + gh_bonus
        ))))
        is_standout = 1 if new_innov >= 9 and quality >= 0.8 else 0

        # Update entry
        a.execute("""UPDATE entries SET
            short_description=?, long_description=?, main_features=?,
            tags=?, innovation=?, quality=?, signal=?, is_standout=?, verdict=?
            WHERE id=?""",
            (short_desc or sd, long_desc, features, json.dumps(clean_tags),
             new_innov, quality, signal, is_standout, '', eid))

        # Reclassify
        mapped = CAT_MAP.get(category, category)
        if mapped and mapped in BORG_TAXONOMY:
            reclassify_entry(a, eid, mapped)

        atl.commit()
        accepted += 1
        logger.info(f"  OK [{model[:20]}] I{new_innov} Q{quality:.2f} S{signal}: {short_desc[:60]}")

        time.sleep(1)

    # Final summary
    logger.info("=" * 60)
    logger.info(f"Research complete: {accepted} enriched, {rejected} rejected, {failed} failed, {skipped} skipped")
    logger.info(f"Model usage: {model_stats}")
    logger.info("=" * 60)

    a.execute("SELECT COUNT(*) FROM entries")
    total = a.fetchone()[0]
    a.execute("SELECT COUNT(*) FROM entries WHERE is_standout=1")
    standout = a.fetchone()[0]
    a.execute("SELECT COUNT(*) FROM entries WHERE LENGTH(long_description) > 50 AND long_description != short_description")
    enriched = a.fetchone()[0]
    logger.info(f"Atlas: {total:,} entries, {enriched:,} enriched, {standout:,} standout")

    atl.close()


if __name__ == "__main__":
    main()
