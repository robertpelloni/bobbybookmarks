import sqlite3

data = [
    ('https://github.com/ContextEngineAI/context-engine', 'AI Agents & Frameworks', 'Context Engine Company Memory', 'A structured timeline and memory system for DevOps that tracks commits and workflows to provide agents with cross-repo business context.', 'devops, company-memory, context, orchestration, timeline', 'Multi-repo intelligence tracking, activity correlation across services, structured context/ directory support, automated company knowledge injection.'),
    ('https://github.com/henkdz/mcp-server-clickhouse', 'MCP', 'ClickHouse MCP Server', 'A Model Context Protocol server providing a secure, read-only SQL interface for ClickHouse clusters and chDB embedded databases.', 'mcp, clickhouse, database, sql, data-analysis', 'Read-only run_query protection, chDB local file querying (Parquet/CSV), schema discovery (list_tables/describe), enterprise security validation.'),
    ('https://github.com/macc-n/wot-mcp-cli', 'Development Tools & Libraries', 'WoT-MCP Interactive CLI', 'A command-line client for interacting with Web of Things devices via the Model Context Protocol, supporting both stdio and HTTP transports.', 'cli, wot, mcp, iot, terminal', 'Interactive device shell, stdio/HTTP transport modes, real-time device property reading, action invocation and event subscription.'),
    ('https://github.com/AbanteAI/tiktoken', 'Development Tools & Libraries', 'AbanteAI Tiktoken Porter', 'A high-performance port of the tiktoken BPE tokenizer designed for precise token counting and context limit management in specialized ecosystems.', 'tokenization, optimization, openai, cost-management, sdk', 'Exact GPT-4/GPT-3.5 token alignment, cl100k_base support, real-time performance optimization, offline encoding support.'),
    ('https://github.com/macc-n/wot-mcp-examples', 'Guides & Articles', 'WoT-MCP Reference Examples', 'A collection of reference implementations and boilerplate for bridging AI models with physical IoT hardware using the Model Context Protocol.', 'mcp, iot, wot, tutorial, examples', 'W3C Thing Description integration, IoT protocol translation (MQTT/CoAP), physical action tool definitions, boilerplate for WoT-aware servers.'),
    ('https://github.com/AbanteAI/mentat-template-js', 'Development Tools & Libraries', 'Mentat Full-Stack Template', 'An AI-optimized React/Express boilerplate designed for high-accuracy development and review workflows using the Mentat coding assistant.', 'boilerplate, react, express, mentat, typescript', 'Mentat-optimized directory structure, automated PR/review workflow support, TypeScript-first safety, built-in CI/CD fix guides.')
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
print('Successfully injected batch 14.')
