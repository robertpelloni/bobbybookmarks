import sqlite3

data = [
    ('https://www.reddit.com/r/google_antigravity/comments/1q6b08t/i_built_mcp_vault_a_lazyloading_gateway_for/', 'Infrastructure & Proxy Layers', 'MCP Vault for Antigravity', 'A persistent gateway that lazyloads MCP servers to prevent Agent Manager crashes and connection loops under heavy engineering payloads.', 'mcp, gateway, antigravity, stability, proxy', 'Lazyloads MCP servers, stabilizes connections, prevents Agent Manager crashes, persists auth tokens.'),
    ('https://www.reddit.com/r/google_antigravity/comments/1qcfw7k/google_antigravity_skills_like_claude_skills_w_a/', 'AI Agents & Frameworks', 'Antigravity Skills', 'An Automation-First skill architecture using TypeScript definitions that grant direct permission to run local code with near-zero latency.', 'skills, typescript, automation, antigravity, framework', 'TypeScript-based execution, near-zero latency, direct local code permissions, "Teaching vs Prompting" paradigm.'),
    ('https://www.reddit.com/r/google_antigravity/comments/1qg7gwg/gsd_get_shit_done_for_antigravity/', 'Agent Orchestration & Workflow', 'GSD Framework for Antigravity', 'A spec-driven workflow designed to eliminate "vibecoding" by enforcing strict Plan-Execute-Verify cycles and atomic commits.', 'gsd, workflow, verification, spec-driven, antigravity', 'Strict /plan to /execute to /verify cycles, atomic commits per sub-task, fresh context sub-agents (200k tokens), empirical verification gates.'),
    ('https://www.reddit.com/r/google_antigravity/comments/1qaae57/control_ag_from_your_phone/', 'Interface & Developer UX', 'Remoat: Mobile Control for AG', 'A tool allowing users to control local Antigravity instances securely via Telegram, supporting mobile prompts, screenshots, and voice notes.', 'mobile, remote-control, telegram, ux, antigravity', 'Telegram-based mobile control, secure local execution without exposed ports, multimodal input (screenshots/voice), remote build triggering.')
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
print('Successfully injected batch 78.')