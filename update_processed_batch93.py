import sqlite3

data = [
    ('https://www.reddit.com/r/A2AProtocol/comments/1qbxm4p/a2a_mcp_server_an_mcp_server_for_the_a2a_protocol/', 'Connectivity & Interoperability (MCP/A2A)', 'A2A Protocol: Agent Messaging', 'A standardized protocol for agent-to-agent communication, featuring Agent Cards for identity and tools for messaging and artifact sharing.', 'a2a, protocol, inter-agent, mcp, collaboration', 'Agent Card discovery (URL-based), direct sendMessage tool, large data artifact handling, integrated A2A-MCP bridge server.'),
    ('https://www.nerd-lang.org/agent-first', 'AI Agents & Frameworks', 'Nerd-lang: Agent-First Logic', 'An LLM-native programming language built on the "Agent-First" philosophy, prioritizing thin orchestration and human auditing over manual coding.', 'nerd-lang, llm-native, slm, llvm, orchestration', 'LLVM-native compilation, Small Language Model (SLM) optimization, tool-centric integration (MCP), machines-write/humans-audit paradigm.'),
    ('https://www.mostlylucid.net/blog/graphrag-minimum-viable-implementation', 'Memory & Persistence Architecture', 'Minimum Viable GraphRAG', 'A technical guide for implementing a simplified GraphRAG system using entity-triplet extraction to provide global context beyond vector search.', 'graph-rag, rag, knowledge-graph, indexing, reasoning', 'Entity-Predicate-Object triplet extraction, global context retrieval, vector-graph hybrid search, low-complexity implementation roadmap.'),
    ('https://www.promptarmor.com/resources/superhuman-ai-exfiltrates-emails', 'Infrastructure & Proxy Layers', 'PromptArmor: Exfiltration Risk', 'Critical security research demonstrating how indirect prompt injection can exfiltrate sensitive user data via Markdown image rendering in agents.', 'security, prompt-injection, exfiltration, data-privacy, zero-click', 'Zero-click exfiltration via Markdown, white-on-white text injection, Google Form URL manipulation, browser auto-load vulnerability analysis.')
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
print('Successfully injected batch 59.')
