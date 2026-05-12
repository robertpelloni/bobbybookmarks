#!/usr/bin/env python3
"""Process incoming_resources.txt into bookmarks.db with scraping and heuristic classification."""

import sqlite3
import sys
import re
import urllib.request
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = 'C:/Users/hyper/workspace/bobbybookmarks/bookmarks.db'
INCOMING_FILE = 'C:/Users/hyper/workspace/bobbybookmarks/incoming_resources.txt'

BORG_CATEGORIES = [
    "Agent Orchestration", "Context Engineering", "Memory & Persistence",
    "Interface/UX", "Connectivity/MCP/A2A", "Infrastructure", "Guides/Trends"
]

GARBAGE_PATTERNS = [
    r'^about:', r'^edge:', r'^chrome:', r'^file:', r'^javascript:',
    r'temu\.com', r'amazon\.com.*/dp/', r'facebook\.com',
    r'reddit\.com/r/(?!AIGuild|AI_Agents|Agent_AI|AIMemory|mcp|MCPservers|LocalLLaMA|LocalLLM|OpenSourceAI|coolgithubprojects|hermesagent|PiCodingAgent|opencodeCLI|OpenaiCodex|GeminiCLI|JulesAgent|LangChain|Rag|superwhisper|aigamedev|multidotdev|StartupMind|ScaleSpace|accelerate|Bard|claudeskills|simpleAIFinds|google_antigravity|nanocoder|tech_x)/',
    r'instagram\.com', r'pinterest\.com', r'tiktok\.com',
    r'walmart\.com', r'target\.com', r'ebay\.com',
    r'discogs\.com', r'google\.com/search', r'duckduckgo\.com',
    r'localhost', r'127\.0\.0\.1',
    r'book\.livingooddailybook\.com', r'portal\.mendfamily\.com',
    r'gofreddie\.com', r'everett-technologies\.com',
    r'rns\.id/app', r'thechilluminati\.com', r'war\.gov',
    r'hervns\.com', r'codingplans\.cc',
]


def normalize_url(url):
    url = url.strip().rstrip('/')
    url = re.sub(r'[\?&](utm_[^&]*|ref=[^&]*|source=[^&]*|campaign=[^&]*|referrer=[^&]*|srsltid=[^&]*|rdt_cid=[^&]*|gad_source=[^&]*|gad_campaignid=[^&]*|gbraid=[^&]*)', '', url)
    url = url.split('#')[0]
    url = url.rstrip('?&')
    return url


def is_garbage(url):
    for pat in GARBAGE_PATTERNS:
        if re.search(pat, url, re.IGNORECASE):
            return True
    return False


def scrape_url(url, timeout=15):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })
        resp = urllib.request.urlopen(req, timeout=timeout, context=ctx)
        html = resp.read().decode('utf-8', errors='replace')[:50000]
        title = ''
        m = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL|re.IGNORECASE)
        if m:
            title = re.sub(r'\s+', ' ', m.group(1)).strip()[:200]
        desc = ''
        m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', html, re.IGNORECASE)
        if m:
            desc = m.group(1).strip()[:500]
        if not desc:
            m = re.search(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']', html, re.IGNORECASE)
            if m:
                desc = m.group(1).strip()[:500]
        if not desc:
            m = re.search(r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']', html, re.IGNORECASE)
            if m:
                desc = m.group(1).strip()[:500]
        content = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL|re.IGNORECASE)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL|re.IGNORECASE)
        content = re.sub(r'<[^>]+>', ' ', content)
        content = re.sub(r'\s+', ' ', content).strip()[:10000]
        return title, desc, content, 200
    except urllib.error.HTTPError as e:
        return '', '', f'HTTP {e.code}', e.code
    except Exception as e:
        return '', '', str(e)[:200], 0


def classify_heuristic(title, desc, content, url):
    text = f"{title} {desc} {content[:3000]}".lower()
    scores = {}
    scores["Agent Orchestration"] = sum(1 for kw in ['agent', 'orchestrat', 'workflow', 'autonomous', 'multi-agent', 'swarm', 'sub-agent', 'task delegation', 'plan-execute', 'codex', 'hermes agent', 'coding agent', 'spec', 'kanban'] if kw in text)
    scores["Context Engineering"] = sum(1 for kw in ['context', 'chunk', 'token reduction', 'schema injection', 'compaction', 'distillat', 'codebase mapping', 'code mode', 'token usage', 'rag', 'retrieval', 'indexing', 'embedding'] if kw in text)
    scores["Memory & Persistence"] = sum(1 for kw in ['memory', 'persist', 'recall', 'cross-session', 'knowledge graph', 'vector store', 'episodic', 'semantic memory', 'mem0', 'memgraph', 'memweave', 'long-term', 'forgetting', 'decay', 'consolidation', 'sqlite', 'graph database', 'typed memory', 'mnemos'] if kw in text)
    scores["Interface/UX"] = sum(1 for kw in ['interface', 'ux', 'dashboard', 'gui', 'ide', 'editor', 'workspace', 'panel', 'visualization', 'theme', 'layout', 'screen', 'desktop app'] if kw in text)
    scores["Connectivity/MCP/A2A"] = sum(1 for kw in ['mcp', 'model context protocol', 'mcp server', 'a2a', 'interop', 'protocol', 'gateway', 'proxy', 'relay', 'bridge', 'skill', 'tool registry', 'registry'] if kw in text)
    scores["Infrastructure"] = sum(1 for kw in ['infra', 'deploy', 'docker', 'kubernetes', 'ci/cd', 'build', 'runtime', 'sandbox', 'vm', 'microvm', 'execution', 'server', 'hosting', 'proxmox', 'template'] if kw in text)
    scores["Guides/Trends"] = sum(1 for kw in ['guide', 'tutorial', 'awesome', 'collection', 'curated', 'trend', 'best practice', 'blueprint', 'comparison', 'benchmark', 'analysis', 'index'] if kw in text)

    if max(scores.values()) == 0:
        return "Guides/Trends", 5, title or f"Resource at {url[:60]}", "Web resource", "resource"

    best_cat = max(scores, key=scores.get)
    innovation = 7
    if any(kw in text for kw in ['novel', 'breakthrough', 'pioneer']):
        innovation = 9
    if any(kw in text for kw in ['mcp server', 'knowledge graph', 'memory tier', 'self-heal', 'autonomous']):
        innovation = 9
    if any(kw in text for kw in ['vector', 'graph', 'embed', 'semantic', 'hybrid']):
        innovation = 8
    if 'awesome' in text or 'list' in text:
        innovation = min(innovation, 6)

    features = []
    feature_keywords = [
        ('memory', 'Persistent memory'), ('mcp', 'MCP integration'),
        ('knowledge graph', 'Knowledge graph'), ('vector', 'Vector search'),
        ('sqlite', 'SQLite storage'), ('agent', 'Agent support'),
        ('session', 'Cross-session persistence'), ('graph', 'Graph relationships'),
        ('semantic', 'Semantic search'), ('api', 'API integration'),
        ('docker', 'Docker deployment'), ('rag', 'RAG pipeline'),
        ('orchestrat', 'Orchestration'), ('skill', 'Skill system'),
        ('tool', 'Tool integration'), ('proxy', 'Proxy/gateway'),
        ('trace', 'Tracing/observability'),
    ]
    for kw, feat_name in feature_keywords:
        if kw in text and feat_name not in features:
            features.append(feat_name)
    feature_str = ', '.join(features[:8]) if features else 'Web content resource'

    tag_words = []
    tag_keywords = ['memory', 'mcp', 'agent', 'coding', 'rag', 'vector', 'graph', 'context', 'tool', 'automation', 'llm', 'ai', 'claude', 'codex', 'orchestration', 'trace', 'proxy', 'gateway', 'skill', 'hermes']
    for tag_kw in tag_keywords:
        if tag_kw in text and tag_kw not in tag_words:
            tag_words.append(tag_kw)
    tag_str = ', '.join(tag_words[:10]) if tag_words else 'resource'

    return best_cat, innovation, desc[:300] if desc else (title or url[:60]), feature_str, tag_str


def main():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM bookmarks WHERE research_level='borg'")
    borg_before = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM bookmarks")
    total_before = c.fetchone()[0]
    print(f"DB before: {total_before} total, {borg_before} borg-researched")

    c.execute("SELECT url FROM bookmarks")
    existing_normalized = set(normalize_url(row[0]) for row in c.fetchall())

    with open(INCOMING_FILE, 'r', encoding='utf-8') as f:
        incoming = [line.strip() for line in f if line.strip()]
    print(f"Incoming URLs: {len(incoming)}")

    new_urls = []
    seen = set()
    for url in incoming:
        if is_garbage(url):
            continue
        norm = normalize_url(url)
        if not norm.startswith('http'):
            continue
        norm_repo = re.sub(r'/blob/main/.*', '', norm)
        norm_repo = re.sub(r'/tree/main/.*', '', norm_repo)
        if norm_repo in existing_normalized or norm in existing_normalized:
            continue
        domain_key = re.sub(r'\?.*', '', norm_repo)
        if domain_key in seen:
            continue
        seen.add(domain_key)
        new_urls.append(norm)

    print(f"New URLs after dedup+filter: {len(new_urls)}")
    print()

    success = 0
    fail = 0
    inserted = 0

    for i, url in enumerate(new_urls):
        print(f"[{i+1}/{len(new_urls)}] {url[:100]}")

        title, desc, content, http_status = scrape_url(url)

        if not title and not desc and not content:
            print("  SKIP: Empty result")
            fail += 1
            continue

        is_error = isinstance(content, str) and (content.startswith('HTTP ') or content.startswith('urllib') or content.startswith('ssl:') or content.startswith('Connection') or content.startswith('Timeout'))

        if is_error:
            category = "Guides/Trends"
            innovation = 4
            short_desc = f"Resource at {url[:60]}"
            features = "Web resource"
            tags = "resource"
        else:
            category, innovation, short_desc, features, tags = classify_heuristic(title, desc, content, url)

        gh_match = re.match(r'https?://github\.com/([^/]+)/([^/]+)', url)
        if gh_match and title:
            title = re.sub(r'\s*[-:·]\s*GitHub\s*$', '', title, flags=re.IGNORECASE).strip()

        now = time.strftime('%Y-%m-%d %H:%M:%S')

        try:
            c.execute('''INSERT OR IGNORE INTO bookmarks 
                (url, category, short_description, long_description, tags, main_features,
                 created_at, research_level, innovation_score, normalized_url, title,
                 description, source, imported_at, is_duplicate, duplicate_of,
                 research_status, http_status, page_title, page_description,
                 researched_at, quality_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (url, category, short_desc, content[:5000] if not is_error else '', tags, features,
                 now, 'borg', str(innovation), normalize_url(url), title or '',
                 desc or '', 'incoming_resources.txt', now, 0, None,
                 'researched', http_status, title or '', desc or '',
                 now, 1 if http_status == 200 else 0))

            if c.rowcount > 0:
                inserted += 1
                print(f"  OK: {category} | score:{innovation} | {(short_desc or '')[:80]}")
            else:
                print("  DUP: Already exists")
        except Exception as e:
            print(f"  ERR: {str(e)[:80]}")
            fail += 1

        success += 1
        time.sleep(0.3)

    conn.commit()

    c.execute("SELECT COUNT(*) FROM bookmarks WHERE research_level='borg'")
    borg_after = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM bookmarks")
    total_after = c.fetchone()[0]

    print(f"\n{'='*60}")
    print("PROCESSING COMPLETE")
    print(f"{'='*60}")
    print(f"Attempted: {len(new_urls)}")
    print(f"Scraped OK: {success}")
    print(f"Failed: {fail}")
    print(f"Inserted: {inserted}")
    print(f"DB: {total_before} -> {total_after} total, {borg_before} -> {borg_after} borg")

    conn.close()


if __name__ == '__main__':
    main()
