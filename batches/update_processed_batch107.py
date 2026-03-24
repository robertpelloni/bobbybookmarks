import sqlite3

data = [
    ('https://www.reddit.com/r/ClaudeAI/comments/1qegsta/announcing_claude_flow_v3_a_full_rebuild_with_a/', 'Agent Orchestration & Workflow', 'Claude Flow v3: Live Viz', 'A full rebuild focusing on multi-agent swarm visibility via an always-on "Heartbeat" status line and spatial graph navigation of reasoning chains.', 'orchestration, visibility, heartbeat, status-line, spatial-graph', 'Live 5s status line refresh, spatial mindmap navigation, 2.5x subscription limit extension, 80% token burn reduction.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1qiv0d3/open_source_i_reduced_claude_code_input_tokens_by/', 'Context Engineering & Isolation', 'GrepAI: Semantic Pruning', 'A Go-based discovery engine that reduces input tokens by 97% by replacing brute-force file reading with surgical semantic snippet retrieval.', 'context-engineering, optimization, token-reduction, semantic-search, golang', '97% Token reduction, local Ollama embeddings, call graph analysis sidecar, compact JSON snippet retrieval.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1qw9hr4/claude_code_has_an_undocumented_persistent_memory/', 'Memory & Persistence Architecture', 'Undocumented Project Memory', 'The discovery of a hidden per-project memory layer in Claude Code that enables cross-session learning via automated `MEMORY.md` injection.', 'memory, persistence, hidden-feature, claude-code, context-management', 'Hub-and-Spoke memory pattern, automated MEMORY.md injection, per-project state isolation, decision/decision persistence.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1qytpl8/using_markdown_to_orchestrate_agent_swarms_as_a/', 'Agent Orchestration & Workflow', 'Markdown Ownership Manifest', 'A prose-based orchestration protocol that uses deterministic glob patterns in `SCOPE.md` files to partition codebases for parallel agent swarms.', 'orchestration, swarm, markdown, code-partitioning, mece', 'SCOPE.md ownership manifests, MECE code slicing, parallel audit protocol, cross-slice merge logic.')
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
