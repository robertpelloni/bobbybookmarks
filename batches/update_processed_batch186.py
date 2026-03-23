import sqlite3

data = [
    ('https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning', 'Guides & Industry Trends', 'Google: Nested Learning', 'A new machine learning paradigm for continual learning that views models as multi-level optimization problems with self-modifying "Hope" architectures.', 'research, continual-learning, optimization, google, architecture', 'Multi-level optimization timescales, Continuum Memory System (CMS), self-modifying "Hope" architecture, elimination of catastrophic forgetting.'),
    ('https://research.aimultiple.com/memory-mcp', 'Memory & Persistence Architecture', 'Memory MCP: Universal Hub', 'A universal memory hub standard enabling cross-agent persistence and relational knowledge graphs via a multi-tier Hot/Warm/Cold storage strategy.', 'mcp, memory, persistence, knowledge-graph, optimization', 'Cross-agent persistent storage, relational knowledge graph indexing, multi-tier Hot/Warm/Cold storage, automated task/action-item extraction.'),
    ('https://red.anthropic.com/2025/smart-contracts', 'Guides & Industry Trends', 'Anthropic: Autonomous Offense', 'A 2025 security report revealing that frontier AI agents have autonomously discovered novel zero-day exploits in newly deployed smart contracts.', 'security, red-team, smart-contracts, vulnerability, cyber-offense', 'Autonomous zero-day discovery, SCONE-bench (405 real exploits), 70% exploit generation efficiency gain, $4.6M simulated autonomous revenue.'),
    ('https://pub.towardsai.net/run-mxbai-rerank-v2-with-infinity-4b73858cd644', 'Infrastructure & Proxy Layers', 'mxbai-rerank-v2: Local SOTA', 'A state-of-the-art reranking model optimized for local inference via Infinity, outperforming Cohere Rerank 3.5 with 8x faster execution.', 'reranking, rag, performance, infinity, optimization', 'NDCG@10 57.49 (beats Cohere), 8x faster than industry standards, local Infinity inference integration, GRPO-optimized 1.5B variant.')
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
print('Successfully injected batch 146.')