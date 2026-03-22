import sqlite3

data = [
    ('https://www.trychroma.com/', 'Development Tools & Libraries', 'Chroma Vector Database', 'An open-source, AI-native vector database designed for simple, high-performance storage and retrieval of embeddings for RAG.', 'chroma, vector-database, rag, embeddings, python', 'Built-in embedding model support, simple single-command installation, metadata filtering for precise retrieval, local-first persistence.'),
    ('https://github.com/pgvector/pgvector', 'Infrastructure', 'pgvector: AI-on-Postgres', 'An open-source extension for PostgreSQL adding native vector search, enabling unified relational and semantic data management.', 'postgres, pgvector, vector-search, sql, infrastructure', 'Native vector data type, HNSW and IVFFlat indexing support, full ACID compliance, seamless integration with existing Postgres environments.'),
    ('https://github.com/CaviraOSS/OpenMemory', 'AI Agents & Frameworks', 'OpenMemory Engine', 'A local-first, multi-sector persistent memory engine designed to give AI agents long-term, human-like cognitive memory.', 'memory, cognitive-computing, temporal-reasoning, mcp, local-first', 'Multi-sector storage (Episodic/Semantic/Procedural), temporal knowledge graph, adaptive memory decay, explainable Waypoint traces.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level)
        VALUES (?, ?, ?, ?, ?, ?, 'deep')
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='deep'
    ''', (url, cat, sd, ld, tags, mf))
conn.commit()
conn.close()
print('Successfully injected batch 21.')
