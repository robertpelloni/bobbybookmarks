import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1py1t6z/release_skill_seekers_v250_multiplatform_support/', 'Development Tools & Libraries', 'Skill Seekers v2.5.0', 'A universal documentation-to-skills converter that deploys generated agent skills across Claude, Gemini, and OpenAI platforms simultaneously.', 'mcp, tools, skills, automation, cross-platform', 'Universal Export formats (ZIP+YAML, grounding, vector), 18 built-in MCP tools, multi-agent deployment, local model enhancement.'),
    ('https://www.reddit.com/r/mcp/comments/1q4iyuh/reticle_a_local_traffic_inspector_for_mcp/', 'Interface & Developer UX', 'Reticle MCP Proxy', 'An open-source, Wireshark-style proxy and traffic inspector designed to solve the "black box" problem of debugging Model Context Protocol communications.', 'mcp, debugging, proxy, observability, reticle', 'Real-time JSON-RPC visibility, token context bloat diagnosis, stderr crash capture, session recording and export.'),
    ('https://www.reddit.com/r/mcp/comments/1q6ipxp/cut_mcp_tool_sprawl_onemcp_is_open_source_give_it/', 'Infrastructure & Proxy Layers', 'OneMCP: Tool Compiler', 'A compiler approach to MCP that translates OpenAPI specs and documentation into cached execution plans to eliminate individual tool sprawl.', 'mcp, compilation, openapi, tool-sprawl, onemcp', 'API-to-MCP compilation, cached execution plans, natural-language to precise-API translation, reduction of hallucinated parameters.'),
    ('https://www.reddit.com/r/mcp/comments/1q6yhmd/daem0nmcp_eternal_memory_for_ai_agents/', 'Memory & Persistence Architecture', 'Daem0n-MCP: Eternal Memory', 'An active memory system using Hybrid Semantic Search and Outcome Reinforcement to force agents to learn from past decisions and avoid repeated failures.', 'mcp, memory, persistence, active-recall, qdrant', 'Hybrid Semantic Search (TF-IDF + Qdrant), Outcome Reinforcement (1.5x boost to failed decisions), background "Dreaming" process, AST code understanding.')
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
print('Successfully injected batch 83.')