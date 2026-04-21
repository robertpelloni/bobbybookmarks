import sqlite3

data = [
    ('https://block.github.io/goose/docs/getting-started/installation', 'Agent Orchestration & Workflow', 'Goose: Action Framework', 'An open-source, extensible agent framework by Block that connects LLMs to real-world engineering actions via MCP and local execution.', 'orchestration, framework, mcp, block, local-first', 'Autonomous engineering actions, dynamic MCP tool discovery, privacy-first local execution, modular LLM provider support (OpenAI/Gemini/Claude).'),
    ('https://blog.google/technology/developers/gemini-cli-extensions', 'Infrastructure & Proxy Layers', 'Gemini CLI Extensions', 'Self-contained packages that extend the Gemini CLI with specialized playbooks (GEMINI.md), custom slash commands, and multi-tool MCP integrations.', 'extension, cli, gemini, orchestration, modularity', 'Pre-packaged agent intelligence, custom .toml slash commands, single-command installation, integrated tool restriction policies.'),
    ('https://blog.google/technology/google-deepmind/gemini-computer-use-model', 'Interface & Developer UX', 'Gemini Computer Use', 'A specialized model designed to interact with GUIs like a human by "seeing" the screen via screenshots and generating precise click/type/scroll actions.', 'vision, computer-use, computer-interaction, deepmind, automation', 'Closed-loop visual perception, screenshot-to-action generation, sub-second adaptation to UI changes, high-impact action safety gates.'),
    ('https://blog.cloudflare.com/code-mode', 'Agent Orchestration & Workflow', 'Cloudflare Code Mode', 'An architectural pattern where agents write and execute sandboxed JS/TS code to orchestrate complex API workflows, reducing context usage by up to 99%.', 'orchestration, code-mode, cloudflare, optimization, security', '99% reduction in API schema bloat, logic chaining (loops/conditionals), isolated V8 Worker execution, automatic TypeScript SDK generation.')
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
print('Successfully injected batch 110.')