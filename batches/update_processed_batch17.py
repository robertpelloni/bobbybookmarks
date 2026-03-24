
import os

links = [
    ('https://code.claude.com/docs/en/desktop', 'Guides & Articles', 'Claude Desktop Documentation', 'Official guide for the Claude Desktop app, covering parallel sessions, worktree isolation, app previews, and visual code reviews.', 'claude-code, desktop, gui, documentation', 'Parallel Sessions, App Preview, Visual Diff, Git Worktrees, Remote Tasks.'),
    ('https://code.claude.com/docs/en/mcp', 'Guides & Articles', 'Claude MCP Documentation', 'Official documentation for Model Context Protocol integration in Claude, including tool connection, resource loading, and server management.', 'mcp, claude-code, integrations, tools', 'Tool Connectors, Remote MCP, Authentication, Slack/GitHub/Notion sync.'),
    ('https://code.claude.com/docs/en/cli', 'Guides & Articles', 'Claude CLI Reference', 'Detailed reference for the Claude Code command-line interface, including permission modes, slash commands, and configuration options.', 'cli, claude-code, terminal, reference', 'Permission Modes (Plan/YOLO), /bug command, .claude.json config, @mentions.'),
    ('https://code.claude.com/docs/en/agent', 'Guides & Articles', 'Claude Agentic Core Docs', 'Documentation on the underlying agentic engine of Claude Code, focusing on task planning, autonomous execution, and self-correction.', 'agentic-ai, reasoning, planning, autonomous', 'Plan-Act-Verify cycle, Codebase Indexing, Structured Output, Usage Governance.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
