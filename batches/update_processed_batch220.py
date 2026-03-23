import sqlite3

data = [
    ('https://github.com/mohammedsamin/mcpup', 'Infrastructure & Proxy Layers', 'mcpup: MCP Manager', 'A critical utility that streamlines the installation and management of Model Context Protocol (MCP) servers, acting as a package manager for the ecosystem.', 'mcp, package-manager, infrastructure, automation, tooling', 'One-command GitHub/npm installation, isolated dependency management (venvs/node_modules), registry synchronization, built-in diagnostic health checks.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1rna5mb/anthropic_just_made_claude_code_run_without_you', 'Agent Orchestration & Workflow', 'Claude Code: Auto Mode', 'The 2026 update introducing autonomous background execution (`/loop` scheduling) and YOLO mode, allowing Claude Code to chain edits without manual approval.', 'claude-code, autonomy, orchestration, scheduled-tasks, terminal', 'Scheduled background tasks (`/loop 1h`), Auto/YOLO Mode (chained execution without "y/n" prompts), user-defined API safety budgets.'),
    ('https://www.reddit.com/r/LocalLLaMA/comments/1rmplvs/open_webuis_new_open_terminal_native_tool_calling', 'Interface & Developer UX', 'Open WebUI: Native Terminal', 'A major 2026 update to Open WebUI that integrates an interactive terminal directly into the web interface and introduces low-latency native tool calling.', 'open-webui, local-llm, terminal, tool-calling, interface', 'Integrated interactive web terminal, native low-latency tool calling (replaces JSON parsers), Qwen 3.5 / Llama 4 support, local Devin-like workflows.'),
    ('https://www.reddit.com/r/accelerate/comments/1rmzc8n/gpt54_and_gpt53_codex_become_the_first_llms_to', 'AI Agents & Frameworks', 'GPT-5.4 Codex: Self-Opt', 'The first LLM series to achieve "True Recursive Self-Optimization," natively rewriting its own routing logic and generating training data for future iterations.', 'gpt-5, codex, recursion, optimization, reasoning', 'Real-time routing logic rewriting, 100k+ line zero-shot repository ingestion, 98% architectural flaw detection accuracy, autonomous training data generation.')
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
print('Successfully injected batch 180.')