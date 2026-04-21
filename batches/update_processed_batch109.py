import sqlite3

data = [
    ('https://www.reddit.com/r/ClaudeCode/comments/1pzyyps/i_built_working_memory_for_claude_code_open/', 'Memory & Persistence Architecture', 'Claude-Cognitive: Working Memory', 'A memory substrate that mimics human attention dynamics, categorizing context into Hot/Warm/Cold states to achieve 95% token savings.', 'working-memory, context-engineering, salience-scoring, optimization, cognitive-ai', 'Hot/Warm/Cold attention scoring, automated context eviction, headers-only "Warm" awareness, 95% token reduction on cold starts.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1q1lmok/the_context_continuity_stack/', 'Context Engineering & Isolation', 'Context Continuity Stack', 'A multi-layered architecture for managing project-specific knowledge via scoped rules and persistent instruction sets.', 'context-continuity, path-scoped-rules, constitution, documentation, best-practices', 'Directory-level Path-Scoped rules, core Project Constitution (CLAUDE.md), automated "Lessons Learned" evolution, rule-clash prevention.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1qai8xe/i_built_a_selfhosted_external_brain_for_claude/', 'Memory & Persistence Architecture', 'External Brain: Persistent Substrate', 'A self-hosted memory layer that prevents "AI amnesia" by providing agents with a persistent, cross-session knowledge bank.', 'external-brain, persistence, self-hosted, knowledge-bank, local-first', 'Cross-session continuity, project-brief/active-context separation, "Zero-Rediscovery" onboarding, automated decision logs.'),
    ('https://github.com/nick-vi/trismegistus', 'Agent Orchestration & Workflow', 'Trismegistus: Stateful Coding', 'An open-source stateful coding system that implements self-improvement loops and multi-provider routing for persistent agent operations.', 'trismegistus, stateful-ai, self-improvement, orchestration, powershell', 'ai-evolve self-improvement command, ai-verify adversarial plan-checking, multi-provider model routing, automated PRD state injection.')
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
print('Successfully injected batch 67.')
