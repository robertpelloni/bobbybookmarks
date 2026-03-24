import sqlite3

data = [
    ('https://www.reddit.com/r/AugmentCodeAI/comments/1qxpx7u/augments_context_engine_is_now_available_for_any/', 'Context Engineering & Isolation', 'Augment Context Engine MCP', 'A universal context engine that brings cross-repo semantic indexing to any MCP-capable agent (Cursor/Claude Code/Zed).', 'context-engine, mcp, semantic-search, organization-context, real-time-indexing', 'Multi-IDE support (Cursor/Zed/Roo), real-time organizational indexing, organizational-scale semantic search, 70-80% code quality improvement.'),
    ('https://www.reddit.com/r/AugmentCodeAI/comments/1r6oxd7/holographic_memory/', 'Memory & Persistence Architecture', 'Holographic/Observational Memory', 'A compression mechanism that treats the context window as layered storage, using background "Reflector" agents to achieve 40x compression.', 'memory-compression, context-engineering, reflector-agents, observational-memory, optimization', '5-40x Context compression ratios, temporal awareness preservation, background reflection loops, elimination of RAG "temporal blindness."'),
    ('https://www.reddit.com/r/BMAD_Method/comments/1q9epo8/i_created_a_tool_that_automates_the_bmad_method/', 'Agent Orchestration & Workflow', 'BMAD Method Automation CLI', 'A community-built Golang CLI that automates the full BMAD story lifecycle, from requirements doc creation to GitHub deployment.', 'bmad, agile, automation, cli, software-factory', 'Yaml-based sprint status tracking, automated story-to-deploy pipeline, worker/reviewer agent pairs, git-backed task persistence.'),
    ('https://www.reddit.com/r/AugmentCodeAI/comments/1qyrjsq/the_end_of_linear_work/', 'Guides & Industry Trends', 'Non-Linear Spec Infrastructure', 'A paradigm shift analysis arguing that the "Spec is the Product" in a world where coordination across parallel agents is the main bottleneck.', 'philosophy, non-linear-work, coordination, spec-driven, software-architecture', 'Parallel agent fleet orchestration, Spec-as-Infrastructure alignment, move from implementation to intent, automated integration verification.')
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
print('Successfully injected batch 65.')
