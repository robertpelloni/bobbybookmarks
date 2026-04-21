import sqlite3

data = [
    ('https://github.com/bkircher/skills', 'AI Agents & Frameworks', 'Minimal Skill Pack', 'A collection of modular instruction sets (skills) designed to extend AI coding agents like Claude Code and Codex with concise, reusable task recipes.', 'claude-code, skills, codex, automation, minimal', 'Modular SKILL.md architecture, task-specific recipes, lightweight extension model.'),
    ('https://github.com/ykdojo/claude-code-tips', 'Guides & Articles', '45 Claude Code Efficiency Tips', 'A comprehensive repository of 45 advanced tips and scripts for maximizing Claude Code efficiency, including custom status lines and autonomous cycles.', 'claude-code, tips, workflow, automation, productivity', 'context-bar.sh status script, context compacting strategies, Git worktree optimization, Write-Test autonomous cycle guide.'),
    ('https://github.com/robertpelloni/metamcp', 'MCP', 'MetaMCP Orchestration Hub', 'A centralized aggregator and orchestration layer for Model Context Protocol (MCP) servers, facilitating multi-agent synchronization in monorepos.', 'mcp, orchestration, synchronization, ai-os, hub', 'Server aggregation, bidirectional context sync, Mission Control monitoring, monorepo-wide tool coordination.'),
    ('https://docs.roocode.com/roo-code-cloud/roomote-control', 'AI Agents & Frameworks', 'Roo Code Cloud Remote', 'Documentation for the transition from local IDE extensions to autonomous, cloud-based AI engineering teams with omnichannel access.', 'roo-code, cloud-agents, collaboration, automation, task-sync', 'Autonomous cloud operation, PR/Slack integration, centralized Task Sync, team-wide configuration enforcement.'),
    ('https://github.com/The-Pocket/PocketFlow-Tutorial-Cursor/blob/main/blog.md', 'AI Agents & Frameworks', 'PocketFlow Agent Framework', 'A minimalist, node-based framework for building autonomous agents using directed graphs and a shared global state dictionary.', 'agent-framework, flow-based, node-js, pocketflow, tutorial', 'Atomic action nodes, bottom-to-top batch editing, YAML-based reasoning loops, minimalist shared store.'),
    ('https://github.com/OpenHands/OpenHands/blob/f7cb2d0f64666e1f090a5152d7c002aa6f28caf9/openhands/controller/agent_controller.py', 'AI Agents & Frameworks', 'OpenHands Event Controller', 'A production-grade, event-driven controller for managing autonomous AI agents through an asynchronous stream with multi-agent delegation.', 'openhands, event-driven, orchestration, sdk, controller', 'Async EventStream architecture, multi-agent controller delegation, conversation window condensing, autonomous safety budget limits.'),
    ('https://benhouston3d.com/blog/building-an-agentic-code-from-scratch', 'Guides & Articles', 'Building an Agentic Coder', "A technical deep-dive by Ben Houston on evolving LLMs into autonomous engineers through smart shells and range-based code editing.", 'agent-engineering, automation, technical-blog, mycoder, vision-agent', 'Adaptive smart shells, range-based character editing, Playwright-based UI verification, README-as-distilled-knowledge pattern.'),
    ('https://simonwillison.net/2025/Oct/5/parallel-coding-agents/', 'Guides & Articles', 'Parallel Agent Architecture', "Simon Willison's analysis of the shift toward parallelized agent workflows, focusing on scouting, low-stakes maintenance, and blast-radius isolation.", 'simon-willison, parallel-agents, scout-pattern, isolation, maintenance', 'Low-stakes scouting pattern, YOLO-mode safety boundaries, multi-agent PoC testing, workflow bottleneck reduction.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1pg2nz9/i_have_gemini_cli_working_basically_as_a_subagent/', 'AI Agents & Frameworks', 'Gemini+Claude Synergy', 'A community-identified orchestration pattern using Claude as the architect and Gemini 1.5 Pro as a specialized wide-context subagent.', 'gemini-cli, claude-code, orchestration, multi-model, context-window', '2M+ token wide-context leverage, multi-model synergy pattern, architectural red-teaming, cross-CLI bash coordination.'),
    ('https://agentclientprotocol.com/overview/agents', 'AI Agents & Frameworks', 'Agent Client Protocol (ACP)', 'A standardized protocol for interoperability between AI agents and developer tools like IDEs and CLIs, centralizing session and tool management.', 'acp, protocol, standard, interoperability, tooling', 'Standardized session setup, unified tool calling, portable agent instructions, multi-client compatibility.')
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
print('Successfully injected batch 2.')
