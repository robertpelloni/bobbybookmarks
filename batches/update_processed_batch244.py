import sqlite3

data = [
    ('https://github.com/Merwynkumar/clawblink', 'Interface & Developer UX', 'clawblink: Semantic CLI', 'A specialized CLI tool for rapid AI-assisted codebase navigation, using local embeddings to provide "blink-of-an-eye" contextual summaries without reading full files.', 'cli, context-engineering, semantic-search, code-navigation, optimization', 'Local embeddings for semantic code search, instant file/function "blinks" (summaries), diff-aware architectural impact analysis, zero-config setup.'),
    ('https://github.com/Eternego-AI/eternego', 'Memory & Persistence Architecture', 'Eternego: Local Persona', 'A local AI persona designed for long-term project reasoning, featuring persistent memory that learns user coding styles and decision patterns over months.', 'memory, persona, local-ai, persistence, autonomous-agents', 'Long-term persistent style/decision memory, three-layer modular architecture (logic/UI separation), "Thinking Model" learning for autonomous scaffolding, 100% local privacy.'),
    ('https://github.com/tgalal/promptcmd', 'Interface & Developer UX', 'promptcmd: Programmable Prompts', 'A CLI manager that treats generative AI prompts as runnable, programmable commands, allowing `.prompt` files to accept arguments and stdin/stdout piping.', 'cli, prompt-engineering, workflow, dev-tools, pipeline', 'Treats `.prompt` files as native CLI commands, shell command nesting within templates, cross-provider load balancing/variants, SSH integration.'),
    ('https://github.com/yazinsai/OpenGranola', 'Agent Orchestration & Workflow', 'OpenGranola: Modular Workflow', 'A lightweight, open-source framework for building modular AI workflows using declarative configurations (POML) optimized for rapid prototyping.', 'orchestration, framework, declarative, workflow, prototyping', 'Declarative Prompt Orchestration Markup Language (POML), decoupled infrastructure components, native integration with Kreuzberg (document analysis) and Kodus (code review).')
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
print('Successfully injected batch 204.')