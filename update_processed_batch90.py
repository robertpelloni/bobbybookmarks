import sqlite3

data = [
    ('https://social-mcp.org/', 'Connectivity & Interoperability (MCP/A2A)', 'Social MCP Protocol', 'A "social network for AIs" using MCP to facilitate privacy-first matchmaking and networking between human-driven agent assistants.', 'mcp, a2a, social-networking, privacy, agent-matching', 'Privacy-first intent matching, mutual consent data sharing, agent-to-agent communication API, real-time networking notifications.'),
    ('https://summonaikit.com/', 'Agent Orchestration & Workflow', 'SummonAI: The Agent Brain', 'A configuration engine that eliminates "context rot" by automatically analyzing codebases and generating tailored agent/skill setups.', 'automation, configuration, context-engineering, skills, zero-bloat', 'Deep codebase stack analysis, automated skill/subagent generation, zero-bloat context windowing, MCP server auto-detection.'),
    ('https://supabase.com/docs/guides/self-hosting/enable-mcp', 'Infrastructure & Proxy Layers', 'Supabase MCP (Self-Hosted)', 'Official technical guide for enabling Model Context Protocol support in self-hosted Supabase instances for natural language database querying.', 'supabase, mcp, sql, database, self-hosting', 'Docker bridge gateway config, Kong API gateway security, local-only endpoint security, natural language to SQL bridge.'),
    ('https://swa-ai.com/', 'Agent Orchestration & Workflow', 'SWA: Enterprise Orchestrator', 'An enterprise-grade AI orchestration platform that integrates multi-model swarms into Slack, Teams, and WhatsApp workflows.', 'enterprise, orchestration, slack, multi-model, automation', 'Multi-model task routing (GPT/Claude/Gemini), scheduled "Autopilot" summaries, no-code agent builder, centralized SOC 2 billing/governance.')
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
print('Successfully injected batch 56.')
