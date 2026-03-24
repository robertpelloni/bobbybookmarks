import sqlite3

data = [
    ('https://github.com/AbanteAI/repo-visualizer', 'Development Tools & Libraries', 'AbanteAI Repo Visualizer', 'An interactive tool that transforms git repositories into dynamic graphs, enabling developers to visualize codebase structure and evolution.', 'visualization, git, architecture, graphs, discovery', 'Interactive node-link diagrams, repository evolution playback, central component detection, automated dependency mapping.'),
    ('https://github.com/AbanteAI/gpt-generals', 'AI Agents & Frameworks', 'GPT-Generals Game Sandbox', 'An experimental strategy game where units are controlled by LLM reasoning, serving as a sandbox for multi-agent coordination research.', 'llm-gaming, strategy, agents, simulation, mentat', 'LLM-powered unit movement, client-server architecture, automated strategy simulation, authored via Mentat.ai.'),
    ('https://github.com/AbanteAI/LoCoDiff-bench', 'Development Tools & Libraries', 'LoCoDiff Benchmark Suite', 'A specialized benchmarking suite designed to measure the accuracy and performance of local AI code generation and diffing algorithms.', 'benchmark, diffing, coding-assistant, performance, evaluation', 'Performance validation metrics, regression testing for code engines, standardized diffing benchmarks.'),
    ('https://github.com/hyperbrowserai/mcp', 'MCP', 'Hyperbrowser MCP Server', 'An implementation of the Model Context Protocol that provides AI agents with secure tools for web scraping, crawling, and browser automation.', 'mcp, browser-automation, scraping, web-agent, tools', 'Scrape/Crawl markdown extraction, browser-use agent integration, Anthropic Computer Use support, secure remote browser access.'),
    ('https://github.com/AbanteAI/qa-party', 'Development Tools & Libraries', 'QA-Party Prototyping Kit', 'A full-stack TypeScript (React/Express) boilerplate project created using Mentat for rapid application prototyping and testing.', 'boilerplate, typescript, react, express, prototyping', 'Strictly typed client-server architecture, pre-configured linting/env setups, modular API routing, Mentat-optimized structure.'),
    ('https://github.com/AbanteAI/vscode', 'AI Agents & Frameworks', 'Agentic VS Code Fork', 'A specialized fork of VS Code designed to support autonomous AI agents with native UI elements for multi-step planning and deep terminal control.', 'ide, vscode-fork, agentic-ui, automation, antigravity', 'Native Accept/Reject UX, enhanced programmatic terminal access, integrated diff views for agentic edits, optimized usage limits.'),
    ('https://github.com/open-webui/mcpo', 'Infrastructure', 'MCPO: MCP-to-OpenAPI Proxy', 'A utility that converts local Model Context Protocol (MCP) servers into standard REST/OpenAPI endpoints for cloud and web-based LLM clients.', 'mcp, bridge, proxy, openapi, infrastructure', 'Zero-config Swagger UI generation, API-key and OAuth 2.1 protection, hot-reloading configurations, production-ready reverse proxy support.')
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
print('Successfully injected batch 12.')
