
import os

links = [
    ('https://www.copilotkit.ai/blog/build-with-googles-new-a2ui-spec-agent-user-interfaces-with-a2ui-ag-ui', 'Guides & Articles', 'A2UI Specification Overview', 'An in-depth guide to Google\'s Agent-to-User Interface (A2UI) spec, which enables AI agents to generate dynamic, interactive UIs on the fly.', 'a2ui, generative-ui, google-spec, copilotkit', 'beginRendering, surfaceUpdate, dataModelUpdate, Data Binding, A2A Integration.'),
    ('https://github.com/google/A2UI', 'AI Agents & Frameworks', 'Google A2UI Official Repository', 'The primary open-source repository for the A2UI specification and its reference implementations, enabling native, interactive AI-generated UIs.', 'google, a2ui, standards, interoperability', 'JSON-RPC Schemas, Component Catalogs, Event Handling, Security Guardrails.'),
    ('https://a2ui.org/', 'Guides & Articles', 'A2UI Official Documentation', 'The central portal for the A2UI spec (hosted at a2ui.org), providing detailed schema documentation and version history (v0.8 stable, v0.9 draft).', 'a2ui, documentation, spec-history, google', 'Schema Definitions, Action Refs, Component Specs, Versioning.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1pa0vcr/i_built_a_python_script_that_spawns_subagents_and/', 'Guides & Articles', 'Sub-agent Spawning Script Discussion', 'Reddit thread featuring a Python script for spawning parallel sub-agents in OpenCode to improve task efficiency and reduce context bloat.', 'reddit, opencode, sub-agents, parallelization', 'Task Decomposition, Result Consolidation, Multiprocessing, Shell Integration.'),
    ('https://github.com/vstorm-co/pydantic-deepagents', 'AI Agents & Frameworks', 'Pydantic DeepAgents Framework', 'A Python framework built on Pydantic-AI for creating production-grade autonomous agents with planning, filesystem, and subagent capabilities.', 'pydantic-ai, deep-agents, autonomous-coding, python', 'Deep Agent Pattern, CLI Chat, DeepResearch App, Budget Enforcement, Sliding Window Context.'),
    ('https://github.com/anthropics/claude-agent-sdk', 'AI Agents & Frameworks', 'Claude Agent SDK (Main)', 'The foundational SDK for building autonomous agents with Claude\'s engineering capabilities, bridging the model with local dev environments.', 'anthropic, agent-sdk, claude-code, autonomous-engineering', 'Codebase Analysis, File Editing, Command Execution, Agentic Workflows.'),
    ('https://github.com/anthropics/claude-agent-sdk-typescript', 'AI Agents & Frameworks', 'Claude Agent SDK for TypeScript', 'The TypeScript implementation of the Claude Agent SDK, enabling programmatic building of autonomous agents with Node.js integration.', 'anthropic, typescript, agent-sdk, mcp', 'TS Schema Definitions, GitHub Actions integration, Workflow Automation.'),
    ('https://github.com/anthropics/claude-agent-sdk-python', 'AI Agents & Frameworks', 'Claude Agent SDK for Python', 'The Python implementation of the Claude Agent SDK, featuring high-level query APIs, interactive clients, and in-process MCP server support.', 'anthropic, python, agent-sdk, hooks', 'Async query(), ClaudeSDKClient, In-process MCP, Pre/Post Tool Hooks.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
