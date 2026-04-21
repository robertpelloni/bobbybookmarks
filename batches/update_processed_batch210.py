import sqlite3

data = [
    ('https://www.reddit.com/r/GithubCopilot/comments/1p9nfvs/memory_bank_with_progressive_disclosure_technique', 'Context Engineering & Isolation', 'Memory Bank: Progressive', 'A workflow technique that organizes context into a hierarchical "Memory Bank," using progressive disclosure to keep the LLM context lean and prevent "context rot."', 'context-engineering, memory-bank, progressive-disclosure, workflow, copilot', 'Hierarchical context disclosure, structured Markdown/YAML memory files, autonomous context navigation, token bloat prevention.'),
    ('https://www.reddit.com/r/HowToAIAgent/comments/1phakmw/google_just_dropped_a_whole_framework_for_multi', 'Agent Orchestration & Workflow', 'Google ADK: Agent Framework', 'Google\'s open-source Agent Development Kit (ADK) that standardizes multi-agent patterns by separating state, memory, and artifacts into distinct "brains."', 'orchestration, multi-agent, google, adk, framework', 'Separation of State/Memory/Artifacts, "Relevance Layer" dynamic retrieval, native MCP protocol standardization, Human-in-the-Loop reflection.'),
    ('https://www.reddit.com/r/grok/comments/1lwsctc/grok_4_coding_comparison_wow', 'Guides & Industry Trends', 'Grok 4: Real-time Planning', 'A community analysis of Grok 4 Code, noting its superior raw logical planning and real-time data access (X integration), despite being slower than Claude 4 Opus.', 'grok, benchmarks, coding, reasoning, xai', 'Real-time X (Twitter) data integration, superior raw logical planning, "tasteful" vs "literal" coding styles, 128K optimal reasoning window.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1p6wtfl/made_a_tool_to_run_claude_code_with_other_models', 'Connectivity & Interoperability (MCP/A2A)', 'Claudish: API Proxy', 'An open-source proxy tool (Claudish) that intercepts Claude Code CLI requests and translates Anthropic-specific tool calls into OpenAI/Gemini-compatible formats.', 'proxy, claude-code, openrouter, interoperability, cli', 'Claude-to-OpenAI tool translation, OpenRouter 580+ model support within Claude Code, bypasses native rate limits, terminal-first workflow retention.')
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
print('Successfully injected batch 170.')