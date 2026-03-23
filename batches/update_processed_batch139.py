import sqlite3

data = [
    ('https://www.reddit.com/r/notebooklm/comments/1qdr5j1/beware_of_audio_overviews_notebooklm_is_not_its/', 'Memory & Persistence Architecture', 'NotebookLM: Gemini RAG', 'A technical clarification that NotebookLM is an application layer on top of Gemini 1.5 Pro, optimized for RAG over large datasets (millions of tokens).', 'notebooklm, gemini, rag, audio-overview, clarification', 'Gemini 1.5 Pro engine, specialized large-scale RAG architecture, grounded Audio Overview generation, high-token capacity.'),
    ('https://www.reddit.com/r/notebooklm/comments/1qhd4vt/notebooklm_llm_logs_as_translation_layer_for/', 'Guides & Industry Trends', 'Cognitive Translation Layer', 'A workflow using personal LLM conversation logs as NotebookLM sources to explain new technical concepts using the user\'s own established vocabulary.', 'notebooklm, learning, vocabulary, personal-logs, translation', 'Personalized learning logs, metaphor-based explanation, high-fidelity technical mapping, introspective journaling sources.'),
    ('https://www.reddit.com/r/notebooklm/comments/1qnkbmj/nblm_query_google_notebooklm_from_your_ai_coding/', 'Connectivity & Interoperability (MCP/A2A)', 'nblm: AI Coding Connector', 'An MCP server and skill that connects AI coding agents directly to NotebookLM for zero-hallucination querying of specific documentation and research.', 'mcp, notebooklm, coding-agent, integration, nblm', 'Zero-hallucination documentation querying, direct file/URL/YouTube uploads, terminal-based NLM control, automated artifact generation.'),
    ('https://www.reddit.com/r/notebooklm/comments/1qs7v2s/notebooklm_mcp_cli_v027_unified_package_file/', 'Infrastructure & Proxy Layers', 'Unified NLM-MCP Package', 'A major refactor merging the NotebookLM CLI and MCP server into a single package, enabling direct file uploads via HTTP and multi-profile authentication.', 'mcp, cli, refactor, automation, deployment', 'Direct HTTP file uploads (bypass browser), Multi-profile Google auth, unified CLI/MCP binary, programmatic artifact downloading.')
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
print('Successfully injected batch 89.')