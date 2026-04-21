import sqlite3

data = [
    ('https://www.reddit.com/r/opencodeCLI/comments/1rhaewu/sdd_pilot_a_specdriven_development_framework_now/', 'Agent Orchestration & Workflow', 'SDD Pilot: AI Workflow', 'A disciplined, phase-by-phase framework (Specify -> Plan -> Implement -> QC) for AI-native development, using specialized agents for pre-coding research.', 'workflow, sdd, spec-driven, orchestration, quality-gate', 'Specify-Plan-Implement-QC loop, specialized multi-agent roles, mandatory online research phase, quality gates for skip prevention.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1ri6lk5/making_vibe_coding_safe_a_git_metalayer_that/', 'Infrastructure & Proxy Layers', 'Git Metalayer for Vibe Coding', 'A proposed safety layer for rapid AI iteration that automates atomic commits, branch management, and state tracking to prevent requirement drift.', 'vibe-coding, git, safety, atomic-commits, state-tracking', 'Automated atomic commit management, branch isolation for experiments, reversible state tracking, protection against orphan functions.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1rkhdk3/ai_glossary_fast_clientside_search_a_semantic/', 'Interface & Developer UX', 'AI Glossary: Semantic Search', 'A static client-side terminology glossary featuring a MDS-projected semantic term map for visualizing conceptual relationships between AI topics.', 'glossary, semantic-search, mds, static-site, visualization', 'Static client-side execution, MDS-projected 2D layout, semantic embedding-based search, Conceptual relationship mapping.'),
    ('https://www.reddit.com/r/perplexity_ai/comments/1qyo0rf/i_put_the_new_perplexity_deep_research_against/', 'Guides & Industry Trends', 'Perplexity Deep Research Analysis', 'A benchmark analysis ranking Perplexity as a top speed-optimized search tool, though trailing OpenAI/Gemini in high-stakes academic/math reasoning.', 'perplexity, search, reasoning, benchmarks, research', 'Proprietary search infrastructure, speed-optimized deep search, Sonar model fine-tuning, competitive multi-agent research performance.')
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
print('Successfully injected batch 95.')