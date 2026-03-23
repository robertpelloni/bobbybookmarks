import sqlite3

data = [
    ('https://www.reddit.com/r/codex/comments/1q8w9xz/codex_cli_agent_to_agent_communication_weave/', 'Connectivity & Interoperability (MCP/A2A)', 'Weave: Inter-Agent Protocol', 'A lightweight messaging substrate that allows CLI agents to prompt each other and issue remote slash commands (e.g., /new to reset context).', 'protocol, a2a, inter-agent, context-isolation, weave', 'Direct #agent-name syntax, remote slash command execution, infinite loop safeguards, context isolation per specialized agent.'),
    ('https://www.reddit.com/r/codex/comments/1qj8cpj/spawning_agents_is_here/', 'Agent Orchestration & Workflow', 'Codex: Native Agent Spawning', 'An official orchestration feature (v0.88+) allowing a main orchestrator to natively spawn and coordinate worker agents in parallel.', 'orchestration, multi-agent, spawning, parallelism, codex', 'Native spawn_agent tool, Orchestrator vs Worker role definitions, parallel execution support, context narrowing strategy.'),
    ('https://www.reddit.com/r/codex/comments/1qjomsz/can_anyone_give_an_example_of_using_collab_multi/', 'Agent Orchestration & Workflow', 'Multi-Agent Collab Pattern', 'A workflow pattern that pairs multi-agent `collab` spawning with Git Worktrees to execute isolated parallel tasks without file system conflicts.', 'orchestration, git-worktrees, collab, multi-agent, workflow', 'Git worktree environment isolation, Orchestrator -> Feature/Review/Merge agent pipeline, elimination of the "lost-in-the-middle" effect.'),
    ('https://www.reddit.com/r/codex/comments/1qjrfn8/codex_feature_flags_explained_plus_undocumented/', 'Infrastructure & Proxy Layers', 'Codex Feature Flags (Undoc)', 'An analysis of undocumented Codex features, revealing advanced performance optimizations like zstd request compression and websocket responses.', 'optimization, feature-flags, codex, compression, performance', 'zstd request compression (enable_request_compression), WebSocket response transport, steer mode configuration, experimental TUI modes.')
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
print('Successfully injected batch 76.')