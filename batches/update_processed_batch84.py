import sqlite3

data = [
    ('https://github.com/IronManus/ironmanus', 'Agent Orchestration & Workflow', 'Iron Manus Orchestrator', 'A high-reliability orchestration framework that manages AI workflows through a defined 8-phase control flow, prioritizing observability and deterministic action.', 'orchestration, workflow, observability, deterministic-ai, framework', '8-Phase control flow logic, built-in task judgment (knowing when to stop), multi-step reasoning visualization, production-grade agent telemetry.'),
    ('https://github.com/fastmcp/fastmcp', 'Connectivity & Interoperability (MCP/A2A)', 'FastMCP Framework', 'A standardized framework and one-click installer for MCP servers, designed to simplify the deployment and scaling of agentic tools across various IDEs.', 'mcp, framework, deployment, standardization, tool-scaling', 'One-click MCP installation, built-in server registry, cross-IDE compatibility (Cursor/VSCode/Claude), auto-schema generation.'),
    ('https://github.com/recallium/recallium', 'Memory & Persistence Architecture', 'Recallium: Universal Memory', 'A local, self-hosted memory system for agents that automatically captures and clusters knowledge across multiple projects to eliminate "AI amnesia."', 'memory, local-first, knowledge-graph, persistence, second-brain', 'Multi-project knowledge clustering, automated fact extraction, local vector storage, unified memory API for agents.'),
    ('https://github.com/context7/context7', 'Context Engineering & Isolation', 'Context7: Real-time Doc Aggregator', 'A specialized context engineering tool that provides agents with real-time documentation for modern frameworks (Next.js 15, Tailwind v4) to bypass stale training data.', 'context-engineering, documentation, rag, real-time-data, optimization', 'Real-time documentation scraping, automated version-aware indexing, token-efficient context injection, support for latest framework updates.')
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
print('Successfully injected batch 50.')
