import sqlite3

data = [
    ('https://github.com/agiresearch/AIOS', 'Infrastructure & Proxy Layers', 'AIOS: Agentic OS Kernel', 'An open-source "LLM Kernel" architecture designed to embed AI intelligence directly into the operating system for agent resource management.', 'ai-os, kernel, scheduling, context-management, infrastructure', 'Agent Scheduler for resource prioritization, Context Manager for multi-agent state, LLM System Call interface, VM/MCP tool controller.'),
    ('https://github.com/agiresearch/Cerebrum', 'AI Agents & Frameworks', 'Cerebrum (AIOS SDK)', 'The official development kit for AIOS, providing a modular four-layer architecture (LLM/Memory/Storage/Tool) for building and sharing agents.', 'sdk, ai-os, modular-agents, agent-hub, developer-tools', 'Four-layer modular design, built-in Agent Hub for distribution, dynamic ToolHub integration, optimized ReAct/CoT patterns.'),
    ('https://github.com/agentscope-ai/agentscope', 'Agent Orchestration & Workflow', 'AgentScope Multi-Agent SDK', 'A developer-centric, message-passing framework for building scalable and trustworthy multi-agent systems with built-in monitoring.', 'agentscope, orchestration, message-passing, monitoring, studio', 'Hierarchical/P2P orchestration patterns, AgentScope Studio visual UI, Human-in-the-Loop guidance hooks, native MCP/A2A support.'),
    ('https://github.com/agentify-sh/safeexec/', 'Infrastructure & Proxy Layers', 'SafeExec: Interactive Guardrail', 'A lightweight shell wrapper that intercepts destructive agent commands and requires manual TTY-based token confirmation to proceed.', 'security, guardrails, tty, command-interception, automation', 'Destructive command interception (rm/reset/revert), TTY-based manual confirmation, lightweight Bash-based wrapper, cross-platform support.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 10) for d in data]:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level, innovation_score)
        VALUES (?, ?, ?, ?, ?, ?, 'borg', ?)
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='borg',
            innovation_score=excluded.innovation_score
    ''', (url, cat, sd, ld, tags, mf, score))
conn.commit()
conn.close()
print('Successfully injected batch 36.')
