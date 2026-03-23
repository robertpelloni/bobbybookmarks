import sqlite3

data = [
    ('https://github.com/theredsix/agent-browser-protocol', 'Connectivity & Interoperability (MCP/A2A)', 'Agent Browser Protocol', 'A Chromium fork embedding MCP and REST APIs directly into the browser engine, solving the race condition between agents and live web pages via deterministic step execution.', 'browser-automation, protocol, chromium, mcp, deterministic', 'Deterministic Step Machine (freezes JS between actions), Engine-level IO thread routing (~100ms overhead), multimodal state output (Accessibility Tree + Screenshot).'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1rqyr4i/hashline_edit_plugin/', 'Context Engineering & Isolation', 'HashLine: OpenCode Edit', 'A high-performance editing plugin for OpenCode CLI that injects unique hashes per line to ensure context clarity and eliminate "edit before read" agent hallucinations.', 'context-engineering, opencode, editing, optimization, cli', 'Unique per-line hash injection, eliminates brittle line-number reliance, highly optimized for Codex 5.3 context windows.'),
    ('https://www.reddit.com/r/mcp/comments/1rr0ja7/webmcp_in_a_react_app_tools_that_update_per_page/', 'Connectivity & Interoperability (MCP/A2A)', 'WebMCP: React Integration', 'A browser-native execution model that exposes React/SPA state directly to AI agents via `navigator.modelContext`, replacing brittle DOM scraping with structured schema tools.', 'mcp, react, web-native, browser-automation, frontend', 'Component-lifecycle contextual tool registration, schema-defined interaction (JSON input vs DOM clicks), native Human-in-the-Loop (`requestUserInteraction`).'),
    ('https://www.reddit.com/r/AIDeveloperNews/comments/1rqkymk/just_found_llmock_by_copilotkit_a_deterministic/', 'Development Tools & Libraries', 'LLMock: Deterministic Tests', 'A standalone, deterministic mock LLM server (CopilotKit) designed to simulate authentic multi-provider SSE streams for CI/CD testing without real API costs.', 'testing, ci-cd, mocking, orchestration, dev-tools', 'Multi-provider SSE simulation (OpenAI/Claude/Gemini), JSON fixture-based routing, real cross-process HTTP server, error injection simulation.')
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
print('Successfully injected batch 186.')