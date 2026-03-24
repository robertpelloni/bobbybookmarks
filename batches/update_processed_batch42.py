import sqlite3

data = [
    ('https://github.com/GoogleCloudPlatform/cloud-run-mcp', 'MCP', 'Cloud Run MCP Server', 'An implementation of the Model Context Protocol that allows AI agents to interact with Google Cloud Run for deployment and management.', 'mcp, gcp, cloud-run, deployment, infrastructure', 'Deploy file contents/folders, List/Get services, Fetch service logs, Create GCP projects.'),
    ('https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio', 'AI Agents & Frameworks', 'Vertex AI Creative Studio', 'A showcase playground for Google Cloud generative media APIs, including tools for video, image, and music generation.', 'vertex-ai, multimodal, media-gen, mesop, gcp', 'Veo 3.1 video gen, Imagen 4.0 image gen, Lyria music gen, Asynchronous task monitoring.'),
    ('https://github.com/gemini-cli-extensions/conductor', 'AI Agents & Frameworks', 'Conductor CDD Orchestrator', 'An extension for Gemini CLI that enforces a strict Context-Driven Development protocol for specifying, planning, and implementing features.', 'gemini-cli, cdd, orchestration, project-management, workflow', 'Proactive context management, Spec/Plan generation, Atomic git commits, Phased implementation tracking.'),
    ('https://github.com/gemini-cli-extensions/mcp-toolbox', 'MCP', 'MCP Database Toolbox', 'A collection of enterprise-grade agent skills for connecting AI agents to Cloud SQL, AlloyDB, and BigQuery data sources.', 'mcp, database, gcp, analytics, enterprise', 'Cloud SQL Postgres Admin/Data skills, automatic skill discovery, enterprise data awareness, validated tool results.'),
    ('https://github.com/google-gemini/gemini-mcp-server', 'MCP', 'Official Gemini MCP Server', "A reference implementation that exposes Google's Gemini AI capabilities, including the 2M context window, to any MCP client.", 'mcp, gemini, google, multimodal, search-grounding', 'multimodal vision/image analysis, Google Search grounding, 2M token context access, asynchronous video generation.'),
    ('https://github.com/modelcontextprotocol/specification', 'AI Agents & Frameworks', 'MCP Specification', 'The foundational open standard for secure and standardized integration between AI applications and external data sources or tools.', 'mcp, standard, protocol, interoperability, specification', 'JSON-RPC communication, TypeScript schema definitions, modular Resource/Tool/Prompt model, client-server contract.'),
    ('https://github.com/modelcontextprotocol/servers', 'MCP', 'MCP Reference Servers', 'The official collection of reference and community-contributed MCP servers for professional tools like GitHub, Slack, and AWS.', 'mcp, community, registry, connectors, tools', 'Official Fetch/Git/Memory servers, community integrations (Postgres/Drive), production-ready drivers.'),
    ('https://github.com/modelcontextprotocol/quickstart', 'Guides & Articles', 'MCP Quickstart Guide', 'Educational resources and minimal examples designed to teach developers how to build and connect their own MCP servers.', 'mcp, quickstart, tutorial, developer-guide, learning', 'Weather server example, Multi-language support (Py/TS), core concept walkthroughs (Tools/Resources), Client implementation code.')
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
print('Successfully injected batch 9.')
