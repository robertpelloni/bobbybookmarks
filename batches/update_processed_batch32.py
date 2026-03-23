
import os

links = [
    ('https://www.dropstone.io/features', 'AI Agents & Frameworks', 'Dropstone Platform Features', 'Overview of Dropstone, an AI platform with infinite context, trajectory search, and a multi-agent swarm architecture for large-scale codebases.', 'dropstone, orchestration, agent-swarms, enterprise', 'Horizon Mode (10k+ paths), Self-Verifying Code, PIP Interface, Figma/Windows MCP.'),
    ('https://github.com/github/awesome-copilot', 'Guides & Articles', 'Awesome GitHub Copilot', 'The official community-driven list of resources, custom agents, instructions, and MCP plugins to extend the capabilities of GitHub Copilot.', 'awesome-list, github-copilot, plugins, mcp', 'Custom Instructions, Agent Workflows, MCP server directory, Community scripts.'),
    ('https://tidewave.ai/blog/claude-code-codex', 'Guides & Articles', 'Tidewave Claude/Codex Integration', 'A blog post detailing how Tidewave.ai integrated Claude Code and OpenAI Codex into a full-stack browser environment using ACP and MCP over WebSockets.', 'blog, tidewave, claude-code, acp', 'ACP/MCP over WebSockets, Deep Framework Access, Browser-based IDE, Open Source infrastructure.'),
    ('https://github.com/milisp/opencode-gui', 'Development Tools & Libraries', 'OpenCode GUI', 'A lightweight desktop application built with Tauri (Rust/TypeScript) providing a graphical chat interface for local OpenCode servers.', 'opencode, gui, tauri, desktop-app', 'Local Server Connection, Project Directory Config, Chat UI.'),
    ('https://github.com/chris-tse/opencode-web', 'Development Tools & Libraries', 'OpenCode Web', 'A web-based frontend designed to manage and visualize the execution of OpenCode AI agents, enabling real-time collaboration.', 'opencode, web-ui, collaboration, visualization', 'Real-time Logs, Agent Orchestration UI, Web Deployment.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
