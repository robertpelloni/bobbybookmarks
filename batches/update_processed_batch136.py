import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1q0e48x/cairn_mcp_memory_server_with_threetier_capture/', 'Memory & Persistence Architecture', 'Cairn MCP Memory Server', 'An open-source memory server automating agent recall via a three-tier capture system: silent logging, explicit trail markers, and organic insights.', 'mcp, memory, persistence, context-management, cairn', 'Three-tier capture logic, silent lifecycle logging, explicit trail markers (cairns), session resumption capabilities.'),
    ('https://www.reddit.com/r/mcp/comments/1r19i1q/built_mcp_support_into_bifrost_llm_gateway_your/', 'Infrastructure & Proxy Layers', 'Bifrost LLM Gateway', 'A high-performance Go-based gateway that aggregates MCP servers and features a "Code Mode" to orchestrate multiple tool calls in a single request.', 'mcp, gateway, proxy, optimization, bifrost', 'Code Mode tool orchestration (40% lower latency), unified MCP aggregation, OAuth 2.0 authentication, observability UI.'),
    ('https://www.reddit.com/r/mcp/comments/1r2m7ev/chromes_webmcp_makes_ai_agents_stop_pretending/', 'Connectivity & Interoperability (MCP/A2A)', 'Chrome WebMCP Standard', 'A proposed web standard allowing websites to expose structured, callable APIs directly to agents via the navigator.modelContext API.', 'webmcp, standards, browser, automation, api', 'navigator.modelContext API, Declarative HTML-to-tool conversion, Imperative JS functions, elimination of fragile UI scraping.'),
    ('https://www.reddit.com/r/mcp/comments/1r3q5wr/camofox_mcp_antidetection_browser_mcp_server_with/', 'Development Tools & Libraries', 'CamoFox Anti-Detection MCP', 'A specialized browser automation MCP server that mimics human-like fingerprints to bypass bot protection, offering accessibility tree snapshots for token efficiency.', 'mcp, browser-automation, stealth, scraping, tokens', 'Stealth human fingerprinting, accessibility tree snapshots (90% token reduction), persistent multi-tab state, cookie import/export.')
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
print('Successfully injected batch 86.')