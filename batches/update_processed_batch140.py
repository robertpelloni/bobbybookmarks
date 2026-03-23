import sqlite3

data = [
    ('https://www.reddit.com/r/openclaw/comments/1qzs5yu/how_i_run_a_14agent_marketing_team_on_a_5_vps_the/', 'Agent Orchestration & Workflow', 'Autonomous Squad VPS Model', 'A high-efficiency orchestration model using OpenClaw to run a 14-agent specialized squad on a $5/month VPS by offloading heartbeats to local models.', 'openclaw, vps, cost-optimization, swarm, orchestration', '14-agent specialized squad, Telegram mission control, local-model heartbeat offloading (Ollama), shared project board communication.'),
    ('https://www.reddit.com/r/openclaw/comments/1r6t4ob/openclaw_lily_memory_optimization_system/', 'Memory & Persistence Architecture', 'Lily Memory Engine', 'A persistent memory system for OpenClaw that uses a local SQLite database and Hybrid Semantic Search to solve the "stateless agent" problem.', 'openclaw, memory, persistence, sqlite, search', 'Local SQLite storage, auto-recall via semantic search, loop detection nudges, memory deduplication on startup.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1pumwee/update_leash_now_has_oneliner_setup_and_catches/', 'Infrastructure & Proxy Layers', 'Leash: CLI Security Guardrails', 'A security layer for AI agents that blocks directory escapes, protected folder access (.env/.git), and dangerous Git operations like force-pushes.', 'security, guardrails, cli, opencode, safety', 'One-liner setup, directory escape blocking, secret folder protection, dangerous git command interception.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1pv2foa/tokscale_finally_a_token_tracker_for_opencode_and/', 'Interface & Developer UX', 'Tokscale: Token Dashboard', 'A TUI-based token tracking dashboard for OpenCode and Claude Code that provides real-time visualization of input/output tokens and session costs.', 'tui, monitoring, token-usage, cost-tracking, metrics', 'Real-time TUI dashboard, 2D/3D token contribution graphs, cost estimation via LiteLLM, cross-tool support (Claude/Gemini/Cursor).')
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
print('Successfully injected batch 90.')