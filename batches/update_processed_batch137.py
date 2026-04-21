import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1res5ug/programmatic_tool_calling_code_mode_for_mcp_turn/', 'Agent Orchestration & Workflow', 'MCP Code Mode: Tool Scripts', 'An architectural pattern replacing hundreds of individual MCP tools with a single sandbox where agents write and execute JS/TS scripts to compose complex API workflows.', 'mcp, code-mode, sandboxing, execution, tool-sprawl', 'Script-based API composition, 97% context window reduction, dynamic worker loader execution, complex multi-step single-inference workflows.'),
    ('https://www.reddit.com/r/mcp/comments/1reoaz5/fragmentbased_memory_mcp_server_that_gives_ai/', 'Memory & Persistence Architecture', 'Memento MCP: Fragment Memory', 'A persistent memory system that decomposes conversations into typed fragments (facts, decisions, errors) with decay rates and a 3-layer retrieval mechanism.', 'mcp, memory, context, fragments, redis', '1-3 sentence typed fragments, L1 Redis keyword index, L2 PostgreSQL metadata filters, L3 pgvector semantic search, Contradiction Detection.'),
    ('https://www.reddit.com/r/mcp/comments/1rfwnpm/i_built_a_zerocopy_vision_transport_for_mcp_it/', 'Infrastructure & Proxy Layers', 'Glazyr Viz: Zero-Copy Vision', 'A high-performance vision transport layer for agents that reads GPU frame buffers directly from POSIX Shared Memory, bypassing the DOM and Chrome CDP.', 'vision, computer-use, zero-copy, performance, stealth', 'POSIX Shared Memory (/dev/shm) frame buffer reads, 49x faster than Puppeteer, structured JSON delta transmission, WAF bypass via DOM avoidance.'),
    ('https://www.reddit.com/r/mcp/comments/1rgrejh/a_threelayer_memory_architecture_for_llms_redis/', 'Memory & Persistence Architecture', 'AOI Three-Layer Architecture', 'A hierarchical memory system for SRE/DevOps agents designed to manage overwhelming volumes of operational data through working, episodic, and semantic layers.', 'memory, architecture, redis, aoi, sre', 'L1 Raw Context Storage, L2 Task Queue Management, L3 Compressed Context Cache (Redis), 72% context compression ratio.')
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
print('Successfully injected batch 87.')