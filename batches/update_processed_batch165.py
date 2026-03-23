import sqlite3

data = [
    ('https://docs.mcphubx.com/', 'Connectivity & Interoperability (MCP/A2A)', 'MCPHubX: Tool Registry', 'A centralized discovery and management platform for the MCP ecosystem, featuring one-click deployment, community ratings, and developer templates.', 'mcp, registry, discovery, ecosystem, management', 'One-click server deployment, centralized tool registry, reliability/skill ratings, developer schema templates.'),
    ('https://docs.roocode.com/roo-code-cloud/roomote-control', 'Interface & Developer UX', 'Roo Code: Roomote Control', 'A bidirectional remote control suite for Roo Code that enables real-time task monitoring, mobile prompting, and ephemeral cloud sandboxing.', 'remote-control, cloud-ide, mobile, orchestration, sandboxing', 'Bidirectional remote task sync, ephemeral cloud sandboxes, live frontend previews, desk-free mobile prompting.'),
    ('https://docs.anythingllm.com/mcp-compatibility/overview', 'Connectivity & Interoperability (MCP/A2A)', 'AnythingLLM: MCP RAG', 'A document-heavy RAG platform with native MCP management, supporting multiple transports (stdio/SSE/HTTP) and workspace-level tool isolation.', 'rag, mcp, anythingllm, isolation, connectivity', 'Native MCP management UI, stdio/SSE/HTTP transport support, workspace-scoped tool isolation, persistent host-machine storage.'),
    ('https://docs.github.com/en/copilot/tutorials/enhance-agent-mode-with-mcp', 'Agent Orchestration & Workflow', 'Copilot Agent: MCP Core', 'The general availability release of GitHub Copilot Agent Mode, featuring native MCP "USB port" integration and enterprise-grade auto-approve governance.', 'copilot, agent-mode, mcp, governance, enterprise', 'Autonomous multi-step goal seeking, native MCP integration, enterprise auto-approve rules, language-aware symbol navigation.')
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
print('Successfully injected batch 115.')