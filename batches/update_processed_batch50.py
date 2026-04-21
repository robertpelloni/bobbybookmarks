import sqlite3

data = [
    ('https://github.com/mem0ai/mem0', 'AI Agents & Frameworks', 'Mem0 Universal Memory', 'A self-improving, multi-level memory system that provides AI agents with personalized long-term memory across users and sessions.', 'mem0, memory, personalization, rag, agent-state', 'Adaptive learning from interactions, multi-level retention (User/Session/Agent), hybrid Vector/Graph storage, automated importance scoring.'),
    ('https://supermemory.ai/', 'Infrastructure', 'Supermemory Context API', 'An enterprise-grade context infrastructure platform that provides a managed API for personal AI memory and high-capacity RAG.', 'memory-as-a-service, context, rag, analytics, mcp', 'Smart Forgetting decay engine, 50M+ token capacity per user, multi-format content extraction, meta-MCP hub integration.'),
    ('https://docs.pieces.app/products/mcp/get-started', 'MCP', 'Pieces.app MCP Bridge', 'An OS-level bridge that allows AI assistants like Cursor and Claude to access local work history, Slack chats, and code snippets via MCP.', 'mcp, context, local-first, privacy, productivity', 'Neural Code Search (NCS), local work history access, end-to-end encrypted storage, multi-client IDE integration.'),
    ('https://github.com/BAI-LAB/MemoryOS', 'AI Agents & Frameworks', 'MemoryOS Research', 'A "memory operating system" for personalized AI agents from EMNLP 2025, implementing OS-like short/mid/long-term memory management.', 'memory-os, research, personalized-ai, architecture, emnlp', 'Hierarchical four-module structure, 49% improvement on LoCoMo benchmark, plug-and-play MCP server, model-agnostic generation.'),
    ('https://github.com/MemMachine/MemMachine', 'AI Agents & Frameworks', 'MemMachine Universal Layer', 'An open-source universal memory layer for AI agents focusing on evolving user profiles and persistent episodic state management.', 'memory, graph-db, neo4j, sql, persistent-state', 'Multi-layered (Episodic/Profile/Procedural) memory, hybrid Neo4j/SQL storage, universal SDK (Py/TS), model-agnostic backend.'),
    ('https://github.com/orneryd/Mimir', 'AI Agents & Frameworks', 'Mimir Long-Term Memory', 'A long-term memory server and MCP server utilizing knowledge graphs and cognitive-inspired decay to help agents learn from interactions.', 'knowledge-graph, cognitive-decay, go, mcp, memory-server', 'Automated cognitive decay (7/69/693 days), NornicDB lightweight vector-native engine, automatic relationship discovery, multi-agent memory locking.')
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
print('Successfully injected batch 17.')
