import sqlite3

data = [
    ('https://chromewebstore.google.com/detail/algonius-browser-mcp/fmcmnpejjhphnfdaegmdmahkgaccghem', 'Connectivity & Interoperability (MCP/A2A)', 'Algonius Browser MCP', 'An open-source MCP server that enables AI agents to control active Chrome sessions via an accessibility tree bridge, allowing interaction with authenticated web apps.', 'mcp, browser-automation, chrome-extension, accessibility-tree, agent-control', 'Active session interaction (bypass login), accessibility-tree compact context, Go-based secure native messaging, direct click/fill/nav tools.'),
    ('https://chromewebstore.google.com/detail/saveday-ai-bookmark-manag/gmfaoihlkhopieoibopcponemocgbloj?hl=en-US', 'Memory & Persistence Architecture', 'SaveDay: Knowledge Assistant', 'An AI-powered bookmark manager that captures multi-format content (links, PDFs, podcasts) and provides semantic search and instant YouTube/article summaries.', 'bookmarks, memory, summarization, semantic-search, knowledge-base', 'Instant AI summaries (YouTube/Article), natural language semantic search, multi-format capture (audio/video/PDF), mobile Telegram bot integration.'),
    ('https://chromewebstore.google.com/detail/phew-ai-tab-ai-auto-group/ccnagafbnapafjidkhbgligfoccmjddb', 'Interface & Developer UX', 'Phew AI Tab: Intelligent Groups', 'An intelligent tab manager that uses AI to auto-group new tabs by content and provides a vertical sidebar with local AES-256 encryption.', 'tabs, productivity, auto-grouping, sidebar, privacy', 'Content-aware AI auto-grouping, vertical tab sidebar, auto-collapse inactive groups, local AES-256 encryption (Supabase sync support).'),
    ('https://chromewebstore.google.com/detail/advance-tab-groups/pfpdhdhhmaaadjdolgfphniimpjnifhh', 'Interface & Developer UX', 'Advance Tab Groups: Regex', 'An automation-focused tab manager that uses Regex rules and domain-based logic to automatically organize and snapshot complex browser sessions.', 'tabs, automation, regex, snapshots, chrome-extension', 'Regex-based auto-grouping rules, session state snapshots (save/restore), extensive keyboard shortcut suite, domain-based isolation.')
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
print('Successfully injected batch 112.')