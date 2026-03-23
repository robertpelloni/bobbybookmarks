import sqlite3

data = [
    ('https://manus.im/', 'Agent Orchestration & Workflow', 'Manus: Meta Agent', 'A "hands-on" autonomous agent acquired by Meta that operates in cloud VMs with full shell/filesystem access and visual reasoning for complex web/code tasks.', 'manus, meta, autonomy, vision, orchestration', 'Autonomous multi-step goal execution, cloud VM sandboxing, vision-based web interaction, local "My Computer Agent" desktop support.'),
    ('https://meshtastic.org/', 'Connectivity & Interoperability (MCP/A2A)', 'Meshtastic: Off-Grid Mesh', 'A decentralized, serverless mesh messaging system using LoRa hardware for long-range, encrypted off-grid communication.', 'mesh-network, lora, p2p, security, off-grid', 'Serverless P2P messaging, 15-20km+ open terrain range, nRF52840 extreme power efficiency, multi-channel encrypted groups (AES-256).'),
    ('https://mbleigh.dev/posts/context-engineering-with-links', 'Context Engineering & Isolation', 'Context Links Pattern', 'An architectural paradigm advocating for the use of hyperlinks (MCP Resources) as primitives for "Just-in-Time" context to prevent token rot.', 'context-engineering, optimization, mcp, resources, navigation', 'URI-addressable "Context Links", JIT resource fetching (file://, data://), prevention of "context rot," HATEOAS for agent discovery.'),
    ('https://medium.com/@slayerfifahamburg/the-dual-agent-workflow-how-to-pair-gemini-cli-and-claude-code-for-autonomous-code-evolution-f8f94900b6fc', 'Agent Orchestration & Workflow', 'Dual Agent: Arch-Impl', 'A collaborative workflow pattern that pairs Gemini CLI (as Architect/Investigator) with Claude Code (as Implementer/TDD) for autonomous evolution.', 'orchestration, gemini, claude, workflow, collaboration', 'Specialized Architect/Implementer roles, cross-agent plan handoffs, Git Worktree isolation, automated TDD implementation loops.')
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
print('Successfully injected batch 137.')