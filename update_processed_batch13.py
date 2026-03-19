
import os

links = [
    ('https://github.com/kaitranntt/ccs', 'AI Agents & Frameworks', 'CCS (Claude Code Switch)', 'A universal AI profile manager and proxy for Claude Code, enabling seamless switching between models (Gemini, GPT, local) and accounts.', 'ccs, claude-code, proxy, multi-model', 'Multi-provider support, Account Switching, Visual Dashboard, Local Model Integration.'),
    ('https://github.com/contextenginehq/context-engine', 'AI Agents & Frameworks', 'Context Engine', 'An open-source platform for deterministic, token-aware context selection for AI agents, ensuring precise context within token budgets.', 'context-engine, token-aware, mcp, determinism', 'MCP Server, Core Scoring Library, Context Caching, deterministic output.'),
    ('https://github.com/anthropics/claude-agent-sdk-demos', 'Guides & Articles', 'Claude Agent SDK Internal Examples', 'Foundational examples within the official Anthropic repositories demonstrating basic agent loops, tool usage, and MCP client/server setup.', 'anthropic, examples, agent-sdk, mcp', 'Hello World, Research Agent, Email Assistant, WebSocket Chat.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
