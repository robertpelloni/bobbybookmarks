import sqlite3

data = [
    ('https://github.com/priyan-coder/multi-agent-orchestration', 'AI Agents & Frameworks', 'Gemini Multi-Agent Orchestrator', 'A specialized framework enabling multiple AI agents to work in parallel with IPC synchronization, specifically designed for the Gemini CLI ecosystem.', 'gemini-cli, orchestration, multi-agent, ipc, synchronization', 'Parallel task execution, IPC-based state management, memory summary synchronization, task dependency handling.'),
    ('https://github.com/sourcegraph/amp-examples-and-guides', 'AI Agents & Frameworks', 'Sourcegraph Amp Guides', 'The central hub for mastering Sourcegraph Amp, featuring SDLC-specific workflows for planning, building, and deploying with agentic AI.', 'sourcegraph, amp, sdk, workflow, guide', 'SDLC phase guides, Agent.md context engineering, MCP integration tutorials, Smart vs Rush mode documentation.'),
    ('https://github.com/jdorfman/awesome-amp-code', 'Guides & Articles', 'Awesome JSON Datasets', 'A highly-curated collection of non-authentication JSON datasets used for testing AI agents and building data-driven prototypes.', 'awesome-list, datasets, json, testing, prototyping', 'Categorized datasets (Finance/Gov/Science), no-auth accessibility, vetted by major dev communities.'),
    ('https://nimbalyst.com/', 'AI Agents & Frameworks', 'Nimbalyst Visual ADE', 'An agent-native visual workspace that provides a mission control layer for terminal-based AI agents like Claude Code and Codex.', 'ade, visual-workspace, orchestration, collaboration, dashboard', 'Visual session manager, agent-powered visual editors, diff review/approve UI, natural language schema planning.'),
    ('https://github.com/code-yeongyu/oh-my-opencode', 'AI Agents & Frameworks', 'Oh My OpenAgent (OMO)', 'A high-performance "battery-included" plugin and harness for OpenCode featuring aggressive orchestrators and specialized discipline agents.', 'opencode, harness, sub-agents, automation, productivity', 'Sisyphus aggressive orchestrator, Oracle/Librarian specialized subagents, Speckit handoff support, AST-aware code intelligence.'),
    ('https://github.com/TheNoeTrevino/claude-hooks', 'AI Agents & Frameworks', 'Claude Code Hooks', 'A foundational resource for implementing deterministic shell commands at specific lifecycle events of an AI coding session.', 'claude-code, hooks, automation, security, quality-gate', 'Deterministic quality gates, Pre/Post-tool use validation, Stop-hook testing enforcement, Notification alerts (Slack/Desktop).'),
    ('https://github.com/vybestack/llxprt-code', 'Development Tools & Libraries', 'LLxprt Code CLI', 'A multi-provider, privacy-first AI development tool that offers a powerful alternative to proprietary AI CLIs without telemetry.', 'cli, multi-provider, privacy, open-source, alternative', 'Provider agnostic (Claude/GPT/Ollama), Explicit telemetry removal, Isolated subagent contexts, Privacy-first architecture.'),
    ('https://github.com/roman-ryzenadvanced/OpenQode-Public-Alpha-GooseUltra-', 'AI Agents & Frameworks', 'OpenQode (Goose Ultra)', 'A professional AI coding assistant that integrates the OpenCode TUI with open-weight models like Qwen for low-cost, high-performance coding.', 'openqode, qwen, goose, automation, vision-agent', 'Low-cost flagship intelligence, desktop "Computer Use" automation, browser control, vision-based UI analysis.'),
    ('https://github.com/superagent-ai/grok-cli', 'AI Agents & Frameworks', 'Grok-3 CLI Agent', "An open-source AI agent that brings the reasoning and coding power of xAI's Grok-3 directly into the developer terminal.", 'grok, xai, cli, agent, reasoning', 'Grok-3 reasoning power, Morph Fast Apply editing, MCP extensibility, Implementation Plan mode.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level)
        VALUES (?, ?, ?, ?, ?, ?, 'deep')
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='deep'
    ''', (url, cat, sd, ld, tags, mf))
conn.commit()
conn.close()
print('Successfully injected batch 6.')
