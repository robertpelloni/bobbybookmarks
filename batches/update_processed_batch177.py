import sqlite3

data = [
    ('https://github.com/BAI-LAB/MemoryOS', 'Memory & Persistence Architecture', 'MemoryOS: Agentic OS', 'An EMNLP 2025 framework that provides agents with a hierarchical memory operating system (Storage/Updating/Retrieval/Generation) for long-term consistency.', 'memory, architecture, emnlp-2025, persistence, context-management', 'Hierarchical Storage system, heat-based memory promotion, ~49% benchmark improvement (LoCoMo), automated user preference profiling.'),
    ('https://github.com/BeehiveInnovations/zen-mcp-server', 'Agent Orchestration & Workflow', 'Zen MCP: Team Layer', 'An advanced orchestration server that establishes a single AI as a Tech Lead capable of delegating to a collaborative team of specialized sub-models.', 'mcp, orchestration, multi-model, consensus, workflow', 'Multi-model consensus loops, context revival across resets, specialized reasoning tools (thinkdeep/analyze), smart token capacity management.'),
    ('https://github.com/browser-use/browser-use', 'Interface & Developer UX', 'browser-use: Web Agent', 'The 2026 industry-standard framework for building vision-native web agents with built-in stealth, CAPTCHA solving, and 89% benchmark success rates.', 'browser-automation, vision, orchestration, stealth, playright', 'Vision-native element recognition, 89% WebVoyager success rate, built-in anti-bot bypass, Python/TS unified SDK.'),
    ('https://github.com/campfirein/cipher', 'Memory & Persistence Architecture', 'Cipher: Context Sync', 'An open-source dual-layer memory system (System 1: Business Logic / System 2: Reasoning) that syncs agent context across IDEs and teams.', 'memory, persistence, collaboration, context-management, ide', 'Dual-layer memory (Logic/Reasoning), universal IDE support (Cursor/Windsurf), team-wide context sharing, multi-backend LLM support.')
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
print('Successfully injected batch 127.')