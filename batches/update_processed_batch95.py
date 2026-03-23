import sqlite3

data = [
    ('https://www.reddit.com/r/AIMemory/comments/1qyjxlb/agents_need_execution_memory_not_just_context/', 'Memory & Persistence Architecture', 'Execution Memory: Sandbox State', 'A paradigm shift proposing that agents need persistent, deduped execution memory (checkpoints) to maintain state across restarts and tool failures.', 'execution-memory, sandboxing, persistence, state-management, reliability', 'Deterministic execution checkpoints, state-deduplication logic, sandbox-persistence value, cross-session tool recovery.'),
    ('https://www.reddit.com/r/AIMemory/comments/1r1asay/memv_predictcalibrate_extraction_bitemporal/', 'Memory & Persistence Architecture', 'MemV: Bitemporal Memory', 'A sophisticated memory extraction system using a Predict/Calibrate loop to ensure high-accuracy bitemporal fact storage.', 'bitemporal-memory, fact-extraction, memv, accuracy, reasoning', 'Predict/Calibrate extraction loop, bitemporal event tracking (Valid Time vs. Transaction Time), conflicting fact calibration, high-fidelity user profiling.'),
    ('https://www.reddit.com/r/AIMemory/comments/1r6ay21/a_plaintext_semantic_tree_os_for_ai_memory_you/', 'Memory & Persistence Architecture', 'Plaintext Semantic Tree OS', 'A memory architecture that treats agent knowledge as a human-editable, plaintext semantic tree, ensuring total transparency and user control.', 'memory-architecture, plaintext, semantic-tree, transparency, human-in-the-loop', 'Human-editable knowledge tree, markdown-based persistence, branch-level memory auditing, transparent reasoning paths.'),
    ('https://www.reddit.com/r/AISystemsEngineering/comments/1r685s5/is_anyone_else_finding_that_reasoning_isnt_the/', 'Agent Orchestration & Workflow', 'Systems-First Agent Design', 'A technical discussion arguing that "Systems Engineering" (feedback loops and harnesses) is now a larger bottleneck for agents than raw reasoning.', 'systems-engineering, feedback-loops, harness, orchestration, optimization', 'Closed-loop verification systems, environment-as-scaffolding, bottleneck shift from logic to ops, reliable build-fix automation.')
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
print('Successfully injected batch 61.')
