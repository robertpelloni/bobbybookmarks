import sqlite3

data = [
    ('https://www.reddit.com/r/Rag/comments/1q4y21e/starting_with_docling/', 'Memory & Persistence Architecture', 'Docling: Structural Parsing', 'An advanced document parsing framework that maps heterogeneous types (PDF/DOCX) into a unified tree-structured data model for high-fidelity RAG.', 'docling, document-intelligence, document-parsing, structural-rag, metadata', 'Unified tree-structured data model, Markdown/JSON export, layout-aware text extraction, hierarchical indexing hooks.'),
    ('https://www.reddit.com/r/Rag/comments/1qhxtt2/chunking_without_document_hierarchy_breaks_rag/', 'Memory & Persistence Architecture', 'Contextual Prefixing Pattern', 'A high-ROI RAG optimization that prepends document hierarchy (Document > Section) to chunks before embedding to prevent "topic identity" loss.', 'rag, optimization, chunking, context-retrieval, accuracy', 'Hierarchical contextual prefixing, reduction of "lost-in-middle" errors, semantic boundary preservation, metadata breadcrumb linking.'),
    ('https://github.com/GrantFlowAI/GrantFlowAI', 'Agent Orchestration & Workflow', 'GrantFlowAI production RAG', 'A production-grade RAG stack blueprint using Litestar, pgvector, and Kreuzberg, focusing on integrated evaluation loops and feedback systems.', 'rag, production-ai, python, pgvector, infrastructure', 'Integrated evaluation layers, Litestar/pgvector backend, automated feedback loops, uv/pnpm monorepo management.'),
    ('https://www.reddit.com/r/Rag/comments/1qynrqv/hierarchical_agentic_rag_knowledge_graph_vector/', 'Memory & Persistence Architecture', 'Tri-Search: Hierarchical RAG', 'A high-scale RAG architecture that fuses Vector Search, Knowledge Graphs, and Reasoning-based routing to achieve massive scale on consumer hardware.', 'graph-rag, rag, hierarchical-routing, search-optimization, tri-search', '3-Address Domain/Topic/Entity routing, Vector/KG/Reasoning fusion (Tri-Search), <400ms latency JSON mode, 600k+ chunk scalability on low-end GPUs.')
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
print('Successfully injected batch 70.')
