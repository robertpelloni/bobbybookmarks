import sqlite3

data = [
    ('https://www.ee.chat/', 'Interface & Developer UX', 'EE Chat: Local AI Client', 'A privacy-first, locally deployed LLM client designed for desktop and mobile, featuring native MCP support and advanced markdown/LaTeX rendering.', 'chat, local-llm, mcp, privacy, desktop-app', '100% local data storage, native Model Context Protocol (MCP) integration, LaTeX/Markdown rendering, multi-tool parallel execution.'),
    ('https://www.exodus1174.com/#/', 'Guides & Industry Trends', 'Exodus 1174: Mod Project', 'A massive community-driven total conversion mod focusing on extreme realism, expanded lore, and complex survival mechanics.', 'modding, game-dev, survival, realism, community', 'Total conversion asset overhaul, hardcore survival mechanics (radiation/hunger), custom-voiced branching narratives, dynamic living ecosystem.'),
    ('https://www.freeciv.org/', 'Interface & Developer UX', 'Freeciv: WebGL Relaunch', 'The gold standard open-source 4X strategy game, featuring a 2026 Freeciv3D WebGL engine relaunch for browser-based play supporting up to 500 players.', 'gaming, open-source, 4x, webgl, strategy', 'Freeciv3D WebGL browser engine, massive multiplayer (126-500 players), cross-platform seamless play, highly customizable rulesets.'),
    ('https://www.e-flux.com/journal/148/631017/society-of-the-psyop-part-2-ai-mind-control-and-magic', 'Guides & Industry Trends', 'Society of the Psyop Pt.2', 'An essay by Trevor Paglen exploring "affective computing" and how modern generative AI algorithms act as "mind hacking" extensions of historical MKUltra-style projects.', 'philosophy, ai-safety, psychology, psyop, manipulation', 'Analysis of "affective computing," AI as active neurological measurement, historical MKUltra parallels, algorithmic reality hallucination.')
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
print('Successfully injected batch 155.')