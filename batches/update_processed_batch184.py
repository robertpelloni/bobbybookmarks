import sqlite3

data = [
    ('https://news.ycombinator.com/item?id=44800746', 'Agent Orchestration & Workflow', 'Aider: terminal-first UX', 'Aider is the premier terminal AI pair programmer, praised for its pragmatic Git-centric UX, AST-aware context, and "Architect" planning mode.', 'aider, terminal, git, pair-programming, orchestration', 'Architect/Implementer dual-mode, AST-aware context (tree-sitter), automatic descriptive commits, high reliability/precision benchmarks.'),
    ('https://news.ycombinator.com/item?id=45415962', 'Agent Orchestration & Workflow', 'Everything Claude Code: OS', 'A comprehensive harness extension system for Claude Code that adds autonomous skills, automated memory persistence, and red-team security pipelines.', 'claude-code, orchestration, security, memory, optimization', 'Red-team/Blue-team security pipeline, automated SKILL.md generation, 13-agent specialized team model, cross-session memory persistence.'),
    ('https://news.ycombinator.com/item?id=45132710', 'Connectivity & Interoperability (MCP/A2A)', 'MCP: AI "USB-C"', 'An open protocol (LSP for agents) designed by Anthropic to standardize how LLMs connect to data sources like Postgres, Slack, and local files.', 'mcp, protocol, standard, connectivity, orchestration', 'Universal data/tool socket, Model-agnostic discovery interface, standardized Resources/Prompts/Tools, solves NxM integration chaos.'),
    ('https://news.ycombinator.com/item?id=44781561', 'Agent Orchestration & Workflow', 'Plandex: Heavy-Duty Agent', 'A heavy-duty AI coding agent for large-scale multi-file tasks, featuring a version-controlled sandbox and support for 2M+ token contexts.', 'orchestration, plandex, context-management, sandbox, sw-bench', 'Version-controlled change sandbox, 2M token effective context, tree-sitter repo indexing (20M+), Full Auto implementation mode.')
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
print('Successfully injected batch 144.')