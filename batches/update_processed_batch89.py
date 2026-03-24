import sqlite3

data = [
    ('https://simonwillison.net/2026/Feb/12/gemini-3-deep-think/', 'Guides & Industry Trends', 'Gemini 3 Deep Think Analysis', "An evaluation of Google's reasoning-aware model, highlighting its 'Thinking Trace' transparency and unprecedented mastery of complex visual SVGs.", 'gemini, reasoning, deep-think, svg, benchmarking', '300s+ Reasoning traces, anatomically correct SVG generation, ARC-AGI-2 record holder (84.6%), zero-hallucination code architecture.'),
    ('https://sibylline.dev/articles/2026-01-22-scribe-swebench-benchmark/', 'Guides & Industry Trends', 'Scribe: Agentic Efficiency', 'A benchmark study of the Scribe harness, which reduces agent token usage by 80% while maintaining a 76% resolution rate on SWE-bench.', 'benchmarks, efficiency, token-reduction, optimization, sw-bench', '80% Token reduction, $0.50 cost-per-fix, "Harness Hook" loop detection, top-tier resolution consistency.'),
    ('https://sluongng.substack.com/p/post-agentic-code-forges', 'Agent Orchestration & Workflow', 'Post-Agentic Code Forges', 'A paradigm shift in source control where forges act as "coordination layers" for high-volume agent commits and "Prompt Requests" replace PRs.', 'git, source-control, forge, workflow, prompt-request', 'Jujutsu (jj) integration for agentic commits, "Prompt Request" (intent-based) submission, Closed-loop self-healing builds, regeneration-over-maintenance philosophy.'),
    ('https://sublang.xyz/ref/gears-ai-ready-spec-syntax/', 'AI Agents & Frameworks', 'Gears: AI-Ready Specs', 'A specialized high-density specification language designed to eliminate context rot and provide unambiguous "Compile-Time" checks for agents.', 'spec-driven, sublang, context-efficiency, documentation, standard', 'High-density architectural syntax, <2k token system ingestion, Spec-to-Code strict parity, formal behavioral constraints.')
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
print('Successfully injected batch 55.')
