import sqlite3

data = [
    ('https://www.reddit.com/r/ClaudeCode/comments/1qsp5zj/the_claude_code_team_just_revealed_their_setup/', 'Agent Orchestration & Workflow', 'Claude Code: Agent Teams', 'The official orchestration system for parallel agent collaboration, using a Team Lead to coordinate specialized Teammates via a shared JSON task list.', 'orchestration, parallel-agents, team-lead, task-tracking, json-protocol', 'Direct agent-to-agent messaging (sendMessage), specialized teammate roles, shared context switchboard, lifecycle management (TeamCreate/TaskCreate).'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1qjn0wm/how_i_used_lsp_cc_to_prune_6400_lines_of_dead/', 'Development Tools & Libraries', 'LSP-Driven Code Pruning', 'A high-velocity maintenance workflow where agents use Language Server Protocol (LSP) diagnostics to verify and delete dead code at scale.', 'lsp, code-maintenance, static-analysis, dead-code, automation', 'Symbol-reference verification, batch unreferenced code removal, cross-service entry point detection, automated AST-based refactoring.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1qyxrid/i_built_codexmonitor_so_i_could_ship_code_while_i/', 'Infrastructure & Proxy Layers', 'CodexMonitor Control Plane', 'A Tauri-based control plane for orchestrating multiple background agent sessions across local and remote workspaces with daemon support.', 'control-plane, background-execution, monitoring, tauri, daemon', 'Spawns per-workspace app-servers, daemon-mode for remote control, git worktree isolation support, integrated Issue/PR CLI management.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1r03a0t/claude_code_playwright_cli_superpowers/', 'Interface & Developer UX', 'Playwright CLI: Stateless Automation', 'A high-efficiency, stateless browser automation pattern that reduces context usage by 16% compared to persistent MCP servers.', 'playwright, browser-use, automation, token-efficiency, self-healing', '16% Context footprint optimization, discrete single-purpose commands, local artifact-first debugging (traces/snapshots), autonomous DOM self-healing.')
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
print('Successfully injected batch 68.')
