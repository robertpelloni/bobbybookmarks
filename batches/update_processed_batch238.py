import sqlite3

data = [
    ('https://www.reddit.com/r/opencodeCLI/comments/1rude4q/enzim_coder_now_supports_opencode_as_a_backend/', 'Connectivity & Interoperability (MCP/A2A)', 'Enzim Coder: OpenCode', 'The integration of OpenCode as a backend provider for Enzim Coder, enabling developers to run advanced models like Kimi K2.5 and Codex within the Enzim ecosystem.', 'enzim, opencode, orchestration, kimi, codex', 'OpenCode backend integration, Kimi K2.5/Codex model support, large context management (up to 300k tokens), "Antigravity" bypass potential.'),
    ('https://www.reddit.com/r/mcp/comments/1rue20c/mcp_is_dead_long_live_mcp/', 'Guides & Industry Trends', 'MCP Fragmentation 2026', 'A community analysis of the 2026 shift away from generic MCP tool-calling due to token bloat (up to 21k tokens per server) towards specialized "Agent Skills" and interactive HTML/JS UIs (SEP-1865).', 'mcp, protocol, standard, architecture, context-engineering', 'Shift from raw JSON-RPC to "Agent Skills", SEP-1865 (MCP Apps Extension) for HTML/JS UIs, mitigation of 21k+ token schema bloat.'),
    ('https://www.reddit.com/r/mcp/comments/1rug4nc/ecosystem_mcp_powering_agentic_representation_of/', 'AI Agents & Frameworks', 'Ecosystem MCP: Personhood', 'An experimental MCP architecture exploring "agentic personhood" for natural ecosystems (e.g., forests, rivers), allowing them to autonomously act in their own self-interest.', 'mcp, ecosystem, autonomous-agents, environmental, research', 'Agentic personhood for ecosystems, autonomous capital allocation (e.g., buying land), open API integration (iNaturalist/EPA), self-interest action logic.'),
    ('https://www.reddit.com/r/LangChain/comments/1rtrjqe/standard_rag_fails_terribly_on_legal_contracts_i/', 'Memory & Persistence Architecture', 'Legal GraphRAG Pattern', 'A discussion highlighting the failure of standard Vector RAG on complex legal documents and the 2026 shift toward GraphRAG (Neo4j) for mapping explicit clause relationships.', 'rag, graph-rag, legal-tech, neo4j, context-engineering', 'Neo4j GraphRAG integration, explicit clause relationship mapping (CONFLICTS_WITH), "Table of Contents" agentic research pattern, Semantic/Logical Chunking.')
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
print('Successfully injected batch 198.')