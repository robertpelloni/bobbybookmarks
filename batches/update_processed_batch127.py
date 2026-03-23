import sqlite3

data = [
    ('https://www.reddit.com/r/codex/comments/1rkxqwk/1m_context_window_confirmed_in_gpt_54_with/', 'AI Agents & Frameworks', 'GPT-5.4: 1M Context', 'A 1 million token context window with an Extreme Reasoning mode designed for long-horizon autonomous tasks.', 'gpt-5-4, context-window, reasoning, codex, long-context', '1M token context, Extreme Reasoning mode (hours-long runs), optimized for multi-step workflows, agentic performance.'),
    ('https://www.reddit.com/r/codex/comments/1rl13vd/github_openaisymphony_symphony_turns_project_work/', 'Agent Orchestration & Workflow', 'OpenAI Symphony', 'An open-source orchestration framework that monitors issue trackers to autonomously spawn Codex agents and deliver verified PRs.', 'symphony, openai, orchestration, issue-to-pr, automation', 'Issue-to-PR pipeline, Linear integration, Elixir-based workflow.mmd definitions, sandboxed autonomous workspaces.'),
    ('https://www.reddit.com/r/cursor/comments/1pz8uc6/i_gave_cursor_persistent_memory_claudemem_gemini/', 'Memory & Persistence Architecture', 'Claude-Mem (Cursor)', 'A semantic memory layer for Cursor that extracts behavioral observations and auto-injects them via rule files to prevent AI amnesia.', 'cursor, memory, persistence, claude-mem, semantic-observations', 'Native hook tracking, semantic observation extraction, auto-injected rules, multi-model (Gemini) consolidation.'),
    ('https://www.reddit.com/r/cursor/comments/1r6oeq0/cursors_context_usage_is_10x_better_than_claude/', 'Context Engineering & Isolation', 'Cursor vs Claude Code Context', 'An analysis of context usage showing Cursor excels at surgical editing via semantic search, while Claude Code is 5.5x more token-efficient for complex, multi-file agentic tasks.', 'context-efficiency, cursor, claude-code, comparison, token-reduction', 'Semantic/hybrid search vs agent-first approach, surgical edits vs complex features, context degradation thresholds (70k vs 200k).')
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
print('Successfully injected batch 77.')