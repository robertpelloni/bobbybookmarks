import sqlite3

data = [
    ('https://www.winboat.app/', 'Infrastructure & Proxy Layers', 'WinBoat: Native Linux VM', 'An open-source virtualization tool designed to run Windows applications on Linux with a seamless "native" window feel, avoiding traditional heavy VM overhead.', 'virtualization, linux, windows, docker, infrastructure', 'Seamless desktop windowing (no VM box), automated Docker/KVM environment setup, Adobe/Office compatibility, smartcard pass-through support.'),
    ('https://www.tuui.com/', 'Interface & Developer UX', 'TUUI: MCP Desktop Client', 'A Vue/TypeScript-based desktop application framework that acts as a unified UI client for Model Context Protocol (MCP) servers, streamlining tool orchestration.', 'mcp, gui, tuui, framework, client', 'Unitary UI for MCP servers, cross-vendor LLM API orchestration, Vue 3/Pinia architecture, dynamic theme engine.'),
    ('https://www.x-cmd.com/', 'Development Tools & Libraries', 'X-CMD: POSIX Modularity', 'A lightweight, modular command-line toolkit written in POSIX Shell/AWK that provides agents with structured CLI skills and a 1000+ tool package manager.', 'cli, shell, posix, tools, automation', '100+ pre-configured shell modules, 1000+ CLI tool package manager (no root required), agent-optimized command wrappers, 3MB lightweight footprint.'),
    ('https://www.trydepth.ai/', 'Development Tools & Libraries', 'TryDepth.ai: Spatial Gen', 'An AI-driven platform for high-fidelity 2D-to-3D depth estimation, providing spatial intelligence data for web AR/VR experiences.', 'vision, depth-estimation, 3d, ar-vr, spatial-intelligence', 'High-fidelity depth map generation, 2D to 3D image conversion, spatial intelligence API, WebGL integration support.')
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
print('Successfully injected batch 177.')