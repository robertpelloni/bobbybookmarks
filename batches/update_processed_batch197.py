import sqlite3

data = [
    ('https://smithery.ai/', 'Connectivity & Interoperability (MCP/A2A)', 'Smithery: MCP Hub', 'The premier "npm for AI agents," acting as a centralized registry and managed cloud host for thousands of Model Context Protocol (MCP) servers.', 'mcp, registry, orchestration, infrastructure, connectivity', '3,000+ managed MCP servers, one-click CLI deployment (`npx smithery setup`), managed OAuth credential state, universal IDE compatibility.'),
    ('https://smooth-operator.online/', 'Agent Orchestration & Workflow', 'Smooth Operator: Autonomy', 'A workflow framework that transitions AI assistants into "autonomous teammates" capable of executing multi-step goals with enterprise governance and HITL gates.', 'orchestration, operator, autonomy, workflow, enterprise', 'Autonomous multi-step execution, Human-in-the-Loop (HITL) review gates, role-based access control (RBAC), multi-agent coordination (Scout/Coder).'),
    ('https://simonwillison.net/2025/Oct/5/parallel-coding-agents', 'Agent Orchestration & Workflow', 'Parallel Coding Workflow', 'Simon Willison\'s strategic methodology for running multiple autonomous coding agents in parallel across separate git worktrees to maximize human review leverage.', 'workflow, parallel-agents, orchestration, git-worktrees, efficiency', 'Parallel git-worktree agent execution, "Scout" vs "Implementer" agent roles, shifting bottleneck from generation to human code review.'),
    ('https://simoncoenen.com/blog/programming/PakFiles', 'Guides & Industry Trends', 'Pak Files: VFS Strategy', 'A technical deep-dive by Simon Coenen into using Virtual File Systems (VFS) and binary "Pak" blobs for high-performance asset management and disk seek optimization.', 'vfs, architecture, performance, file-systems, game-dev', 'Header-first encryption/metadata, per-file internal compression, random memory access without full decompression, VFS path abstraction.')
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
print('Successfully injected batch 157.')