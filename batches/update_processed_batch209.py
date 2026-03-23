import sqlite3

data = [
    ('https://www.reddit.com/r/CodexAutomation/comments/1piwstk/codex_cli_0660_safer_execpolicy_windows_stability', 'Infrastructure & Proxy Layers', 'Codex CLI 0.66.0: Hardening', 'A security-focused update to Codex CLI introducing strict ExecPolicy enforcement, pipeline inspection, and Windows platform stability fixes.', 'codex, cli, security, windows, execution-policy', 'Strict ExecPolicy non-bypass, pipeline inspection for unsafe tails (`| rm -rf`), TUI amendment proposals for unsafe commands, Windows CRLF patching.'),
    ('https://www.reddit.com/r/ContextEngineering/comments/1phmia8/i_promised_an_mvp_of_universal_memory_last_week_i', 'Memory & Persistence Architecture', 'Global Context Delivery (GCDN)', 'The 2026 architectural shift from manual universal clipboards to Global Context Delivery Networks (GCDN), acting as an API-driven "Cloudflare for Context."', 'context-engineering, memory, gcdn, architecture, persistence', 'Global Context Delivery Network (GCDN) architecture, 5-stage engineering pipeline (Curate/Compress/Structure/Deliver/Refresh), Hot/Cold tiered retrieval.'),
    ('https://www.reddit.com/r/cursor/comments/1og22hk/fyi_codesupernova1million_many_times_a_better_job', 'AI Agents & Frameworks', 'CodeSuperNova-1M: Cursor', 'A stealth, ultra-long-context model available in Cursor, praised for massive codebase sweeps and mass refactoring, despite extreme generation latency.', 'cursor, models, long-context, refactoring, code-supernova', '1M token effective context, mass repository refactoring capability, 5-10 minute extreme latency profiles, vulnerability to "instruction drift."'),
    ('https://www.reddit.com/r/DeepSeek/comments/1nuiviq/deepseek_v32_is_released_heres_everything_you', 'AI Agents & Frameworks', 'DeepSeek V3.2: Thinking Tools', 'The December 2025 release of DeepSeek V3.2, introducing "Thinking in Tool-Use" to combine advanced reasoning with strict JSON/CSV schema outputs.', 'deepseek, reasoning, tool-use, structured-output, optimization', 'Thinking-in-Tool-Use integration, DeepSeek Sparse Attention (DSA) for long-context, Speciale high-compute variant, 50% API cost reduction ($0.07/1M hits).')
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
print('Successfully injected batch 169.')