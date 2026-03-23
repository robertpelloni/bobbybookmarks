import sqlite3

data = [
    ('https://news.ycombinator.com/item?id=46315583', 'Guides & Industry Trends', 'HN: National Data Breach', 'A discussion on the technical challenges of searching and indexing irreversibly public data leaks, featuring suggestions for large-scale SQLite indexing.', 'security, data-breach, sqlite, privacy, community-discussion', '164GB+ leak scale analysis, local indexing via SQLite/grep, long-term privacy implications, technical triage strategies.'),
    ('https://news.ycombinator.com/item?id=46316367', 'Guides & Industry Trends', 'HN: Lapsus$ Hacker Sentencing', 'A community analysis of the Lapsus$ GTA 6 hack, focusing on the use of ultra-low-end hardware (Firestick/Phone) and social engineering techniques.', 'security, adversarial-ai, hacking, social-engineering, hardware-constraints', 'Low-hardware exploit feasibility (Amazon Firestick), social engineering vs complex technical feats, law enforcement protection gaps.'),
    ('https://news.ycombinator.com/item?id=46338437', 'Guides & Industry Trends', 'HN: Private Fiat vs Scams', 'A high-level debate on the production costs and intrinsic value of privately issued currencies like Bitcoin versus traditional fiat and scams.', 'crypto, economics, philosophy, bitcoin, community-debate', 'Production cost vs nominal value analysis, early-adopter wealth tension, mining hardware industry evolution, libertarian rhetoric critique.'),
    ('https://news.ycombinator.com/item?id=46348971', 'Development Tools & Libraries', 'HN: Best Community Clients', 'A curated community thread recommending the most efficient tools and extensions for consuming and filtering Hacker News discussions.', 'cli, reader, productivity, rss, hn-clients', 'HNCute extension, HnRSS service integration, Material Hacker News mobile client, domain-based news filtering patterns.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 8) for d in data]:
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
print('Successfully injected batch 49.')
