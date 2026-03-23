import sqlite3

data = [
    ('https://flowingedge.com/flowingedge-home-edition', 'Infrastructure & Proxy Layers', 'FlowingEdge: Cloud-Free Sync', 'A decentralized, server-to-server file sharing solution that uses xchaha20 encryption to transfer unlimited data without a central cloud intermediary.', 'file-sharing, decentralization, xchaha20, security, sync', 'Cloud-free direct device transfer, xchaha20 packet-level encryption, unlimited file scale (terabytes), smart resume logic.'),
    ('https://gail.wharton.upenn.edu/prompt-library', 'Guides & Industry Trends', 'Wharton AI Prompt Library', 'An evidence-based library of generative AI prompt templates and best practices developed by the Wharton Generative AI Labs.', 'prompt-engineering, education, framework, best-practices, research', 'Evidence-based prompt templates (CC BY 4.0), model-specific performance guidance, iterative "steering" frameworks, few-shot prompting standards.'),
    ('https://genai-showdown.specr.net/', 'Guides & Industry Trends', '2026 GenAI ELO Leaderboard', 'A performance tracking leaderboard for early 2026 emphasizing "Reasoning Effort" and multimodal context efficiency across frontier models.', 'benchmarks, elo, reasoning, multimodal, research', 'Reasoning Effort ELO tracking, multimodal integration metrics, speed-to-quality ratio analysis, interactive model comparison.'),
    ('https://getmicropad.com/', 'Interface & Developer UX', 'MicroPad: Infinite Canvas', 'A non-linear, infinite-canvas note-taking application built with React.js that features μSync client-side AES-256 encryption.', 'note-taking, infinite-canvas, sync, privacy, open-source', 'Infinite digital whiteboard workspace, μSync client-side AES-256 encryption, Jupyter Notebook (.ipynb) integration, smart hashtag linking.')
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
print('Successfully injected batch 124.')