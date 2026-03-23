import sqlite3

data = [
    ('https://www.google.com/search?q=AI+Bookmark+Organizer', 'Memory & Persistence Architecture', 'AI Bookmark Organizer', 'A modern AI-powered "second brain" that uses semantic search, RAG, and automatic categorization to organize and summarize saved links.', 'bookmarks, memory, rag, semantic-search, organization', 'Semantic search via RAG, automatic clustering without tags, multi-modal capture (PDFs/YouTube), conversational retrieval.'),
    ('https://www.google.com/search?q=Firefox+AI+tab+organizer', 'Interface & Developer UX', 'Firefox AI Tab Organizer', 'Mozilla\'s local-first AI integration for Firefox that manages "tab sprawl" using on-device ML to auto-group tabs based on content similarity.', 'firefox, browser-extension, tabs, productivity, privacy', 'Local ML tab grouping, auto-generated group names/colors, sidebar chatbot integration, AI-generated link previews.'),
    ('https://excire.com/', 'Development Tools & Libraries', 'Excire Search 2026', 'An AI-powered Lightroom Classic plug-in providing 100% local object recognition, scene detection, and AI-assisted photo culling.', 'lightroom, photo-management, vision, local-ai, tagging', '100% local processing, text-prompt image search, AI-assisted culling (sharpness/aesthetics), face sharpness detection strip.'),
    ('https://www.google.com/search?q=pdf+to+youtube+video+with+ai', 'Development Tools & Libraries', 'PDF-to-Video Generators', 'A category of AI tools (like DeepBrain AI, Wondercraft) that autonomously convert static documents/PDFs into narrated, avatar-led video presentations.', 'video-generation, document-intelligence, tts, avatars, automation', 'Automated script generation from PDFs, realistic AI avatar presenters, semantic scene segmentation, 140+ language localization.')
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
print('Successfully injected batch 158.')