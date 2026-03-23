import sqlite3

data = [
    ('https://bolt.new/', 'Interface & Developer UX', 'Bolt.new: Browser IDE', 'An AI-powered full-stack development agent that uses StackBlitz WebContainers to build, run, and deploy Node.js apps entirely within the browser tab.', 'webcontainers, ide, stackblitz, browser-automation, full-stack', 'In-browser Node.js runtime (WebContainers), POSIX-compliant WASM OS, direct terminal/filesystem control, one-click Netlify deployment.'),
    ('https://borgbackup.readthedocs.io/en/stable', 'Infrastructure & Proxy Layers', 'BorgBackup: Deduplication', 'A high-efficiency deduplicating backup tool using content-defined chunking and authenticated AES-256 encryption for secure, daily offsite snapshots.', 'backup, security, deduplication, snapshots, storage', 'Content-defined chunking (CDC), client-side AES-256 encryption, LZ4/Zstd compression support, FUSE mountable archives.'),
    ('https://bytecodealliance.org/articles/wasmtime-26.0', 'Infrastructure & Proxy Layers', 'Wasmtime 26.0: WASM Runtime', 'A standalone WebAssembly runtime optimized for sub-5ms module instantiation and secure execution, featuring new 64-bit table support and Windows ARM64 parity.', 'wasm, runtime, performance, security, bytecode-alliance', '64-bit table extension support, Pulley interpreter for non-JIT platforms, 5-10% native execution overhead, small 15MB runtime footprint.'),
    ('https://c3-lang.org/', 'Development Tools & Libraries', 'C3 Language: C Evolution', 'A systems programming language that evolves C with modules, semantic macros, and safe slices while maintaining full binary ABI compatibility.', 'c, systems-programming, abi-compatibility, safer-c, language-design', 'Zero-cost C integration (no wrappers), semantic macro system, built-in design-by-contract (逐步 contracts), type-safe error handling (Result).')
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
print('Successfully injected batch 111.')