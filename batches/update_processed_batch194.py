import sqlite3

data = [
    ('https://www.bitflux.ai/blog/memory-is-slow-part2', 'Infrastructure & Proxy Layers', 'Memory Latency: Bitflux', 'A technical analysis of memory latency bottlenecks in modern hardware, advocating for vectorization and massive parallelism to hide stable cache miss costs.', 'performance, hardware, optimization, memory, architecture', 'Memory vs Disk latency trends, cache-miss cost analysis, vectorization strategies, parallel data pipelining.'),
    ('https://www.bravent.net/en/news/autogen-revolutionizing-agent-orchestration-with-ai', 'Agent Orchestration & Workflow', 'AutoGen: Event-Driven', 'Microsoft\'s 2026 evolution of AutoGen into a production-ready asynchronous multi-agent platform featuring native MCP integration and "Token Bleeding" protection.', 'autogen, orchestration, multi-agent, mcp, automation', 'Event-driven asynchronous core, "User Proxy" autonomous loops, MCP-standardized tool usage, API budget safety guardrails.'),
    ('https://www.chaoticafractals.com/', 'Development Tools & Libraries', 'Chaotica: GPU Fractals', 'A high-performance fractal engine by Glare Technologies featuring OpenCL GPU acceleration, double-precision math, and progressive real-time rendering.', 'fractals, gpu-acceleration, opencl, generative-art, visualization', 'OpenCL multi-GPU rendering, double-precision convergence, HDR progressive engine, real-time interactive editing.'),
    ('https://www.chrisharrison.net/index.php/Visualizations/BibleViz', 'Guides & Industry Trends', 'BibleViz: Link Mapping', 'A landmark data visualization project mapping 63,779 biblical cross-references into an arc diagram to reveal the inherent information density and structural integrity of the text.', 'visualization, data-science, bibleviz, information-theory, mapping', '63,000+ cross-reference arc diagram, frequency-based social network mapping, verse-volume structural bar charts, information density visualization.')
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
print('Successfully injected batch 154.')