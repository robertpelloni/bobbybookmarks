import sqlite3

data = [
    ('https://www.reddit.com/r/Rag/comments/1r2st4j/vectorless_rag_why_document_trees_beat_embeddings/', 'Memory & Persistence Architecture', 'Vectorless RAG: Tree Reasoning', 'A paradigm shift replacing vector similarity with structured LLM reasoning over document hierarchies (trees), enabling high-precision retrieval and explicit reasoning traces.', 'vectorless-rag, context-engineering, tree-traversal, logical-inference, precision', 'Hierarchical tree ingestion, "Text-free" reasoning over summaries, logical branch exploration, 100% explainable retrieval traces.'),
    ('https://www.reddit.com/r/Rag/comments/1r7ds0f/hyperspacedb_v20_lockfree_serverless_vector_db/', 'Infrastructure & Proxy Layers', 'HyperspaceDB: Lock-Free Search', 'A high-performance, Rust-based vector database optimized for extreme concurrency and serverless cold starts via a lock-free hot path and mmap-based ingestion.', 'vector-db, rust, serverless, concurrency, performance', 'Lock-free index access (ArcSwap), mmap-based cold starts, SIMD-accelerated distance metrics, 12k QPS search / 59k QPS ingestion.'),
    ('https://www.reddit.com/r/Rag/comments/1rf89ip/built_a_context_engineering_layer_for_my/', 'Context Engineering & Isolation', 'Borg Context Layer (Concept)', 'An architectural shift from prompt engineering to context engineering, treating LLM context like OS memory with managed eviction and KV-cache optimization.', 'context-engineering, kv-cache, state-management, memory-os, efficiency', 'KV-cache optimized stable prefixes, filesystem-backed context snapshots, procedural failure tracking, semantic context eviction logic.'),
    ('https://www.reddit.com/r/Rag/comments/1rl34oz/i_built_an_embeddingfree_rag_engine_llm_sql_works/', 'Memory & Persistence Architecture', 'Embedding-Free RAG (SQL)', 'A high-accuracy retrieval system that uses LLMs to generate rich tags and metadata for SQL storage, bypassing the inaccuracies of vector distance math.', 'rag, sqlite, metadata, keyword-search, precision', 'LLM-generated document tagging, standard SQL exact-match retrieval, secondary LLM reranking, 100% transparent debugging path.')
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
