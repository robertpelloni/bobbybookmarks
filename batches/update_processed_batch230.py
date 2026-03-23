import sqlite3

data = [
    ('https://www.reddit.com/r/GithubCopilot/comments/1rozgi9/vs_code_version_1111_has_autopilot_mode/', 'Agent Orchestration & Workflow', 'VS Code Autopilot Mode', 'Introduced in VS Code 1.111, this mode allows GitHub Copilot to execute autonomously, continuously auto-approving tool calls and retrying errors to complete complex tasks.', 'copilot, vscode, autonomy, orchestration, orchestration', 'Autonomous multi-step execution, auto-approval of tool calls, automated error retry loops, recommended use with Dev Containers/Terminal Sandboxing.'),
    ('https://www.reddit.com/r/CognitionLabs/comments/1rmi9yy/devin_22_is_out_and_they_rebuilt_the_whole_thing/', 'Agent Orchestration & Workflow', 'Devin 2.2: Closed Loop', 'A ground-up rebuild of Devin featuring a "closed-loop" architecture where the agent can use a virtual desktop to test its own work, self-verify, and auto-fix bugs.', 'devin, orchestration, autonomy, testing, multi-agent', 'Closed-loop self-verification via virtual desktop, 3x faster startup times, ability to schedule and manage sub-Devins (multi-agent workflows).'),
    ('https://github.com/muxi-ai/skills-rce', 'Infrastructure & Proxy Layers', 'MUXI: skills-rce', 'A specialized infrastructure service designed to provide secure, declarative Remote Code Execution (RCE) environments for AI agent "skills."', 'rce, security, infrastructure, sandboxing, muxi', 'Remote Code Execution (RCE) provisioning, declarative agent formation specification, native integration with MUXI orchestration/observability layers.'),
    ('https://github.com/jpmelos/agentcontainer', 'Context Engineering & Isolation', 'AgentContainer (jpmelos)', 'A Rust-based utility that standardizes how AI agent environments are declared and run, ensuring reproducible, isolated dependencies for agentic workflows.', 'containers, isolation, rust, environment-management, orchestration', 'Standardized agent environment declaration, Rust-native performance, reproducible dependency isolation, Docker-like standard for agents.')
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
print('Successfully injected batch 190.')