
import os

links = [
    ('https://github.com/farion1231/cc-switch', 'AI Agents & Frameworks', 'cc-switch Unified Manager', 'A Tauri-based desktop assistant for managing and switching between AI CLI tools (Claude Code, Codex, Gemini) with built-in provider presets and cost tracking.', 'cc-switch, cli-manager, tauri, multi-provider', '50+ Provider Presets, Unified MCP panel, Local Proxy, Session Management, Usage Tracking.'),
    ('https://github.com/farion1231/cc-switch-mcp', 'MCP', 'cc-switch MCP Server', 'A specialized MCP server that integrates with the cc-switch ecosystem to provide centralized tool and skill management for multiple AI agents.', 'mcp, cc-switch, tools, skills', 'Centralized MCP Sync, Skill Management, Plugin Lifecycle support.'),
    ('https://github.com/farion1231/cc-switch-action', 'AI Agents & Frameworks', 'cc-switch GitHub Action', 'An official GitHub Action for automating configurations, token management, and provider failover within the cc-switch ecosystem.', 'github-actions, automation, ci-cd, infra', 'Automated Key Rotation, Provider Failover, Syncing configs.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
