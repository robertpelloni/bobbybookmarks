import sqlite3

data = [
    ('https://github.com/run-llama/llama_index', 'Memory & Persistence Architecture', 'LlamaIndex Data Framework', 'The industry-standard data framework for building context-augmented AI applications, specializing in connecting private data sources to LLMs.', 'rag, data-framework, indexing, embeddings, context', '130+ Data connectors, Query Engine Tools for agents, Event-driven multi-step workflows, built-in Knowledge Graph support.'),
    ('https://blog.google/technology/developers/file-search-gemini-api/', 'Infrastructure & Proxy Layers', 'Gemini Managed File Search', 'A fully managed RAG system built directly into the Gemini API that automates the entire document indexing and retrieval lifecycle.', 'gemini, google, rag, file-search, infrastructure', 'Automated chunking and indexing, UI-ready citations, grounded answer generation, cost-efficient token-based pricing.'),
    ('https://github.com/medright/vectorize-ui', 'Interface & Developer UX', 'Vectorize-UI Manager', 'A specialized frontend and management layer designed to streamline the creation, monitoring, and debugging of vector knowledge bases.', 'gui, management, monitoring, rag, visualization', 'AgentStreamDisplay real-time panel, AES-256-GCM key security, Hybrid search optimization, built-in MCP service support.'),
    ('https://github.com/Tencent/WeKnora', 'Memory & Persistence Architecture', 'Tencent WeKnora Engine', 'An enterprise-grade document understanding and retrieval framework specializing in complex, multi-modal document processing and GraphRAG.', 'enterprise, multmodal, graph-rag, tencent, indexing', 'Multimodal cognitive engine (PDF/OCR), Hybrid BM25/Vector/Graph retrieval, Knowledge Graph visualization, local deployment support.'),
    ('https://github.com/mindsdb/mindsdb', 'Agent Orchestration & Workflow', 'MindsDB AI Automation', 'An open-source AI orchestration platform that abstracts models as virtual tables, enabling ML operations directly on top of 200+ data sources.', 'automation, mlops, sql, orchestration, data-unification', '200+ Data source connectors, Generative AI SQL tables, real-time prediction engine, autonomous agent deployment on data.'),
    ('https://github.com/bytebase/dbhub', 'Connectivity & Interoperability (MCP/A2A)', 'DBHub Database Gateway', 'A zero-dependency, token-efficient database MCP server that acts as a secure gateway for agents to explore and query multiple database types.', 'mcp, database, gateway, sql, security', 'Multi-database support (PG/MySQL/SQLite), visual workbench interface, SSH/SSL security guardrails, multi-connection TOML config.'),
    ('https://github.com/sensuslab/spark-mcp', 'Interface & Developer UX', 'Spark-MCP Computer Control', 'A production-grade MCP server integrating ByteBot dual-API architecture for independent task execution and direct desktop computer control.', 'computer-use, browser-use, mcp, automation, task-execution', 'Direct mouse/keyboard interaction, autonomous task management, real-time status WebSockets, strict TypeScript implementation.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 9) for d in data]:
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
print('Successfully injected batch 25.')
