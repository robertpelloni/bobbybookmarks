import sqlite3

data = [
    ('https://docs.letta.com/guides/agents/memory-blocks/', 'AI Agents & Frameworks', 'Letta Memory Blocks', 'The core abstraction for agentic context management in Letta, using structured, agent-editable blocks for persistent state.', 'letta, memory-blocks, context-management, memgpt, persistence', 'Structured Label/Value schema, autonomous agent self-editing, persistent state across sessions, XML-prompt implementation.'),
    ('https://github.com/letta-ai/letta-code', 'AI Agents & Frameworks', 'Letta Code Harness', 'A memory-first coding harness and CLI tool that turns LLMs into long-lived coworkers with git-backed persistent context.', 'letta, coding-agent, git-backed, persistence, cli', 'Git-backed context versioning, multi-agent concurrent work, #1 Terminal-Bench ranking, model-agnostic (Claude/GPT/Gemini).'),
    ('https://github.com/supermemoryai/supermemory', 'Infrastructure', 'SuperMemory Framework', 'An open-source personal memory framework that endows AI applications with long-term memory via hybrid search and extensive connectors.', 'memory, rag, personal-ai, connectors, infrastructure', 'Hybrid personalized RAG search, 50ms retrieval latency, auto-syncing connectors (Drive/Gmail/Notion), multi-modal content extraction (OCR/Transcription).')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level)
        VALUES (?, ?, ?, ?, ?, ?, 'deep')
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='deep'
    ''', (url, cat, sd, ld, tags, mf))
conn.commit()
conn.close()
print('Successfully injected batch 20.')
