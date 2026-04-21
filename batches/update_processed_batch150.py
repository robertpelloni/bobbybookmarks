import sqlite3

data = [
    ('https://www.reddit.com/r/warpdotdev/comments/1r15jvm/introducing_oz_the_platform_to_run_agents_in_the/', 'Infrastructure & Proxy Layers', 'Oz: Cloud Agent Platform', 'A cloud-native orchestration platform by Warp that runs coding agents in isolated Docker containers, supporting multi-repo environments and live steering.', 'oz, warp, orchestration, cloud-native, containers', 'Isolated cloud sandboxes, multi-repo support, live log steering/nudging, automated task scheduling (oz schedule).'),
    ('https://www.reddit.com/r/warpdotdev/comments/1q4wiwk/how_our_engineering_team_built_the_mcp_search/', 'Connectivity & Interoperability (MCP/A2A)', 'Warp MCP Search Subagent', 'A model-agnostic subagent implementation for efficient tool discovery that reduces context bloat by 26% through natural-language search over tool schemas.', 'mcp, search, optimization, warp, subagent', 'Model-agnostic search subagent, 26% reduction in MCP token bloat, dynamic tool/resource discovery, lossless quality pruning.'),
    ('https://www.reddit.com/r/warpdotdev/comments/1pzcqkf/git_worktrees_are_for_agentic_dev/', 'Agent Orchestration & Workflow', 'Agentic Git Worktrees', 'A workflow pattern using Git Worktrees to provide isolated feature directories for parallel agent sessions, preventing file conflicts and enabling rapid rollback.', 'git-worktrees, parallelism, isolation, orchestration, workflow', 'Parallel feature branching, isolated directory per agent, atomic rollback via worktree deletion, "treehouse" pool management.'),
    ('https://www.reddit.com/r/windsurf/comments/1rjqsfr/which_al_is_stealing_your_ideas/', 'Guides & Industry Trends', 'AI Privacy: Leakage vs Convergence', 'A community analysis of AI data privacy and the fears of "convergent evolution" where AI-assisted development may inadvertently lead to competitive IP leakage.', 'privacy, ip-protection, security, philosophy, data-retention', 'Zero Data Retention (ZDR) limitations, convergent evolution risk analysis, competitive IP leakage tracking, security-first vibe coding.')
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
print('Successfully injected batch 100.')