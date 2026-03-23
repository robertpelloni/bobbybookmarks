import sqlite3

data = [
    ('https://www.smabbler.com/', 'Memory & Persistence Architecture', 'Smabbler: Graph Memory', 'A knowledge platform utilizing Semantic Hypergraphs (Galaxia™) to provide LLMs with a long-term memory layer based on structured reasoning rather than text chunks.', 'memory, persistence, knowledge-graph, smabbler, rag', 'Semantic Hypergraphs (long-term memory), Galaxia™ reasoning layer, 1-billion character context processing, automated data labeling.'),
    ('https://www.stagehand.dev/', 'Interface & Developer UX', 'Stagehand: AI Playwright', 'An open-source AI web automation SDK by Browserbase that acts as a resilient, self-healing alternative to Playwright by using LLMs to navigate without brittle CSS selectors.', 'browser-automation, stagehand, playwright, orchestration, testing', 'Self-healing UI navigation (no CSS selectors), AI primitives (`act`/`extract`/`observe`), CDP direct-browser communication (v3), Accessibility Tree extraction.'),
    ('https://www.theregister.com/2024/11/12/trapc_memory_safe_fork', 'Infrastructure & Proxy Layers', 'TrapC: Memory Safe C', 'A minimalist fork of the C programming language designed to eliminate Undefined Behavior (UB) and enforce memory safety through automatic lifetime management and pointer bounds checking.', 'c, memory-safety, trapc, compiler, infrastructure', 'Automatic pointer lifetime management (no GC), elimination of UB (Undefined Behavior), backwards C/C++ compatibility, AI-assisted compiler refactoring.'),
    ('https://www.tenki.cloud/', 'Development Tools & Libraries', 'Tenki Cloud: CI/CD & AI', 'A high-performance CI/CD infrastructure platform offering bare-metal GitHub Actions runners and an integrated AI agent that reviews full codebases during Pull Requests.', 'ci-cd, github-actions, code-review, automation, dev-tools', 'Bare-metal GitHub Actions runners (35% faster), automated AI Pull Request code reviewer, drop-in YAML replacement wizard, 50% CI cost reduction.')
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
print('Successfully injected batch 176.')