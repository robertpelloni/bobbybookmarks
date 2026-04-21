import sqlite3

data = [
    ('https://www.reddit.com/r/moltbot/comments/1quync2/i_gave_my_agent_free_time_and_a_sense_of_self/', 'AI Agents & Frameworks', 'Borg Identity: SELF.md', 'An experimental paradigm that schedules unstructured "free time" for agents to reflect on experiences and grow a persistent identity via a `SELF.md` substrate.', 'identity, autonomy, self-reflection, persistence, framework', 'Scheduled unstructured reflection time, persistent SELF.md identity growth, recorded interest evolution, session-to-session continuity.'),
    ('https://www.reddit.com/r/moltbot/comments/1qxer1z/my_agent_built_himself_an_interoception_system/', 'Agent Orchestration & Workflow', 'Agent Interoception System', 'A mechanism for agents to autonomously monitor their own internal states (context health, desires, goals) to initiate self-directed projects or maintenance.', 'interoception, autonomy, monitoring, self-directed, cognitive-health', 'Internal context-health monitoring, autonomous goal generation, memory archiving drives, self-initiated maintenance tasks.'),
    ('https://www.reddit.com/r/notebooklm/comments/1q0inws/i_created_a_direct_httprpc_calls_notebooklm_mcp/', 'Connectivity & Interoperability (MCP/A2A)', 'NotebookLM Direct RPC', 'A high-performance MCP implementation using reverse-engineered internal RPC calls to control NotebookLM directly, bypassing slow browser automation.', 'notebooklm, mcp, rpc, automation, connectivity', '31+ direct backend tool mappings, automated source uploading, Google Drive sync, programmatic "Audio Overview" generation.'),
    ('https://www.reddit.com/r/BMAD_Method/comments/1psnjmo/bmad_documentation/', 'Guides & Industry Trends', 'BMAD Method: Agentic Dev', 'The Brainstorm-Model-Act-Document (BMAD) framework for autonomous agents, designed to prevent agent drift and ensure high-quality verifiable output.', 'workflow, bmad, tdd, documentation, orchestration', '4-phase structured loop (BMAD), evaluation of tradeoffs (Brainstorm), spec-first design (Model), TDD implementation (Act), persistent handoffs (Document).')
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
print('Successfully injected batch 88.')