import sqlite3

data = [
    ('https://github.com/OpenBMB/ChatDev', 'Agent Orchestration & Workflow', 'ChatDev Software Company', 'A multi-agent framework that operates as a "Virtual Software Company," orchestrating specialized roles (CEO/CTO/Dev) to automate the full SDLC.', 'chatdev, multi-agent, sdlc, collective-intelligence, framework', 'Specialized agent roles, functional seminars for collaboration, end-to-end automated implementation, zero-code task orchestration.'),
    ('https://github.com/OpenCodeInterpreter/OpenCodeInterpreter', 'AI Agents & Frameworks', 'OpenCodeInterpreter', 'An open-source system that bridges the gap between models and code execution, featuring self-healing loops based on compiler diagnostics.', 'code-interpreter, self-healing, human-feedback, MbPP, HumanEval', 'Iterative code refinement, integration with compiler diagnostics, Code-Feedback dataset training, 33B parameter flagship performance.'),
    ('https://github.com/Opencode-DCP/opencode-dynamic-context-pruning', 'Context Engineering & Isolation', 'OpenCode DCP (Context Pruner)', 'A specialized context management plugin that uses dynamic pruning and summarization to maintain high performance in long-running AI agent sessions.', 'context-engineering, optimization, token-reduction, pruning, opencode', 'Redundant tool-call deduplication, automated stale error removal, active agent-driven context discarding, session summarization.')
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
print('Successfully injected batch 35.')
