import sqlite3

data = [
    ('https://opencode.ai/docs/ecosystem/', 'AI Agents & Frameworks', 'OpenCode Ecosystem', 'An open-source, local-first terminal AI coding agent ecosystem featuring a pluggable architecture for sandboxing, security, and PTY management.', 'opencode, local-first, terminal-ai, plugins, ecosystem', '75+ Model support, pluggable PTY/Security/Sandboxing, type-safe JS/TS SDK, direct LSP integration, client-server architecture.'),
    ('https://opencode.ai/docs/zen/#privacy', 'Infrastructure & Proxy Layers', 'OpenCode Zen Privacy', 'A curated, US-hosted AI gateway specifically optimized for coding agents with a strict zero-retention policy for user data.', 'privacy, gateway, zero-retention, compliance, enterprise-ai', 'Zero-retention data policy, pre-optimized provider configurations, US-based hosting, direct EU/local endpoint fallback support.'),
    ('https://openspec.dev/', 'AI Agents & Frameworks', 'OpenSpec: Agent Standard', 'A "Spec-Driven Development" (SDD) framework that standardizes how AI agents communicate and execute tasks via structured filesystem-based files.', 'spec-driven, standard, inter-agent, portability, automation', 'Structured project/task/spec files, delta-based spec versioning (ADDED/MODIFIED), tool-agnostic handoff support, context loss prevention.'),
    ('https://quesma.com/blog/ghidra-mcp-unlimited-lives/', 'Connectivity & Interoperability (MCP/A2A)', 'Ghidra MCP: Binary AI', 'A Model Context Protocol server that bridges AI reasoning with the Ghidra suite for automated binary annotation and reverse engineering.', 'mcp, reverse-engineering, security, ghidra, binary-analysis', 'Automated function annotation, structural normalized hashing, malware pattern identification, one-shot binary markups.')
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
print('Successfully injected batch 54.')
