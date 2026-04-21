import sqlite3

data = [
    ('https://metamcp.com/', 'Connectivity & Interoperability (MCP/A2A)', 'MetaMCP: Proxy Router', 'A unified proxy router that aggregates multiple MCP servers into a single connection for clients, featuring GUI-based management and workspace isolation.', 'mcp, gateway, proxy, orchestration, management', 'Unified multi-server proxy endpoint, namespace isolation to prevent tool conflicts, visual App Store installation, local-first SDK encryption.'),
    ('https://plugged.in/', 'Connectivity & Interoperability (MCP/A2A)', 'Plugged.in: MCP Hub', 'An enterprise-grade MCP Hub that aggregates tool servers, providing universal transport compatibility (STDIO/SSE/HTTP) and built-in cross-agent persistent memory.', 'mcp, gateway, memory, rag, enterprise', 'Universal transport bridging (STDIO to HTTP/SSE), workspace-scoped persistent memory, built-in RAG v2 Document Exchange, integrated multi-model testing playground.'),
    ('https://old.reddit.com/r/mcp/comments/1p1lpz2/what_if_you_create_an_mcp_server_that_exposes_mcp', 'Agent Orchestration & Workflow', 'Autonomous Loop Patterns', 'The 2026 evolution of "keep agent running in a loop" scripts, replacing simple loops with Durable Execution (Temporal/Inngest) and autonomous Evaluator-Optimizer termination.', 'orchestration, autonomy, durable-execution, workflow, script', 'Durable Execution state recovery (Temporal), Evaluator-Optimizer termination criteria, Background Tasking (non-blocking subprocesses), Human-in-the-Loop triggers.'),
    ('https://grokcli.io/', 'Connectivity & Interoperability (MCP/A2A)', 'Grok CLI as MCP', 'An MCP integration for the Grok CLI that grants other agents (like Claude or GPT-4) real-time access to X (Twitter) search and Grok\'s native "Raw Mode" reasoning.', 'mcp, grok, xai, search, integration', 'Real-time X (Twitter) social data access, Grok "Raw Mode" unfiltered debugging reasoning, autonomous multi-step web research exposure.')
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
print('Successfully injected batch 159.')