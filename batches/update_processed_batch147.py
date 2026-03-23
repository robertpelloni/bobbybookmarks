import sqlite3

data = [
    ('https://www.reddit.com/r/projects/comments/1q9lkac/im_building_drosk_a_reactive_file_organizer_that/', 'Development Tools & Libraries', 'Drosk: Reactive AI Organizer', 'A smart desktop file organizer that reacts instantly to system changes based on deterministic rules and AI sorting.', 'drosk, automation, desktop-tool, file-management, reactive', 'Real-time background monitoring, deterministic sorting core (C/C++), automatic format conversion (WebP/PNG), customizable routing rules.'),
    ('https://www.reddit.com/r/replit/comments/1r63cbb/use_claude_code_codex_cli_on_replit_full_setup/', 'Infrastructure & Proxy Layers', 'Claude Code on Replit', 'A persistence and authentication workflow for running AI coding agents within Replit shells by redirecting configs to persistent workspace folders.', 'replit, cli, persistence, setup, cloud-ide', 'Replit Secret config redirection (CLAUDE_CONFIG_DIR), headless OAuth capture (curl), parallel Claude/Codex multi-tab workflow.'),
    ('https://www.reddit.com/r/solanadev/comments/1qxx2dq/just_shipped_leek_terminal_v11_on_solana_full/', 'Connectivity & Interoperability (MCP/A2A)', 'Leek Terminal: Solana Bot', 'An autonomous deflationary ecosystem on Solana featuring automated arbitrage, daily SOL airdrops, and a "Burn & Earn" fee system.', 'solana, crypto, automation, arbitrage, blockchain', 'Automated SOL revenue sharing, 1% transaction fee distribution, self-balancing arbitrage bots, integrated points farming/staking.'),
    ('https://www.reddit.com/r/BMAD_Method/comments/1psnjmo/bmad_documentation/', 'Agent Orchestration & Workflow', 'BMAD Method Framework', 'A universal AI development framework (Brainstorm-Model-Act-Document) that uses context sharding and 12 specialized agents to ensure production-ready code.', 'workflow, bmad, spec-driven, orchestration, optimization', 'Context sharding (90% token reduction), specialized 12-agent persona suite, Documentation-as-Truth paradigm, Spec-Plan-Implement-QC pipeline.')
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
print('Successfully injected batch 97.')