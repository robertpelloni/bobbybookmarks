import sqlite3

data = [
    ('https://bbycroft.net/llm', 'Guides & Industry Trends', 'LLM 3D Walkthrough', 'A 3D interactive visualization project by Brendan Bycroft that maps GPT-style architectures down to individual tensor mathematical operations.', 'visualization, theory, transformer, architecture, learning', 'Interactive 3D block diagrams, layer-by-step walkthroughs, animated tensor flow (nano-GPT/GPT-3), mathematical operation granularity.'),
    ('https://big-agi.com/', 'Interface & Developer UX', 'Big-AGI: Maximum Agency', 'An open-source generative AI suite focused on autonomous capabilities, multi-model parallel thinking (Beam), and native Model Context Protocol support.', 'big-agi, orchestration, beam, mcp, desktop-app', 'Agent Mode multi-file edits, Beam multi-model reasoning, native MCP server support, local-first data privacy.'),
    ('https://blog.arcbjorn.com/megaeth-just-feels-different', 'Infrastructure & Proxy Layers', 'MegaETH: Real-Time L2', 'A high-performance Ethereum Layer-2 blockchain targeting 100,000 TPS and sub-millisecond block times via node specialization and high-end hardware.', 'blockchain, performance, low-latency, crypto, infrastructure', '100k Transactions Per Second (TPS), 1-10ms sub-millisecond block times, specialized Sequencer/Prover nodes, Ethereum L2 real-time core.'),
    ('https://blog.fsck.com/2025/10/09/superpowers', 'Agent Orchestration & Workflow', 'Superpowers: Multi-Agent', 'A sophisticated agentic development workflow featuring persistent vector memory, specialized review roles, and GraphViz process formalization.', 'superpowers, orchestration, workflow, memory, documentation', 'Persistent vector conversation memory, split Spec/Code review agents, GraphViz process documentation, modular SKILL.md capability learning.')
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
print('Successfully injected batch 117.')