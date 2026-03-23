import sqlite3

data = [
    ('https://venturebeat.com/ai/chinese-researchers-unveil-memos-the-first-memory-operating-system-that-gives-ai-human-like-recall', 'Memory & Persistence Architecture', 'MemOS: Memory Operating System', 'A foundational research framework (Shanghai Jiao Tong University) that treats memory as a unified resource via metadata-rich "MemCubes."', 'memory, architecture, memos, persistence, research', 'Standardized MemCubes (content+metadata), cross-platform memory migration, 159% boost in temporal reasoning, unified short/long-term structure.'),
    ('https://v0.app/', 'Interface & Developer UX', 'v0: Agentic Builder', 'Vercel\'s 2026 evolution of v0 into a full-stack agentic platform capable of autonomous planning, debugging, and existing codebase refactoring.', 'vercel, v0, full-stack, automation, orchestration', 'Autonomous agentic workflows, existing codebase (GitHub) integration, shadcn/ui React generation, integrated Supabase backend sync.'),
    ('https://vectorvfs.readthedocs.io/en/latest', 'Memory & Persistence Architecture', 'VectorVFS: Filesystem RAG', 'A lightweight Python library that turns standard Linux filesystems into vector databases by storing embeddings directly in file extended attributes (xattrs).', 'filesystem, rag, xattrs, local-first, metadata', 'Zero-overhead indexing via xattrs, native Linux VFS integration, multimodal support (Meta PE), 100% local/offline execution.'),
    ('https://vikrampawar.github.io/2025/06/14/claude-code-vs-github-copilot-a-week-that-changed-my-workflow.html', 'Guides & Industry Trends', 'Claude Code: Autonomous Shift', 'A workflow analysis comparing Claude Code\'s autonomous delegation ("Fix all lint errors") to GitHub Copilot\'s reactive inline assistance.', 'claude-code, copilot, orchestration, productivity, audit', 'Task-level autonomous delegation, terminal/test execution loops, Sonnet 3.5 reasoning precision, security audit vs adversarial framing analysis.')
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
print('Successfully injected batch 152.')