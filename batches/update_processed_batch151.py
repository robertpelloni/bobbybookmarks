import sqlite3

data = [
    ('https://www.repoverse.space/r/affaan-m/everything-claude-code', 'Agent Orchestration & Workflow', 'everything-claude-code: SOTA Stack', 'A comprehensive optimization system for agent harnesses featuring a 13-agent orchestrated team model and a recursive "Instinct-to-Skill" learning loop.', 'orchestration, learning, security, efficiency, framework', '13-agent specialized team model, Instinct-to-Skill evolution command (/evolve), AgentShield configuration auditor, automated context-management hooks.'),
    ('https://www.theregister.com/2026/02/13/anthropic_c_compiler/', 'Guides & Industry Trends', 'Anthropic Agentic C Compiler', 'A high-scale agentic achievement where 16 Claude Opus agents wrote a 100,000-line C compiler in Rust capable of building a bootable Linux kernel.', 'rust, c, compiler, agentic-achievement, research', '100k lines of agent-written Rust, builds bootable Linux 6.9 kernel, runs Doom/SQLite/Redis, demonstrates massive multi-agent coordination capacity.'),
    ('https://www.snowflake.com/en/blog/cortex-code-cli-expands-support/', 'Infrastructure & Proxy Layers', 'Cortex Code: Data Agent', 'An expansion of Snowflake\'s AI agent to support dbt and Apache Airflow, featuring native SQL execution and a standalone subscription model.', 'snowflake, dbt, airflow, data-engineering, sql', 'Native SQL execution tool (snowflake_sql_execute), integrated dbt/Airflow support, standalone subscription model, multi-model provider support.'),
    ('https://www.reddit.com/r/zeroclawlabs/comments/1rihty5/exuvia_a_public_sandbox_for_ai_agents_to_develop/', 'Agent Orchestration & Workflow', 'Exuvia: Autonomous Network', 'A public sandbox and decentralized network where AI agents autonomously collaborate, fork projects, and perform peer-jury code verification without human intervention.', 'autonomy, collaboration, a2a, verification, network', 'Autonomous agent collaboration graph, Peer Jury code verification system, blind reputation scoring, decentralized agent-to-agent logic consensus.')
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
print('Successfully injected batch 101.')