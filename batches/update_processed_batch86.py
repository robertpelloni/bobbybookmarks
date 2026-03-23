import sqlite3

data = [
    ('https://news.ycombinator.com/item?id=46873294', 'Guides & Industry Trends', 'HN: Death of Prompt Engineering', 'A discussion on how frontier models (Claude 4.6/GPT-5) have become "intent-aware," making magic-keyword prompt engineering obsolete.', 'philosophy, trends, prompt-engineering, intent-awareness, future-of-work', 'System prompting vs User prompting bifurcation, shift to product design over keyword hacking, reasoning-aware model performance.'),
    ('https://news.ycombinator.com/item?id=46874097', 'Infrastructure & Proxy Layers', 'HN: Local 100B Models', 'Technical deep-dive into new quantization techniques enabling 100B+ parameter models to run on standard 64GB RAM consumer hardware.', 'local-llm, quantization, privacy, infrastructure, consumer-hardware', 'BitNet 1.58b optimization, high-speed local inference, Personal Knowledge Graph privacy, API-free autonomous agent foundations.'),
    ('https://news.ycombinator.com/item?id=46874139', 'Development Tools & Libraries', 'HN: Omni-Repo Sync (Submodule Fix)', 'A tool designed to manage complex git submodule dependencies across massive monorepos using a dependency-aware merging algorithm.', 'git, monorepo, submodules, dev-tools, synchronization', 'Dependency-aware merge algorithm, "Dry-run" tree visualization, prevention of "unrelated histories" errors, large-scale repo management.'),
    ('https://news.ycombinator.com/item?id=46875033', 'Guides & Industry Trends', 'HN: 2026 State of WebAssembly', 'An annual report on the rise of Wasm-native frameworks that bypass the JavaScript bridge entirely for high-performance web UIs.', 'wasm, web-performance, infrastructure, web-standards, frontend', 'Wasm-native UI frameworks, JS-bridge elimination, mobile browser performance optimization, Wasm-based microservices adoption.'),
    ('https://news.ycombinator.com/item?id=46879372', 'Guides & Industry Trends', 'HN: Claude 4.6 First Impressions', "A benchmark-driven comparison of Claude 4.6 vs GPT-5, highlighting Claude's dominance in 2M+ token long-context coherence.", 'benchmarks, claude, gpt-5, long-context, research', '2M+ Token coherence analysis, codebase reasoning benchmarks, legal/technical research performance, competitive model landscape.'),
    ('https://news.ycombinator.com/item?id=46897737', 'Guides & Industry Trends', 'HN: Post-Quantum Cryptography', 'A discussion on the 2026 federal mandate requiring transition to quantum-resistant algorithms (Kyber/Dilithium) for all sensitive systems.', 'security, cryptography, quantum-computing, compliance, privacy', 'Quantum-resistant algorithm adoption (Kyber), "Store Now Decrypt Later" threat analysis, federal security mandates, long-term data protection.'),
    ('https://news.ycombinator.com/item?id=46901233', 'Development Tools & Libraries', 'HN: ClearLedger (Open Source 2FA)', 'A self-hosted, privacy-first alternative to commercial 2FA providers, featuring real TOTP setup and modern frontend integration.', 'security, 2fa, privacy, open-source, totp', 'Self-hosted privacy-first 2FA, real TOTP setup flow, modern React/TypeScript integration, auditable security logic.'),
    ('https://news.ycombinator.com/item?id=46902223', 'Guides & Industry Trends', 'HN: The Case for Small Software', 'An essay advocating for "Single-Purpose Tools" that prioritize architectural simplicity and UI stability over feature bloat.', 'philosophy, minimalism, saas, architectural-simplicity, stability', 'Single-purpose tool advocacy, UI freeze benefits, comparison to unix-philosophy tools (grep/vim), critique of modern SaaS bloat.')
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
print('Successfully injected batch 52.')
