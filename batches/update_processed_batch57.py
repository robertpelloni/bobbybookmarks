import sqlite3

data = [
    ('https://mcphubx.com/', 'Connectivity & Interoperability (MCP/A2A)', 'MCP Hub Directory', 'A central community registry and discovery platform for finding and integrating Model Context Protocol (MCP) servers across various domains.', 'mcp, registry, community, tools, discovery', 'Categorized server discovery, one-click Claude Desktop config, trending tools tracking, community submission portal.'),
    ('https://github.com/poly-mcp/Polymcp', 'Agent Orchestration & Workflow', 'Polymcp Orchestrator', 'A multi-language framework for building and orchestrating MCP servers and agents with built-in multi-tab inspector and Docker support.', 'mcp, orchestration, python, typescript, framework', 'Standalone MCP Inspector, PolyClaw autonomous worker, multi-server tool routing, UI-based MCP app SDK.'),
    ('https://github.com/portofcontext/pctx', 'Context Engineering & Isolation', 'pctx Context Porter', 'An open-source "Code Mode" gateway that converts sequential tool calls into a single execution block to reduce context window usage.', 'context-engineering, code-mode, optimization, deno, sandbox', '58% token reduction, 56% cost efficiency, isolated Deno sandboxing, unified multi-server authentication.'),
    ('https://github.com/chris-schra/mcp-funnel', 'Context Engineering & Isolation', 'MCP Funnel Proxy', 'A specialized proxy that performs "tree-shaking" on MCP servers to filter out unused tools and significantly reduce context token consumption.', 'mcp, proxy, optimization, context-window, efficiency', 'Wildcard tool filtering (tree-shaking), 40-60% context reduction, multi-server aggregation, developer-centric proxy.'),
    ('https://github.com/roddutra/agent-mcp-gateway', 'Connectivity & Interoperability (MCP/A2A)', 'Enterprise Agent Gateway', 'A high-performance Rust-based control plane for managing secure connectivity, authentication, and audit logs for MCP and A2A agents.', 'mcp, a2a, gateway, security, enterprise', 'Centralized JWT/API auth, high-throughput Rust engine, unified tool discovery, multi-agent state management.'),
    ('https://github.com/sathish316/opus_agents', 'Agent Orchestration & Workflow', 'Opus Agent Swarm', 'A framework specifically optimized for Claude 3 Opus, implementing a Manager-Worker orchestration pattern for autonomous task execution.', 'claude-opus, swarm, orchestration, patterns, workflow', 'Manager-Worker hierarchy, multi-step reasoning loops, local file/web tool integration templates.'),
    ('https://github.com/portel-dev/ncp', 'Infrastructure & Proxy Layers', 'Native Context Protocol (NCP)', 'A lower-level protocol designed for high-performance context passing between hardware or OS-native processes, as opposed to application-level MCP.', 'ncp, protocol, low-level, systems, context', 'Memory-mapped state transfer, low-latency binary transport, hardware context optimization, OS-level integration.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
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
    ''', (url, cat, sd, ld, tags, mf, 8))
conn.commit()
conn.close()
print('Successfully injected batch 23.')
