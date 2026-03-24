import sqlite3

data = [
    ('https://lmarena.ai/leaderboard', 'Guides & Industry Trends', 'LMSYS Chatbot Arena', 'The industry-standard LLM leaderboard, identifying the "Superintelligence Tier" of models for coding, reasoning, and vision.', 'benchmarks, leaderboard, elo, coding-performance, sw-bench', 'Claude Opus 4.6 (Coding King), GPT-5.3-Codex (DevOps Leader), Gemini 3.1 Pro (Vision-to-Code), DeepSeek R1 (#1 Open Source).'),
    ('https://lucumr.pocoo.org/2026/1/18/agent-psychosis/', 'Guides & Industry Trends', 'Agent Psychosis: A Critique', 'A seminal critique by Armin Ronacher on the "dopamine loop" of agent development and the danger of "maintainer asymmetry" in open source.', 'philosophy, critique, ai-slop, maintainer-friction, human-in-the-loop', 'Dæmon parallel (impulses vs reality), "Slop at Scale" warning, unsupervised agent PR risks, developer-maintainer power dynamics.'),
    ('https://lynchmark.com/blog/gemini-optimal-temperature', 'Guides & Industry Trends', 'Gemini Optimal Temperature', 'A technical benchmark of 231 automated coding tests determining the optimal temperature setting for production-grade agent reasoning.', 'optimization, hyperparameters, gemini, reliability, benchmarking', 'Optimal Temperature = 0.35, "Cluster of Perfection" (0.0-0.5) identification, median vs average performance analysis, entropy threshold detection.'),
    ('https://medium.com/sadasant/god-mode-ux-why-your-next-interface-will-look-more-like-starcraft-than-slack-12498eb274d4', 'Interface & Developer UX', 'God Mode UX: RTS Agents', 'A UX philosophy proposing a spatial, "StarCraft-like" vantage point for managing agent swarms and tracking compute resource economies.', 'gui, ux-design, rts, orchestration, agent-societies', 'Resource dashboards (Gold/Lumber/Tokens), "Strategic Zoom" macro/micro management, agents-as-spatial-units, orchestration clarity.')
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
print('Successfully injected batch 48.')
