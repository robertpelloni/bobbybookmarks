import sqlite3

data = [
    ('https://www.reddit.com/r/Msty_AI/comments/1r803eh/msty_admin_mcp_v500_bloom_behavioral_evaluation/', 'Infrastructure & Proxy Layers', 'Msty Bloom: Behavioral Eval', 'A behavioral evaluation framework that uses multi-turn unit tests to detect sycophancy and hallucinations in local models, triggering escalations to more capable remote models.', 'evaluation, calibration, behavioral-test, local-llm, quality-gate', 'Multi-turn behavioral unit tests, Sycophancy/Overconfidence scoring (0.0-1.0), automated handoff triggers, task-category reliability mapping.'),
    ('https://www.reddit.com/r/Nix/comments/1r4qbx8/nixcsi_042_released/', 'Infrastructure & Proxy Layers', 'NixCSI: Declarative Agent Infra', 'A bridge between Nix package management and K8s that enables immutable, reproducible agent environments with high-efficiency resource sharing via hardlink CSI mounts.', 'nix, k8s, infrastructure, declarative, reproducibility', 'Declarative environment injection (flakeRef), hardlink inode sharing (0-overhead), LRU Lix temporal garbage collection, atomic environment evolution.')
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
print('Successfully injected batch 66.')
