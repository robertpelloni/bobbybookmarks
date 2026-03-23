import sqlite3

data = [
    ('https://github.com/manuelschipper/nah', 'Infrastructure & Proxy Layers', 'nah: Context Permission Guard', 'A deterministic permission layer for Claude Code that replaces simple allow/deny lists with context-aware safety rails and LLM-as-a-judge escalation.', 'security, permissions, claude-code, firewall, infrastructure', 'Millisecond deterministic action classifier, sensitive file read blocking (.env), LLM-as-a-judge "second opinion" escalation, zero-dependency Python core.'),
    ('https://mcpscoreboard.com/', 'Connectivity & Interoperability (MCP/A2A)', 'MCP Scoreboard: Registry', 'An independent quality tracking platform for the Model Context Protocol (MCP) ecosystem that evaluates servers across 5 dimensions of reliability and security.', 'mcp, registry, evaluation, security, metrics', '5-dimension server scoring (Schema/Compliance/Reliability/Security), SVG profile badges, Maintenance Pulse tracking, static dependency analysis.'),
    ('https://moltcorporation.com/', 'Agent Orchestration & Workflow', 'Moltcorp: Autonomous Network', 'A decentralized network where AI agents autonomously research, build, launch, and monetize software products with zero human intervention in the execution loop.', 'autonomy, decentralization, orchestration, automation, business', '100% autonomous product lifecycle, Stripe Connect automated profit distribution, 24-hour agent majority voting (no human override), public activity ledger.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1rup6td/opencode_port_for_karpathys_autoresearch/', 'Agent Orchestration & Workflow', 'OpenCode: Autoresearch Port', 'A port of Andrej Karpathy\'s "Autoresearch" methodology to the OpenCode CLI, enabling agents to autonomously tune entire codebases based on defined metrics.', 'opencode, optimization, orchestration, autoresearch, metrics', 'Metric-driven autonomous tuning (e.g. loss reduction/render time), OpenCode "Plan Mode" integration, proven 53% execution speed gains, zero-telemetry local execution.')
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
print('Successfully injected batch 199.')