import sqlite3

data = [
<<<<<<< HEAD
    ('https://www.reddit.com/r/codex/comments/1q30nd4/gpt52_high_gptcodex52high_and_even_extrahigh/', 'AI Agents & Frameworks', 'GPT-5.2 Codex: XHigh Reasoning', 'A deep analytical mode for complex software engineering that spends 5-10 minutes on internal simulations to catch errors before code generation.', 'codex, gpt-5-2, reasoning-effort, xhigh, agi-adjacent', 'XHigh 5-10m reasoning cycle, internal error-simulation loops, optimized for large-scale refactors, AGI-adjacent coding performance.'),
    ('https://www.reddit.com/r/codex/comments/1qc3x5b/codex_manager_v100_desktop_app_to_manage_openai/', 'Interface & Developer UX', 'Codex Manager: Asset Hub', 'A cross-platform desktop application for centralized management of agent configurations, skills, and Model Context Protocol (MCP) servers.', 'gui, desktop-app, management, mcp, skills', 'Centralized config management, Skill/MCP GUI installer, stacked diff configuration previews, token/rate-limit usage dashboard.'),
    ('https://www.reddit.com/r/codex/comments/1qjapzz/claude_code_cli_uses_way_more_input_tokens_than/', 'Infrastructure & Proxy Layers', 'Codex: Response Compaction', 'A loss-aware context compression mechanism that serializes conversation state into opaque items, enabling 3x higher token efficiency than competitors.', 'optimization, context-compression, token-efficiency, scale, infrastructure', 'Loss-aware context compaction, encrypted state serialization, 3x-4x higher efficiency vs Claude Code, support for virtually infinite sessions.'),
    ('https://www.reddit.com/r/codex/comments/1q60bfz/okay_seriously_worktrees_52_xhigh_mcps_skills_im/', 'Agent Orchestration & Workflow', 'Codex: Worktree Parallelism', 'A standardized orchestration pattern that uses Git Worktrees to provide isolated directories for parallel agent threads sharing a single object database.', 'git-worktrees, parallelism, isolation, orchestration, performance', 'Automated worktree creation (detached HEAD), isolated directory per agent thread, shared global .git object store, automated environment setup scripts.')
=======
    ('https://www.reddit.com/r/Rag/comments/1q4y21e/starting_with_docling/', 'Memory & Persistence Architecture', 'Docling: Structural Parsing', 'An advanced document parsing framework that maps heterogeneous types (PDF/DOCX) into a unified tree-structured data model for high-fidelity RAG.', 'docling, document-intelligence, document-parsing, structural-rag, metadata', 'Unified tree-structured data model, Markdown/JSON export, layout-aware text extraction, hierarchical indexing hooks.'),
    ('https://www.reddit.com/r/Rag/comments/1qhxtt2/chunking_without_document_hierarchy_breaks_rag/', 'Memory & Persistence Architecture', 'Contextual Prefixing Pattern', 'A high-ROI RAG optimization that prepends document hierarchy (Document > Section) to chunks before embedding to prevent "topic identity" loss.', 'rag, optimization, chunking, context-retrieval, accuracy', 'Hierarchical contextual prefixing, reduction of "lost-in-middle" errors, semantic boundary preservation, metadata breadcrumb linking.'),
    ('https://github.com/GrantFlowAI/GrantFlowAI', 'Agent Orchestration & Workflow', 'GrantFlowAI production RAG', 'A production-grade RAG stack blueprint using Litestar, pgvector, and Kreuzberg, focusing on integrated evaluation loops and feedback systems.', 'rag, production-ai, python, pgvector, infrastructure', 'Integrated evaluation layers, Litestar/pgvector backend, automated feedback loops, uv/pnpm monorepo management.'),
    ('https://www.reddit.com/r/Rag/comments/1qynrqv/hierarchical_agentic_rag_knowledge_graph_vector/', 'Memory & Persistence Architecture', 'Tri-Search: Hierarchical RAG', 'A high-scale RAG architecture that fuses Vector Search, Knowledge Graphs, and Reasoning-based routing to achieve massive scale on consumer hardware.', 'graph-rag, rag, hierarchical-routing, search-optimization, tri-search', '3-Address Domain/Topic/Entity routing, Vector/KG/Reasoning fusion (Tri-Search), <400ms latency JSON mode, 600k+ chunk scalability on low-end GPUs.')
>>>>>>> feature/reorg-and-integrate
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
<<<<<<< HEAD
print('Successfully injected batch 72.')
=======
print('Successfully injected batch 70.')
>>>>>>> feature/reorg-and-integrate
