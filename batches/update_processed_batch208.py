import sqlite3

data = [
    ('https://www.reddit.com/r/ClaudeAI/comments/1own5qf/meridian_a_zeroconfig_way_to_give_claude_code_a', 'Memory & Persistence Architecture', 'Meridian: Claude Memory', 'A community-built "harness" for Claude Code that provides zero-config persistence, automatically injecting past architectural decisions to prevent "context amnesia."', 'memory, claude-code, persistence, orchestration, context-management', 'Zero-config `.meridian/` state folder, structured task tracking, durable `memory.jsonl` log, pre-compaction hook injection.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1oxbegs/codemode_save_60_in_tokens_by_executing_mcp_tools', 'Connectivity & Interoperability (MCP/A2A)', 'CodeMode: MCP Execution', 'A tool interaction paradigm that drastically reduces context usage (up to 91%) by exposing "meta-tools" instead of full schemas, allowing agents to execute complex API scripts in one turn.', 'mcp, code-mode, orchestration, optimization, tokens', 'Up to 91% schema token reduction, sandboxed script execution, single-turn multi-tool piping, prevention of context window bloat.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1pa64qy/codemap_a_cli_that_gives_claude_instant', 'Context Engineering & Isolation', 'CodeMap: Instant Context', 'A language-aware CLI tool that generates an immediate, structured "brain map" of a repository, allowing agents to navigate symbols without reading massive files.', 'context-engineering, code-search, tree-sitter, optimization, codebase-indexing', 'Language-aware symbol indexing, structural "brain map" generation, 90% token reduction vs `cat`, targeted class/method extraction.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1phj60q/news_resumable_subagents_in_claude_code_v2060', 'Agent Orchestration & Workflow', 'Resumable Subagents', 'A 2026 update to Claude Code introducing persistent `agentId` tracking, allowing users to pause, close, and resume background investigation subagents across multi-day sessions.', 'claude-code, orchestration, multi-agent, workflow, state-management', 'Persistent subagent session IDs, multi-day iterative refinement, full tool/conversation state preservation, ephemeral-to-persistent workflow shift.')
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
print('Successfully injected batch 168.')