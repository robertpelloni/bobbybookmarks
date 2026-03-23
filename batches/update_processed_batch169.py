import sqlite3

data = [
    ('https://en.m.wikipedia.org/wiki/Palantir_Technologies', 'AI Agents & Frameworks', 'Palantir AIP: Agent Studio', 'An enterprise execution platform where autonomous agents operate within a digital-twin "Ontology" to re-route supply chains and execute production edits.', 'palantir, aip, ontology, orchestration, enterprise', 'Autonomous Agent Studio, Agentic AI Hives (multi-agent collab), Ontology-grounded execution, AIP Evals safety framework.'),
    ('https://en.m.wikipedia.org/wiki/Open_Mind_Common_Sense', 'Guides & Industry Trends', 'OMCS: AI Common Sense', 'A historical MIT project (1999) that pioneered crowdsourced AI data collection to teach computers everyday "common sense" facts, leading to ConceptNet.', 'ai-history, common-sense, crowdsourcing, conceptnet, mit', 'Crowdsourced natural language facts (1M+), ConceptNet semantic network, "Wisdom of the crowd" AI data, Marvin Minsky legacy.'),
    ('https://en.m.wikipedia.org/wiki/Mindpixel', 'Guides & Industry Trends', 'Mindpixel: Digital Soul', 'A historical AI project (2000-2005) that attempted to build a "Generic Artificial Consciousness" by validating millions of true/false "pixels" of human knowledge.', 'ai-history, consciousness, consensus, mindpixel, philosophy', 'True/False knowledge units (pixels), human validation consensus loop, generic artificial consciousness (GAC) goal, historical crowdsourced AI.'),
    ('https://en.m.wikipedia.org/wiki/Outer_Wilds', 'Guides & Industry Trends', 'Outer Wilds: Knowledge Engine', 'A space exploration game celebrated for its "Metroidbrainia" structure where progress is gated entirely by information rather than physical upgrades.', 'narrative-design, information-gating, time-loop, knowledge-management, game-design', '22-minute time loop structure, information-based progress engine, persistent Ship Log detective board, non-linear knowledge discovery.')
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
print('Successfully injected batch 119.')