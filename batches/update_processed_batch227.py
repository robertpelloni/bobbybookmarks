import sqlite3

data = [
    ('https://github.com/diegosouzapw/OmniRoute', 'Infrastructure & Proxy Layers', 'OmniRoute: AI Gateway', 'A high-performance AI gateway providing a single OpenAI-compatible endpoint with built-in TLS fingerprint spoofing and smart load balancing to bypass bot detection.', 'gateway, proxy, routing, stealth, anti-bot', 'TLS Fingerprint spoofing (wreq-js), smart multi-provider load balancing, built-in circuit breakers, real-time terminal-style observability logs.'),
    ('https://github.com/obsessiondb/rudel', 'Agent Orchestration & Workflow', 'Rudel: Claude Analytics', 'An analytics platform and CLI tool designed specifically for teams using Claude Code, tracking session metadata, agent usage, and codebase context via ClickHouse.', 'analytics, claude-code, observability, teamwork, workflow', 'Automated session transcript uploads via hooks, ClickHouse-powered metrics, Git contextual metadata tracking (branch/SHA), team-wide privacy controls.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1rowe0e/symdex_opensource_mcp_codeindexer_that_cuts_ai', 'Context Engineering & Isolation', 'SymDex: MCP Indexer', 'A high-efficiency MCP server that pre-indexes repository symbols to reduce agent token consumption by 97%, replacing expensive file reads with targeted semantic lookups.', 'mcp, indexing, context-engineering, optimization, rag', '97% token reduction (3,400 to 100 per lookup), Call Graph dependency tracking, SymDex Watch native OS incremental indexing, privacy-first local search.'),
    ('https://github.com/pbakaus/impeccable', 'Interface & Developer UX', 'Impeccable: AI Capture', 'A specialized web capturing tool designed to generate "AI-Ready" structured snapshots of pixel-perfect UI layouts, optimizing complex frontends for Vision-Language Models.', 'vision, testing, ui-capture, computer-vision, dev-tools', 'Pixel-perfect CSS/layout state capture, AI-optimized structured data output, visual regression QA integration, high-performance execution.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 10) for d in data]:
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
    ''', (url, cat, sd, ld, tags, mf, score))
conn.commit()
conn.close()
print('Successfully injected batch 187.')