import sqlite3

data = [
    ('https://github.com/antl3x/ToolRAG', 'Connectivity & Interoperability (MCP/A2A)', 'ToolRAG Framework', 'A framework that applies RAG principles to tool definitions, allowing agents to access unlimited tools via semantic search without context bloat.', 'tool-discovery, rag, optimization, context-window, efficiency', 'Vector-indexed tool schemas, zero context penalty for unused tools, support for thousands of tools, LibSQL backend.'),
    ('https://github.com/pathintegral-institute/mcpm.sh', 'Development Tools & Libraries', 'mcpm: MCP Package Manager', 'A specialized CLI package manager for the Model Context Protocol that centralizes server installation and configuration across AI clients.', 'mcp, cli, package-manager, productivity, configuration', 'Global cross-client configuration, virtual tool profiles, built-in server registry search, agent-friendly non-interactive mode.'),
    ('https://github.com/thirdstrandstudio/mcp-tool-chainer', 'Connectivity & Interoperability (MCP/A2A)', 'MCP Tool Chainer', 'An MCP server that enables sequential tool execution, allowing agents to pass data between multiple tools in a single context-efficient turn.', 'mcp, chaining, workflow, automation, performance', 'Sequential "CHAIN_RESULT" passing, JsonPath data filtering, multi-server tool discovery, reduced LLM round-trips.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
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
    ''', (url, cat, sd, ld, tags, mf, 9))
conn.commit()
conn.close()
print('Successfully injected batch 24.')
