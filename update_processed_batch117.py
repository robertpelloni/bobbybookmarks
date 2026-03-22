import sqlite3

data = [
    ('https://www.reddit.com/r/GoogleAntigravityIDE/comments/1qlerfg/drift_isnt_a_tool_its_your_2026_productivity_hack/', 'Guides & Industry Trends', 'ADD: Alignment-Driven Dev', 'A governance-first productivity hack designed to prevent "Vibe Build Drift" by ensuring every agent-generated code line traces back to a human-approved decision.', 'alignment, governance, add, productivity, trends', 'Directional alignment monitoring, business-decision traceability, anti-drift governance layer, strategic intent enforcement.'),
    ('https://www.reddit.com/r/GoogleAntigravityIDE/comments/1qxuztj/praxis_a_development_framework_that_bridges/', 'Agent Orchestration & Workflow', 'Praxis P3M Bridge', 'A holistic development framework that acts as a bridge between high-level management objectives and ground-level execution using standardized data schemas.', 'praxis, orchestration, methodology, p3m, bridge', 'Four-pillar integration (Knowledge/Methodology/Competence/Maturity), hierarchical synchronization, standardized management schemas, synchronized monitoring/control.'),
    ('https://www.reddit.com/r/GoogleAIStudio/comments/1qa78qj/using_gemini_as_a_multiperspective_simulator_to/', 'AI Agents & Frameworks', 'Adversarial Perspective Sim', 'An experimental AI Studio workflow that treats LLMs as simulators to stress-test ideas by generating multiple conflicting adversarial viewpoints.', 'simulation, adversarial-ai, brainstorming, ai-studio, verification', 'Multi-viewpoint simulation (User/Skeptic/Expert), adversarial prompt stress-testing, decision quality improvement, reduced iteration loops.'),
    ('https://www.reddit.com/r/GoogleAntigravityIDE/comments/1r07o41/idea_versioncontrolling_gemini_with_git_so_the/', 'Memory & Persistence Architecture', 'Git-Based Config Memory', 'A persistence pattern that turns the agent configuration directory into a Git repository to create permanent, machine-independent AI memory.', 'git, memory, configuration, persistence, learning-loop', 'Git-tracked GEMINI.md/skills, dated mistake-correction logging, machine-independent memory sync, auditable behavioral evolution.')
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
print('Successfully injected batch 68.')
