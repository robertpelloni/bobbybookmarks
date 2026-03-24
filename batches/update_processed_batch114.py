import sqlite3

data = [
    ('https://www.reddit.com/r/FactoryAi/comments/1qov9hn/factory_cli_v0560_released_acp_daemon_mode_and/', 'Infrastructure & Proxy Layers', 'Factory ACP Daemon Mode', 'A background control process for the Agent Control Protocol (ACP) that enables persistent background sessions and lazy context loading.', 'acp, daemon, persistence, optimization, lazy-loading', 'Persistent background agent sessions, lazy message loading for low latency, isolated MCP tool schemas, automated session recovery.'),
    ('https://www.reddit.com/r/GeminiAI/comments/1ptr5a0/gemini_is_too_good_and_its_worrying/', 'Guides & Industry Trends', 'Gemini Reasoning Lead', "User research identifying Gemini 3 Flash's lead in detecting reasoning errors in other models, particularly in specialized academic and technical domains.", 'benchmarks, gemini, reasoning, error-detection, research', 'Superior technical error detection, high-fidelity reasoning traces, academic domain dominance, cross-model verification capabilities.'),
    ('https://www.reddit.com/r/GeminiAI/comments/1r6otou/i_gave_gemini_a_hard_drive_1076_sessions_later_it/', 'Memory & Persistence Architecture', 'Athena: Tiered Memory', 'An open-source state-persistence layer that uses a tiered architecture (Canonical/Vector/Graph) to give agents long-term, cross-session memory.', 'memory-architecture, persistence, athena, rag, state-management', 'Materialized CANONICAL.md state, Tiered (Core/Archival) memory, deterministic /start boot sequence, semantic LRU disk cache.'),
    ('https://www.reddit.com/r/GeminiFeedback/comments/1raj36f/googles_session_lock_scam_how_the_gemini_ui_lies/', 'Guides & Industry Trends', 'Session Lock Transparency', 'Critical community research exposing a bug where UI toggles fail to hand off backend reasoning modes, resulting in billing/intelligence mismatches.', 'transparency, compliance, reasoning-traces, auditing, safety-paradox', 'UI-to-Backend mode verification, reasoning trace validation mandate, credit-drain risk identification, model-routing auditing.')
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
print('Successfully injected batch 66.')
