import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1rv4oo3/solving_the_multiagent_memory_silo_why_i_built_a/', 'Memory & Persistence Architecture', 'MCP Memory Silo Solution', 'A community analysis on using Model Context Protocol (MCP) servers to bridge "memory silos," allowing disconnected agents (Cursor, Claude Desktop) to share a single persistent knowledge base.', 'mcp, memory, persistence, interoperability, local-first', 'Cross-tool shared memory (bridging silos), local-first unified knowledge base, elimination of redundant context retrieval.'),
    ('https://www.reddit.com/r/CustomAI/comments/1rv4vue/mtarsier_open_source_tool_to_manage_mcp_servers/', 'Infrastructure & Proxy Layers', 'mTarsier: MCP Dashboard', 'An open-source desktop application that auto-detects installed AI clients and provides a visual dashboard to centrally manage and edit MCP server JSON configurations.', 'mcp, infrastructure, dashboard, configuration, dev-tools', 'Auto-detection of AI clients (Claude/Cursor/VS Code), Visual JSON config editor with syntax validation, one-click MCP Marketplace installation, portable `.tsr` snapshots.'),
    ('https://www.reddit.com/r/AIAgentsStack/comments/1rv1yp9/everyone_is_talking_about_clawbot_i_think_people/', 'Agent Orchestration & Workflow', 'Clawbot / Moltbot', 'A self-hosted, TypeScript-based AI assistant (Moltbot) that integrates with messaging platforms (WhatsApp/Discord) to execute local system commands and web browsing.', 'orchestration, self-hosted, automation, assistant, security', 'Messaging app integration (WhatsApp/Discord), local system CLI execution, "Live Canvas" visual workspace, indirect prompt injection vulnerability warnings.'),
    ('https://www.reddit.com/r/aigossips/comments/1rv7usa/kimi_just_published_attention_residuals_and_the/', 'Guides & Industry Trends', 'Kimi: Attention Residuals', 'A breakthrough architectural paper from Moonshot AI (Kimi) addressing "PreNorm Dilution" by replacing standard residual connections with selective "Attention Residuals" (AttnRes).', 'architecture, research, attention-residuals, kimi, optimization', 'AttnRes (Attention Residuals) mechanism, mitigation of PreNorm Dilution in deep layers, <4% training overhead, performance equivalent to 1.25x compute scaling.')
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
print('Successfully injected batch 201.')