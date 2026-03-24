import sqlite3

data = [
    ('https://www.reddit.com/r/ClaudeAI/comments/1prcypb/anthropic_just_dropped_claude_for_chrome_ai_that/', 'Interface & Developer UX', 'Claude for Chrome: Tab Groups', 'An official browser extension that brings multi-tab awareness to agents via a "Tab Grouping" system and DOM/Screenshot snapshots.', 'chrome, browser-use, multi-tab, automation, anthropic', 'Tab Grouping context management, DOM/Screenshot hybrid recognition, dashboard data extraction, native browser interaction tools.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1pw8yoh/i_built_a_claude_code_skill_that_spawns_37_ai/', 'Agent Orchestration & Workflow', 'Loki Mode: 37-Agent Swarm', 'A massive multi-agent skill for Claude Code that orchestrates 37 specialized agents across 6 swarms to automate the full startup lifecycle.', 'loki-mode, swarm, orchestration, autonomous-startup, claude-code', '37 Specialized agent roles, 6 functional swarms (Eng/Sec/Data/etc.), PRD-to-Revenue automation, coordinated multi-repo build-outs.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1py9ica/claude_took_control_of_the_editor_by_writing_a/', 'Interface & Developer UX', 'Bridge-Script UI Control', 'A paradigm where agents bypass standard UIs by autonomously writing their own MCP servers or file-based bridges to interact with complex engines.', 'mcp, bridge-script, game-engine, automation, innovation', 'Autonomous MCP server generation, component-specific "Lens" filtering, real-time 3D hierarchy inspection, zero-UI direct engine control.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1pur39y/achieve_tokenized_asceticism_introducing_declaude/', 'Context Engineering & Isolation', 'DeClaude: Tokenized Asceticism', 'A specialized context pruner for Claude Code that reduces system prompt overhead from 49,000 tokens to ~18 tokens via tool toggling.', 'context-engineering, optimization, token-reduction, declaude, efficiency', 'Tool-level activation toggles, 99.9% system prompt reduction, session-specific tool profiles, context-bloat prevention.')
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
print('Successfully injected batch 68.')
