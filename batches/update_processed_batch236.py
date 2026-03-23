import sqlite3

data = [
    ('https://www.reddit.com/r/OpenSourceAI/comments/1rruamz/meet_superml_a_plugin_that_gives_you_ml/', 'Development Tools & Libraries', 'SuperML: Agentic Plugin', 'An open-source MCP plugin designed to give coding agents expert-level machine learning knowledge, boosting ML task success rates by 60%.', 'mcp, ml, superml, agents, tooling', '60% boost in ML task success rate, agentic memory for hardware/hypotheses, deep research integration (papers/GitHub), specialized `ml-expert` routing.'),
    ('https://www.reddit.com/r/artificial/comments/1rrss36/built_an_ai_memory_system_based_on_cognitive/', 'Memory & Persistence Architecture', 'Cognitive Memory Decay', 'An AI memory system built on cognitive science models (ACT-R, Hebbian learning) that uses active decay and forgetting curves instead of traditional vector databases.', 'memory, persistence, cognitive-science, decay, optimization', 'Active memory decay (Ebbinghaus curve), recency/frequency prioritization, $0 inference cost via pure Python, 230k+ recalls in 30 days without noise bloat.'),
    ('https://www.reddit.com/r/OpenSourceAI/comments/1rt0dg9/mengram_opensource_memory_layer_that_gives_any/', 'Memory & Persistence Architecture', 'MenGram: Tri-Layer Memory', 'An open-source persistent memory layer for LLMs that categorizes information into Semantic, Episodic, and Procedural layers, mirroring human memory architectures.', 'memory, persistence, mengram, architecture, graph', 'Semantic (facts), Episodic (events/context), and Procedural (workflows) memory layers, automated entity/relationship extraction, "cognitive profile" generation.'),
    ('https://www.reddit.com/r/LekhAI/comments/1rt51gm/lekh_ai_60_for_mac_is_out_knowledge_hub_rag/', 'Interface & Developer UX', 'Lekh AI 6.0: Local macOS', 'A privacy-focused, fully local AI application for Apple Silicon featuring a new Knowledge Hub and external drive support for massive GGUF/MLX model libraries.', 'local-llm, macos, privacy, lekh-ai, rag', 'Knowledge Hub memory management, external drive model storage (GGUF/MLX), 100% on-device multimodal processing, enhanced local document RAG.')
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
print('Successfully injected batch 196.')