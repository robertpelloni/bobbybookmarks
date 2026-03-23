import sqlite3

data = [
    ('https://www.reddit.com/r/codex/comments/1ppy057/introducing_gpt52codex/', 'AI Agents & Frameworks', 'GPT-5.2 Codex: Agentic Core', 'A frontier-class model optimized for autonomous task-grinding and terse precision, featuring a dedicated experimental Agent Mode sandbox.', 'codex, gpt-5-2, agent-mode, task-grinding, precision', 'Autonomous task persistence, terse instruction following, dedicated Agent Mode sandbox, optimized for multi-hour implementation loops.'),
    ('https://www.reddit.com/r/codex/comments/1przfmn/0770_shell_snapshotting_quick_analysis_of_the/', 'Infrastructure & Proxy Layers', 'Shell Snapshotting (Zero-Latency)', 'A context-preservation mechanism that freezes the execution environment at session start, bypassing redundant login scripts for millisecond shell access.', 'infrastructure, optimization, context-preservation, shell, performance', 'Environment freezing (env/alias/func), zero-latency tool calls, deterministic shell state, bypasses .zshrc/.bash_profile overhead.'),
    ('https://www.reddit.com/r/clawdbot/comments/1r61erx/i_migrated_42_skills_and_56_agents_from_claude/', 'Agent Orchestration & Workflow', 'Metadata-Driven Routing', 'A scalable orchestration pattern using strict YAML frontmatter and intent-mapping to prevent "specialist invisibility" in multi-agent swarms.', 'orchestration, metadata, skill-discovery, intent-mapping, scaling', 'Strict YAML skill metadata, prioritized Intent Mapping (Explicit > Keyword > Fallback), model-driven routing validation, 50+ agent fleet coordination.'),
    ('https://www.reddit.com/r/codex/comments/1pu6ja7/total_recall_rag_search_across_all_your_claude/', 'Memory & Persistence Architecture', 'Total Recall: Conversational RAG', 'A cross-session memory layer that implements RAG search across all previous agent/user conversations to retain the technical history of discovery.', 'memory-architecture, rag, cross-session, persistence, conversation-history', 'Conversational RAG search, multi-provider context sync (Claude/Codex), persistent technical rationale tracking, zero-loss project onboarding.')
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
print('Successfully injected batch 75.')
