import sqlite3

data = [
    ('https://tidewave.ai/blog/claude-code-codex', 'Guides & Articles', 'Tidewave Claude/Codex Integration', 'Technical blog post announcing the integration of Claude Code and OpenAI Codex into the Tidewave browser-based ADE.', 'blog, tidewave, claude-code, acp, codex', 'WebSocket-based ACP/MCP integration, deep framework access, browser-based agentic coding environment.'),
    ('https://github.com/milisp/opencode-gui', 'Development Tools & Libraries', 'OpenCode GUI', 'A lightweight desktop interface for OpenCode built with Tauri, providing a graphical alternative to the CLI.', 'opencode, gui, tauri, desktop-app', 'Native cross-platform UI, local server connection, real-time agent visualization.'),
    ('https://github.com/chris-tse/opencode-web', 'Development Tools & Libraries', 'OpenCode Web', 'A web-based frontend for managing and visualizing OpenCode AI agents, enabling remote collaboration.', 'opencode, web-ui, collaboration, visualization', 'Real-time execution logs, browser-based agent orchestration, multi-user session viewing.'),
    ('https://opencode.ai/docs/plugins/', 'Guides & Articles', 'OpenCode Plugin Documentation', 'Comprehensive technical guide for extending the OpenCode platform using JavaScript/TypeScript plugins.', 'opencode, plugins, documentation, extensibility', 'System event hooks, tool overriding, custom prompt injection, session management APIs.'),
    ('https://github.com/slashtechno/amped', 'Development Tools & Libraries', 'Amped Account Switcher', 'A Go-based utility for seamlessly switching between multiple profiles and providers for the Amp and Claude Code agents.', 'cli, account-switcher, claude-code, go', 'Secure credential management, automatic service context switching, multi-account support.'),
    ('https://github.com/slopus/happy', 'Development Tools & Libraries', 'Happy Remote Agent', 'An open-source mobile and web client providing secure remote access and push notifications for local AI agent sessions.', 'remote-access, mobile-app, claude-code, security', 'End-to-End encrypted sessions, mobile push notifications, instant device handoff, voice support.'),
    ('https://github.com/2mawi2/schaltwerk', 'AI Agents & Frameworks', 'Schaltwerk ADE', 'A specialized Agentic Development Environment that utilizes git worktrees to run multiple coding agents in parallel.', 'terminal-ui, orchestration, git-worktrees, parallel-agents', 'Isolated branch development, dual-terminal testing setup, conflict-free parallel implementation.'),
    ('https://github.com/steipete/claude-code-mcp', 'MCP', 'Claude Code One-Shot Wrapper', 'A specialized MCP server that runs Claude Code in a one-shot mode, bypassing permissions for automated tasks.', 'mcp, claude-code, automation, tool-offloading', 'Permission bypass mode, command queuing, cross-model tool offloading.'),
    ('https://github.com/brwse/claude-tools-mcp', 'MCP', 'Claude Tools HTTP Server', "An MCP server that securely exposes Claude Code's file and shell manipulation tools over HTTP for remote agents.", 'mcp, tools, file-ops, shell-execution', 'Secure remote shell execution, line-based file modification, path validation and safety gates.'),
    ('https://github.com/OpenHands/OpenHands', 'AI Agents & Frameworks', 'OpenHands Platform', 'A complete open-source platform for AI-driven development providing a composable agent SDK and visual workspace.', 'openhands, agent-sdk, gui, enterprise', 'Composable Agent SDK, React-based visual workspace, multi-LLM support, enterprise RBAC and Kubernetes integration.'),
    ('https://www.dropstone.io/features', 'AI Agents & Frameworks', 'Dropstone Platform', 'An AI-native platform with infinite context, trajectory search, and a multi-agent swarm architecture for large codebases.', 'dropstone, orchestration, agent-swarms, enterprise', 'Infinite context knowledge graph, Horizon Mode (10k+ paths), self-verifying code generation.'),
    ('https://github.com/github/awesome-copilot', 'Guides & Articles', 'Awesome GitHub Copilot', 'The official community-driven list of custom agents, instructions, and plugins to extend the capabilities of GitHub Copilot.', 'awesome-list, github-copilot, plugins, mcp', 'Custom instruction sets, agentic workflow templates, curated MCP server directory.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level)
        VALUES (?, ?, ?, ?, ?, ?, 'deep')
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='deep'
    ''', (url, cat, sd, ld, tags, mf))
conn.commit()
conn.close()
print('Successfully upgraded earlier high-value links to deep research.')
