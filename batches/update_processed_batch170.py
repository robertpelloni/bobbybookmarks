import sqlite3

data = [
    ('https://en.wikipedia.org/wiki/Briar_(software)', 'Connectivity & Interoperability (MCP/A2A)', 'Briar: Mesh Messaging', 'A peer-to-peer mesh messaging system that uses Bluetooth, Wi-Fi, and Tor to synchronize data without central servers, featuring Delay-Tolerant Networking (DTN).', 'p2p, mesh-network, briar, privacy, decentralization', 'Multi-transport sync (BT/Wi-Fi/Tor), store-and-forward Delay-Tolerant Networking, Bramble protocol suite, encrypted ad-hoc mesh networking.'),
    ('https://en.wikipedia.org/wiki/Enuma_Anu_Enlil', 'Guides & Industry Trends', 'Enuma Anu Enlil: Logic', 'A foundational 1st millennium BCE series of Babylonian astrological omens utilizing a strict Protasis-Apodosis logic structure (If X, then Y).', 'babylonian, history, logic, pattern-recognition, omens', '70-tablet cuneiform series, 7,000+ conditional omens, Protasis-Apodosis logic structure, thematic categorical organization (Moon/Sun/Weather/Stars).'),
    ('https://en.wikipedia.org/wiki/Book_of_the_Dead', 'Guides & Industry Trends', 'Book of the Dead: Guidebook', 'A collection of ancient Egyptian spells and funerary texts designed as a practical guidebook for navigating the complex hazards of the underworld (Duat).', 'egyptology, history, information-design, mythology, spells', '~190 spells for underworld navigation, "Weighing of the Heart" judgment ceremony, customized papyrus scroll structure, magical warding instructions.'),
    ('https://en.wikipedia.org/wiki/Comparison_of_file-sharing_applications', 'Guides & Industry Trends', '2026 File-Sharing Audit', 'A comparative analysis of the 2026 file-sharing market, highlighting the dominance of Stash and Smash for large-scale, privacy-first E2EE transfers.', 'file-sharing, comparison, e2ee, privacy, storage', 'Unlimited free transfers (Stash/Smash), true end-to-end encryption (E2EE), account-free recipient access, 15TB+ enterprise video support (Masv).')
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
print('Successfully injected batch 120.')