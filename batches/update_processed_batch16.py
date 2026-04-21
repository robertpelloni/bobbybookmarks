
import os

links = [
    ('https://github.com/generalaction/emdash', 'AI Agents & Frameworks', 'Emdash Agentic Development Environment', 'A provider-agnostic ADE desktop application for running multiple AI coding agents in parallel, isolated via Git worktrees and integrated with issue trackers.', 'emdash, ade, orchestration, git-worktrees', 'Parallel Agent Execution, Worktree Isolation, 22+ Agent support, SSH/SFTP, Issue Integration.'),
    ('https://github.com/generalaction/emdash-mcp', 'MCP', 'Emdash MCP Server', 'A specialized MCP server that allows AI agents to interact with the Emdash environment, including its worktree management and issue tracking systems.', 'mcp, emdash, tools, workflow', 'Worktree Management, Issue Sync, Environment Context, Multi-agent tools.'),
    ('https://www.emdash.ai/', 'Guides & Articles', 'Emdash Official Portal', 'The main product site and documentation hub for the Emdash ADE, providing setup guides and feature overviews for agentic orchestration.', 'emdash, portal, documentation, ade', 'Product Overview, Quickstart, Feature Roadmap, Documentation links.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
