import sqlite3

data = [
    ('https://www.reddit.com/r/ArtificialInteligence/comments/1qyystc/symbolic_reasoning_language_srl_that_could_give/', 'AI Agents & Frameworks', 'Symbolic Reasoning Language (SRL)', 'A neuro-symbolic bridge that enforces rigid logical constraints by having LLMs generate deterministic logic code instead of raw text.', 'neuro-symbolic, logic-engine, verifiability, srl, reasoning', 'Verifiable reasoning traces, deterministic logic solvers, elimination of probabilistic hallucinations, formal proof generation.'),
    ('https://www.reddit.com/r/ArtificialInteligence/comments/1q9q5su/meta_harvard_just_published_a_longmemory_ai_agent/', 'Memory & Persistence Architecture', 'Meta/Harvard: Hierarchical Latent Memory', 'A three-tier memory architecture (Working/Episodic/Semantic) that uses self-directed consolidation to turn experiences into persistent rules.', 'memory-architecture, long-memory, meta, harvard, research', 'Self-directed fact consolidation, background "reflective" processing, three-tier memory hierarchy, significant token/latency reduction.'),
    ('https://www.reddit.com/r/ArtificialInteligence/comments/1qyt6m5/holy_grail_open_source_autonomous_development/', 'Agent Orchestration & Workflow', 'Holy Grail: OSS Software Factory', 'A viral end-to-end autonomous development pipeline designed to be a local-first, shippable alternative to Devin or Copilot Workspace.', 'holy-grail, open-source, autonomous-dev, software-factory, local-first', 'End-to-end PR-to-deploy pipeline, self-improvement review loops, stateful JSON/Vector memory, local execution safety.'),
    ('https://www.reddit.com/r/ArtificialInteligence/comments/1qkq97p/chinese_ai_is_quietly_eating_us_developers_lunch/', 'Guides & Industry Trends', 'Chinese Open-Weight Dominance', 'An analysis of the strategic shift toward Chinese models (DeepSeek/Qwen/GLM) due to their high performance, local hostability, and zero-censorship.', 'deepseek, qwen, glm, open-weight, trends', '90%+ parity with US flagships, aggressive open-weight strategy, near-zero margin pricing, local hostability for privacy-first dev.')
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
print('Successfully injected batch 63.')
