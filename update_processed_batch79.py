import sqlite3

data = [
    ('https://github.com/supermemoryai/supermemory', 'Memory & Persistence Architecture', 'SuperMemory: AI Second Brain', 'An open-source memory engine designed to provide LLMs with infinite context by building persistent user profiles and fact-based knowledge graphs.', 'memory-engine, second-brain, context-management, rag, self-updating', 'Infinite context API, self-updating knowledge base, multi-LLM support (Claude/Cursor), ranked #1 on memory benchmarks.'),
    ('https://github.com/steveyegge/gastown', 'Agent Orchestration & Workflow', 'Gastown: Stateless Agent Factory', 'A multi-agent workspace manager that treats AI sessions as ephemeral "cattle," using a persistent external state system (Beads) to ensure context survival.', 'stateless-agents, orchestration, git-worktrees, beads, parallelism', 'Stateless agent sessions, "The Mayor" central orchestrator, git-backed persistence (Beads), parallel multi-agent execution.'),
    ('https://github.com/tad-hq/universal-session-viewer', 'Interface & Developer UX', 'Tad: Universal Session Viewer', 'A high-performance desktop application powered by DuckDB for viewing and analyzing large tabular datasets (CSV/Parquet/SQLite) with sub-second pivot speed.', 'gui, data-visualization, duckdb, analytics, high-performance', 'DuckDB-in-memory engine, hierarchical pivot tables, smooth scrolling for millions of rows, CLI-native launch support.'),
    ('https://github.com/superagent-ai/reag', 'Memory & Persistence Architecture', 'ReAG: Reasoning-Augmented Gen', 'A project proposing a paradigm shift from traditional RAG to "Reasoning-Augmented Generation," feeding full documents directly to the LLM for holistic evaluation.', 'reag, reasoning, rag-alternative, accuracy, context-engineering', 'Holistic full-document evaluation, retrieval-generation reasoning loop, elimination of "lost-in-middle" chunking issues, high-accuracy synthesis.')
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
print('Successfully injected batch 45.')
