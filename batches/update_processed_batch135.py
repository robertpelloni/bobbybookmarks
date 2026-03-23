import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1qpn0d5/lada2a_how_ai_agents_find_each_other_on_local/', 'Connectivity & Interoperability (MCP/A2A)', 'LAD/A2A: Agent Discovery', 'An open discovery protocol using mDNS/DNS-SD to allow AI assistants to automatically find and connect with other local agents on a network.', 'a2a, discovery, networking, mdns, protocol', 'Zero-configuration mDNS discovery, TLS security, signed AgentCards, Decentralized Identifiers (DIDs).'),
    ('https://www.reddit.com/r/mcp/comments/1qlw3r1/polymcp_transform_any_python_function_into_an_mcp/', 'Development Tools & Libraries', 'PolyMCP: Function Exposure', 'A framework that transforms legacy Python or TypeScript functions into AI-ready MCP tools with single-line decorators.', 'mcp, typescript, python, orchestration, legacy-code', 'Cross-language support (Python/TS), automatic input/output validation, unified agent orchestration layer, production guardrails.'),
    ('https://www.reddit.com/r/mcp/comments/1qi86q3/i_built_receipts_for_ai_agents_so_i_can_see/', 'Infrastructure & Proxy Layers', 'Mantora: AI Receipts', 'An open-source MCP proxy for databases that intercepts SQL queries to provide active guardrails and shareable Markdown audit trails ("Receipts").', 'mcp, database, security, audit, mantora', 'Active SQL guardrails (blocks DROP/DELETE), Markdown receipt generation, real-time UI monitoring ("Network Tab for AI").'),
    ('https://www.reddit.com/r/mcp/comments/1qjzh6v/thirdeyemcp_a_privacyfirst_screen_capture_mcp/', 'Interface & Developer UX', 'ThirdEye-MCP: Screen Capture', 'A specialized MCP server enabling AI agents to capture visual context from a user\'s screen with strict privacy controls.', 'mcp, vision, screen-capture, privacy, context', 'Privacy-first visual capture, granular user-defined visibility controls, Claude Desktop / Antigravity integration.')
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
print('Successfully injected batch 85.')