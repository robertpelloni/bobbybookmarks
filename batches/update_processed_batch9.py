
import os

links = [
    ('https://github.com/anthropics/claude-code/tree/main/plugins', 'AI Agents & Frameworks', 'Claude Code Plugin Architecture', 'A modular system for extending the Claude Code CLI with slash commands, specialized agents, expert skills, and lifecycle hooks.', 'claude-code, plugins, architecture, extensibility', 'Slash Commands, Specialized Agents, Agent Skills, Event Hooks, MCP Integration.'),
    ('https://github.com/anthropics/claude-code/blob/main/plugins/README.md', 'Guides & Articles', 'Plugin Development Guide', 'Documentation defining the standard hierarchical structure and metadata requirements for creating Claude Code plugins.', 'claude-code, documentation, plugin-dev, manifest', 'plugin.json, directory-structure, component-loading, context-injection.'),
    ('https://github.com/anthropics/claude-code/tree/main/plugins/feature-dev', 'AI Agents & Frameworks', 'Feature Dev Plugin', 'A core plugin implementing a comprehensive 7-phase guided workflow for end-to-end feature development within the CLI.', 'claude-code, workflow, feature-development, automation', 'Phased Execution, Mandatory Specs, Validation Loops, Automated Implementation.'),
    ('https://github.com/anthropics/claude-code/tree/main/plugins/security-guidance', 'AI Agents & Frameworks', 'Security Guidance Plugin', 'A plugin providing security monitoring and warning hooks that intercept tool usage to enforce safety patterns and standards.', 'claude-code, security, guardrails, hooks', 'PreToolUse monitoring, Security Warnings, Pattern Detection, Audit Logging.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
