import sqlite3

data = [
    ('https://github.com/getzep/zep', 'AI Agents & Frameworks', 'Zep Memory Platform', 'A context engineering platform providing AI agents with temporal knowledge graph memory that understands evolving user preferences.', 'zep, memory, knowledge-graph, temporal, agent-context', 'Temporal awareness (valid_at/invalid_at), Graphiti relationship extraction, sub-200ms retrieval latency, hybrid vector/graph search.'),
    ('https://github.com/topoteretes/cognee', 'AI Agents & Frameworks', 'Cognee Knowledge Engine', 'A memory system implementing cognitive science patterns and ontology grounding to transform raw data into structured knowledge graphs.', 'memory, cognitive-science, ontology, neo4j, knowledge-engine', 'Ontology grounding for data structure, "Cognify" transformation process, Neo4j/Vector hybrid storage, built-in multi-tenant isolation.'),
    ('https://github.com/langchain-ai/langmem', 'AI Agents & Frameworks', 'LangMem Adaptive Memory', 'A managed memory lifecycle framework for LangChain agents that enables adaptation and learning from historical interactions.', 'langchain, memory, adaptation, langgraph, learning', 'Hot/Background memory paths, automatic knowledge consolidation, LangGraph AsyncPostgresStore integration, automated instruction refinement.'),
    ('https://github.com/neuml/txtai', 'AI Agents & Frameworks', 'txtai Semantic Framework', 'An all-in-one AI framework that treats memory as a unified union of vector indexes, graph networks, and relational SQL databases.', 'semantic-search, multimodal, embeddings, graph-rag, database', 'Unified Embeddings+SQL database, GraphRAG topic modeling, multimodal support (Audio/Image/Video), semantic workflow pipelines.'),
    ('https://github.com/tesserato/CodeWeaver', 'Development Tools & Libraries', 'CodeWeaver CLI', 'A Go-based command-line tool that "weaves" an entire codebase into a single, navigable Markdown document for LLM consumption.', 'cli, markdown, documentation, llm-context, go', 'Recursive directory scanning, automated tree representation, robust Regex filtering (-include/-ignore), direct clipboard integration.'),
    ('https://github.com/steveyegge/beads', 'AI Agents & Frameworks', 'Beads: Memory Upgrade', 'A stateful memory upgrade for coding agents created by Steve Yegge, using dependency-aware graph databases to solve context window limbo.', 'beads, infinite-context, dolt, state-management, steveyegge', 'Dependency-aware graph state (Dolt), issue-based task orchestration, semantic memory decay/compaction, stateless agent session support.'),
    ('https://github.com/qdrant/mcp-server-qdrant/', 'MCP', 'Qdrant MCP Server', 'A Model Context Protocol server that integrates the Qdrant vector database into AI environments for high-performance semantic code search.', 'mcp, qdrant, vector-database, semantic-search, memory', 'Local FastEmbed generation, automatic background re-indexing, .gitignore-aware indexing, consistency-driven code retrieval.')
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
print('Successfully injected batch 16.')
