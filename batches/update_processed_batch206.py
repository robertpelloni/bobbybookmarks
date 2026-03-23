import sqlite3

data = [
    ('https://www.reddit.com/r/AI_Agents/comments/1piuf1s/i_reverse_engineered_chatgpts_memory_system_and', 'Memory & Persistence Architecture', 'ChatGPT Memory System', 'A reverse-engineering analysis of ChatGPT\'s memory architecture, revealing a four-layer context injection system rather than a real-time vector RAG database.', 'memory, chatgpt, architecture, context-injection, reverse-engineering', 'Four-layer context injection (Metadata/User/Recent/Session), pre-computed periodic distillation, ephemeral session metadata, non-vector RAG approach.'),
    ('https://www.reddit.com/r/AIAGENTSNEWS/comments/1lpny6w/i_vibecoded_vibecrafter', 'Agent Orchestration & Workflow', 'VibeCrafter: Audio Agent', 'An agent-assisted composition workflow tool integrating with FluxMusic to allow musicians to automate repetitive production tasks while maintaining artistic "vibe" control.', 'orchestration, music-generation, audio, vibe-coding, workflow', 'FluxMusic integration, emotional tone parameterization, collaborative AI-musician workflow, cross-track aesthetic consistency.'),
    ('https://www.reddit.com/r/AIMemory/comments/1pg5fro/i_built_a_local_semantic_memory_layer_for_ai', 'Memory & Persistence Architecture', 'Sem-Mem: Local Memory Layer', 'An open-source, local-first tiered memory system for AI agents utilizing a Hot Cache (RAM) and Cold Storage (HNSW) for privacy-focused persistence.', 'memory, local-first, hnsw, persistence, semantic-search', 'Tiered Hot (RAM) / Cold (HNSW) storage, automatic background fact extraction, LLM-powered query expansion, 100% local disk persistence.'),
    ('https://www.reddit.com/r/AutoGenAI/comments/1phnq3c/daveagent_a_coding_assistant_inspired_by_the', 'Agent Orchestration & Workflow', 'DaveAgent: Local Coder', 'An open-source terminal coding assistant built on AutoGen, inspired by Gemini CLI and optimized for local DeepSeek models to eliminate telemetry.', 'autogen, orchestration, coding-agent, deepseek, local-llm', 'AutoGen framework core, 55.5% SWE-bench capability, optimized for local DeepSeek models, Claude-compatible SKILL.md system integration.')
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
print('Successfully injected batch 166.')