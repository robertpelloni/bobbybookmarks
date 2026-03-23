import sqlite3

data = [
    ('https://www.reddit.com/r/opencodeCLI/comments/1r6o7kr/desloppify_a_tool_to_help_agents_identify_and/', 'Development Tools & Libraries', 'Desloppify: Agent Harness', 'An open-source harness that combines mechanical linting with subjective LLM review to provide agents with a strict "beautiful code" score to chase.', 'desloppify, code-quality, harness, refactoring, next-loop', 'Mechanical/Subjective combined review, "North Star" quality score, stateful `desloppify next` loop, 29+ language support.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1rce8jw/built_an_opensource_telegram_client_for_opencode/', 'Connectivity & Interoperability (MCP/A2A)', 'Agent Telegram Monitoring', 'A pattern using Telegram bots/clients to allow agents to "inbox" users with status updates or notifications upon completion of long-running tasks.', 'telegram, monitoring, remote-management, notifications, opencode', 'Real-time agent pings, VPS monitoring support, CAR (Codex-Autorunner) integration, mobile task management.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1rf8v3s/plugin_truemem_automatic_ai_memory_that_actually/', 'Memory & Persistence Architecture', 'TrueMem: Cross-Model Memory', 'A model-agnostic memory layer utilizing a dual architecture (episodic/semantic) to prevent AI amnesia while delivering up to 99% token savings.', 'memory, persistence, context-management, truemem, token-efficiency', 'Dual-memory (episodic/semantic) system, model-agnostic gateway layer, 99% token savings via memory retrieval, enterprise state management.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1rfwlzk/i_have_2004_ai_skills_installed_heres_how_i/', 'Context Engineering & Isolation', 'SkillPointer: Scalable Skills', 'An organizational pattern that manages 2000+ specialized AI skills by replacing raw skill loading with lightweight "category pointers" for dynamic discovery.', 'skills, context-optimization, modularity, skillpointer, scaling', 'Category-based skill pointers, dynamic "vault" discovery, 80K to 255 token startup reduction, handles multi-thousand skill environments.')
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
print('Successfully injected batch 94.')