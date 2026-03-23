import sqlite3

data = [
    ('https://www.reddit.com/r/kilocode/comments/1oe9szp/task_management_wkilo', 'Agent Orchestration & Workflow', 'Kilo Code: Agentic IDE', 'An open-source "Agentic Engineering" platform featuring Orchestrator Mode, allowing users to launch and coordinate multiple parallel coding agents directly from the CLI/IDE.', 'kilocode, ide, orchestration, multi-agent, automation', 'Orchestrator Mode (parallel agent execution), persistent cross-platform Memory Bank, Kilo Gateway BYOK API support, one-click shipping.'),
    ('https://www.reddit.com/r/kilocode/comments/1oi3ufm/openskills_cli_use_claude_code_skills_with_any', 'Connectivity & Interoperability (MCP/A2A)', 'OpenSkills CLI', 'A standardization utility that implements the Agent Skills Specification, enabling `SKILL.md` files to be shared across Claude Code, Cursor, and Gemini CLI.', 'skills, standardization, interoperability, mcp, prompt-engineering', 'Cross-platform SKILL.md compatibility, Progressive Loading (100 token minimal scan), dynamic context injection, Superpowers/ClaudeMem ecosystem support.'),
    ('https://www.reddit.com/r/LocalLLaMA/comments/1o4wg6q/stanford_researchers_released_agentflow_flowgrpo', 'AI Agents & Frameworks', 'AgentFlow: Flow-GRPO', 'A reinforcement learning framework from Stanford that decomposes tasks into modular agents (Planner/Executor/Verifier) and optimizes them using Flow-GRPO to solve "sparse reward" failures.', 'rl, reasoning, grpo, agentflow, stanford', 'Flow-based Group Refinement Policy Optimization (Flow-GRPO), modular Planner/Executor architecture, 28.4% reduction in tool-call errors, trajectory-level success broadcasting.'),
    ('https://www.reddit.com/r/mcp/comments/1p4bj9i/nano_banana_pro_mcp_to_understand_your_source_code', 'Connectivity & Interoperability (MCP/A2A)', 'Nano Banana Pro MCP', 'The integration of Google\'s Gemini 3 Pro Image ("Nano Banana") into the Model Context Protocol, allowing agents to generate and edit high-resolution 4K UI mockups and storyboards.', 'mcp, vision, image-generation, gemini, multimodal', 'Native 4K (3840x2160) generation, "Thinking Mode" compositional structuring, 5-character identity consistency, native MCP editing tools.')
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
print('Successfully injected batch 171.')