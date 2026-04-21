import sqlite3

data = [
    ('https://www.reddit.com/r/kilocode/comments/1q6ubk8/ama_i_built_code_reviews_in_kilo/', 'Interface & Developer UX', 'Kilo Code Reviews', 'A customizable code review feature in Kilo supporting 500+ models with strict, balanced, and lenient modes.', 'code-review, customization, quality-gate, productivity, kilo', '500+ model support, multi-intensity review modes, specific focus area toggles (security/perf), open token pricing.'),
    ('https://www.reddit.com/r/kilocode/comments/1q89rq0/why_peanut_buttering_ai_onto_your_existing/', 'Guides & Industry Trends', 'The Kilo Model Workflow', 'An analysis arguing against "peanut buttering" AI onto old workflows, proposing a single-engineer model directing a suite of specialized agents.', 'workflow, orchestration, multi-agent, philosophy, productivity', 'Single-engineer feature ownership, specialized agent suite (Architect/Orchestrator/Code/Debug), human as reviewer.'),
    ('https://www.reddit.com/r/kiroIDE/comments/1ptourc/kiro_steering_for_turborepo_monorepos_a_practical/', 'Context Engineering & Isolation', 'Kiro Turborepo Steering', 'A practical guide for configuring Kiro IDE to understand workspace boundaries and dependency graphs within massive Turborepo monorepos.', 'monorepo, turborepo, context-engineering, kiro, optimization', 'Workspace boundary configuration, dependency graph awareness, specialized steering hooks.'),
    ('https://www.reddit.com/r/kiroIDE/comments/1qwlgbq/new_cli_release_125_with_acp_support_and_builtin/', 'Infrastructure & Proxy Layers', 'Kiro CLI ACP Support', 'The version 12.5 update for Kiro CLI introducing Agentic Control Protocol (ACP) support for better session persistence and cross-interface capabilities.', 'cli, acp, persistence, session-management, kiro', 'Agentic Control Protocol (ACP) support, session persistence, cross-interface resume capabilities.')
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
print('Successfully injected batch 81.')