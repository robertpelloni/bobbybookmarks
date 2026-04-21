import sqlite3

data = [
    ('https://www.reddit.com/r/opencodeCLI/comments/1qljsw3/opencodenvim_opencode_fully_integrated_into_neovim/', 'Interface & Developer UX', 'opencode.nvim: Neovim Native', 'A native Neovim integration for OpenCode that rebuilds the CLI interface into a native editor component, often paired with Tmux or CodeCompanion.', 'neovim, vim, editor, integration, opencode', 'Native Neovim component UI, CodeCompanion adapter support, Tmux pane orchestration, file system synchronization.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1r0okeg/adversarial_code_review_subagent_strategy/', 'Agent Orchestration & Workflow', 'Adversarial Subagent Review', 'An "elite pattern" for code integrity where a team of subagents from different providers (GPT-5/Claude/Gemini) are instructed to destroy or disprove each other\'s work before merging.', 'orchestration, review, multi-agent, adversarial, security', 'Cross-provider consensus loops, Security Attacker / Performance Critic roles, destructive disproof mandates, high-integrity implementation.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1r080rx/mnemo_indexes_opencode_sessions_search_all_your/', 'Memory & Persistence Architecture', 'Mnemo: Cross-Tool Indexer', 'A unified local indexer that aggregates session history from 12+ tools (OpenCode, Claude Code, Antigravity) into a local SQLite DB for token-free context injection.', 'memory, search, sqlite, persistence, context-management', 'Unified 12-tool session index, local SQLite FTS5 search, token-free context retrieval, historical architectural recall.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1qzswfa/i_built_an_opencode_plugin_so_you_can_monitor_and/', 'Interface & Developer UX', 'Owlex: Web Control for CLI', 'An MCP server (Owlex) that enables monitoring and control of local OpenCode sessions directly from web browsers like the Claude.ai console.', 'web-interface, remote-control, mcp, monitoring, opencode', 'Web-based CLI monitoring, browser-to-local task control, Owlex MCP transport, hybrid web/local development.')
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
print('Successfully injected batch 93.')