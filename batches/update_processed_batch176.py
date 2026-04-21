import sqlite3

data = [
    ('https://github.com/AnswerDotAI/shell_sage', 'Agent Orchestration & Workflow', 'Shell Sage: tmux Context', 'An AI terminal assistant that uses tmux pane capture to provide high-fidelity context awareness and executes shell commands via a safe allow-list.', 'terminal, tmux, aish, orchestration, security', 'tmux pane/history capture, `safecmd` allow-list execution, Agent Mode filesystem access, multi-hour implementation loops.'),
    ('https://github.com/antl3x/ToolRAG', 'Connectivity & Interoperability (MCP/A2A)', 'ToolRAG: Dynamic Discovery', 'A specialized RAG framework that enables "unlimited" tool support by using vector search to dynamically inject relevant tool schemas into the context.', 'mcp, rag, optimization, tool-discovery, search', 'Dynamic tool schema injection, 97% retrieval accuracy benchmarks, tool-name-only embedding logic, context bloat prevention.'),
    ('https://github.com/Automata-Labs-team/code-sandbox-mcp', 'Infrastructure & Proxy Layers', 'Automata: Code Sandbox', 'A secure, isolated execution environment for AI agents that uses disposable Docker containers to run code and stream logs without host access.', 'security, sandboxing, docker, mcp, execution', 'Disposable Docker containers, real-time log streaming, host-to-sandbox file transfers, custom image support (Python/Node).'),
    ('https://github.com/anthropics/claude-code/blob/main/plugins/README.md', 'Infrastructure & Proxy Layers', 'Claude Code: Plugin Hub', 'A modular 2026 architecture for extending Claude Code via .claude-plugin artifacts that bundle MCP servers, skills, subagents, and hooks.', 'extension, modularity, plugin-system, architecture, standard', 'Bundled MCP/Skill/Agent artifacts, PreToolUse/PostToolUse hooks, plugin.json manifest, private enterprise marketplaces.')
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
print('Successfully injected batch 126.')