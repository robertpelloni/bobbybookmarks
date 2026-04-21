import sqlite3

data = [
    ('https://github.com/nokodo-labs/os1', 'AI Agents & Frameworks', 'OS1: Open Source Platform', 'A comprehensive open-source AI platform providing a private, polished alternative to ChatGPT with deep enterprise-grade controls and hybrid RAG search.', 'os1, open-source, platform, rag, enterprise', 'Hybrid RAG & agentic web search, automated agentic context extraction (terminals/files), Jinja execution template manager, enterprise ACL/security.'),
    ('https://github.com/PatrickSys/codebase-context', 'Context Engineering & Isolation', 'Codebase-Context: Preflight', 'An MCP server functioning as a local-first "second brain" that provides AI agents with codebase-specific "preflight" reports to prevent hallucinated refactoring.', 'context-engineering, mcp, rag, architecture, validation', 'Context Guardrails (warns agents of weak search results), "Preflight" editing risk reports, automated pattern/convention detection, definition-first hybrid ranking.'),
    ('https://www.reddit.com/r/moltiverse/comments/1rp4z7q/opensourcing_openodus_a_lightweight_faissbased', 'Memory & Persistence Architecture', 'OpenOdus: FAISS RAG', 'A lightweight, open-source RAG gateway using FAISS for local vector similarity search, designed to reduce API costs by feeding precise context to smaller local models.', 'rag, faiss, local-llm, optimization, vector-search', 'FAISS local vector similarity search, API cost optimization via precise context injection, 100% on-premise privacy focus.'),
    ('https://www.reddit.com/r/singularity/comments/1rqymbn/anthropic_recursive_self_improvement_is_here_the', 'Guides & Industry Trends', 'Anthropic: Recursive R&D', 'A viral discussion on the reality of recursive self-improvement in AI, noting that 70-90% of the code for Anthropic\'s future models is now written autonomously by Claude.', 'recursion, anthropic, singularity, self-improvement, research', '70-90% autonomous model R&D code generation, compression of release cycles (months to weeks), fully automated AI research roadmap (2027 estimate).')
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
print('Successfully injected batch 188.')