import sqlite3

data = [
    ('https://github.com/google/adk-js', 'AI Agents & Frameworks', 'Google Agent Development Kit (JS)', 'An open-source, code-first toolkit for building and deploying A2A-compliant agents, providing fine-grained orchestration control.', 'adk, a2a, protocol, agent-sdk, google-cloud', 'Agent2Agent protocol implementation, peer-to-peer agent communication, distributed multi-agent coordination, unified TS/Go/Java/Py framework.'),
    ('https://github.com/av/awesome-llm-services', 'Guides & Articles', 'Awesome Self-Hostable AI', 'A high-signal curated list of over 115+ self-hostable LLM services, backends, and frontends for local AI sovereignty.', 'awesome-list, self-hosted, inference, ai-sovereignty, homelab', '115+ Vetted projects, relevance-scored rankings, categorization by stack layer, dedicated MCP section.'),
    ('https://github.com/agentic-mcp-tools/memora', 'AI Agents & Frameworks', 'Memora Persistent Memory', 'A lightweight MCP server providing AI agents with persistent, long-term memory via hybrid search and knowledge graph visualization.', 'memory, mcp, context, persistence, knowledge-graph', 'Semantic and hybrid search, interactive graph visualization, SQLite/S3/D1 cloud sync, LLM-powered memory deduplication.'),
    ('https://github.com/saikiranrallabandi/inframind', 'AI Agents & Frameworks', 'InfraMind IaC Optimizer', 'A fine-tuning toolkit utilizing RL (GRPO) to transform small language models into high-accuracy Infrastructure-as-Code generators.', 'iac, fine-tuning, slm, reasoning, grpo', '97.3% IaC accuracy, Group Relative Policy Optimization (GRPO), domain-specific reward functions, optimized for Qwen2.5-0.5B.'),
    ('https://github.com/EJ-Tether/Tether-Chat', 'AI Agents & Frameworks', 'Tether-Chat Desktop', 'A native C++ desktop LLM client that manages rolling memory journals to enable unlimited conversation length without context loss.', 'desktop-app, c++ , memory, local-first, context-management', 'Short-term and Long-term journal system, automated LLM reflections, native QML performance, local SQLite storage.'),
    ('https://github.com/ojowwalker77/Claude-Matrix', 'AI Agents & Frameworks', 'Claude-Matrix Plugin', 'A comprehensive Claude Code plugin that adds semantic memory, code indexing, and automated background tasks to the CLI.', 'claude-code, automation, memory, tree-sitter, workflow', 'Automated "Dreamer" background tasks, Tree-sitter code indexing, persistent semantic memory, safety interception hooks.'),
    ('https://github.com/digit1024/mcp_obsidian_notes', 'MCP', 'Obsidian MCP (Standalone)', 'A Model Context Protocol server that provides standalone access to Obsidian vaults via high-performance SQLite Full-Text Search.', 'mcp, obsidian, tools, knowledge-base, search', 'No Obsidian app dependency, SQLite-based FTS, Standalone vault access, optimized for smaller LLMs.'),
    ('https://github.com/tylergraydev/claude-limitline', 'Development Tools & Libraries', 'Claude Limitline UI', 'A real-time terminal statusline utility for Claude Code users to track their session and weekly usage limits.', 'claude-code, productivity, limit-tracking, cli, dashboard', 'Real-time usage percentage tracking, persistent terminal status bar, simple npx integration, low-overhead monitoring.'),
    ('https://github.com/AbanteAI/spice', 'AI Agents & Frameworks', 'AbanteAI Spice Accelerant', 'A Python-based performance optimizer for the Mentat agent ecosystem, focusing on reducing context processing latency.', 'mentat, optimization, performance, agent-acceleration, python', 'Reduced context-switching overhead, optimized codebase indexing, specific speed-ups for Mentat agents.'),
    ('https://github.com/AbanteAI/party', 'AI Agents & Frameworks', 'AbanteAI Party Agentic UI', 'A declarative UI framework for AI agents, focusing on interactive, multi-step sessions with synchronized collaborative state.', 'agentic-ui, ux, a2ui, interactive-agent, collaboration', 'Declarative UI projection, A2UI protocol support, real-time state synchronization, interactive forms and pickers.')
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
print('Successfully injected batch 11.')
