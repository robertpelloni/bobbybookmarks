import sqlite3

data = [
    ('https://www.mousemux.com/', 'Interface & Developer UX', 'MouseMux: Multi-Cursor', 'A multi-cursor collaboration tool for Windows that allows multiple users to operate their own independent mouse and keyboard simultaneously on a single PC.', 'mousemux, collaboration, windows, multi-cursor, productivity', 'True simultaneous multi-user interaction (Multiplex mode), independent cursor configuration, RustDesk remote integration.'),
    ('https://www.nongnu.org/bookmarkfs', 'Memory & Persistence Architecture', 'BookmarkFS: Mount Links', 'A FUSE-based pseudo-filesystem for GNU/Linux that mounts browser bookmark files (Firefox/Chromium) as standard directory structures for CLI manipulation.', 'filesystem, fuse, bookmarks, linux, cli', 'Mounts places.sqlite/Bookmarks as VFS, allows standard POSIX tools (ls, cp, grep, fdupes) for bookmark management.'),
    ('https://www.noti.tg/', 'Interface & Developer UX', 'NotITG: Modchart Engine', 'A highly modified StepMania engine designed for "modchart" creators, featuring Lua scripting and GLSL shaders to manipulate game windows and note paths.', 'gaming, rhythm-game, lua, glsl, engine', 'Real-time modchart effect previews, GLSL shader support, arbitrary window manipulation, Sight Reading Tournament (SRT) focus.'),
    ('https://www.npmjs.com/package/@modelcontextprotocol/server-everything', 'Connectivity & Interoperability (MCP/A2A)', 'MCP: server-everything', 'The official reference test server for the Model Context Protocol (MCP), implementing all primitives (Prompts, Resources, Tools) to help developers validate MCP clients.', 'mcp, reference, testing, protocol, sdk', 'Comprehensive primitive implementation (Prompts/Resources/Tools), completion/sampling testing, baseline for IDE client validation.')
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
print('Successfully injected batch 164.')