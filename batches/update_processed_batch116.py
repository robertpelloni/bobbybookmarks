import sqlite3

data = [
    ('https://www.reddit.com/r/GithubCopilot/comments/1qrosx4/vercel_says_agentsmd_matters_more_than_skills/', 'AI Agents & Frameworks', 'AGENTS.md Protocol Layer', 'A structured project manifest that defines agent roles and scopes behavior to repository boundaries, outperforming skill-based discovery in reliability.', 'agents-md, role-scoping, protocol, context-engineering, standard', 'Pre-injected system prompt extensions, project-specific role scoping, 79% skill invocation accuracy, architectural boundary enforcement.'),
    ('https://www.reddit.com/r/GithubCopilot/comments/1qy8bz4/unlock_slate_local_ai_orchestration_for_vscode/', 'Infrastructure & Proxy Layers', 'SLATE: Local-First Orchestration', 'A local-first framework that leverages user hardware (Ollama/CUDA) to run deep codebase analysis and nightly jobs without cloud API costs.', 'local-first, ollama, cuda, infrastructure, optimization', 'Hardware-aware local runners, ActionGuard privacy security, 100% local "Nightly Jobs," unified cloud-local state sync.'),
    ('https://www.reddit.com/r/GithubCopilot/comments/1r19usz/is_using_a_0x_request_model_as_an_orchestrator/', 'Agent Orchestration & Workflow', '0x Orchestrator Pattern', 'A strategic cost-optimization pattern using "cheap" models (GPT-4o-mini) as planners to orchestrate "expensive" implementation models (Claude Opus).', 'cost-optimization, orchestration, model-routing, tiered-economics, efficiency', 'Cheap Planner / Expensive Implementer split, subagent "Fan-out" budget management, token-burn risk mitigation, multi-provider routing.'),
    ('https://www.reddit.com/r/GithubCopilot/comments/1r2ll4m/we_just_launched_cooper_v101/', 'Interface & Developer UX', 'Cooper: Visual Autonomy', 'A design-centric GUI for the Copilot SDK that visualizes the "Agentic Brain" task queue and reasoning chains in real-time.', 'gui, visual-reasoning, agent-workspace, collaboration, productivity', 'Real-time task queue visualization, Reasoning Chain playback, multi-session isolated state, collaborative "Peer" interaction model.')
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
