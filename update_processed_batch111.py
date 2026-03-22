import sqlite3

data = [
    ('https://www.reddit.com/r/ClaudeCode/comments/1r43cdr/introducing_cmux_tmux_for_claude_code/', 'Agent Orchestration & Workflow', 'cmux: Parallel Worktrees', 'A session manager that maps tmux panes to ephemeral git worktrees, enabling agents to execute 15+ parallel workstreams with state isolation.', 'orchestration, git-worktrees, parallelism, tmux, workflow', 'Parallel worktree management, state persistence across context switches, headless orchestration support, multi-agent terminal synchronization.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1rhe89z/i_split_my_claudemd_into_27_files_heres_the/', 'Context Engineering & Isolation', 'Fragmented Rule Architecture', 'A JIT context injection strategy that replaces monolithic rule files with path-scoped markdown fragments to eliminate token waste and relevance dilution.', 'context-engineering, optimization, rule-fragmentation, jit-loading, modularity', 'Path-scoped rule activation (glob patterns), Tiered constraint architecture (Core/Shared/Specific), PostToolUse hook enforcement, context window preservation.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1r6o6ib/desloppify_050_agent_tools_to_refine_your/', 'Agent Orchestration & Workflow', 'Desloppify: Subjective QA', 'An agentic toolset that uses sub-agent persona reviews to "taste-test" code abstractions, naming conventions, and architectural "vibe."', 'quality-gate, code-review, sub-agents, taste-testing, automation', 'Subjective persona-based reviews, "External pre-frontal cortex" loop, modular language plugins, automated abstraction audit.'),
    ('https://www.reddit.com/r/ClaudePlaysPokemon/comments/1qf3mna/gemini_3_pro_almost_visiononly_harness_plays/', 'Interface & Developer UX', 'Vision-Only State Harness', 'An empirical verification pattern where agents must verify state via screenshots and visual feedback rather than direct memory injection.', 'vision-agent, verification, visual-feedback, real-time, harness', 'Pure visual verification loop, temporal gap-bridging via text logs, anonymized entity ID handling, reduced "hand-holding" via visual proof.')
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
print('Successfully injected batch 70.')
