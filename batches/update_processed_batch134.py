import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1q7qg4i/reverse_mcp_server_now_my_tools_can_be_in_local/', 'Connectivity & Interoperability (MCP/A2A)', 'Reverse MCP Server', 'An architecture allowing local development tools behind NATs/firewalls to connect to cloud-hosted AI agents via WebSockets.', 'mcp, reverse-mcp, connectivity, networking, local-dev', 'Reverse-remote-http transport, cloud-to-local tool access, secure WebSocket tunneling, NAT traversal.'),
    ('https://www.reddit.com/r/mcp/comments/1q91axj/lazy_loading_for_mcp_servers/', 'Context Engineering & Isolation', 'Lazy Loading MCP Gateway', 'A resource and token optimization strategy (e.g., Peta Gateway) that dynamically loads MCP servers and schemas only when invoked.', 'mcp, lazy-loading, context-optimization, orchestration, gateway', 'Dynamic server startup, auto-shutdown after 5m inactivity, context window token savings, dynamic tool search.'),
    ('https://www.reddit.com/r/mcp/comments/1qa0lhd/i_built_an_task_orchestrator_to_stop_ai_agents/', 'Agent Orchestration & Workflow', 'Graph-Based Task Orchestrator', 'An MCP server backed by a graph database (Neo4j) to strictly manage task dependencies and prevent agents from deviating from master plans.', 'orchestration, neo4j, graph-database, task-management, strict-routing', 'Neo4j dependency tracking, strict Claim/Complete task lifecycle, independent context per task, prevention of agentic drifting.'),
    ('https://www.reddit.com/r/mcp/comments/1qdk5br/otel_semantic_conventions_for_mcp/', 'Infrastructure & Proxy Layers', 'OTEL Conventions for MCP', 'A community initiative to standardize OpenTelemetry (OTEL) semantic conventions for MCP implementations to improve observability of nested tool calls.', 'mcp, observability, otel, opentelemetry, debugging', 'Standardized tracing for Model Context and Tool Execution, cross-implementation compatibility, nested tool-call tracking.')
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
print('Successfully injected batch 84.')