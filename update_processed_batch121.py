import sqlite3

data = [
    ('https://www.reddit.com/r/PydanticAI/comments/1qpd2hq/pydanticairlm_handle_massive_contexts_with/', 'Context Engineering & Isolation', 'PydanticAI: Recursive RLM', 'A high-scale inference paradigm that enables agents to reason over massive contexts by programmatically exploring data in a Python REPL environment.', 'pydanticai, rlm, long-context, recursive-reasoning, optimization', 'Recursive self-calling loops, programmatic context exploration (grep/slice), "out-of-core" prompt handling, massive context ingestion (millions of lines).'),
    ('https://www.reddit.com/r/PydanticAI/comments/1qyb2tm/text_to_sql_database_toolset_for_pydanticai_sql/', 'Connectivity & Interoperability (MCP/A2A)', 'PydanticAI: Secure SQL Tools', 'A security-first database toolset for AI agents featuring keyword blocking, comment-aware parsing, and resource-limited query execution.', 'pydanticai, sql, database, security, automation', 'Destructive keyword blocking (DROP/DELETE), comment-aware injection protection, max_rows/timeout resource limits, native SQLite/Postgres support.'),
    ('https://www.reddit.com/r/Qwen_AI/comments/1rcqezx/qwen_3_5_for_mlx_is_like_its_own_industrial/', 'Guides & Industry Trends', 'Qwen 3.5: MLX Performance', 'An analysis of Qwen 3.5 on Apple Silicon MLX, achieving 2x speed gains and 3x latency improvements for local-first industrial AI applications.', 'qwen, mlx, apple-silicon, local-llm, performance', '2x Token generation throughput, 3x latency improvement vs llama.cpp, 17B active MoE parameters, industrial-grade healthcare AI deployments.'),
    ('https://www.reddit.com/r/Rag/comments/1pu8rf5/introducing_context_mesh_lite_hybrid_vector/', 'Memory & Persistence Architecture', 'Context Mesh Lite: Hybrid RAG', 'A high-accuracy retrieval system that fuses Hybrid Vector Search, SQL Search, and Graph Extraction to capture complex data relationships.', 'rag, hybrid-search, context-mesh, accuracy, graph-rag', 'Fused Vector/SQL/Graph retrieval, entity-triplet relationship awareness, Supabase/n8n integration, accuracy-first retrieval logic.')
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
print('Successfully injected batch 67.')
