import sqlite3

data = [
    ('https://newsletter.owainlewis.com/p/the-simplest-way-to-build-ai-agents', 'Agent Orchestration & Workflow', 'Micro-Agent Architecture', 'A minimalist approach to agent building that prioritizes a folder-based structure (AGENTS.md, tools/, context/) over complex frameworks.', 'micro-agents, minimalist, orchestration, cli-tools, structure', 'AGENTS.md versioned instructions, simple tool script delegation, no infrastructure overhead, local folder-based context management.'),
    ('https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code', 'Guides & Industry Trends', 'Orchestration Philosophy (OpenClaw)', "The 'I ship code I don't fully read' philosophy, shifting the engineer's role from manual implementation to high-level system verification.", 'philosophy, productivity, system-verification, open-source, automation', 'Shift to system orchestration, verification-over-audit approach, high-velocity commit loops (6k+ monthly), focus on architectural integrity.'),
    ('https://openai.com/index/harness-engineering/', 'Agent Orchestration & Workflow', 'OpenAI: Harness Engineering', 'A formal methodology for building large-scale software with agents by designing the environment of scaffolding, constraints, and feedback loops.', 'harness-engineering, quality-gate, orchestration, autonomous-dev, methodology', 'Architectural "Wisdom Frames," automated garbage collection for documentation, deterministic tool feedback loops, context engineering pillars.'),
    ('https://openclaw.ai/blog/introducing-openclaw', 'AI Agents & Frameworks', 'OpenClaw: Local-First Agent OS', 'A fast-growing open-source personal AI assistant designed for data sovereignty and proactive action via a local-first "heartbeat" daemon.', 'local-first, sovereignty, proactive-ai, omnichannel, nodejs', 'Local-first hardware execution, proactive "heartbeat" tasking, 20+ messaging channel connectors, full shell/browser control.')
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
print('Successfully injected batch 53.')
