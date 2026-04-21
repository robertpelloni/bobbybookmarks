import sqlite3

data = [
    ('https://github.com/gemini-cli-extensions/nanobanana', 'AI Agents & Frameworks', 'Nanobanana Visual Extension', 'A professional image generation and manipulation extension for the Gemini CLI, leveraging Gemini 3.1 Flash Image models.', 'gemini-cli, media-gen, imagen, visual-tools, productivity', '/generate text-to-image, /edit natural language image modification, /restore photo enhancement, app icon generation.'),
    ('https://github.com/gemini-cli-extensions/jules', 'AI Agents & Frameworks', 'Jules Background Agent', 'An autonomous asynchronous agent for the Gemini CLI that handles complex coding tasks, PRs, and refactors in the background.', 'gemini-cli, autonomous, sidekick, background-tasks, workflow', 'VM-based background execution, native GitHub PR integration, parallel multi-issue tasking, real-time status tracking.'),
    ('https://github.com/smonux/chgpt-mcp-bridge', 'Infrastructure', 'OpenAI-MCP Bridge', 'A middleware proxy that allows OpenAI-compatible clients to utilize Model Context Protocol (MCP) tools and servers.', 'mcp, bridge, openai, proxy, middleware', 'Unified REST API for MCP servers, streaming completion support, SSE bridge integration, LLM-agnostic tool calling.'),
    ('https://github.com/macc-n/wot-mcp', 'MCP', 'Web of Things MCP Server', 'An implementation of the Model Context Protocol that bridges AI agents with smart devices supporting the W3C Web of Things standard.', 'mcp, wot, iot, smart-devices, automation', 'Automatic device capability discovery, property state reading (temp/light), action invocation (toggles), event-based state monitoring.'),
    ('https://github.com/eqtylab/agent-console', 'Development Tools & Libraries', 'Agent Console Visualizer', 'A web-based console for monitoring and managing multiple AI coding agent sessions across isolated git worktrees.', 'gui, monitoring, dashboard, git-worktrees, orchestration', 'Unified session dashboard, live agent thought monitoring, integrated side-by-side diffing, Cupcake policy evaluation viewer.'),
    ('https://github.com/unkn0wn-root/resterm', 'Development Tools & Libraries', 'Resterm TUI API Client', 'A keyboard-driven terminal API client for HTTP, GraphQL, and gRPC, designed as a terminal-native alternative to Postman.', 'tui, cli, api-client, terminal, productivity', 'Local-first .http/.rest files, SSH tunnel support, Kubernetes port-forwarding, RestermScript (RTS) request chaining.'),
    ('https://github.com/Papr-ai/memory-opensource', 'AI Agents & Frameworks', 'Papr Predictive Memory', 'A sophisticated predictive memory layer combining vector databases and knowledge graphs for long-term agent context.', 'memory, context, knowledge-graph, agent-memory, persistence', '91% accuracy on Stanford STARK benchmark, <100ms retrieval latency, structured relationship extraction, multi-database support (MongoDB/Qdrant/Neo4j).')
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
print('Successfully injected batch 10.')
