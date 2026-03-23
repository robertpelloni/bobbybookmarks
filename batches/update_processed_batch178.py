import sqlite3

data = [
    ('https://github.com/cloudflare/agents/blob/main/docs/codemode.md', 'Agent Orchestration & Workflow', 'Cloudflare Code Mode', 'A programmatic tool-calling paradigm that reduces context usage by 99.9% by allowing agents to write and execute sandboxed SDK code instead of individual API calls.', 'code-mode, cloudflare, optimization, tokens, security', '99.9% token reduction, sandboxed V8 Worker execution, automatic SDK generation, five core production patterns (Routing/Parallelization/etc.).'),
    ('https://github.com/coleam00/mcp-mem0', 'Memory & Persistence Architecture', 'MCP-Mem0: Persistent Context', 'A Model Context Protocol implementation of Mem0 that provides agents with persistent, searchable long-term memory across sessions and restarts.', 'mcp, mem0, memory, persistence, context-management', 'Persistent memory storage, semantic search/recall tools, autonomous fact extraction (Add/Update/Delete), local-first SQLite/ChromaDB support.'),
    ('https://github.com/ComposioHQ/awesome-claude-skills', 'Infrastructure & Proxy Layers', 'Composio: Skill Action Engine', 'A unified framework wrapping 860+ SaaS apps into "Skills" with managed OAuth, progressive disclosure loading, and secure remote code execution.', 'mcp, skills, saas, automation, security', 'Unified OAuth/Auth management, Progressive Disclosure loading (100 token match), 860+ SaaS integrations, remote code execution sandbox.'),
    ('https://github.com/CopilotKit/open-mcp-client', 'Interface & Developer UX', 'CopilotKit: Generative UI', 'An MCP client implementation focused on Generative UI (AG-UI protocol) to bring interactive elements and state synchronization into the agent experience.', 'mcp, generative-ui, ag-ui, ux, frontend', 'AG-UI protocol standardization, Generative UI support (ui:// references), sandboxed iframe MCP apps, real-time agent/user state sync.')
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
print('Successfully injected batch 128.')