import sqlite3

data = [
    ('https://www.augmentcode.com/blog/a-real-time-index-for-your-codebase-secure-personal-scalable', 'Context Engineering & Isolation', 'Augment Code: Real-time Index', 'A leading enterprise context engine that provides instant (sub-second) indexing for 400,000+ file repositories and native MCP support.', 'context-engineering, optimization, augment-code, mcp, search', 'Instant synchronization (seconds), 400k+ file capacity, personalized per-developer indices, native MCP server integration.'),
    ('https://www.asus.com/networking-iot-servers/desktop-ai-supercomputer/ultra-small-ai-supercomputers/asus-ascent-gx10', 'Infrastructure & Proxy Layers', 'Asus Ascent: 1 PetaFLOP', 'A personal AI supercomputer powered by the NVIDIA Grace Blackwell superchip, delivering 1 petaFLOP of AI compute in a compact 150mm chassis.', 'hardware, nvidia, blackwell, supercomputer, performance', 'NVIDIA Grace Blackwell Superchip, 1 petaFLOP (1,000 TOPS) compute, 128GB Unified LPDDR5x RAM, NVIDIA DGX OS stack support.'),
    ('https://www.androidauthority.com/aluminium-os-android-for-pcs-3619092', 'Guides & Industry Trends', 'Aluminium OS: Desktop Android', 'Google\'s internal project to bring a desktop-class Android experience to PCs, featuring Gemini-core intelligence and native windowing.', 'google, android, os, gemini, productivity', 'Native desktop windowing/snapping, Gemini-at-the-core AI intelligence, cross-device Handoff continuity, Android app ecosystem on PC.'),
    ('https://www.betonit.ai/p/what-the-infamous-heroin-study-said', 'Guides & Industry Trends', 'Bet On It: Agent Economy 2026', 'A strategic analysis of the 2026 "Agent Economy," predicting the shift from prototypes to autonomous employees driven by ultra-low inference costs.', 'economics, strategy, agent-economy, productivity, benchmarks', 'Autonomous employee workflows, "Great Token Deflation" costs, integration-as-moat thesis, data governance priority.')
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
print('Successfully injected batch 153.')