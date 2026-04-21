import sqlite3

data = [
    ('https://cursor.com/docs/background-agent', 'Agent Orchestration & Workflow', 'Cursor: Background Agents', 'Remote, asynchronous agents that run in isolated cloud containers to autonomously implement features, run tests, and draft Pull Requests.', 'cursor, background-agent, cloud-orchestration, autonomy, pr-automation', 'Isolated Ubuntu cloud environments, GitHub/Linear integration, autonomous test/lint/format loops, multi-task parallel execution.'),
    ('https://devblogs.microsoft.com/powershell/preview-6-ai-shell', 'Infrastructure & Proxy Layers', 'PowerShell AI Shell (aish)', 'An interactive CLI framework by Microsoft that acts as an MCP client and provides deep terminal integration for AI-driven command execution.', 'powershell, cli, mcp, infrastructure, dev-tools', 'MCP Client integration, `run_command_in_terminal` tool, predictive IntelliSense injection, sidecar split-pane UI.'),
    ('https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability', 'Connectivity & Interoperability (MCP/A2A)', 'Google A2A Protocol', 'An open, vendor-neutral protocol for standardized agent-to-agent communication, enabling cross-vendor discovery and coordination on complex tasks.', 'a2a, interoperability, google, standard, protocol', 'Vendor-neutral agent discovery, context/task sharing across opaque agents, built on JSON-RPC/HTTP standards, high-integrity peer coordination.'),
    ('https://dev.to/charmpic/title-supercharging-the-gemini-cli-how-i-made-claude-and-gemini-pair-program-35l1', 'Agent Orchestration & Workflow', 'Multi-AI Pair Programming', 'A collaborative workflow pattern that leverages specialized model roles (Claude for UI, Gemini for Architecture) in a shared terminal environment.', 'gemini, claude, orchestration, pair-programming, workflow', 'Role-based model specialization, cross-consultation bug fixing, shared repository context (WSL), cost-efficient context leveraging (Gemini 1M).')
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
print('Successfully injected batch 114.')