import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1pqliuz/anthropics_agent_skills_new_open_standard/', 'AI Agents & Frameworks', 'Anthropic Agent Skills', 'An open standard for agent capabilities using a "Progressive Disclosure" model to load instructions only when relevant.', 'skills, standard, anthropic, progressive-disclosure, context-efficiency', 'SKILL.md directory structure, Progressive Disclosure (Summary -> Instruction -> Asset), multi-platform adoption (OpenAI/GitHub).'),
    ('https://www.reddit.com/r/mcp/comments/1pswgh2/mcp_is_broken_and_anthropic_just_admitted_it/', 'Guides & Industry Trends', 'MCP Cognitive Overload', 'A viral critique highlighting how static upfront exposure of massive MCP schemas (50k+ tokens) leads to agent hallucinations and planning failures.', 'mcp, critique, context-bloat, cognitive-overload, planning-failure', 'Analysis of schema bloat, context window exhaustion, "Static vs Dynamic" loading debate, need for governance layers.'),
    ('https://www.reddit.com/r/mcp/comments/1ptd3ck/stop_wasting_your_context_window_ltp_lazy_tool/', 'Context Engineering & Isolation', 'Lazy Tool Protocol (LTP)', 'An architectural shift arguing that orchestration belongs in the server, proposing "Lazy" tool calls that return only necessary outcomes to prevent token pollution.', 'ltp, context-optimization, tool-calling, token-reduction, architecture', 'Server-side orchestration, prevention of raw API payload pollution, outcome-based tool responses, context preservation.'),
    ('https://www.reddit.com/r/mcp/comments/1ptwtsv/we_opensourced_an_mcp_server_gateway_after/', 'Infrastructure & Proxy Layers', 'MCP Server Gateway', 'Open-source gateways designed to aggregate multiple MCP servers into a single endpoint, adding crucial layers for permissioning, logging, and rate-limiting.', 'mcp, gateway, aggregation, security, governance', 'Centralized MCP management, tool filtering based on session intent, security permissioning, rate-limiting and logging.')
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
print('Successfully injected batch 82.')