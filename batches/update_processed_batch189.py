import sqlite3

data = [
    ('https://www.allaboutai.com/ai-agents/open-ai-codex-vs-github-copilot-vs-claude', 'Agent Orchestration & Workflow', '2026 Agent Comparison', 'A strategic analysis of the 2026 agentic landscape, ranking Claude Code (80.8% SWE-bench) as the leader in autonomous execution over Copilot and Codex.', 'orchestration, benchmarks, swe-bench, comparison, agents', 'Claude Code 80.8% SWE-bench Verified leader, 1M token context window, multi-agent "Team" standard, Copilot multi-model integration.'),
    ('https://wild-card.ai/deepcontext', 'Connectivity & Interoperability (MCP/A2A)', 'DeepContext: Semantic MCP', 'An MCP server by Wildcard AI that provides high-speed semantic search over large repositories using Tree-sitter AST parsing and incremental indexing.', 'mcp, search, semantic-search, tree-sitter, optimization', 'Tree-sitter AST parsing, 50% faster than standard grep, 40% reduction in token costs, incremental codebase indexing.'),
    ('https://wiki.qt.io/C%2B%2B_reflection_(P2996)_and_moc', 'Guides & Industry Trends', 'C++26 Reflection (P2996)', 'The finalized C++26 reflection standard featuring the `^^` (cat-ears) operator and `std::meta::info` for zero-overhead static introspection.', 'cpp, reflection, p2996, meta-programming, standards', 'Unary `^^` (reflection) operator, `std::meta::info` metadata type, March 2026 final ballot status, Clang/EDG/GCC experimental support.'),
    ('https://winfsp.dev/rel', 'Infrastructure & Proxy Layers', 'WinFsp 2.x: VFS Proxy', 'A high-performance Windows File System Proxy that enables user-mode filesystem development with NTFS parity and a 2026 "no-reboot" installer.', 'windows, vfs, filesystem, fuse, proxy', 'NTFS security/ACL parity, user-mode FUSE compatibility, new "no-reboot" 2.x installer, multi-million install production stability.')
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
print('Successfully injected batch 153.')