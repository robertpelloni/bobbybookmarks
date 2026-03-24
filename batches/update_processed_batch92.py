import sqlite3

data = [
    ('https://www.fiddler.ai/agentic-observability', 'Guides & Industry Trends', 'Fiddler: Agentic Observability', 'An enterprise control plane for tracking agent reasoning chains, handoff failures, and "Agentic Drift" via high-dimensional UMAP visualizations.', 'observability, monitoring, agentic-drift, enterprise-ai, traceability', '3D UMAP anomaly detection, reasoning lineage tracking, Jensen-Shannon Divergence metrics, multi-agent handoff monitoring.'),
    ('https://www.codebuff.com/', 'Agent Orchestration & Workflow', 'Codebuff Multi-Agent System', 'An open-source system that orchestrates specialized agents (Explorer/Planner/Editor) to manage large-scale "brownfield" codebases.', 'orchestration, multi-agent, code-indexing, typescript-sdk, openrouter', 'Specialized agent roles, human-readable `knowledge.md` memory, whole-codebase mapping, model-agnostic OpenRouter support.'),
    ('https://www.coderabbit.ai/cli', 'Interface & Developer UX', 'CodeRabbit CLI', 'A "CLI-first" AI review system designed to provide senior-level feedback on local, uncommitted diffs to maintain developer flow state.', 'cli, code-review, automation, productivity, flow-state', 'Line-by-line local diff reviews, one-click CLI fixes, AST-based logic analysis, quality gate for coding agents.'),
    ('https://www.humanlayer.dev/blog/brief-history-of-ralph', 'Guides & Industry Trends', 'The Ralph Wiggum Technique', 'A brute-force autonomous coding methodology that uses "Contextual Pressure Cooking" to force agents to escape error loops via persistent failure feedback.', 'philosophy, autonomous-coding, self-healing, brute-force, trends', '5-line Bash origin, "Naive Persistence" philosophy, stack-trace pressure cooking, self-healing build-fix automation.')
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
print('Successfully injected batch 58.')
