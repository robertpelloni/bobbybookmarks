import sqlite3

data = [
    ('https://www.reddit.com/r/OpenAI/comments/1jcpoao/manus_vs_operator', 'Guides & Industry Trends', 'Manus vs Operator', 'A comparative analysis of the 2026 agentic landscape highlighting Manus (autonomous task completion/delegation) vs OpenAI Operator (interactive reasoning).', 'manus, operator, orchestration, autonomy, benchmarks', 'Manus autonomous Plan Mode execution, OpenAI Operator conversational integration, "delegate-and-walk-away" vs "human-in-the-loop" paradigms.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1ogu78z/opencode_vs_codebuff_vs_factory_droid_vs_charm', 'Agent Orchestration & Workflow', 'Terminal Agent Wars 2026', 'A community breakdown of top terminal AI coders: OpenCode (Swiss Army Knife), Factory Droid (Superior .MD planning), and Codebuff (Expensive/Powerful).', 'opencode, cli, codebuff, factory-droid, orchestration', 'OpenCode Auto Compact context saving, Factory Droid `.MD` planning superiority, 75+ multi-provider support, cost-efficiency optimization.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1p3c9py/codenomad_v021dev_released_images_remote_access', 'Interface & Developer UX', 'CodeNomad: Desktop Hub', 'A multi-instance desktop client for OpenCode designed for long-form coding sessions, featuring remote mobile access and a unified Permission Center.', 'gui, opencode, orchestration, multi-agent, remote-access', 'Multi-instance workspace tabs, Session Tree hierarchy grouping, QR-code mobile remote access, unified tool-call Permission Center.'),
    ('https://www.reddit.com/r/opensource/comments/1i6dewf/smart_bookmark_an_aipowered_bookmark_manager', 'Memory & Persistence Architecture', 'Smart Bookmark Manager', 'An open-source AI bookmark manager featuring natural language search, automatic tagging, and experimental "Living Avatars" that fade if links are ignored.', 'bookmarks, memory, semantic-search, open-source, ux', 'Natural language semantic search, automated AI summarization/tagging, "Living Avatars" accountability layer, local self-hosted privacy options.')
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
print('Successfully injected batch 173.')