import sqlite3

data = [
    ('https://github.com/spranab/contextcache', 'Memory & Persistence Architecture', 'ContextCache: Tool Output', 'A persistent Key-Value (KV) cache specifically designed to optimize the performance and token cost of AI agents that rely heavily on external tools.', 'cache, performance, tools, persistence, optimization', 'Content-Hash Addressing (prevents redundancy), cross-session persistent storage, optimization for high-latency MCP tool calls.'),
    ('https://github.com/computeruseprotocol/computeruseprotocol', 'Interface & Developer UX', 'ComputerUseProtocol', 'The industry standard protocol allowing AI agents to perceive and control computer interfaces (mouse, keyboard, screen) across Windows, macOS, and Linux.', 'computer-use, vision, gui-automation, protocol, standard', 'Standardized cross-OS action primitives (click/type/scroll), visual feedback loop for error correction, secure sandboxed execution, native MCP integration.'),
    ('https://agentica.genlabs.dev/', 'Interface & Developer UX', 'Agentica: Open-Source IDE', 'A fully open-source AI coding assistant environment offering a transparent alternative to proprietary tools, with Bring Your Own Key (BYOK) support.', 'ide, open-source, code-editor, agentica, automation', 'BYOK API support (OpenAI/Anthropic/Local Ollama), "no black boxes" transparent agent logic, high-velocity community update cycle.'),
    ('https://github.com/octoflow-lang/octoflow', 'Agent Orchestration & Workflow', 'Octoflow: Continuous AI', 'An agentic workflow framework that replaces rigid YAML CI/CD configurations with natural language markdown, enabling context-aware repository automation.', 'orchestration, automation, ci-cd, workflow, markdown', 'Natural language workflow definitions (Markdown), full repository context awareness, Supervisor-Worker swarm delegation, autonomous failure self-correction.')
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
print('Successfully injected batch 183.')