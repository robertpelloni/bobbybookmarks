import os

links = [
    ('https://opencode.ai/docs/plugins/', 'Guides & Articles', 'OpenCode Plugin Docs', 'Documentation for creating and using plugins to extend the OpenCode platform via hooks, tools, and custom configurations.', 'opencode, plugins, documentation, extensibility', 'NPM Package support, Tool Hooks, Session Management, Event Subscription.'),
    ('https://github.com/slashtechno/amped', 'Development Tools & Libraries', 'Amped Account Switcher', 'A CLI utility written in Go for seamlessly switching between multiple accounts/profiles for Amp and Claude Code.', 'cli, account-switcher, claude-code, go', 'Secure Credential Storage, Multi-Account Switching, Automatic Service Context.'),
    ('https://github.com/slopus/happy', 'Development Tools & Libraries', 'Happy Remote Agent', 'An open-source mobile and web client providing secure remote access and push notifications for local Claude Code and Codex sessions.', 'remote-access, mobile-app, claude-code, security', 'End-to-End Encryption, Instant Device Switching, Push Notifications, Voice Support.'),
    ('https://github.com/2mawi2/schaltwerk', 'AI Agents & Frameworks', 'Schaltwerk ADE', 'A native terminal AI agent interface that utilizes git worktrees to run multiple agentic coding CLIs simultaneously for spec-driven development.', 'terminal-ui, orchestration, git-worktrees, parallel-agents', 'Dual-terminal Setup, MCP Orchestration, Privacy-focused, Conflict-free branches.'),
    ('https://github.com/steipete/claude-code-mcp', 'MCP', 'Claude Code MCP Server', 'A specialized MCP server that runs Claude Code in a one-shot mode, bypassing permissions to allow other agents to automate shell and file operations.', 'mcp, claude-code, automation, tool-offloading', 'Permission Bypassing, Command Queuing, Cross-Model Offloading, Shell Execution.'),
    ('https://github.com/brwse/claude-tools-mcp', 'MCP', 'Claude Tools MCP Server', 'An MCP server that securely exposes Claude Code\'s file and shell manipulation tools over HTTP for remote AI agents.', 'mcp, tools, file-operations, shell-execution', 'Shell Execution with timeout, File offsets/replacement, Glob Search, Security Validation.'),
    ('https://github.com/OpenHands/OpenHands', 'AI Agents & Frameworks', 'OpenHands Platform', 'An open-source platform for AI-driven development providing a composable Software Agent SDK, CLI, and visual workspace for complex engineering tasks.', 'openhands, agent-sdk, gui, enterprise', 'Composable Agent SDK, React GUI, Multiple LLMs, Enterprise RBAC/Kubernetes.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
