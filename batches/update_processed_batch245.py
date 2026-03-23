import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1rwg27s/introducing_smriti_mcp_human_like_memory_for_ai/', 'Memory & Persistence Architecture', 'Smriti MCP: Associative Memory', 'An MCP server that moves beyond simple vector search by mimicking human associative memory, where thoughts trigger related concepts based on recency and reinforcement.', 'mcp, memory, associative-memory, cognitive-science, persistence', 'Associative memory graph ("thought trails"), memory decay and reinforcement mechanics, namespace isolation, SQLite FTS5 backend.'),
    ('https://www.reddit.com/r/mcp/comments/1rvg0z1/turbomcp_studio_full_featured_mcp_suite_for/', 'Development Tools & Libraries', 'TurboMCP Studio: Testing Suite', 'A native desktop application (Rust/Tauri) often described as "Postman for MCP," designed for developing, testing, and debugging MCP servers and prompts.', 'mcp, dev-tools, debugging, rust, tauri', 'Visual Tool & Resource Explorer, built-in Prompt Designer, low-level MCP protocol inspector, SIMD-accelerated multi-transport support (STDIO/HTTP/SSE).'),
    ('https://github.com/builderz-labs/mission-control', 'Agent Orchestration & Workflow', 'Mission Control: Agent Fleet', 'An open-source, local-first orchestration dashboard designed for managing and monitoring fleets of AI agents across complex software development tasks.', 'orchestration, dashboard, multi-agent, local-first, workflow', '32 Real-Time telemetry panels, "Aegis" Quality Gates (human/agent review blocking), GitHub Issue to Kanban sync, built-in Skills Hub registry.'),
    ('https://github.com/jarrodwatts/claude-hud', 'Interface & Developer UX', 'Claude HUD: Context Monitor', 'A terminal plugin for Claude Code that provides a real-time "Heads-Up Display" tracking context window health, tool usage, and background task progress.', 'claude-code, plugins, ux, dev-tools, telemetry', 'Real-time context window "health" monitoring, active sub-agent tracking, in-terminal TODO progress visualization, zero-config plugin installation.')
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
print('Successfully injected batch 205.')