import sqlite3

data = [
    ('https://github.com/cryxnet/DeepMCPAgent', 'Agent Orchestration & Workflow', 'DeepMCPAgent: Peer Collab', 'A model-agnostic framework enabling LangGraph agents to dynamically discover MCP tools and collaborate as peers via broadcast/ask tools.', 'mcp, langchain, langgraph, a2a, orchestration', 'Dynamic HTTP/stdio tool discovery, cross-agent Peer Communication (v0.5), Pydantic argument validation, Planner-Executor agent loops.'),
    ('https://github.com/AIDC-AI/Pixelle-MCP', 'Connectivity & Interoperability (MCP/A2A)', 'Pixelle-MCP: Omnimodal AIGC', 'An omnimodal framework bridging ComfyUI node-graphs to LLMs via MCP, allowing agents to trigger complex image, sound, and video pipelines.', 'mcp, comfyui, multimodal, aigc, video-generation', 'Zero-code ComfyUI to MCP conversion, Text/Image/Sound/Video generation, standalone server/client modes, Chainlit integration.'),
    ('https://huggingface.co/driaforall/mem-agent', 'AI Agents & Frameworks', 'Mem-Agent: Obsidian Memory', 'A specialized 4B parameter model optimized for long-term human-readable memory management using a Markdown-based file system and GSPO policy.', 'memory, persistence, qwen3, gspo, markdown-memory', 'Markdown-based retrieval/updating, 4B parameter efficiency, GSPO sub-task optimization, Python-sandboxed memory interaction.'),
    ('https://www.reddit.com/r/codex/comments/1rn4vta/54_vs_53_codex_both_xhigh/', 'Guides & Industry Trends', 'Codex 5.4 vs 5.3 Benchmarks', 'A comparative analysis of the "Extra High" reasoning tiers, ranking 5.3 as the "Sweet Spot" for reliability and 5.4 as the "Speed Demon" for benchmark chasing.', 'codex, benchmarks, xhigh, reasoning, performance', '5.3 higher signal-to-noise ratio, 5.4 significantly faster subagent spawning, 5.4 hyper-literalism risks, 1M context window support.')
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
print('Successfully injected batch 104.')