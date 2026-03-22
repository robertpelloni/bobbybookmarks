import sqlite3

data = [
    ('https://github.com/a2aproject/A2A', 'AI Agents & Frameworks', 'Agent2Agent Protocol (A2A)', 'An open standard enabling secure interoperability and standardized communication between independent AI agents across different frameworks.', 'a2a, protocol, interoperability, standard, linux-foundation', 'JSON-RPC 2.0 communication, Agent Discovery via Agent Cards, SSE streaming support, Enterprise security and auth layers.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1pkki12/swarm_of_80_opencode_subagents_just_generated_the/', 'AI Agents & Frameworks', 'OpenCode 80-Agent Swarm', 'A pioneering case study in orchestrating a massive swarm of 80 specialized subagents to generate complex marketing and business strategies.', 'opencode, swarm, multi-agent, orchestration, case-study', 'Diverse model orchestration (Claude/Grok), Subject Matter Expert (SME) delegation, Independent audit and validation, MCP-based live data integration.'),
    ('https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/', 'MCP', 'Docker MCP Toolkit', 'A suite of tools from Docker for containerizing, isolating, and managing MCP servers via a unified local gateway.', 'mcp, docker, container, gateway, toolkit', 'Isolated server environments, Secure secret storage, Unified API gateway for multiple clients, Docker Desktop dashboard integration.'),
    ('https://www.verdent.ai/', 'AI Agents & Frameworks', 'Verdent AI-Native IDE', 'An agentic development platform focusing on a plan-first workflow, parallel execution via worktrees, and proactive ambiguity resolution.', 'verdent, ide, agentic-coding, git-worktrees, automation', 'Isolated Git Worktree execution, Proactive clarification engine, DiffLens transparent diffing, Multi-model support (Claude/Gemini).'),
    ('https://docs.anythingllm.com/agent/custom/developer-guide', 'AI Agents & Frameworks', 'AnythingLLM Custom Skills', 'Developer documentation for extending AnythingLLM agents with custom, JavaScript-based skills and OS-level integrations.', 'anythingllm, skills, plugin, node-js, extensibility', 'JavaScript/Node.js skill framework, Hot-loading support, OS-level script execution, standardized plugin.json manifest.'),
    ('https://github.com/cluesmith/codev', 'AI Agents & Frameworks', 'Codev OS', 'A human-agent development operating system that orchestrates collaboration using the SPIR (Specification, Plan, Implementation, Review) methodology.', 'codev, dev-os, spir-protocol, orchestration, automated-pr', 'Agent Farm (af) CLI, Phased SPIR/ASPIR workflows, Multi-model consultation (Claude vs Gemini), Porch automated quality gates.')
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
print('Successfully injected batch 3.')
