import sqlite3

data = [
    ('https://github.com/alvii147/piston-mcp', 'Infrastructure & Proxy Layers', 'Piston Remote Execution', 'An MCP server implementation for the Piston engine, enabling agents to execute code in 70+ languages without local runtimes.', 'mcp, code-execution, piston, remote-runtime, security', '70+ Language support, Linux namespace isolation, unprivileged user execution, standardized tool-calling interface.'),
    ('https://github.com/zerocore-ai/microsandbox', 'Infrastructure & Proxy Layers', 'microsandbox: MicroVM Isolation', 'A local-first, hardware-isolated execution environment for AI agents that uses microVMs (libkrun) for strong security boundaries.', 'sandboxing, microvm, security, oci-compatible, infrastructure', '200ms Instant startup, hardware-level libkrun isolation, OCI container image support, built-in lifecycle MCP server.'),
    ('https://github.com/e2b-dev/code-interpreter', 'Infrastructure & Proxy Layers', 'E2B Stateful Sandboxes', 'Cloud-native infrastructure providing long-running, stateful sandboxes for AI agents to perform complex data analysis and coding tasks.', 'e2b, stateful-execution, cloud-sandbox, code-interpreter, infrastructure', 'Persistent session state, Python/JS/TS SDKs, resource monitoring, high-scale enterprise readiness.'),
    ('https://github.com/cohere-ai/cohere-terrarium', 'Infrastructure & Proxy Layers', 'Cohere Terrarium (WASM)', 'An ultra-secure, stateless Python sandbox using Pyodide (WASM) to isolate LLM-generated code within a restricted browser-like environment.', 'wasm, pyodide, stateless, security, python', 'WebAssembly-native isolation, zero host filesystem access, stateless request recycling, multi-layered Docker/Node/WASM wrapping.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 9) for d in data]:
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
print('Successfully injected batch 26.')
