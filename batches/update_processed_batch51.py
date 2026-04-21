import sqlite3

data = [
    ('https://github.com/letta-ai/letta', 'AI Agents & Frameworks', 'Letta Agent Platform', 'The commercial evolution of MemGPT into a stateful "Agents-as-a-Service" platform with persistent memory and a native development environment.', 'letta, memgpt, stateful-agents, memory, persistence', 'Self-editing memory, hierarchical storage (Core/Archival/Recall), multi-user REST API, graphical Agent Development Environment (ADE).'),
    ('https://github.com/GreatScottyMac/context-portal', 'MCP', 'Context Portal Memory Bank', 'An open-source MCP server designed as a persistent memory bank for AI coding assistants to track decisions and architectural patterns.', 'mcp, context, memory-bank, coding-assistant, knowledge-graph', 'Structured relational/graph storage, semantic and SQL search, project knowledge graph visualization, optimized for VS Code/Claude Code.'),
    ('https://github.com/vectorize-io/hindsight', 'AI Agents & Frameworks', 'Hindsight Biomimetic Memory', 'A biomimetic memory system for AI agents that mimics human cognitive processes through a "Retain, Recall, Reflect" lifecycle.', 'hindsight, biomimetic, memory, learning, cognitive-computing', 'LLM-powered entity extraction, spreading activation recall, automated mental model generation, multi-session temporal reasoning.'),
    ('https://github.com/Dicklesworthstone/beads_viewer', 'Development Tools & Libraries', 'Beads Viewer TUI', 'A graph-aware TUI engine for the Beads issue tracker that calculates PageRank and centrality metrics to offload dependency logic from LLMs.', 'tui, graph-theory, task-management, dependencies, automation', 'Automated graph-based triage, deterministic PageRank/Critical Path metrics, robot-mode for agentic planning, terminal-native visualization.'),
    ('https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/', 'Guides & Articles', 'Google Nested Learning', 'A groundbreaking Google Research blog introducing a new paradigm for continual learning and unbounded in-context reasoning in AI systems.', 'google-research, continual-learning, machine-learning, hope-architecture, future-ai', 'Nested optimization problems, Continuum Memory Systems (CMS), self-modifying "Hope" architecture, solution to catastrophic forgetting.'),
    ('https://github.com/verygoodplugins/mcp-automem', 'MCP', 'AutoMem Graph-Vector Memory', 'A Model Context Protocol service that implements a graph-vector architecture using FalkorDB and Qdrant for persistent AI memory.', 'mcp, memory, falkordb, qdrant, persistent-state', 'Hybrid graph-vector retrieval, MELODI memory compression, HippoRAG 2 associative memory, durable cross-platform state.'),
    ('https://github.com/DrDavidL/sem-mem', 'AI Agents & Frameworks', 'Semantic Memory Layer', 'A high-performance local-first memory layer for AI agents featuring zero-latency hot recall and time-decay relevance scoring.', 'memory, semantic-search, local-first, optimization, hnwslib', 'LRU-based "hot" recall, hybrid Vector/Lexical search, half-life time-decay scoring, automated Playwright content extraction.'),
    ('https://github.com/zeddy89/Context-Engine', 'AI Agents & Frameworks', 'Claude Code Context Engine', 'An autonomous project builder and context management harness specifically designed to prevent performance degradation in Claude Code sessions.', 'claude-code, context-management, orchestration, automation, productivity', 'Four-layer memory architecture, automated "overnight" implementation loops, native hook state restoration, proven multi-feature scalability.'),
    ('https://github.com/roampal-ai/roampal-core', 'AI Agents & Frameworks', 'RoamPal Outcome-Based Memory', 'A persistent memory engine focusing on "Outcome-Based Memory" that learns which AI interactions actually work using statistical scoring.', 'memory, machine-learning, wilson-score, knowledge-graph, effectiveness', 'Interaction effectiveness tracking, Wilson Lower Bound scoring, triple knowledge graph integration, automated promotion/deletion of patterns.')
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
print('Successfully injected batch 18.')
