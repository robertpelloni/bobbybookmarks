import sqlite3

data = [
    ('https://www.reddit.com/r/vibecoding/comments/1qm6rjh/big_news_claude_code_agent_can_now_run_locally/', 'Infrastructure & Proxy Layers', 'Claude Code: Local Ollama', 'A major update enabling Claude Code to run 100% locally for free using Ollama and open-source models like qwen3-coder.', 'ollama, local-llm, claude-code, free, privacy', '100% local execution, zero API costs, Qwen3-coder support, 32K context window required, bypasses official rate limits.'),
    ('https://www.reddit.com/r/vibecoding/comments/1qhm39l/i_built_a_small_cli_to_stop_vibe_coding_tools/', 'Context Engineering & Isolation', 'CodeMap: Context Slicing', 'A lightweight CLI that builds a "dumb" index of repository symbols to allow models to request specific code slices rather than rereading entire files.', 'context-engineering, optimization, codemap, search, tokens', 'Symbol-based indexing, targeted code slicing, prevents context bloat, optimized for large-scale repo research.'),
    ('https://www.reddit.com/r/vibecoding/comments/1qyse4b/gemini_3_pro_with_github_copilot_pro/', 'Guides & Industry Trends', 'Gemini 3 Pro: Copilot Integration', 'A technical analysis of Gemini 3 Pro\'s integration into GitHub Copilot, highlighting its high autonomy and "Senior Developer" proactive refactoring behavior.', 'gemini, copilot, integration, proactive, coding-agent', '37.5% Humanity\'s Last Exam score, proactive whole-project refactoring, zero-hallucination UI layout, Senior Developer archetype.'),
    ('https://www.reddit.com/r/vibecoding/comments/1rfma79/i_got_tired_of_copy_pasting_between_agents_i_made/', 'Agent Orchestration & Workflow', 'AgentChattr: Context Sync', 'An orchestration project that creates a shared "chat room" for multiple agents to share context and MCP servers, eliminating manual copy-pasting.', 'orchestration, a2a, shared-context, mcp, collaboration', 'Shared agent chat room, multi-agent MCP server sharing, cross-terminal context injection, persistent project-level rules.')
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
print('Successfully injected batch 99.')