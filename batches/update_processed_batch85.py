import sqlite3

data = [
    ('https://nadh.in/blog/code-is-cheap/', 'Guides & Industry Trends', 'Code is Cheap (Kailash Nadh)', 'A philosophical analysis of the commoditization of coding, arguing that value has shifted from implementation to "The Talk" (intent and architecture).', 'philosophy, code-is-cheap, architecture, intent, verification-debt', 'Commoditization of syntax, move from implementer to architect, "Verification Debt" warning, high-leverage intent definition.'),
    ('https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/', 'Guides & Industry Trends', 'The AI User Bifurcation', 'An analysis of the emerging productivity gap between autonomous agent "Power Users" and limited "Enterprise Chat" users.', 'trends, productivity, agent-orchestration, vibe-coding, enterprise-ai', '90% Cost reduction for power users, "Super Manager" agent orchestration, enterprise IT constraints vs independent speed, bifurcation of dev skills.'),
    ('https://marginlab.ai/blog/the-problem-with-coding-benchmarks/', 'Guides & Industry Trends', 'Coding Benchmark Volatility', 'Technical research proving that AI models have "bad days," with 10-15% daily performance swings due to non-determinism and backend updates.', 'benchmarks, reliability, non-determinism, tracking, sw-bench', 'Daily statistical performance tracking, 10-15% model performance variance, documented Claude Code degradation (4.1% in 30 days), need for dynamic evals.'),
    ('https://danielmiessler.com/blog/Personal_AI_Infrastructure', 'AI Agents & Frameworks', 'Miessler PAI Framework (v3.0)', 'A 6-layer scaffolding framework (TELOS, Memory, Effort Levels, Skills, Context, Format) for turning LLMs into personalized assistants.', 'framework, architecture, personalization, memory, skills', 'Multi-layered memory (Episodic/Semantic), 8 effort levels with completion gates, 39+ modular skill library, Tiered Context architecture (Always-on vs On-demand).')
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
print('Successfully injected batch 51.')
