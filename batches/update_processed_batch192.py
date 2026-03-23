import sqlite3

data = [
    ('https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a', 'Memory & Persistence Architecture', 'Beads: Graph Memory', 'A distributed graph issue tracker by Steve Yegge designed to provide agents with persistent session memory via a version-controlled Dolt database.', 'memory, issue-tracking, dolt, persistence, orchestration', 'Graph-based dependency tracking, Dolt (SQL+Git) backend, hash-based conflict resolution, automated semantic task compaction.'),
    ('https://starship.rs/', 'Interface & Developer UX', 'Starship: Rust Prompt', 'A high-performance, cross-shell prompt written in Rust that provides 10ms rendering and intelligent context detection for 80+ tools.', 'terminal, tui, rust, performance, dev-tools', '10-15ms rendering speed, universal shell support (Zsh/Bash/PowerShell), intelligent tool context detection, TOML-based declarative configuration.'),
    ('https://superagi.com/top-10-ai-orchestration-tools-for-2025-a-comparison-of-features-and-benefits', 'Agent Orchestration & Workflow', 'Top 10 Orchestrators 2025', 'A comparative analysis of the leading AI orchestration platforms, ranking SuperAGI, AutoGen, and LangChain as the top frameworks for autonomous swarms.', 'orchestration, frameworks, multi-agent, comparison, swarm', 'SuperAGI autonomous swarms, Microsoft AutoGen multi-agent loops, LlamaIndex RAG orchestration, Apache Airflow pipeline integration.'),
    ('https://store.minisforum.com/products/minisforum-ms-s1-max-mini-pc', 'Infrastructure & Proxy Layers', 'MS-S1 Max: AI Workstation', 'A high-end AI Mini Workstation powered by AMD Strix Halo, delivering 126 TOPS total AI compute and up to 128GB unified memory for local LLM inference.', 'hardware, amd, strix-halo, local-llm, performance', '50 TOPS dedicated NPU (XDNA 2), 126 TOPS total AI compute, 128GB LPDDR5X-8000 unified memory, 235B model local execution support.')
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
print('Successfully injected batch 150.')