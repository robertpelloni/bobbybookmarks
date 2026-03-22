import sqlite3

data = [
    ('https://github.com/MemoriLabs/Memori', 'AI Agents & Frameworks', 'Memori Memory Fabric', 'An open-source, SQL-native memory layer that adds persistent context across entities, processes, and sessions to any LLM application.', 'memory, sql-native, persistent-state, orchestration, session-management', 'Multi-level entity/session tracking, background context augmentation, model-agnostic LLM interceptor, support for custom datastores.'),
    ('https://recallbricks.com/', 'Infrastructure', 'RecallBricks Context Stack', 'A model-agnostic context infrastructure platform designed to solve AI statelessness through automated capture and semantic extraction.', 'context-management, rag, semantic-search, infrastructure, scaling', 'Vector-powered semantic search, auto-capture extraction engine, infinite memory scaling, one-line API integration.'),
    ('https://github.com/google-gemini/gemini-cli', 'AI Agents & Frameworks', 'Gemini CLI Foundation', 'The official open-source extension framework that transforms the Gemini CLI into a scalable platform via Playbooks and MCP servers.', 'gemini-cli, framework, extensions, playbooks, ecosystem', 'Shipping container extension model, GEMINI.md playbook support, native system keychain security, community tool catalog integration.'),
    ('https://github.com/LifeContext/lifecontext', 'AI Agents & Frameworks', 'LifeContext Digital Twin', 'An open-source framework for building a personalized "digital twin" through life-scale long-term retrieval and multimodal memory.', 'digital-twin, personal-ai, browser-extension, privacy, multimodal', 'Deep browser history integration, proactive life-insight generation, local-first private storage, automated prompt optimization.'),
    ('https://github.com/marketplace/actions/memvault-sync', 'Infrastructure', 'MemVault Sync Action', "A GitHub Action that automatically syncs repository documentation and code into an agent's long-term memory Knowledge Graph.", 'github-action, graphrag, automation, devops, knowledge-graph', 'Automated repository ingestion, async "Sleep Cycle" graph extraction, seamless YAML-based configuration, preventative vector-loss architecture.'),
    ('https://news.ycombinator.com/item?id=46301470', 'Guides & Articles', 'Agent Memory Evolution', 'A high-signal community discussion on the transition from simple markdown memory banks to automated graph-consolidated memory for agents.', 'hacker-news, discussion, memory-bank, graph-rag, engineering', 'Analysis of Roo Code vs OpenCode memory, graph consolidation benefits, "lost-in-the-middle" solution strategies.'),
    ('https://github.com/cnicolov/opencode-plugin-simple-memory', 'Development Tools & Libraries', 'OpenCode Simple Memory', 'A specialized persistent memory plugin for OpenCode designed to maintain categorized coding-specific context across sessions.', 'opencode, plugin, memory, coding-context, persistence', 'Categorized memory (Decision/Learning/Pattern), tool-based memory_recall, AGENTS.md native integration, architectural decision tracking.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level)
        VALUES (?, ?, ?, ?, ?, ?, 'deep')
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='deep'
    ''', (url, cat, sd, ld, tags, mf))
conn.commit()
conn.close()
print('Successfully injected batch 19.')
