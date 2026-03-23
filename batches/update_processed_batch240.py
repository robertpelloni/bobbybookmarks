import sqlite3

data = [
    ('https://github.com/dennishavermans/agentfile', 'Context Engineering & Isolation', 'agentfile: Agent Dockerfile', 'A configuration-as-code standard acting as a `Dockerfile` for AI agents, defining exact tools, system prompts, and MCP dependencies for consistent execution.', 'configuration, agentfile, standardization, mcp, dev-tools', 'Standardized agent environment declaration, MCP server dependency mapping, cross-platform workflow portability, deterministic system prompt injection.'),
    ('https://www.june.kim/union-find-compaction', 'Memory & Persistence Architecture', 'Union-Find Compaction', 'A graph-based context management algorithm that replaces flat summarization with a recoverable "Union-Find" tree structure to eliminate batch-stall latency.', 'context-engineering, memory, optimization, algorithms, compaction', 'O(1) incremental message compaction, `expand(root_id)` lossless summary reinflation, graph-based message provenance tracking, multi-user shared memory support.'),
    ('https://www.reddit.com/r/mcp/comments/1ruy1xd/penfield_memory_persistent_memory_and_knowledge/', 'Memory & Persistence Architecture', 'Penfield Memory: MCP', 'A high-performance MCP server providing dual-layer long-term storage (Episodic + Knowledge Graph) to map project dependencies and historical architectural decisions.', 'mcp, memory, persistence, knowledge-graph, neo4j', 'Dual-layer memory (SQLite FTS5 Episodic + Knowledge Graph), automated microservice dependency mapping, cross-session architectural decision persistence.'),
    ('https://github.com/denoland/t4a', 'Infrastructure & Proxy Layers', 't4a: Deno Tools for Agents', 'Deno\'s specialized runtime framework designed for building secure, edge-deployed AI agents with native Model Context Protocol (MCP) support.', 'deno, typescript, framework, security, edge-computing', 'Native MCP tool integration, Deno V8 secure sandboxing, TypeScript-first strict type safety, zero cold-start edge deployment optimization.')
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
print('Successfully injected batch 200.')