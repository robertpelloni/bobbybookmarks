import sqlite3

data = [
    ('https://www.reddit.com/r/ClaudeAI/comments/1q2p03x/i_reverseengineered_the_workflow_that_made_manus/', 'Agent Orchestration & Workflow', 'Manus Reasoning Trace', 'A reverse-engineered context engineering pattern using a 3-file state machine (todo/findings/progress) to prevent agentic drift.', 'manus, context-engineering, state-machine, ooda-loop, autonomous-dev', '3-File State Machine logic, recursive OODA cycle, filesystem-based reasoning trace, Python-as-action (CodeAct) core.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1qc5g4s/anthropic_just_launched_claude_cowork_for_100mo_i/', 'Infrastructure & Proxy Layers', 'Claude Cowork', 'Anthropic\'s enterprise-grade agentic tier that provides direct local file agency and high-token autonomous loops for "Set and Forget" tasks.', 'cowork, anthropic, enterprise-ai, autonomous-ops, system-operator', 'Direct local file agency, high-token "burning" loops, multi-step autonomous planning, sovereign system operator role.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1qb1024/ultimate_claude_skillmd_autobuilds_any_fullstack/', 'AI Agents & Frameworks', 'Ultimate Fullstack Skill', 'A community-crafted instruction set for Claude Code that enables "Zero-Question" fullstack application building through phased execution.', 'skill-md, claude-code, fullstack, automation, blueprint', '18-Phase execution plan, silent decision-making mode, "Production-Ready" stack defaulting, automated monorepo construction.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1q2y94k/claude_code_hype_the_terminal_is_the_new_chatbox/', 'Interface & Developer UX', 'Terminal-as-Chatbox', 'A paradigm shift toward using the CLI as the primary high-velocity workspace for orchestrating agents with native PTY and system-level access.', 'cli, tui, pty, developer-ux, orchestration', 'Native PTY interactive prompts, direct git/system log access, natural language terminal commands, high-velocity strategic workspace.')
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
print('Successfully injected batch 69.')
