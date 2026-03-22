import sqlite3

data = [
    ('https://github.com/4regab/TaskSync', 'AI Agents & Frameworks', 'TaskSync Workflow Optimizer', 'A VS Code extension and workflow tool designed to batch and queue instructions for AI agents, enabling autonomous long-running task execution.', 'tasksync, vs-code, automation, workflow, productivity', 'Smart Queue Mode, Autopilot autonomous response cycle, Workspace isolation, Reusable Slash Commands.'),
    ('https://github.com/rayai-labs/agentic-ray', 'Infrastructure', 'Agentic Ray Scaling Engine', 'Distributed infrastructure built on the Ray framework for running massive, parallel AI agent workloads with secure sandboxing and fault tolerance.', 'ray, distributed-computing, scaling, agents, infrastructure', 'Massive parallelism across nodes, Automatic checkpointing/failover, Secure sandboxed execution, Resource-aware scheduling.'),
    ('https://github.com/biagruot/agentdepot-agents', 'AI Agents & Frameworks', 'AgentDepot Data Backbone', 'The open-source data layer for AgentDepot.dev, centralizing verified and tested configurations for Cursor, Claude Code, and other AI IDEs.', 'agent-depot, registry, configurations, ide, community', 'Multi-format indexing (Cursor/Claude/Windsurf), Verified/tested configurations, Actionable setup docs, community-driven database.'),
    ('https://github.com/vstorm-co/pydantic-deepagents', 'AI Agents & Frameworks', 'Pydantic DeepAgents', 'A Python framework built on Pydantic AI for building "Deep Agents" that utilize planning, subagent delegation, and direct filesystem access.', 'pydantic-ai, deep-agents, autonomous, python, sdk', 'Planning Mode subagent, Filesystem-first operations, Subagent delegation protocol, Persistent MEMORY.md storage, Built-in cost tracking.'),
    ('https://github.com/denniszielke/agentic-playground', 'AI Agents & Frameworks', 'Agentic Orchestration Lab', 'A comprehensive laboratory for testing and demonstrating agent patterns like ReAct, multi-agent coordination, and event-driven architectures.', 'playground, lab, patterns, react, orchestration', 'Multi-agent Manager/Worker patterns, Event-driven agent response, Multimodal vision/voice testing, MCP integration testing.'),
    ('https://www.copilotkit.ai/blog/build-with-googles-new-a2ui-spec-agent-user-interfaces-with-a2ui-ag-ui', 'AI Agents & Frameworks', 'A2UI Declarative UI Spec', 'A JSON-based specification for AI agents to describe interactive user interfaces declaratively, ensuring security and cross-platform compatibility.', 'a2ui, generative-ui, standard, protocol, ux', 'Declarative JSON format, Component catalog security, Incremental surface updates, Framework-agnostic rendering.'),
    ('https://github.com/ag-ui-protocol/ag-ui', 'AI Agents & Frameworks', 'AG-UI Interaction Protocol', 'A lightweight, event-based protocol designed to standardize real-time communication and state synchronization between AI agents and frontends.', 'ag-ui, protocol, real-time, sse, hitl', 'Unified JSON event stream (SSE), Bi-directional state sync (JSON Patch), Native Human-in-the-Loop support, multi-model backend flexibility.')
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
print('Successfully injected batch 4.')
