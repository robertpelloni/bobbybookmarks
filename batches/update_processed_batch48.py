import sqlite3

data = [
    ('https://github.com/AbanteAI/experiments', 'AI Agents & Frameworks', 'AbanteAI Prototypes', 'A collection of experimental projects and agentic workflow prototypes from the creators of Mentat, focusing on GitHub-native AI engineering.', 'mentat, experiments, prototypes, agentic-workflow, ai-research', 'Early-stage LLM app scaffolding, proof-of-concept coding tools, experimental agent coordination patterns.'),
    ('https://github.com/hangwin/mcp-chrome', 'MCP', 'MCP Chrome Extension', 'An extension-based MCP server that connects AI agents to your actual daily browser session, preserving logins and cookies for deep web research.', 'mcp, chrome, extension, browser-agent, research', 'Native browser context preservation, cross-tab semantic search via vector DB, 20+ integrated DOM/network tools, local-first privacy.'),
    ('https://github.com/AgentDeskAI/browser-tools-mcp', 'MCP', 'AgentDesk Browser Tools', 'A specialized suite of "eyes and hands" for AI agents, providing tools for DOM manipulation, accessibility auditing, and performance monitoring.', 'mcp, tools, browser-automation, auditing, debugging', 'Real-time console/network monitoring, intelligent DOM truncation for context efficiency, automated accessibility/SEO auditing.'),
    ('https://www.reddit.com/r/mcp/comments/1ppokmm/use_natural_language_to_query_blockchain_data/', 'Guides & Articles', 'Blockchain NLP Analysis', 'Community discussion on leveraging MCP to perform natural language queries against indexed blockchain data from over 63 networks.', 'blockchain, nlp, query, mcp, analysis', 'DAO governance tracking, English-language whale movement monitoring, on-chain activity filtering via GoldSky/Envio.'),
    ('https://github.com/goldsky-io/mcp-server', 'MCP', 'GoldSky Blockchain MCP', 'A Model Context Protocol server that allows AI agents to perform complex, real-time data queries across multiple blockchain networks using natural language.', 'mcp, blockchain, indexing, web3, analytics', 'Multi-chain support (63+ networks), real-time event indexing, natural language SQL-like querying, sub-second latency data retrieval.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level)
        VALUES (?, ?, ?, ?, ?, ?, 'deep')
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='deep'
    ''', (url, cat, sd, ld, tags, mf))
conn.commit()
conn.close()
print('Successfully injected batch 15.')
