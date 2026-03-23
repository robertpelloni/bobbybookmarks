import sqlite3

data = [
    ('https://microsoft.github.io/autogen/stable/index.html', 'Agent Orchestration & Workflow', 'Microsoft Agent Framework (AutoGen GA)', 'The General Availability (GA) release of Microsoft\'s unified agent framework, featuring an Orleans-based Actor Model architecture and native MCP/A2A support.', 'autogen, orchestration, microsoft, actor-model, framework', 'Orleans-based Actor Model, event-driven asynchronous runtime, native MCP/A2A integration, production-grade OTel observability.'),
    ('https://modal.com/llm-almanac/advisor', 'Infrastructure & Proxy Layers', 'Modal LLM Almanac: Self-Hosting', 'A 2026 economic analysis by Modal highlighting the 8x throughput gains and cost-effectiveness of self-hosting open-weight models (Llama 4/DeepSeek) on H100 clusters.', 'infrastructure, modal, self-hosting, economics, throughput', '8x throughput increase via batching (~20k tokens/sec), speculative decoding support (SGLang), self-hosting vs API economic shift, Offline/Online workload triad.'),
    ('https://minusx.ai/blog/decoding-claude-code', 'Agent Orchestration & Workflow', 'Claude Code: Single-Loop Architecture', 'An architectural deconstruction of Claude Code revealing its reliance on a single main loop, small model (Haiku) offloading, and direct `ripgrep` search over vector RAG.', 'claude-code, architecture, orchestration, optimization, search', 'Single-loop/one-branch architecture, 50% Haiku offloading for low-level tasks, direct `ripgrep/find` over vector RAG, mandatory `claude.md` grounding.'),
    ('https://monero.forex/is-monero-totally-private-a-comprehensive-analysis-of-de-anonymization-attacks-against-the-privacy-coin', 'Guides & Industry Trends', 'Monero: Privacy Audit 2026', 'A technical deep-dive into the 2026 privacy landscape of Monero, covering the FCMP++ zero-knowledge upgrade and persistent EAE/Flooding vulnerabilities.', 'crypto, privacy, monero, security, zero-knowledge', 'FCMP++ zero-knowledge upgrade, EAE (Eve-Alice-Eve) केवाईसी-exchange vulnerability, decoy-clogging Flooding attacks, full on-chain fungibility analysis.')
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
print('Successfully injected batch 138.')