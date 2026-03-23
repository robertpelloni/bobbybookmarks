import sqlite3

data = [
    ('https://chunkhound.github.io/', 'Memory & Persistence Architecture', 'Chunkhound: cAST Chunking', 'An open-source, local-first tool that uses the Context-Aware Syntax Tree (cAST) algorithm to provide AI agents with high-fidelity, structure-aware codebase search.', 'codebase-indexing, rag, tree-sitter, local-first, search', 'Context-Aware Syntax Tree (cAST) chunking, 4.3pt retrieval benchmark gain, multi-hop semantic relationship mapping, real-time git-watch indexing.'),
    ('https://chutes.ai/app', 'Infrastructure & Proxy Layers', 'Chutes.ai: Decentralized Compute', 'A decentralized serverless compute platform on the Bittensor network for low-cost AI inference, featuring Trusted Execution Environments (TEE) for prompt privacy.', 'infrastructure, bittensor, serverless, gpu, security', 'Decentralized GPU network, TEE confidential compute, pre-built vLLM/SGLang templates, TAO-based token payment system.'),
    ('https://copy.sh/v86', 'Infrastructure & Proxy Layers', 'v86: In-Browser x86', 'A WebAssembly-based x86 emulator that runs full operating systems (Linux/Windows) directly in the browser, enabling "local-like" agent execution in a browser tab.', 'wasm, virtualization, emulator, sandboxing, browser-automation', 'x86-compatible CPU emulation, virtio hardware support, zero-install portable execution, near-native performance translation.'),
    ('https://composio.dev/blog/10-awesome-mcp-servers-to-make-your-life-easier', 'Connectivity & Interoperability (MCP/A2A)', 'Composio: Managed MCP Gateway', 'A centralized MCP gateway that manages authentication and refreshes for 250+ integrations, allowing agents to interact with SaaS tools without local setup.', 'mcp, gateway, managed-auth, saas, orchestration', '250+ managed SaaS integrations, automated OAuth/refresh handling, remote execution infrastructure, unified model context endpoint.')
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
print('Successfully injected batch 113.')