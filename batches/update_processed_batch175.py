import sqlite3

data = [
    ('https://github.com/ag2ai/ag2', 'Agent Orchestration & Workflow', 'AG2: Multi-Agent OS', 'The community-driven evolution of AutoGen, designed as an "AgentOS" for building complex, conversable multi-agent systems with native RAG and observability.', 'autogen, ag2, orchestration, agent-os, swarm', 'Conversable agent primitives, complex orchestration (Swarm/Group/Nested), Python/C#/Java support, AG2 Studio visual interface.'),
    ('https://github.com/agent0ai/agent-zero', 'Agent Orchestration & Workflow', 'Agent-Zero: OS Utility', 'A general-purpose agentic framework designed to use the OS as its primary tool, capable of hierarchical sub-agent spawning and persistent behavior learning.', 'orchestration, automation, linux, self-improving, framework', 'OS-as-a-tool execution, hierarchical multi-agent spawning, persistent solution memory, SKILL.md standardized capabilities.'),
    ('https://github.com/addyosmani/gemini-cli-tips', 'Guides & Industry Trends', 'Gemini CLI Master Tips', 'A curated collection of pro-tips for Gemini CLI by Addy Osmani, focusing on GEMINI.md grounding and reference-based data retrieval from Google ecosystem.', 'gemini, cli, best-practices, grounding, productivity', 'GEMINI.md project grounding, Google Drive/Docs reference retrieval, global preference memory (~/.gemini), multi-step plan execution.'),
    ('https://github.com/agentsea/r1-computer-use', 'Interface & Developer UX', 'R1 Computer Use: Logic', 'An implementation applying DeepSeek-R1 reasoning to computer-use tasks, enabling high-accuracy autonomous GUI and browser interaction.', 'computer-use, vision, reasoning, r1, deepseek', 'DeepSeek-R1 reasoning core, browser-use framework integration, 89% benchmark accuracy, local execution support (Ollama).')
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
print('Successfully injected batch 125.')