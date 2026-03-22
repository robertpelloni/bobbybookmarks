import sqlite3

data = [
    ('https://blog.cloudflare.com/code-mode-mcp/', 'Connectivity & Interoperability (MCP/A2A)', 'Cloudflare Code Mode', 'A revolutionary paradigm shift where agents write scripts to interact with APIs via a typed SDK, reducing context usage by 99.9%.', 'code-mode, cloudflare, optimization, mcp, context-efficiency', '99.9% Token reduction (1.1M to 1k), multi-step batch execution in one turn, sandboxed Dynamic Worker Loader, constant context footprint.'),
    ('https://blog.palantir.com/securing-agents-in-production-agentic-runtime-1-5191a0715240', 'Infrastructure & Proxy Layers', 'Palantir Agentic Runtime', 'A comprehensive security framework for deploying autonomous agents in mission-critical enterprise environments with strict governance.', 'security, enterprise, governance, k8s, production-ai', 'Rubix (hardened K8s) isolation, JIT credential propagation, Reasoning "flight recorder" audit logs, provenance-based security policies.'),
    ('https://blogs.oracle.com/developers/comparing-file-systems-and-databases-for-effective-ai-agent-memory-management', 'Memory & Persistence Architecture', 'Oracle Memory Analysis', 'A strategic decision framework for selecting between file-systems and databases as the substrate for AI agent long-term memory.', 'memory-architecture, database, filesystem, scaling, enterprise-ai', 'Unified multi-model memory substrate, file-system vs database decision tree, concurrency/auditability benchmarks, low-latency memory retrieval.')
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
print('Successfully injected batch 29.')
