import sqlite3

data = [
    ('https://code.claude.com/docs/en/agent-teams', 'Agent Orchestration & Workflow', 'Claude Code: Agent Teams', 'An experimental orchestration system enabling multiple independent agents to collaborate on a single project via direct agent-to-agent messaging.', 'claude-code, orchestration, multi-agent, collaboration, experimentation', 'Team Lead orchestration, direct peer-to-peer sendMessage tool, broadcast inbox system, shared JSON task list with dependency tracking.'),
    ('https://cra.mr/skill-synthesis/', 'AI Agents & Frameworks', 'Cramer Skill Synthesis', 'A framework focusing on "Skill-First" development by programmatically combining atomic agent capabilities into high-level, verifiable workflows.', 'skill-synthesis, abstraction, automation, verification, quality-gate', 'Programmatic skill combination, Builder-Validator pattern, cross-team skill reusability, automated output verification steps.'),
    ('https://composio.dev/blog/secure-moltbot-clawdbot-setup-composio', 'Infrastructure & Proxy Layers', 'Composio Managed Auth', 'A security layer providing brokered OAuth and credential isolation for autonomous agents with high system permissions.', 'security, composio, managed-auth, oauth, sandboxing', 'Brokered OAuth (no local secrets), connected account ID abstraction, Docker-hardened network isolation, audit logging for all agent actions.'),
    ('https://developer.chrome.com/blog/webmcp-epp', 'Connectivity & Interoperability (MCP/A2A)', 'Chrome WebMCP Protocol', 'A W3C-incubated standard allowing websites to register tools that AI agents can discover and call natively via the browser.', 'mcp, webmcp, w3c, browser-standard, interoperability', 'navigator.modelContext browser API, declarative HTML-to-tool conversion, imperative JS tool exposure, native session/auth inheritance.')
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
print('Successfully injected batch 31.')
