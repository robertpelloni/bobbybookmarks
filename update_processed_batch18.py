
import os

links = [
    ('https://github.com/Chat2AnyLLM/code-assistant-manager', 'AI Agents & Frameworks', 'Code Assistant Manager (CAM)', 'A Python-based CLI for managing configurations, prompts, and MCP plugins for 17+ AI coding assistants (Claude, Gemini, Copilot).', 'manager, cli, config-sync, mcp-registry', 'TUI Manager, Unified Env management, Prompt Syncing, Plugin Installer.'),
    ('https://github.com/vstorm-co/pydantic-deepagents', 'AI Agents & Frameworks', 'Pydantic DeepAgents Framework', 'A Python framework for building production-grade autonomous agents with planning, subagent delegation, and persistent memory using Pydantic-AI.', 'pydantic-ai, deep-agents, autonomous-coding, python', 'Subagent Delegation, Context Compression, Budget Enforcement, Docker Sandbox.'),
    ('https://github.com/anthropics/claude-agent-sdk-typescript/tree/main/packages/sdk/src/orchestration', 'AI Agents & Frameworks', 'Claude Agent SDK Orchestration', 'Core patterns within the TypeScript SDK for managing agent interactions, including Sequential, Parallel, and Hierarchical orchestration.', 'anthropic, orchestration, patterns, multi-agent', 'Sequential Handoffs, Parallel Execution, Hierarchical Management, Shared State.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
