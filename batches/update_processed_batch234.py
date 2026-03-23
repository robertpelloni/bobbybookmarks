import sqlite3

data = [
    ('https://openai.com/index/equip-responses-api-computer-environment/', 'Agent Orchestration & Workflow', 'OpenAI: Computer Environment', 'The evolution of OpenAI\'s Responses API into a task-execution agent runtime, providing models with a secure, full Unix terminal inside an isolated container.', 'openai, orchestration, container, shell, workflow', 'Full Unix terminal access (Node.js/Go/Java/Ruby), Native Context Compaction (server-side token compression), Egress Proxy (domain allowlists), persistent session filesystem.'),
    ('https://github.com/jkerdels/dependency-graph-mcp', 'Context Engineering & Isolation', 'Dependency-Graph-MCP', 'An MCP server functioning as a specialized analysis engine to generate dependency graphs (JSON/DOT) and detect architectural "deadlocks" across codebases.', 'mcp, context-engineering, graph-rag, architecture, dependencies', 'Multi-language support (TS/JS/C#/Python), DOT format visual rendering, architectural debt scoring, circular dependency deadlock detection.'),
    ('https://kunnas.com/articles/the-hypercodex', 'Memory & Persistence Architecture', 'The Hypercodex (Kunnas)', 'A meta-documentation framework proposing a "master semantic index" for agentic workflows, enabling cross-model portability of learned skills and context.', 'memory, persistence, context-management, architecture, standardization', 'Cross-model portability of learned skills, semantic "master index" for just-in-time context loading, hyper-graph symbol linking.'),
    ('https://www.reddit.com/r/mcp/comments/1rrviz4/perplexity_drops_mcp_cloudflare_explains_why_mcp/', 'Guides & Industry Trends', 'Perplexity/Cloudflare vs MCP', 'A 2026 industry debate where major players (Perplexity, Cloudflare) distance themselves from MCP in favor of "Code Mode" due to token waste and security gaps.', 'mcp, industry-trends, code-mode, optimization, architecture', 'Critique of MCP token waste (JSON-RPC verbosity), shift toward "Code Mode" (agents write code that calls APIs directly), Perplexity drops MCP for REST/CLIs.'),
    ('https://morgin.ai/articles/ablation-vs-heretic-vs-obliteratus.html', 'AI Agents & Frameworks', 'Uncensored Models: Ablation', 'A technical comparison of techniques (Ablation, Heretic, Obliteratus) used to remove safety alignments from local LLMs without retraining.', 'local-llm, safety, alignment, ablation, fine-tuning', 'Ablation (orthogonalizing refusal directions), Heretic (automated TPE-based Optuna parameter optimization), Obliteratus (brute-force layer-wise unfiltering).')
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
print('Successfully injected batch 194.')