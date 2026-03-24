import sqlite3

data = [
    ('https://www.reddit.com/r/GoogleAntigravityIDE/comments/1rf6p37/showcase_antigravity_phone_connect_v0221_now_with/', 'Interface & Developer UX', 'Antigravity Phone Connect', 'A multi-device bridge that mirrors desktop AI assistants to mobile devices via CDP, enabling continuous context maintenance and remote task control.', 'multi-device, cdp, remote-control, context-maintenance, infrastructure', 'Remote "Run/Reject" triggers, Base64 visual asset streaming, occurrence index UI tracking, continuous context persistence.'),
    ('https://www.reddit.com/r/GoogleAntigravityIDE/comments/1riq4q6/update_ai_cli_manager_v122_major_readme_revamp/', 'Development Tools & Libraries', 'AI CLI Manager (v1.2.2)', 'A centralized control utility for managing multiple AI command-line tools (Gemini, Claude, local agents) and maintaining a clean developer environment.', 'cli, management, productivity, orchestration, dev-tools', 'Centralized tool installation/launch, unified credential management, environment-cleaner scripts, automated multi-agent versioning.'),
    ('https://www.reddit.com/r/GoogleGemini/comments/1pyj003/gemini_3_flash_is_stupid_fast_googles_lowlatency/', 'Guides & Industry Trends', 'Gemini 3 Flash: Speed King', "Technical analysis of Google's low-latency model, highlighting its 'stupid fast' performance as the primary enabler for real-time agentic vision.", 'gemini, performance, low-latency, flash, real-time', 'Frontier-level logic at 10x speed, optimized for real-time feedback loops, massive context window (1M+), ideal background indexing model.'),
    ('https://www.reddit.com/r/GoogleAntigravityIDE/comments/1qm0x9m/how_to_fix_antigravitys_tunnel_vision_fix_for/', 'Context Engineering & Isolation', 'AG Tunnel Vision Fix', 'A context-refresh mechanism that uses a shared global configuration bridge (~/.gemini/) to provide agents with full repository awareness.', 'context-engineering, tunnel-vision, optimization, awareness, infrastructure', 'Shared ~/.gemini global config, conductor-style repo mapping, session hydration via pre-built metadata, elimination of agent exploration turns.')
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
print('Successfully injected batch 68.')
