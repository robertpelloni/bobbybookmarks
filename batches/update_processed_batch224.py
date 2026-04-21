import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1rnteki/fixflow_collective_memory_for_ai_agents_one_agent', 'Memory & Persistence Architecture', 'FixFlow: Collective Memory', 'An MCP server designed to create a shared "Knowledge Base" (KB) for AI agents, operating on the principle that "one agent solves a bug — every agent gets the fix instantly."', 'mcp, memory, knowledge-base, collective-intelligence, debugging', 'Shared agent Knowledge Base (KB), `save_kb_card` write capability, full-text search with success-rate ranking, cross-agent bug-fix synchronization.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1rms6qg/update_truemem_v12_optional_semantic_embeddings', 'Memory & Persistence Architecture', 'TrueMem v1.2: OpenCode', 'A specialized memory management layer for OpenCode CLI that uses local vector embeddings to retrieve relevant code snippets without context window pollution.', 'opencode, memory, semantic-search, cli, persistence', 'Atomic state snapshots (prevents context loss during model swaps), semantic retrieval via local vector embeddings, cross-session pattern linking.'),
    ('https://github.com/Beam-directory/beam-protocol', 'Infrastructure & Proxy Layers', 'Beam Protocol: Cross-Chain', 'A privacy-focused DeFi ecosystem and protocol utilizing Mimblewimble architecture to enable cross-chain messaging and confidential asset transactions.', 'crypto, blockchain, privacy, mimblewimble, protocol', 'Mimblewimble "Scriptless Scripts", Dandelion network traffic obfuscation, optional transaction auditability ("window blind" feature), confidential asset support.'),
    ('https://github.com/clkao/agentlore', 'Context Engineering & Isolation', 'AgentLore: Persona Context', 'A framework for managing AI agent "personalities" and long-term project lore, ensuring role consistency across swarms without bloating token counts.', 'context-engineering, memory, role-playing, orchestration, lore', 'Dynamic "world-building" context injection, role/boundary consistency enforcement, behavioral state versioning (rollback capability), swarm-wide lore synchronization.')
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
print('Successfully injected batch 184.')