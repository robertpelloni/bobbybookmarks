import sqlite3

data = [
    ('https://docs.sentry.io/product/sentry-mcp#codex', 'Agent Orchestration & Workflow', 'Sentry MCP: Seer Fixes', 'An MCP server connecting agents to Sentry issues and Seer (AI root cause analysis) for autonomous bug-fixing pipelines.', 'mcp, sentry, observability, debugging, seer', '16+Issue management tools, direct Seer AI fix suggestions, OAuth security, remote/local transport modes, agent performance monitoring.'),
    ('https://duckdb.org/docs/stable/core_extensions/vss', 'Memory & Persistence Architecture', 'DuckDB VSS: Vector Search', 'A high-performance local vector similarity search extension for DuckDB using HNSW indexes via the usearch library.', 'duckdb, vss, vector-search, hnsw, local-rag', 'HNSW indexing (usearch), distance metrics (L2/Cosine), fuzzy joins (vss_join), progress-tracked index builds, experimental disk persistence.'),
    ('https://dogbolt.org/?id=8f1e28f5-3bfc-4d41-8be2-82c12f54487f', 'Development Tools & Libraries', 'Dogbolt: Decompiler Explorer', 'A web-based visual tool comparing outputs from multiple decompilers (Ghidra, Hex-Rays, Binary Ninja) side-by-side.', 'reverse-engineering, decompiler, security, visualization, ghidra', 'Multi-engine comparison, Time Travel Debugging (Undo.io), interactive C/C++ source diffs, programmatic CLI client.'),
    ('https://en.m.wikipedia.org/wiki/Compound_File_Binary_Format', 'Guides & Industry Trends', 'CFBF: OLE2 File System', 'A legacy sector-based binary format ("file system within a file") used for MSI, older Office docs, and proprietary industrial data.', 'filesystem, legacy, cfbf, ole2, storage', 'Hierarchical Storage/Stream objects, sector-based FAT allocation, MiniFAT for small data, 2GB v3 size limit.')
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
print('Successfully injected batch 118.')