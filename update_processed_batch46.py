import sqlite3

data = [
    ('https://github.com/pedramamini/Maestro', 'AI Agents & Frameworks', 'Maestro Agent Fleet', 'A cross-platform desktop application designed to orchestrate a fleet of AI coding agents through isolated sessions and git worktrees.', 'maestro, orchestration, automation, worktrees, productivity', 'Compact & Continue context management, Markdown-based task playbooks, parallel agent execution, automated multi-project handoffs.'),
    ('https://www.conductor.build/', 'AI Agents & Frameworks', 'Conductor Team Orchestrator', 'A Mac-native interface for running parallel AI agent teams and an enterprise platform for Answer Engine Optimization (AEO).', 'conductor, team-orchestration, aeo, enterprise, mac-app', 'Isolated worktree automation, Linear/Jira ticket-to-PR integration, Topical Authority Maps for AEO, AI Content Scoring.'),
    ('https://github.com/oraios/serena', 'Development Tools & Libraries', 'Serena Semantic Toolkit', 'An open-source toolkit providing AI agents with symbol-level code retrieval and editing tools, acting as an IDE for LLMs.', 'serena, semantic-code, lsp, mcp, symbols', 'Symbol-level find/insert tools, deep LSP integration, standalone MCP server, framework-agnostic architecture.'),
    ('https://github.com/Muvon/octocode', 'Development Tools & Libraries', 'Octocode GraphRAG', 'A semantic codebase utility that utilizes GraphRAG and knowledge graphs to provide AI agents with comprehensive memory of large repositories.', 'octocode, graphrag, indexing, semantic-search, context', 'Intelligent knowledge graph mapping, Detective Engine reasoning thread, LanceDB high-performance vector storage, automated index optimization.')
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
print('Successfully injected batch 13.')
