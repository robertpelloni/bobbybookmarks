import sqlite3

data = [
    ('https://github.com/BloopAI/vibe-kanban', 'Agent Orchestration & Workflow', 'Vibe Kanban Orchestrator', 'A visual orchestration platform for running parallel AI agents in isolated git worktrees, central to the "vibe coding" paradigm.', 'vibe-coding, kanban, orchestration, git-worktrees, automation', 'Parallel agent execution, isolated worktree management, inline diff review, integrated browser preview.'),
    ('https://github.com/Canner/WrenAI', 'Memory & Persistence Architecture', 'WrenAI Semantic Layer', 'A Generative Business Intelligence engine that uses a Modeling Definition Language (MDL) to provide agents with a semantic layer for SQL data.', 'genbi, semantic-layer, sql, data-agent, business-intelligence', 'MDL semantic modeling, automated SQL/chart generation, Wren Engine embeddable core, multi-database support.'),
    ('https://github.com/Cluster444/agentic', 'Context Engineering & Isolation', 'Cluster444 Agentic Harness', 'A structured context management tool that implements a /thoughts directory to provide agents with long-term memory and systematic workflows.', 'context-engineering, memory, workflow, opencode, productivity', 'Structured /thoughts directory, phased implementation loops, specialized subagent delegation, automated ticket decomposition.'),
    ('https://github.com/Intrect-io/OpenSwarm', 'Agent Orchestration & Workflow', 'OpenSwarm Software Factory', 'An autonomous AI development team orchestrator that spawns collaborative Claude Code pairs to automate Linear and GitHub issues.', 'swarm, multi-agent, linear-integration, software-factory, automation', 'Worker/Reviewer agent pairs, Linear ticket auto-pickup, LanceDB cognitive memory, Discord-based human approval UI.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 9) for d in data]:
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
print('Successfully injected batch 34.')
