import sqlite3

data = [
    ('https://github.com/openai/symphony?tab=readme-ov-file', 'Agent Orchestration & Workflow', 'OpenAI Symphony: Work-Runs', 'An autonomous project management framework that transforms issue tracking into scalable implementation runs, handling coding, CI, and PR merging.', 'orchestration, symphony, openai, issue-to-pr, automation', 'Linear issue-to-PR pipeline, autonomous CI/CD verification, Proof of Work artifact generation, Elixir-based multi-language spec.'),
    ('https://github.com/BeehiveInnovations/pal-mcp-server', 'Agent Orchestration & Workflow', 'PAL: Personal AI Layer', 'An orchestration MCP server providing a CLI-to-CLI bridge (clink) and specialized tools like apilookup and challenge to ensure context continuity.', 'mcp, orchestration, clink, documentation, logic-engine', '`clink` CLI-to-CLI bridge, apilookup documentation force, `challenge` logic verifier, Gemini 1M context delegation.'),
    ('https://github.com/docker/mcp-gateway', 'Infrastructure & Proxy Layers', 'Docker MCP Gateway', 'A centralized proxy for orchestrating containerized MCP servers, providing restricted host privileges, secret injection, and PII payload interceptors.', 'mcp, gateway, docker, security, infrastructure', 'Containerized MCP isolation, secure Docker Desktop secret injection, payload PII interceptors, dynamic container tool discovery.'),
    ('https://github.com/supermemoryai/supermemory-mcp', 'Memory & Persistence Architecture', 'Supermemory: Cross-Agent Recall', 'A universal memory layer that provides AI assistants with persistent, searchable embeddings of conversations and web content across different platforms.', 'memory, persistence, vector-search, mcp, second-brain', 'Cross-platform memory hub, semantic embedding-based recall, OAuth security, project-scoped memory organization.')
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
print('Successfully injected batch 103.')