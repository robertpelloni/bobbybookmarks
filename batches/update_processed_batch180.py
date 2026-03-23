import sqlite3

data = [
    ('https://github.com/FoundationAgents/OpenManus', 'Agent Orchestration & Workflow', 'OpenManus: Open Autonomy', 'A community-driven, open-source alternative to proprietary autonomous agents that uses RL-based decision making (GRPO) to execute multi-step web and code tasks.', 'autonomy, open-source, meta-gpt, rl, orchestration', 'Autonomous workflow execution, OpenManus-RL decision engine, Playwright/Python tool integration, real-time reasoning visualization.'),
    ('https://github.com/FSoft-AI4Code/HyperAgent', 'Agent Orchestration & Workflow', 'HyperAgent: Repo Engineering', 'A generalist multi-agent system (Planner/Navigator/Editor/Executor) optimized for repository-level software engineering and automated fault localization.', 'orchestration, multi-agent, engineering, swe-bench, repair', 'Specialized agent roles (Planner/Navigator), semantic code search (Zoekt), automated fault localization, high SWE-bench performance.'),
    ('https://github.com/exa-labs/exa-mcp-server', 'Connectivity & Interoperability (MCP/A2A)', 'Exa MCP: Semantic Search', 'An MCP server connecting agents to Exa\'s neural search engine for conceptually relevant technical research and clean, token-efficient content scraping.', 'mcp, exa, semantic-search, neural-search, research', 'Neural conceptual search, specialized `exa-code` snippets, clean content scraping (token savings), autonomous deep research synthesis.'),
    ('https://github.com/eyaltoledano/claude-task-master', 'Agent Orchestration & Workflow', 'Claude Task Master: PRD Ops', 'An AI-powered task management system that automates the PRD-to-task lifecycle, using dependency tracking and verification loops to prevent "code slop."', 'task-management, workflow, prd, verification, automation', 'Automated PRD-to-Task conversion, Perplexity-driven subtask expansion, explicit dependency chain tracking, autonomous implementation verification.')
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
print('Successfully injected batch 126.')