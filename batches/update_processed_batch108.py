import sqlite3

data = [
    ('https://www.reddit.com/r/ClaudeCode/comments/1ptj4fg/claudemem_80_introducing_modes_and_support_for_28/', 'Memory & Persistence Architecture', 'ClaudeMem: Domain-Specific Memory', 'A sophisticated memory layer introducing a "Mode" system that tailors what agents remember based on the active workflow (Code/Email/Investigate).', 'memory-architecture, domain-specific, context-management, salience-filter, optimization', 'Specialized observation schemas, task-based salience filters, inheritance for language-specific modes, dynamic mode-aware prompting.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1r2tt7q/i_saved_10m_tokens_89_on_my_claude_code_sessions/', 'Infrastructure & Proxy Layers', 'rtk: Output Distillation Proxy', 'A deterministic CLI proxy that intercepts raw tool output and prunes "noise" (ANSI codes, verbose logs) to reduce session token burn by 89%.', 'token-reduction, optimization, proxy, cli, efficiency', 'Pre-ToolUse interception hook, real-time redundancy elimination, structural compression of terminal output, graceful "verbose mode" degradation.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1pzczjn/git_worktrees_are_a_superpower_for_agentic_dev/', 'Agent Orchestration & Workflow', 'Worktree Parallelism Pattern', 'A production orchestration pattern using Git Worktrees to provide agents with isolated, parallel directories sharing a single object database.', 'git-worktrees, parallelism, isolation, orchestration, workflow', 'Parallel agent environment spawning, single object-database efficiency, MECE codebase partitioning, shared global `git fetch/pull` state.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1r6f3ux/i_built_a_braininspired_memory_system_that_runs/', 'Memory & Persistence Architecture', 'Claude-Engram: Bio-Memory', 'A brain-inspired memory system implementing a Hippocampal processing layer with deliberate decay rates and 3-day "Sleep Consolidation" cycles.', 'cognitive-architecture, memory-decay, brain-inspired, persistence, refinement', '4D Salience Scoring (Novelty/Relevance), deliberate forgetting curves (0.015/day), periodic "Sleep" consolidation cycles, episodic-to-semantic conversion.')
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
print('Successfully injected batch 66.')
