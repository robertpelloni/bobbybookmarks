import sqlite3

data = [
    ('https://asmjit.com/', 'Infrastructure & Proxy Layers', 'AsmJit: Machine Code Gen', 'A premier lightweight C++ library for low-latency machine code generation (x86/A64), critical for building high-performance JIT compilers.', 'asmjit, low-level, cpp, jit, performance', 'Multi-level emitters (Assembler/Builder/Compiler), zero-dependency embedding, W^X security-mapped allocator, type-safe semantic checks.'),
    ('https://awesomeclaude.ai/code-cheatsheet', 'Guides & Industry Trends', 'Claude Code Master Guide', 'A comprehensive technical cheatsheet for Claude Code, covering extension mechanisms (agents/skills/hooks) and architectural best practices like CLAUDE.md.', 'claude-code, cheatsheet, extension, architecture, guide', 'Extension via .claude/agents and /skills, session compaction logic, PreToolUse/PostToolUse hooks, CLAUDE.md grounding paradigm.'),
    ('https://awesome-llm-papers.github.io/tsne-viz.html?y0=1964&y1=2025', 'Guides & Industry Trends', 'AI Research t-SNE Map', 'A visualization mapping thousands of LLM research papers from arXiv into a 2D cluster map using t-SNE embeddings to identify research "white space."', 'research, visualization, llm-papers, t-sne, embeddings', 'Embedding-based 2D clustering, identified research "islands" (RLHF/RAG), interactive temporal filtering (1964-2025), visual analytics for academic discovery.'),
    ('https://arxiv-viz.ianhsiao.xyz/landing', 'Interface & Developer UX', 'arXiv Viz: Research Graphs', 'An AI-powered visual analytics platform that untangles academic literature reviews into interactive citation graphs and step-by-step visual summaries.', 'research, graphs, visualization, arxiv, summarization', 'Interactive citation lineage mapping, AI-powered step-by-step visual summaries, personalized research cluster discovery, spatial academic exploration.')
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
print('Successfully injected batch 109.')