import sqlite3

data = [
    ('https://factory.ai/product/cli', 'Agent Orchestration & Workflow', 'Factory.ai Droid CLI', 'A terminal-based interface for running autonomous "Droids" that perform end-to-end engineering tasks like refactors and bug fixes.', 'factory, droids, autonomous, cli, sw-engineering', 'End-to-end task implementation, multi-repo knowledge unification (GitHub/Jira), automated PR submission, Unix-style one-line command triggers.'),
    ('https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/', 'AI Agents & Frameworks', 'GitHub Copilot Agent Skills', 'A standardized modular framework for extending AI assistants with portable instructions, scripts, and specialized domain knowledge.', 'copilot, skills, standard, agentskills, mcp', 'Modular SKILL.md architecture, dynamic skill activation, cross-IDE portability (VS Code/JetBrains), native Claude Code directory support.'),
    ('https://github.com/AnandChowdhary/continuous-claude', 'Agent Orchestration & Workflow', 'Continuous Claude', 'An autonomous CLI wrapper for Claude Code that manages the entire PR lifecycle, from branch creation to successful merge.', 'claude-code, autonomous-pr, workflow, git-worktrees, automation', 'Autonomous PR lifecycle management, SHARED_TASK_NOTES.md persistent state, Git worktree parallelism, automated CI failure recovery.'),
    ('https://github.com/AsyncFuncAI/jules-agent-sdk-python', 'AI Agents & Frameworks', 'Jules Agent SDK', "A Pythonic SDK for delegating complex coding tasks to Google's Jules agent, enabling background execution in secure cloud environments.", 'jules, google, sdk, async-delegation, cloud-agent', 'Asynchronous task delegation, secure cloud repo cloning, background implementation loops, unified session/activity management.')
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
print('Successfully injected batch 33.')
