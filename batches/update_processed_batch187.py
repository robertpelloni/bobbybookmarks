import sqlite3

data = [
    ('https://openai.com/index/introducing-upgrades-to-codex', 'Agent Orchestration & Workflow', 'Codex: multi-agent App', 'The 2026 evolution of Codex into a multi-agent orchestration app featuring GPT-5.3-Codex (400K context) and native git-worktree isolation.', 'openai, codex, orchestration, gpt-5-3, desktop-app', 'Multi-agent parallel execution, 400K token context window, native Git Worktree support, 25% faster reasoning core.'),
    ('https://operator.browserbase.com/', 'Interface & Developer UX', 'Operator: Vision-Action', 'OpenAI\'s GUI agent featuring a high-frequency vision-action loop and Browserbase infrastructure for 10x cheaper browser-based automation.', 'openai, operator, browserbase, vision, computer-use', 'Vision-action loop (pixel counting), human-in-the-loop takeover mode, Browserbase headless infrastructure, Project Atlas agent OS integration.'),
    ('https://otincontext.com/', 'Infrastructure & Proxy Layers', 'AI Observability: Contextual', 'A 2026 shift in telemetry focusing on "AI in Context," monitoring Data, System, Code, and Model pillars with LLM-powered natural language insights.', 'observability, opentelemetry, debugging, telemetry, context', 'Four-pillar observability (Data/System/Code/Model), service-dependency topology, natural language anomaly explanation, OpenTelemetry distribution.'),
    ('https://old.reddit.com/r/retrogamedev/comments/1gqhilj/we_converted_super_mario_bros_3_physics_code_into', 'Guides & Industry Trends', 'SMB3 Physics: Hot-Pixels', 'A technical reverse-engineering project porting Super Mario Bros. 3 6502 assembly to C, revealing its unique "hot-pixel" ejection collision logic.', 'reverse-engineering, physics, game-dev, c, nes', '6502 assembly to C translation, "Hot-pixel" ejection logic, forgiving collision rectangles, velocity/acceleration parameter tuning.')
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
print('Successfully injected batch 147.')