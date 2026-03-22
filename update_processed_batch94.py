import sqlite3

data = [
    ('https://www.reddit.com/r/A2AProtocol/comments/1r131wn/internet_of_agents_ioa_how_mcp_and_a2a_actually/', 'Connectivity & Interoperability (MCP/A2A)', 'Internet of Agents (IoA)', 'An open-source framework and protocol stack designed to transform isolated bots into a collaborative, decentralized ecosystem of networked agents.', 'ioa, decentralized, orchestration, inter-agent, framework', 'Recursive fractal scalability, dynamic teaming on-demand, asynchronous task switchboard, standardized peer discovery.'),
    ('https://www.reddit.com/r/AIForAbsoluteBeginner/comments/1ptfmu7/interesting_a2ui_agenttouser_interface_just/', 'Interface & Developer UX', 'A2UI: Agent-to-User Interface', 'A declarative UI protocol that shifts interface ownership to the agent, sending structured JSON blueprints instead of executable code for native rendering.', 'a2ui, declarative-ui, secure-rendering, ux-ownership, protocol', 'JSON-based layout blueprints, native design system inheritance, XSS-proof secure rendering, real-time dynamic form generation.'),
    ('https://www.reddit.com/r/AIMemory/comments/1pwea30/the_context_layer_ai_agents_actually_need/', 'Memory & Persistence Architecture', 'Hierarchical AIMemory Layer', 'A multi-layer memory architecture (Working/Episodic/Semantic/Procedural) designed to replace inefficient "context stuffing" with intelligent retrieval.', 'memory-architecture, context-engineering, hierarchical-memory, rag, optimization', 'Working dialogue state, Episodic narrative summaries, Semantic "Genesis Canon," Procedural behavioral learning rules.'),
    ('https://www.reddit.com/r/AIMemory/comments/1ps55qq/how_do_you_prevent_an_ai_agents_memory_from/', 'Memory & Persistence Architecture', 'Anti-Hoarding Memory Patterns', 'Community-driven strategies for preventing agent memory from becoming a liability, focusing on surgical retrieval and treating "forgetting" as a feature.', 'memory-management, anti-hoarding, optimization, forgetting, efficiency', 'Surgical vector retrieval, memory "half-life" consolidation, proactive summarization chunks, significance-based Ego Scoring.')
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
print('Successfully injected batch 60.')
