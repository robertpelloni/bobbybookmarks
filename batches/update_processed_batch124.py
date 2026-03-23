import sqlite3

data = [
    ('https://www.reddit.com/r/bun/comments/1r8rrgi/blazediff_now_has_native_bun_matchers_rustpowered/', 'Development Tools & Libraries', 'BlazeDiff: Rust Backend', 'A high-performance image diffing library that uses a Rust backend via N-API to achieve computational peak performance for visual regression.', 'rust, performance, image-diffing, n-api, bun', 'Fastest overall image diff, hybrid JS/Rust architecture, SSIM/GMSD algorithmic rigor, verified against MATLAB standards.'),
    ('https://www.reddit.com/r/claude/comments/1r06tvt/i_built_a_claudemd_that_solves_the/', 'Memory & Persistence Architecture', 'CLAUDE.md: Persistent State', 'A disk-persistent state machine mechanism that replaces volatile conversation memory with structured Markdown handoff files (plan/findings/progress).', 'memory-architecture, persistence, context-management, state-machine, handoff', 'Handoff file serialization, 10x token savings on warm starts, prevention of auto-summarization loss, structured rationale preservation.'),
    ('https://www.reddit.com/r/claude/comments/1q7mxe6/my_manusstyle_claude_code_skill_now_automatically/', 'Agent Orchestration & Workflow', 'PreToolUse Grounding Hooks', 'An orchestration pattern that enforces agent alignment by automatically re-reading task manifests and findings before every destructive file or terminal action.', 'orchestration, grounding, alignment, hooks, autonomous-dev', 'PreToolUse automatic re-reading, 2-action findings persistence rule, 3-strike error protocol, elimination of agentic drift.'),
    ('https://www.reddit.com/r/chutesAI/comments/1qk5xx1/3_new_chutes_to_spread_the_weight_created_by_tee/', 'Infrastructure & Proxy Layers', 'Chutes: TEE/fp8 Infrastructure', 'A distributed compute infrastructure providing Trusted Execution Environments (TEE) and fp8-quantized model "chutes" for high-availability agent hosting.', 'infrastructure, tee, security, quantization, distributed-compute', 'Secure TEE agent hosting, fp8 high-availability fallbacks, load-balanced model distribution, low-latency agent inference.')
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
print('Successfully injected batch 74.')
