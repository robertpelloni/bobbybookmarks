import sqlite3

data = [
    ('https://github.com/fynnfluegge/agtx', 'Agent Orchestration & Workflow', 'agtx: Kanban Multi-Agent', 'A multi-session AI coding terminal manager that orchestrates multiple autonomous agents (Claude, Codex, Gemini) using a centralized Kanban board and isolated tmux worktrees.', 'orchestration, multi-agent, kanban, tmux, workflow', 'Centralized MCP Kanban board orchestration, parallel tmux/git-worktree execution, autonomous conflict resolution (Review stage), idle-state self-healing.'),
    ('https://www.wired.com/story/nvidia-planning-ai-agent-platform-launch-open-source/', 'Guides & Industry Trends', 'Nvidia NemoClaw: OS Agents', 'Wired reports on Nvidia\'s "NemoClaw," an upcoming open-source platform for deploying enterprise AI agents, marking a strategic shift from hardware lock-in to software ecosystems.', 'nvidia, enterprise, orchestration, hardware-agnostic, open-source', 'Open-source enterprise agent deployment, hardware-agnostic execution (non-CUDA reliant), focus on sequential multi-step employee tasks.'),
    ('https://www.highcaffeinecontent.com/blog/20260301-A-Month-With-OpenAIs-Codex', 'Guides & Industry Trends', 'A Month With Codex 5.3', 'A developer\'s 2026 battle-test report on OpenAI Codex 5.3, highlighting the workflow shift from "writing code" to "reviewing and tasting" AI-generated logic within Xcode 26.3.', 'codex, workflow, developer-experience, xcode, review', 'Seamless Xcode 26.3 integration, "lightning fast" Codex 5.3 generation, workflow shift from authoring to "taste/review" bottleneck.'),
    ('https://webmatik.ai/', 'Interface & Developer UX', 'Webmatik: Vision Auditing', 'An autonomous AI web automation tool designed to rapidly audit websites across SEO, UI, and accessibility by reasoning through web structures rather than relying on brittle scripts.', 'testing, vision, web-automation, qa, auditing', '4-minute rapid 8-category site audit, autonomous structural reasoning (no fixed scripts), goal-oriented visual UI inconsistency detection.'),
    ('https://github.com/VoltAgent/awesome-openclaw-skills', 'Context Engineering & Isolation', 'VoltAgent: 5k Skills Repo', 'A curated, security-audited collection of over 5,000 modular `SKILL.md` runbooks for OpenClaw and other local AI assistants.', 'skills, openclaw, registry, security, context-engineering', '5,000+ audited `SKILL.md` runbooks, Red-Team "Abaddon" mode skills, YAML frontmatter dependency tracking, active community malware filtering.')
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
print('Successfully injected batch 197.')