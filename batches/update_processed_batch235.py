import sqlite3

data = [
    ('https://github.com/thebabush/xr', 'Development Tools & Libraries', 'xr: Fast Disassembler', 'An ultra-fast, Rust-based CLI tool designed for parallel extraction of cross-references from stripped binaries, significantly outperforming traditional disassemblers.', 'rust, reverse-engineering, binary-analysis, performance, cli', 'Parallel cross-reference extraction (from_va, to_va), ELF/Mach-O/PE support, linear/paired scanning modes, native Claude Code skill integration.'),
    ('https://github.com/loderunner/scrt', 'Infrastructure & Proxy Layers', 'scrt: CLI Secret Manager', 'An open-source, Go-based CLI secret manager that keeps the entire secret lifecycle securely within the terminal using NaCl primitives.', 'security, secrets-management, cli, go, encryption', 'NaCl (libsodium) E2E encryption, Git/S3 storage backend support, composable Unix-philosophy commands, CI/CD pipeline optimization.'),
    ('https://github.com/mostlygeek/llama-swap', 'Infrastructure & Proxy Layers', 'llama-swap: Proxy Router', 'An intelligent proxy server (Go) that allows users to hot-swap local LLMs on demand, automatically managing the lifecycle of inference servers like vLLM or llama.cpp.', 'proxy, local-llm, infrastructure, optimization, orchestration', 'Automatic inference server hot-swapping, OpenAI/Anthropic API compatibility, Time-To-Live (TTL) model unloading, "Groups" for multi-model concurrent running.'),
    ('https://github.com/NiaExperience/PearlOS', 'AI Agents & Frameworks', 'PearlOS: AI Environment', 'An open-source, browser-based "intelligent environment" powered by a self-evolving AI companion (Pearl) capable of voice interaction and autonomous codebase patching.', 'os, voice-ai, self-evolving, framework, companion', 'Real-time WebRTC voice interaction, autonomous "Sub-Agent Swarms" for self-patching, semantic multi-layer memory, Discord/Slack omni-channel awareness.'),
    ('https://www.qodo.ai/blog/qodo-outperforms-claude-in-code-review-benchmark/', 'Guides & Industry Trends', 'Qodo: Code Review SOTA', 'A 2026 benchmark report demonstrating Qodo\'s multi-agent architecture outperforming Claude Code by 12 F1 points (79% vs 67%) in production code review tasks.', 'benchmarks, code-review, qodo, claude-code, multi-agent', '79% F1 score in code review benchmarks (vs Claude 67%), superior "recall" for subtle architectural bugs, 100x cost efficiency ($0.12 vs $15 per review).')
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
print('Successfully injected batch 195.')