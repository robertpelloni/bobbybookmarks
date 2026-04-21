import sqlite3

data = [
    ('https://github.com/cyclotruc/gitingest', 'Context Engineering & Isolation', 'Gitingest: Repo Grounding', 'A foundational tool for grounding LLMs in codebase context by transforming Git repositories into structured, prompt-friendly text digests.', 'git, context-engineering, grounding, optimization, ingest', 'URL-to-digest conversion (replace hub with ingest), smart LLM-friendly formatting, real-time token counting, browser extension support.'),
    ('https://github.com/danny-avila/LibreChat', 'Agent Orchestration & Workflow', 'LibreChat: Agentic Stack', 'A comprehensive multi-agent platform featuring app-agnostic agents, deep MCP integration, and an open-source Code Interpreter API (2026).', 'orchestration, multi-agent, mcp, code-interpreter, framework', 'Multi-agent collaboration framework, native MCP server management, open-source Code Interpreter API, intelligent conversation summarization.'),
    ('https://github.com/DS4SD/docling', 'Memory & Persistence Architecture', 'Docling: Smart Documents', 'An advanced document parsing framework (IBM) utilizing the Heron layout model and a dedicated MCP server for agentic document understanding.', 'docling, document-parsing, rag, mcp, ibm', 'Heron layout parsing model, agentic MCP server integration, expanded format support (XBRL/LaTeX), pluggable VLM support (SmolDocling).'),
    ('https://github.com/elysiajs/elysia', 'Infrastructure & Proxy Layers', 'ElysiaJS: Bun Performance', 'A high-performance TypeScript framework optimized for the Bun runtime, featuring the Sucrose JIT compiler and automatic OpenAPI generation.', 'typescript, bun, performance, jit, backend', 'Sucrose JIT compiler, 2x faster than competition benchmarks, automatic type inference/validation, unified OpenAPI/Swagger generation.')
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
print('Successfully injected batch 129.')