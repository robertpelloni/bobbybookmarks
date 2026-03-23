import sqlite3

data = [
    ('https://www.reddit.com/r/kiroIDE/comments/1rrffc2/i_indexed_45k_ai_agent_skills_into_an_open_source/', 'Context Engineering & Isolation', '4.5k Agent Skills Index', 'A massive open-source initiative organizing 4,500+ unique AI agent skills into a standardized "Universal Skill Registry," effectively creating an NPM for agent capabilities.', 'skills, indexing, context-engineering, registry, open-source', '4,500+ standardized agent skills (SKILL.md), cross-framework compatibility (CrewAI/LangGraph), "hot-swappable" capability modularity.'),
    ('https://www.reddit.com/r/mcp/comments/1rrf1sh/i_built_100_mcp_servers_well_technically_its_one/', 'Infrastructure & Proxy Layers', 'Meta-MCP Gateway Pattern', 'An architectural pattern where a single Meta-MCP Gateway dynamically routes requests to 100+ "virtual" MCP servers to bypass resource limits in IDE clients.', 'mcp, gateway, architecture, optimization, routing', 'Dynamic on-demand tool loading, monolithic gateway / micro-plugin architecture, memory/resource bloat reduction in local IDEs.'),
    ('https://www.reddit.com/r/mcp/comments/1rr31ee/mcp_is_up_to_32_more_expensive_than_cli/', 'Guides & Industry Trends', 'MCP Token Overhead Audit', 'A 2026 cost-analysis report revealing that the JSON-RPC handshakes and schema verbosity of the Model Context Protocol incur a 32% API cost premium compared to raw CLI tool execution.', 'mcp, cost-analysis, tokens, benchmarks, optimization', '32% token overhead penalty vs raw CLI, strict JSON schema verbosity bloat, tradeoff between safety/structure and token efficiency.'),
    ('https://www.reddit.com/r/DeepSeek/comments/1rr863d/hunter_alpha_model_on_openrouter_1t_params_1m/', 'AI Agents & Frameworks', 'Hunter Alpha (DeepSeek V4)', 'A stealth 1-Trillion parameter MoE model released on OpenRouter, widely suspected to be an early test of DeepSeek V4, optimized for massive 1M token agentic workflows.', 'models, deepseek, 1t-params, agent-core, inference', '1 Trillion parameter MoE architecture, 1M token context window, optimized for long-horizon agentic planning, free/low-cost experimental tier.')
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
print('Successfully injected batch 193.')