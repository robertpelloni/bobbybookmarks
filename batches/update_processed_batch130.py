import sqlite3

data = [
    ('https://www.reddit.com/r/highfreqtrading/comments/1q8aedw/memglass_peeking_into_live_trading_systems/', 'Infrastructure & Proxy Layers', 'MemGlass: HFT Observability', 'A real-time, cross-process observation tool for C++ POD objects via shared memory, providing a "cheap peephole" for latency-sensitive production systems.', 'observability, hft, cpp, low-latency, shared-memory', 'Zero-overhead shared memory observation, cross-process POD inspection, non-blocking lock-free reads, production-safe "peephole" monitoring.'),
    ('https://www.reddit.com/r/highfreqtrading/comments/1qdz5ju/open_source_lowlatency_c_order_book_engine/', 'Memory & Persistence Architecture', 'Low-Latency Order Book Engine', 'A C++ order book implementation optimized for bare-metal deterministic P99 latency, bypassing standard library containers to process operations in 23-50 CPU cycles.', 'cpp, low-latency, data-structures, hft, optimization', 'Chunked bitmaps, vector-backed node pools, intrusive index-based linked lists, zero-allocation hot paths.'),
    ('https://www.reddit.com/r/highfreqtrading/comments/1qkslbi/i_built_a_deterministic_l3_replay_paper_execution/', 'Development Tools & Libraries', 'LOBSIM: Deterministic L3 Replay', 'A high-performance Limit Order Book Simulator combining a C++20 core with Python bindings for deterministic replay of tens of millions of L3 events.', 'simulation, hft, cpp, python-bindings, testing', 'C++20 core performance, event-by-event deterministic replay, queue position tracking, structured diagnostic data streaming.'),
    ('https://www.reddit.com/r/SmartDumbAI/comments/1r4fwpt/10x_your_openclaw_ai_setup_into_a_productiongrade/', 'Agent Orchestration & Workflow', 'OpenClaw Production Tiering', 'A framework for upgrading OpenClaw from a chat interface to an autonomous operator by implementing smart model routing and self-verification pipelines.', 'orchestration, openclaw, model-routing, verification, automation', 'Smart routine-task routing (Haiku vs Opus), autonomous cross-verification loops, persistent 24/7 operator mode, task delegation logic.')
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
print('Successfully injected batch 80.')