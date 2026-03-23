import sqlite3

data = [
    ('https://github.com/universal-tool-calling-protocol/utcp-mcp', 'Connectivity & Interoperability (MCP/A2A)', 'Universal Tool Calling (UTCP)', 'An open standard designed as a lightweight alternative to MCP, allowing agents to call tools directly via their native protocols (HTTP/gRPC) without proxy wrappers.', 'Direct native execution, OpenAPI auto-ingestion, Zero "wrapper tax," Low-latency tool calling.', 9, 'utcp, protocol, standard, tool-calling, interop'),
    ('https://github.com/huggingface/smolagents', 'Agent Orchestration & Workflow', 'HuggingFace smolagents', 'A minimalist agent framework focused on "Action as Code" where primary agents write and execute Python to solve complex tasks.', 'Python CodeAgent execution, Secure E2B/Docker sandboxing, Model & Tool agnostic, ~1000 line core logic.', 8, 'smolagents, huggingface, code-as-action, sdk, python'),
    ('https://www.anthropic.com/engineering/code-execution-with-mcp', 'Guides & Industry Trends', 'Progressive Code Execution', 'An architectural pattern from Anthropic for reducing token usage by having agents write code to interact with tool schemas lazily.', '98% token reduction, Progressive schema disclosure, Client-side data filtering, Enhanced context privacy.', 10, 'anthropic, context-engineering, code-execution, optimization'),
    ('https://github.com/microsoft/mcp-gateway', 'Infrastructure & Proxy Layers', 'Microsoft MCP Gateway', 'An enterprise-grade reverse proxy and management plane for MCP servers, optimized for Kubernetes and cloud-scale deployment.', 'Session-aware routing, Entra ID identity propagation, Centralized governance/policy, Multi-server lifecycle management.', 9, 'mcp, gateway, microsoft, infrastructure, enterprise')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, mf, score, tags in data:
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
print('Successfully injected batch 22.')
