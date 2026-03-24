import sqlite3

data = [
    ('https://github.com/langgenius/dify', 'Infrastructure & Proxy Layers', 'Dify: Visual LLMOps', 'An open-source LLMOps platform designed for building and operating AI apps via a visual orchestration interface and robust RAG pipelines.', 'llmops, orchestration, rag, visual-workflow, dev-tools', 'Visual workflow canvas, Prompt IDE, 50+ built-in tool connectors, production-ready log analysis & monitoring.'),
    ('https://github.com/llamastack/llama-stack', 'Infrastructure & Proxy Layers', 'Meta Llama Stack', 'A framework that standardizes core building blocks (Inference, RAG, Agents) into a unified API layer for Llama-based applications.', 'llama, standardization, infrastructure, api, meta', 'Standardized Inference/RAG/Agent APIs, verified local/cloud distributions, plugin-based architecture, multi-environment flexibility.'),
    ('https://github.com/lobehub/lobehub', 'Interface & Developer UX', 'LobeHub Agent Workspace', 'A design-centric AI agent framework and polished chat interface featuring a modular plugin system and multi-model support.', 'gui, agent-workspace, modular, design, chat-ui', 'MCP server support, comprehensive plugin marketplace, built-in TTS/STT voice interaction, multi-model backend integration.'),
    ('https://github.com/mastra-ai/mastra', 'Agent Orchestration & Workflow', 'Mantra: TS Agent SDK', 'A TypeScript-first AI framework for building production-grade agents with graph-based deterministic workflows and persistent memory.', 'typescript, sdk, orchestration, deterministic-workflow, memory', 'Graph-based .then()/.parallel() logic, persistent agent memory substrate, integrated RAG subsystem, built-in observability hooks.')
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
print('Successfully injected batch 41.')
