import sqlite3

data = [
    ('https://www.reddit.com/r/AIToolsPerformance/comments/1r23h46/glm5_vs_claude_opus_45_the_docs_finally_admit/', 'Guides & Industry Trends', 'GLM-5: Agentic Engineering', 'A performance analysis of GLM-5, identifying its 128K output token limit as a game-changer for "first-shot" multi-file project generation.', 'glm-5, benchmarks, agentic-engineering, long-horizon, zhipu-ai', '128K Output token limit, dedicated Reasoning Mode, parity with Opus 4.5 in complex backend reasoning, optimized for multi-file generation.'),
    ('https://www.reddit.com/r/AI_Agents/comments/1qap7ym/google_just_dropped_ucp_the_biggest_shift_in/', 'Connectivity & Interoperability (MCP/A2A)', 'Google Universal Commerce (UCP)', 'A standardized protocol for agent-to-agent shopping that enables a "shared context" across discovery, cart management, and secure checkout.', 'ucp, google, commerce, shared-context, interoperability', 'Shared cross-journey context, bridge between MCP/A2A/AP2, standardized merchant metadata, programmatic agent-driven checkout.'),
    ('https://www.reddit.com/r/AI_Agents/comments/1qefmh0/vector_dbs_are_not_memory_learned_this_the_hard/', 'Memory & Persistence Architecture', 'MemOS: The RAG Alternative', 'A strategic shift away from Vector DBs toward "MemOS" architectures that treat agent memory as a mutable, managed state with a defined lifecycle.', 'memory-architecture, rag-alternative, stateful-ai, sqlite, kv-store', 'Mutable state (overwrite/update), memory lifecycle (Activated/Merged/Archived), elimination of context pollution, KV/SQLite-first fact storage.'),
    ('https://www.reddit.com/r/AI_Agents/comments/1rei6km/i_made_mcps_94_cheaper_by_generating_clis_from/', 'Infrastructure & Proxy Layers', 'CLI-First MCP Optimization', 'A technical optimization that reduces MCP token costs by 94% by converting tool schemas into lazy-loading local CLIs.', 'mcp, optimization, token-reduction, cli, infrastructure', '94% Token reduction at session start, tool name lazy-loading, `--help` based parameter discovery, model-agnostic schema pruning.')
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
print('Successfully injected batch 60 (Correction).')
