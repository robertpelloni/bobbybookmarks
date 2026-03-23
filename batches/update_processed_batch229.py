import sqlite3

data = [
    ('https://github.com/oct4pie/toolbridge?tab=readme-ov-file', 'AI Agents & Frameworks', 'ToolBridge: SFT Pipeline', 'An open-source dataset and pipeline for Supervised Fine-Tuning (SFT) designed to equip standard LLMs with robust, verified tool-calling capabilities.', 'sft, tool-calling, orchestration, dataset, pipeline', '178k+ curated SFT tool-use entries, three-phase Selection/Conversion/Filtering pipeline, automated code execution consistency validation.'),
    ('https://www.openverb.org/', 'Connectivity & Interoperability (MCP/A2A)', 'OpenVerb Protocol', 'A deterministic action layer protocol that standardizes AI real-world execution through JSON-defined "Verbs" to prevent hallucinated tool calls.', 'protocol, standard, openverb, automation, security', 'Deterministic JSON "Verb" action definitions, registry-driven execution validation, explicit side-effect/permission constraints.'),
    ('https://github.com/iii-hq/agentos', 'Agent Orchestration & Workflow', 'Agent OS v3 (Builder Methods)', 'A lightweight framework for managing and dynamically injecting architectural standards and coding context into agents like Claude Code or Cursor.', 'orchestration, context-management, standards, workflow, framework', '`discover-standards` architectural auto-documentation, dynamic context injection, project-specific "profiles" (e.g., Laravel vs Internal Tools).'),
    ('https://github.com/knowsuchagency/mcp2cli', 'Connectivity & Interoperability (MCP/A2A)', 'mcp2cli: Dynamic Discovery', 'A runtime utility that converts MCP servers and OpenAPI specs into functional CLIs without code generation, reducing agent context bloat by 99%.', 'mcp, cli, dynamic-discovery, optimization, integration', 'Zero-codegen dynamic CLI generation, 99% reduction in context window schema bloat, multi-protocol support (MCP/OpenAPI/GraphQL), built-in OAuth PKCE caching.')
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
print('Successfully injected batch 189.')