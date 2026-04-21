import sqlite3

data = [
    ('https://github.com/tensorchord/Awesome-LLMOps', 'Guides & Industry Trends', 'Awesome-LLMOps (Agentic)', 'A curated directory of LLMOps tools reflecting the 2026 shift toward agent-specific observability, tracing, and multi-agent orchestration.', 'llmops, observability, agent-ops, orchestration, directory', 'Agent-specific tracing, drift detection for autonomous workers, dedicated "Context Engine" categories, unified MCP integration paths.'),
    ('https://github.com/wusimpl/AntigravityQuotaWatcher', 'Infrastructure & Proxy Layers', 'Antigravity Quota Watcher', 'A real-time monitoring utility for Google Antigravity and Kiro credits, featuring status bar indicators and a multi-account management dashboard.', 'monitoring, quota, antigravity, gemini, usage-tracking', 'Real-time VS Code status polling, color-coded health indicators, direct GOOGLE_API sync, multi-account credential auto-import.'),
    ('https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools', 'Guides & Industry Trends', 'AI Tools System Prompt Repo', 'A high-value research collection of extracted system prompts and tool configurations from top-tier agents like Cursor, Devin, and Windsurf.', 'prompt-engineering, reverse-engineering, reasoning-chains, benchmarks, research', 'Extracted agentic reasoning loops, meta-prompting templates, security benchmarking for instruction leakage, internal tool schema visibility.'),
    ('https://github.com/ulab-uiuc/LLMRouter', 'Infrastructure & Proxy Layers', 'UIUC LLM Router (Router-R1)', 'An intelligent model routing framework that uses RL and semantic classification to dynamically route queries to the most cost-effective model.', 'routing, model-selection, rl, optimization, cost-reduction', '16+ Built-in routing strategies, Router-R1 (NeurIPS \\'25) integration, unified CLI/Web interface, plugin-based custom routing logic.')
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
print('Successfully injected batch 46.')
