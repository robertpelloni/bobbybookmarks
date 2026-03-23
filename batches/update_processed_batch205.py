import sqlite3

data = [
    ('https://www.osohq.com/post/right-approach-to-authorization-in-rag', 'Guides & Industry Trends', 'Oso: RAG Authorization', 'A 2026 security architecture standard defining "Partition-Level Isolation" within the retrieval layer to prevent cross-tenant data leakage and agentic goal hijacking.', 'security, rag, authorization, architecture, oso', 'Partition-Level vector isolation, metadata-based query filtering, prevention of "Trust Paradox" LLM leaks, mitigation of retrieval-based goal hijacking.'),
    ('https://www.patronus.ai/blog/announcing-the-first-multimodal-llm-as-a-judge', 'AI Agents & Frameworks', 'Patronus: Multimodal Judge', 'The industry\'s first dedicated Multimodal LLM-as-a-Judge, specifically designed to evaluate image-to-text generation and detect visual caption hallucinations.', 'evaluation, multimodal, vision, hallucination-detection, patronus', 'Visual caption hallucination detection, Spatial/Grid awareness analysis, native OCR validation, Gemini-powered objective backbone.'),
    ('https://www.philschmid.de/context-engineering', 'Context Engineering & Isolation', 'Context Engineering: Phil Schmid', 'A foundational 2026 shift from Prompt Engineering to Context Engineering, focusing on "Agent Harnesses" that manage state, compaction, and memory isolation.', 'context-engineering, architecture, optimization, memory, state-management', 'Context Compaction (noise reduction), Agent Harness architectural pattern, State offloading to persistent disk, modular "build-to-delete" design.'),
    ('https://www.ragie.ai/', 'Memory & Persistence Architecture', 'Ragie.ai: RAG-as-a-Service', 'A fully managed "Plaid for AI" RAG platform featuring an Agentic Retrieval engine, white-labeled SaaS connectors, and a context-aware MCP server.', 'rag, mcp, infrastructure, document-intelligence, api', 'Agentic Retrieval engine (self-checking), context-aware MCP server, Ragie Connect white-label auth, high-speed 10k+ page PDF parsing.')
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
print('Successfully injected batch 165.')