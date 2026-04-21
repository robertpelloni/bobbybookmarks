import sqlite3

data = [
    ('https://github.com/kvlar-io/kvlar', 'Infrastructure & Proxy Layers', 'Kvlar: Agentic Firewall', 'A dual-firewall security layer designed for MCP and autonomous agent networks that strips malicious prompt injections by converting them to domain-specific protocols.', 'security, firewall, mcp, orchestration, protocol', 'Language Converter Firewall (strips prompt injections), Data Abstraction Firewall (PII/context masking), Deterministic Graph Orchestration, real-time MCP server auditing.'),
    ('https://github.com/assafkip/founder-skills', 'Agent Orchestration & Workflow', 'Founder-Skills: Business', 'A framework of advanced AI skills designed to operate at the "Founder Level," enabling agents to perform strategic business logic, market research, and financial modeling.', 'skills, orchestration, business-logic, workflow, automation', 'Think-Verify-Pivot reasoning loops, autonomous Product Hunt/YC data scraping, financial burn-rate modeling, automated pitch-deck generation.'),
    ('https://github.com/ryanreh99/skills-sync', 'Context Engineering & Isolation', 'Skills-Sync: Cross-Agent', 'A platform enabling the standardization and synchronization of agent capabilities (SKILL.md) across different collaborative coding environments.', 'skills, synchronization, context-management, orchestration, standardization', 'AI-powered skill normalization, cross-platform synchronization, adaptive complexity scaling, standardized SKILL.md management.'),
    ('https://hackmyclaw.com/', 'Development Tools & Libraries', 'HackMyClaw: OpenClaw Mod', 'A specialized open-source engine fork of OpenClaw that modernizes the classic game with high-refresh rate decoupling and a built-in Lua scripting engine.', 'game-dev, modding, openclaw, engine, lua', 'Decoupled frame/tick rate logic (144Hz support), Lua-based advanced scripting engine, live asset hot-reloading (.pid/.wag), integrated Level Editor mode.')
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
print('Successfully injected batch 181.')