import sqlite3

data = [
    ('https://alternativeto.net/software/jan-ai/about', 'Interface & Developer UX', 'Jan AI: Local LLM Hub', 'A cross-platform, local-first alternative to ChatGPT that provides an OpenAI-compatible API and native MCP integration for private agentic workflows.', 'local-llm, privacy, openai-api, mcp, desktop-app', 'OpenAI-compatible local API (localhost:1337), one-click Hugging Face downloads, automatic GPU optimization, native MCP server support.'),
    ('https://alternativeto.net/software/gpt4all/about', 'AI Agents & Frameworks', 'GPT4All: Privacy AI', 'A privacy-focused framework by Nomic AI for running 1000+ open-source models on standard consumer hardware, featuring LocalDocs for private RAG.', 'privacy, local-llm, rag, nomin-ai, cpu-optimized', 'LocalDocs private document RAG, 1000+ model support (GGUF), optimized CPU/GPU inference, domain-specific AI agents.'),
    ('https://alternativeto.net/software/upscayl/about', 'Development Tools & Libraries', 'Upscayl: Image Enhancement', 'A free, open-source AI image upscaler that supports resolution enhancement up to 16x and batch processing using diverse specialized models.', 'image-upscaling, open-source, enhancement, batch-processing, vision', 'Up to 16x resolution upscaling, batch processing for hundreds of files, specialized models (Real-ESRGAN/Remacri), 100% local/private desktop app.'),
    ('https://alternativeto.net/software/tagstudio/about', 'Memory & Persistence Architecture', 'TagStudio: Meta-Layer', 'A photo and file organization system that uses a robust, tag-based SQLite metadata layer to manage libraries without altering the underlying filesystem.', 'file-management, tagging, sqlite, metadata, organization', 'SQLite-based metadata storage, nested tags and aliases, powerful Boolean search, cross-platform media previews (PSD/Blender/Krita).')
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
print('Successfully injected batch 107.')