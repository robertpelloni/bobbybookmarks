import sqlite3

data = [
    ('https://www.reddit.com/r/google_antigravity/comments/1r4hg92/i_uninstalled_the_quota_monitor_and_created_my/', 'Interface & Developer UX', 'Antigravity Quota Monitor', 'A lightweight, open-source VS Code extension that reads quota data directly from the local Antigravity instance without background API polling.', 'quota, monitoring, optimization, antigravity, vscode', 'Local instance reading, zero background API polling, 120kb footprint, reduces artificial rate limits.'),
    ('https://www.reddit.com/r/google_antigravity/comments/1r66n4q/running_several_agents_at_the_same_time/', 'Agent Orchestration & Workflow', 'Simultaneous Agent Execution', 'A pattern for invoking separate CLI sessions via external scripts to isolate context and prevent bias (e.g., coder vs reviewer) in multi-agent workflows.', 'orchestration, multi-agent, context-isolation, cli, script', 'External Python/Bash orchestration, separate CLI session invocation, strict context isolation, bias prevention.'),
    ('https://www.reddit.com/r/google_antigravity/comments/1rfj1jo/i_built_a_memory_bank_system_that_makes/', 'Memory & Persistence Architecture', 'Project Athena: Memory Bank', 'A personalization layer that stores project context and architectural decisions as plain Markdown files, allowing agents to remember across hundreds of sessions.', 'memory-architecture, markdown, persistence, context-rot, antigravity', 'Plain Markdown storage, read/write at session boundaries, provider-agnostic memory, solves cross-session context rot.'),
    ('https://www.reddit.com/r/google_antigravity/comments/1rg0483/how_to_make_true_parallel_agent_teams_in/', 'Agent Orchestration & Workflow', 'True Parallel Agent Teams', 'Strategies for achieving true parallel execution using Antigravity SDK, shared Markdown state, or Git-based feature branching.', 'orchestration, parallel-agents, sdk, git, shared-state', 'Antigravity SDK orchestration, shared Markdown/MCP state, Git-based parallel branching, Manager view execution.')
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
print('Successfully injected batch 79.')