
import os

links = [
    ('https://github.com/SaladDay/cc-switch-cli', 'AI Agents & Frameworks', 'cc-switch-cli', 'A CLI tool likely related to the cc-switch ecosystem for managing and switching between AI CLI tools and profiles.', 'cli, cc-switch, profile-manager, ai-tools', 'Profile switching, Environment management, Provider config.'),
    ('https://github.com/Dianel555/gemini-superclaude-mcp-server', 'MCP', 'Gemini SuperClaude MCP', 'An advanced MCP server that provides SuperClaude Framework v4 compatibility for the Gemini CLI, featuring 14 domain-expert agents.', 'mcp, superclaude, gemini-cli, orchestration', '22 Specialized Commands, Business Panel, 14 Expert Agents, Behavioral Modes.'),
    ('https://github.com/SuperClaude-Org/SuperClaude_Framework/tree/master', 'AI Agents & Frameworks', 'SuperClaude Framework', 'A comprehensive meta-programming configuration framework that transforms Claude Code into a structured, high-performance development platform.', 'superclaude, claude-code, framework, orchestration', '30 Slash Commands, 16 Specialized Agents, Deep Research (v4.2), 7 Behavioral Modes, 8 MCP Integrations.'),
    ('https://github.com/Piebald-AI/splitrail', 'Development Tools & Libraries', 'Splitrail Token Tracker', 'A fast, cross-platform Rust tool for tracking real-time token usage and costs across AI CLIs (Gemini, Claude Code, Copilot).', 'token-tracking, cost-management, rust, mcp', 'Real-time tracking, Cross-machine aggregation, VS Code extension, MCP Server integration.'),
    ('https://github.com/awesome-opencode/awesome-opencode', 'Guides & Articles', 'Awesome OpenCode', 'A curated collection of resources, plugins, themes, and extensions for the OpenCode terminal AI agent ecosystem.', 'awesome-list, opencode, plugins, ecosystem', 'Plugin Directory, Custom Agents, GUI/TUI frontends, Proxies, Telemetry tools.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
