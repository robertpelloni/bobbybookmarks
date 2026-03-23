import sqlite3

data = [
    ('https://www.reddit.com/r/codex/comments/1q30nd4/gpt52_high_gptcodex52high_and_even_extrahigh/', 'AI Agents & Frameworks', 'GPT-5.2 Codex: XHigh Reasoning', 'A deep analytical mode for complex software engineering that spends 5-10 minutes on internal simulations to catch errors before code generation.', 'codex, gpt-5-2, reasoning-effort, xhigh, agi-adjacent', 'XHigh 5-10m reasoning cycle, internal error-simulation loops, optimized for large-scale refactors, AGI-adjacent coding performance.'),
    ('https://www.reddit.com/r/codex/comments/1qc3x5b/codex_manager_v100_desktop_app_to_manage_openai/', 'Interface & Developer UX', 'Codex Manager: Asset Hub', 'A cross-platform desktop application for centralized management of agent configurations, skills, and Model Context Protocol (MCP) servers.', 'gui, desktop-app, management, mcp, skills', 'Centralized config management, Skill/MCP GUI installer, stacked diff configuration previews, token/rate-limit usage dashboard.'),
    ('https://www.reddit.com/r/codex/comments/1qjapzz/claude_code_cli_uses_way_more_input_tokens_than/', 'Infrastructure & Proxy Layers', 'Codex: Response Compaction', 'A loss-aware context compression mechanism that serializes conversation state into opaque items, enabling 3x higher token efficiency than competitors.', 'optimization, context-compression, token-efficiency, scale, infrastructure', 'Loss-aware context compaction, encrypted state serialization, 3x-4x higher efficiency vs Claude Code, support for virtually infinite sessions.'),
    ('https://www.reddit.com/r/codex/comments/1q60bfz/okay_seriously_worktrees_52_xhigh_mcps_skills_im/', 'Agent Orchestration & Workflow', 'Codex: Worktree Parallelism', 'A standardized orchestration pattern that uses Git Worktrees to provide isolated directories for parallel agent threads sharing a single object database.', 'git-worktrees, parallelism, isolation, orchestration, performance', 'Automated worktree creation (detached HEAD), isolated directory per agent thread, shared global .git object store, automated environment setup scripts.')
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
print('Successfully injected batch 72.')
