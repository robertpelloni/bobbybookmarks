import sqlite3

data = [
    ('https://www.reddit.com/r/opencodeCLI/comments/1qcsm90/opencode_black_is_now_generallyavailable/', 'Guides & Industry Trends', 'OpenCode Black: Power Tier', 'A premium $200/month high-tier subscription for OpenCode CLI that provides massive usage allowances (up to $200/week) for enterprise power users.', 'subscription, opencode, enterprise, usage-limits, pro-tier', 'High usage allowances, early feature access, enterprise-grade support, bypasses standard Pro rate limits.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1qigg6v/vercel_just_launched_skillssh_and_it_already_has/', 'Infrastructure & Proxy Layers', 'skills.sh: AI Skill Registry', 'An open-source registry and CLI for standardized AI agent skills, allowing predictable, versioned command package execution (e.g., `npx skills add stripe`).', 'vercel, skills, registry, standard, modularity', 'Versioned command packages, Snyk-integrated security scanning, support for 30+ agents, separates reasoning from execution.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1qimlua/we_built_kuse_cowork_an_opensource_rustnative/', 'Interface & Developer UX', 'Kuse CoWork: Rust Agent', 'A Rust-native, local-first alternative to Claude Cowork that uses Docker sandboxing and a BYOK model for high-performance model-agnostic development.', 'rust, tauri, local-first, sandboxing, performance', 'Rust-native performance, Docker container isolation, model-agnostic (BYOK), 48-hour rapid development build.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1qh86pv/i_built_clancy_wiggum_to_supervise_my_ralph/', 'Agent Orchestration & Workflow', 'Clancy Wiggum: Loop Supervisor', 'An open-source Go-based supervisor tool designed to manage "Ralph Wiggum loops" by enforcing iteration limits, budget caps, and specific safe-word termination.', 'orchestration, supervision, safety, guardrails, automation', 'Loop iteration caps, API budget enforcement, safe-word termination protocol, prevention of agentic "flailing."')
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
print('Successfully injected batch 92.')