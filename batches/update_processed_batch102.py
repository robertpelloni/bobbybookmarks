import sqlite3

data = [
    ('https://www.reddit.com/r/BMAD_Method/comments/1rcq4w1/bmad_v6_is_finally_here_pure_magic/', 'Agent Orchestration & Workflow', 'BMAD v6: Brownfield Magic', 'A major update to the BMAD framework optimized for seamless integration into existing (brownfield) codebases and human-in-the-loop flexibility.', 'bmad, brownfield, orchestration, workflow, human-in-the-loop', 'Flexible planning-to-execution mapping, enhanced PRD/Architecture auto-generation, multi-agent project context sync, optimized for legacy codebase refactors.'),
    ('https://www.reddit.com/r/BMAD_Method/comments/1r2ra7i/i_loved_bmadmethod_and_ralph_separately_so_i/', 'Agent Orchestration & Workflow', 'bmalph: The Plan-Execute Hybrid', 'A powerful architectural pattern that combines BMAD-METHOD (Structured Planning) with Ralph (Autonomous TDD Loops) for high-velocity project builds.', 'bmalph, tdd, automation, planning, feedback-loops', 'Plan-to-Task auto-conversion, autonomous implementation loops (Ralph), fresh-context per story to prevent drift, 60+ story project execution in <40 hours.'),
    ('https://www.reddit.com/r/Bard/comments/1qa513c/gemini_3_flash_preview_ranks_2_in_our_ai_vs_human/', 'Guides & Industry Trends', 'Gemini 3 Flash: Visual Dominance', 'A benchmark analysis showing Gemini 3 Flash Vision significantly outperforming its text counterpart in spatial reasoning and real-time interaction.', 'gemini, benchmarks, vision-agent, low-latency, real-time', '14% Visual win rate vs 6% Text in competitive games, superior spatial reasoning core, optimal for low-latency visual agent tasks, high-speed non-thinking execution.'),
    ('https://www.reddit.com/r/Bard/comments/1qbuv3j/leak_google_is_working_on_a_new_tool_for_gemini/', 'Connectivity & Interoperability (MCP/A2A)', 'Gemini Leak: Auto Browse', 'A leaked autonomous browsing tool for Gemini that enables tab management, research, and native web-task execution via deep Chrome integration.', 'gemini, browser-use, automation, chrome, google-leak', 'Autonomous multi-tab management, native Chrome integration, remote Linux session infrastructure, session-persistent web synthesis.')
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
print('Successfully injected batch 64.')
