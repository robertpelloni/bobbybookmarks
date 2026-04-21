import sqlite3

data = [
    ('https://github.com/aayoawoyemi/Ori-Mnemos', 'Memory & Persistence Architecture', 'Ori-Mnemos: Identity Memory', 'A persistent memory layer and MCP server for AI agents utilizing a "Recursive Memory Harness" to maintain persona consistency and long-term knowledge.', 'memory, persistence, mcp, knowledge-graph, identity', 'Markdown-native knowledge graph, "Vitality Model" memory decay/promotion, 3-signal retrieval (Semantic + BM25 + PageRank), automatic session identity injection.'),
    ('https://github.com/mazrean/dockportless', 'Infrastructure & Proxy Layers', 'dockportless: Zero-Port', 'A local Zig-based service router that eliminates Docker port conflicts by assigning "pretty" local URLs and routing traffic without exposing host ports.', 'docker, infrastructure, networking, proxy, development', 'Zero-config automatic port assignment, `<service>.<project>.localhost` routing, parallel git worktree support (isolated instances), SO_REUSEPORT multi-process proxy.'),
    ('https://getviktor.com/product', 'Agent Orchestration & Workflow', 'Viktor: Autonomous Slack Agent', 'An autonomous "AI Coworker" that integrates deeply into Slack and internal tools to proactively execute multi-step workflows without waiting for prompts.', 'orchestration, slack, automation, enterprise, autonomous', 'Proactive, unprompted task execution, 3000+ deep tool integrations (Linear/GitHub/Ads), cloud sandbox for code execution, multi-week persistent memory.'),
    ('https://github.com/oldany/dropmind', 'Interface & Developer UX', 'DropMind: Lightweight Cache', 'A self-hosted, lightweight "memory cache" PWA designed for the rapid capture, categorization, and retrieval of digital thoughts, links, and files.', 'pwa, self-hosted, memory, capture, productivity', 'Message-style rapid capture inbox, multi-clipboard organization, PWA cross-platform sync (Docker deployed), Apple Shortcuts / Android Share native integration.')
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
print('Successfully injected batch 191.')