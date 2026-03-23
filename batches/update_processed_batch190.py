import sqlite3

data = [
    ('https://temporal.io/', 'Infrastructure & Proxy Layers', 'Temporal: Durable Execution', 'A durable execution platform that virtualizes application state to enable crash-proof workflows, now a core infrastructure pillar for OpenAI\'s Agents SDK.', 'temporal, infrastructure, durable-execution, orchestration, reliable-ai', 'State virtualization (crash-proof), OpenAI Agents SDK integration, persistent event history logs, sub-second state reconstruction.'),
    ('https://theia-ide.org/', 'Interface & Developer UX', 'Theia AI: Open-Source IDE', 'A modular, vendor-neutral IDE framework by the Eclipse Foundation that embeds LLMs and MCP servers into custom developer workspaces.', 'ide, theia, eclipse, open-source, orchestration', 'Modular agentic IDE framework, native MCP server integration, Open VSX vendor-neutral hub, customizable agentic behaviors.'),
    ('https://supermemory.ai/', 'Memory & Persistence Architecture', 'Supermemory: Agent Recall', 'A model-agnostic reference memory layer providing agents with long-term context across sessions via an automated ingestion and user profiling API.', 'memory, persistence, context-management, api, second-brain', 'Universal long-term memory API, automated data ingestion (docs/chat), sub-400ms retrieval latency, dynamic user preference profiling.'),
    ('https://synthetic.new/hf/zai-org/GLM-4.6', 'AI Agents & Frameworks', 'GLM-4.6: Z.ai Flagship', 'The flagship 357B parameter Mixture-of-Experts (MoE) model by Z.ai, featuring 200K context and near parity with Claude Sonnet 4 in coding.', 'moe, zai, coding-model, benchmarks, research', '357B parameter MoE architecture, 200K token context window, 48.6% CC-Bench win rate, optimized for deep research synthesis.')
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
print('Successfully injected batch 151.')