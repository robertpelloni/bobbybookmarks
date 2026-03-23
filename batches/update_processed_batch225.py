import sqlite3

data = [
    ('https://github.com/paularlott/llmrouter', 'Agent Orchestration & Workflow', 'LLMRouter: Smart Routing', 'An intelligent inference routing system that dynamically selects the most suitable LLM based on task complexity, cost, and performance requirements.', 'orchestration, routing, optimization, inference, llmrouter', 'Dynamic cost/performance routing, 16+ routing models (KNN/SVM/Elo), ComfyUI visual pipeline builder, OpenClaw production integration.'),
    ('https://github.com/cortexd-labs/neurond', 'Infrastructure & Proxy Layers', 'Cortical Labs: Neurond', 'Biological computing infrastructure ("Wetware as a Service") utilizing live human neurons on silicon chips for extreme energy-efficient machine learning.', 'biocomputing, hardware, wetware, cortical-labs, research', 'Live human neuron biological chips (CL1), "Wetware as a Service" remote access, ultra-low energy footprint, rapid biological plasticity learning.'),
    ('https://github.com/vtxf/mcp-all-in-one', 'Connectivity & Interoperability (MCP/A2A)', 'MCP-All-in-One: Bundler', 'A comprehensive aggregator and manager for the Model Context Protocol (MCP), bundling multiple related tools into standardized servers to reduce deployment overhead.', 'mcp, aggregator, gateway, infrastructure, orchestration', 'Bundled multi-tool MCP servers, single-endpoint proxying, OAuth 2.1 enterprise security, unified manifest-based permissions.'),
    ('https://github.com/david-martin/mcp-helper', 'Development Tools & Libraries', 'MCP-Helper: Dev Utility', 'A developer-centric utility framework designed to simplify the creation, scaffolding, and real-time debugging of Model Context Protocol (MCP) servers.', 'mcp, sdk, dev-tools, debugging, infrastructure', 'Python/Node.js scaffolding templates, real-time MCP Inspector integration, standardized Prompt/Resource/Tool primitives, local-to-cloud bridge deployment.')
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
print('Successfully injected batch 185.')