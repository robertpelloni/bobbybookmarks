import sqlite3

data = [
    ('https://agent.ii.inc/', 'Agent Orchestration & Workflow', 'II-Agent (Sovereign AI)', 'An open-source, auditable autonomous assistant framework focusing on data privacy and cost control through a BYOK model.', 'sovereign-ai, autonomous, byok, open-source, research-agent', 'Multimodal file/web synthesis, citation-backed reporting, specialized implementer agents, modular skill-based architecture.'),
    ('https://ai-sdk.dev/', 'Infrastructure & Proxy Layers', 'Vercel AI SDK', 'The industry-standard TypeScript toolkit for building AI-powered web applications with a unified, provider-agnostic abstraction layer.', 'sdk, vercel, typescript, mcp, multi-model', 'Unified model abstraction (generateText/streamText), native MCP support, framework-agnostic UI hooks, automated RAG middleware.'),
    ('https://blog.arcade.dev/mcp-tool-patterns', 'Connectivity & Interoperability (MCP/A2A)', 'Arcade MCP Tool Patterns', 'A seminal research piece defining 54 critical design patterns for building reliable and agent-usable Model Context Protocol tools.', 'mcp, design-patterns, tool-calling, idempotency, best-practices', 'Idempotency for retries, Tool Federation via Gateway pattern, Atomic vs Orchestrated tool design, CLI-first agent interaction.'),
    ('https://blog.brokk.ai/why-gemini-3-flash-is-the-model-openai-is-afraid-of/', 'Guides & Industry Trends', 'Gemini 3 Flash Analysis', "Technical analysis of Google's high-performance, low-cost 'workhorse' model, demonstrating frontier-level intelligence at 5x lower cost.", 'gemini, performance, benchmarking, cost-optimization, sw-bench', '78% SWE-bench Verified score, 218 tokens/sec throughput, 5x cost reduction vs flagships, optimal tradeoff for 80% of dev tasks.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 9) for d in data]:
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
print('Successfully injected batch 28.')
