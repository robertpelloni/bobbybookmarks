import sqlite3

data = [
    ('https://venturebeat.com/orchestration/mits-new-recursive-framework-lets-llms-process-10-million-tokens-without', 'Context Engineering & Isolation', 'MIT Recursive Language Models', 'A framework enabling agents to reason over 10M+ tokens by treating the prompt as an external environment and recursively self-calling over data snippets.', 'recursive-llm, long-context, systems-architecture, mit, optimization', 'Recursive self-calling mechanism, "out-of-core" prompt handling, 91% accuracy on massive context tasks, zero-retraining long-context reasoning.'),
    ('https://vercel.com/blog/how-we-made-v0-an-effective-coding-agent', 'Agent Orchestration & Workflow', 'Vercel v0: Vertical Integration', 'An analysis of how deep vertical integration with the Vercel platform and deterministic autofixers turned v0 into a production-grade coding agent.', 'v0, vercel, vertical-integration, self-healing, deployment', 'LLM Suspense streaming layer, real-time deterministic autofixers, direct production repo ingestion, multi-step agentic pipeline.'),
    ('https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills', 'AI Agents & Frameworks', 'Anthropic Agent Skills', 'A modular expertise framework using "Progressive Disclosure" to load procedural knowledge only when relevant, reducing token usage by 70-90%.', 'skills, anthropic, optimization, context-efficiency, modularity', 'SKILL.md structured instructions, bash-read progressive loading, 90% token reduction per session, portable agent expertise.'),
    ('https://www.augmentcode.com/blog/generating-tech-debt-at-the-speed-of-light', 'Guides & Industry Trends', 'Augment: Comprehension Debt', 'An analysis of "Comprehension Debt"—the gap between AI-generated code and human understanding—and the need for architectural context engines.', 'tech-debt, comprehension-debt, software-architecture, quality-gate, trends', 'Comprehension vs Technical debt analysis, "LGTM" reflex risk mitigation, edge-aware context engines, system-wide architectural coherence.')
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
print('Successfully injected batch 57.')
