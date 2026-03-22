import sqlite3

data = [
    ('https://www.reddit.com/r/GithubCopilot/comments/1qkg5eb/i_tested_github_copilots_new_sdk_by_building_a/', 'AI Agents & Frameworks', 'GitHub Copilot SDK', 'A standardized "Agent-as-a-Service" framework that abstracts orchestration, tool-calling, and context management into pluggable primitives.', 'sdk, copilot, agent-as-a-service, orchestration, extensibility', 'Pluggable agentic core (Plan-Act-Observe), unified tool interface (Exa/Filesystem), askUserQuestionTool for clarification, native Claude Code skill support.'),
    ('https://www.reddit.com/r/GithubCopilot/comments/1qjcn35/huge_week_for_copilot_cli_native_plan_mode_with/', 'Agent Orchestration & Workflow', 'Copilot CLI: Native Plan Mode', 'A pre-execution "thinking" phase where agents must generate a verifiable task list and architectural spec before being allowed to call tools.', 'plan-mode, orchestration, spec-driven, verification, quality-gate', 'Verifiable task list generation, user-gated tool execution, reasoning effort selection (Low/Med/High), automated /specify and /plan commands.'),
    ('https://www.reddit.com/r/GithubCopilot/comments/1qmr5pu/copilot_skins_powerful_ui_for_copilot_sdk/', 'Interface & Developer UX', 'Copilot Skins: Meta-Agent UI', 'A UI framework built on the Copilot SDK that manages multiple isolated agent sessions, each with its own git worktree and persistent state.', 'gui, agent-workspace, isolation, git-worktrees, tauri', 'Multi-agent session sidebar, Git worktree isolation, autocomplete for skills/prompts, real-time "Queue vs Steer" activity tracking.'),
    ('https://www.reddit.com/r/GithubCopilot/comments/1qklkl6/stop_vibecoding_with_copilot_a_simple_2_model/', 'Agent Orchestration & Workflow', 'Architect/Implementer Bifurcation', 'A 2-model strategic workflow that separates high-reasoning architectural design from fast, low-cost code implementation.', 'workflow, bifurcation, optimization, architect-model, cost-reduction', 'High-reasoning "Architect" planning (Opus/GPT-4o), fast "Implementer" execution (Mini/Lite), mandatory PLAN.md artifacts, elimination of "vibe-coding" drift.')
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
print('Successfully injected batch 72.')
