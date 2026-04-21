import sqlite3

data = [
    ('https://www.reddit.com/r/codex/comments/1qwsrqo/codex_53_is_out/', 'AI Agents & Frameworks', 'Codex 5.3: Mid-Turn Thinking', 'A paradigm shift in interaction where agents stream internal reasoning and tool-use intent in real-time to enable active steering and intervention.', 'codex, interaction-design, steerability, transparency, real-time', 'Real-time reasoning streaming, active mid-turn intervention, dynamic 20-step todo updating, 40% reduction in alignment drift.'),
    ('https://www.reddit.com/r/codex/comments/1r30pvl/new_model_gpt53_codexspark_dropped/', 'Infrastructure & Proxy Layers', 'Codex Spark: 1000 TPS', 'An ultra-low latency model variant डिजाइन for context gathering and sub-agent orchestration, achieving human-imperceptible 1,000 TPS inference.', 'performance, low-latency, sub-agents, context-gathering, cerebras', '1,000 Tokens-per-second throughput, Cerebras-hardware optimized, "Nanobot" discovery persona, low-cost architectural exploration.'),
    ('https://www.reddit.com/r/codex/comments/1r4x4xc/i_ported_gemini_conductor_into_codex_and_damn_it/', 'Agent Orchestration & Workflow', 'Codex Conductor Pattern', 'An implementation of context-driven development for Codex that organizes work into persistent Markdown "spines" to eliminate redundant alignment.', 'orchestration, cdd, context-driven, workflow, persistence', 'Persistent context "spines" (specs.md), `codex_init` bootstrap automation, rule-scoped role enforcement, automated Plan-Approve loops.'),
    ('https://www.reddit.com/r/codex/comments/1qu5rho/standalone_codex_app_has_been_launched/', 'Interface & Developer UX', 'Standalone Codex Platform', 'An integrated agentic platform featuring local/cloud execution toggles and native desktop automation with cost-parity to the CLI.', 'gui, desktop-app, platform, automation, cost-optimization', 'Local vs Cloud execution toggle, native system-level automation, unified multi-agent workspace, CLI cost-parity logic.')
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
print('Successfully injected batch 73.')
