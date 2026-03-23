import sqlite3

data = [
    ('https://github.com/liberzon/claude-hooks', 'Agent Orchestration & Workflow', 'Claude Code Hooks', 'A framework enabling shell scripts to trigger automatically at specific Claude Code lifecycle events, enforcing safety guardrails and project standards.', 'claude-code, hooks, automation, security, dev-tools', 'Lifecycle event triggers (BeforeCommit/PostCompact), context re-injection upon compaction, automated linting/formatting, secret file access blocking.'),
    ('https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative', 'Connectivity & Interoperability (MCP/A2A)', 'Apideck CLI: Context Saver', 'A "CLI-first" alternative to MCP that reduces context starvation by replacing massive JSON tool schemas with an 80-token prompt and on-demand `--help` discovery.', 'mcp, optimization, context-engineering, cli, apideck', 'Progressive disclosure (on-demand `--help` lookup), massive context reduction (50k tokens to 80 tokens), native compatibility with shell-enabled agents.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1rvxzc0/cocoindexcode_cli_for_opencode_super_lightweight', 'Interface & Developer UX', 'OpenCode CLI (cocoindexcode)', 'A Go-based open-source CLI/TUI coding assistant that features built-in multi-provider support, persistent sessions, and automated context compaction.', 'opencode, cli, orchestration, context-management, dev-tools', 'Multi-provider fallback (DeepSeek/Anthropic/Ollama), Auto-Compaction at 95% context limit, Language Server Protocol (LSP) integration, SQLite session forking.'),
    ('https://www.reddit.com/r/Rag/comments/1rw5637/releasing_bb25_bayesian_bm25_v040', 'Memory & Persistence Architecture', 'BB25: Bayesian BM25 v0.4', 'A Rust-based library for hybrid RAG search that uses Multi-Head Attention and Bayesian temporal decay to optimize both lexical and semantic vector retrieval.', 'rag, rust, search, optimization, bb25', 'Multi-Head Attention fusion (lexical/semantic), Temporal Bayesian Transform (freshness decay), Block-Max WAND Index optimization, Platt scaling score calibration.')
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
print('Successfully injected batch 202.')