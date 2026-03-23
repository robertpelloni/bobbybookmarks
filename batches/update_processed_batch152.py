import sqlite3

data = [
    ('https://www.wsj.com/tech/ai/openai-forges-multibillion-dollar-computing-partnership-with-cerebras-746a20e4', 'Guides & Industry Trends', 'OpenAI-Cerebras: $10B Deal', 'A massive multi-year partnership where OpenAI secures 750 megawatts of computing power via Cerebras Wafer-Scale Engines for low-latency reasoning.', 'openai, cerebras, infrastructure, hardware, low-latency', '10B multi-year agreement, Wafer-Scale Engine hardware, 15x faster inference speeds, independent of Nvidia/standard cloud.'),
    ('https://yieldcode.blog/post/isolating-claude-code/', 'Infrastructure & Proxy Layers', 'Agent Isolation: Vagrant', 'A security strategy for isolating autonomous coding agents using Vagrant virtual machines to provide a stronger OS-level kernel boundary than Docker.', 'security, isolation, vagrant, virtualization, hardening', 'Full OS-level virtualization, stronger kernel boundary than containers, isolated environment variables, protection against secret extraction.'),
    ('https://www.reddit.com/r/mcp/comments/1rmi3r2/codegraphcontext_an_mcp_server_that_converts_your/', 'Memory & Persistence Architecture', 'CodeGraphContext: Graph RAG', 'An MCP server that provides relationship-aware context using Graph RAG to map codebase imports, inheritance, and call chains for precise agent navigation.', 'mcp, graph-rag, codebase-indexing, context-engineering, navigation', 'Symbol-level relationship mapping, real-time code graph updates, 14-language support, dual CLI/MCP mode.'),
    ('https://www.reddit.com/r/vibecoders_/comments/1rlkzp7/top_9_agentic_frameworks/', 'Agent Orchestration & Workflow', '2026 Agentic Frameworks', 'A comprehensive list of the industry-standard frameworks for building autonomous multi-agent systems, featuring LangGraph, CrewAI, and PydanticAI.', 'orchestration, frameworks, multi-agent, pydanticai, langgraph', 'Top 9 industry-standard frameworks, role-based collaboration (CrewAI), stateful multi-actor (LangGraph), type-safe Python (PydanticAI).')
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
print('Successfully injected batch 102.')