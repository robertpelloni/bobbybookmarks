import sqlite3

data = [
    ('https://github.com/airshelf/mcpfs', 'Connectivity & Interoperability (MCP/A2A)', 'mcpfs: Plan 9 for Agents', 'A FUSE-based filesystem that mounts Model Context Protocol (MCP) servers as local directories, allowing AI agents to interact with SaaS APIs as if they were local files.', 'mcp, fuse, filesystem, api, integration', 'FUSE filesystem mounting for MCP servers, unified data access via POSIX commands (ls, cat, grep), upstream tool proxying.'),
    ('https://github.com/toroleapinc/claude-brain', 'Context Engineering & Isolation', 'Claude Brain: State Sync', 'A synchronization and evolution layer for Claude Code that ensures an agent\'s memory, skills, and architectural rules follow the developer across different machines.', 'claude-code, memory, sync, persistence, workflow', 'Automated Pre/Post session state sync, LLM-powered semantic memory merging, auto-evolution of repeated patterns into durable rules.'),
    ('https://github.com/QAInsights/superkey', 'Development Tools & Libraries', 'SuperKey: JMeter UX', 'A productivity-focused command palette plugin for Apache JMeter that brings a "Spotlight Search" experience to performance test scripting.', 'jmeter, performance-testing, ux, productivity, plugin', 'Keyboard-first component search (Cmd+P style), IDE action runner from the home row, custom shortcuts and aliases.'),
    ('https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-lightsail-openclaw/', 'Infrastructure & Proxy Layers', 'AWS Lightsail OpenClaw', 'A managed, one-click deployment blueprint for OpenClaw (self-hosted AI assistant) on Amazon Lightsail, natively integrated with Bedrock.', 'aws, lightsail, openclaw, hosting, infrastructure', 'One-click OpenClaw VPS provisioning, native Amazon Bedrock integration (Claude 3.5), omnichannel messaging routing (Slack/Discord), built-in agent sandboxing.')
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
print('Successfully injected batch 179.')