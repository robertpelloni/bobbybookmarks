import sqlite3

data = [
    ('https://github.com/alinaqi/claude-bootstrap', 'Agent Orchestration & Workflow', 'Claude Project Bootstrapper', 'An opinionated project initialization system for Claude Code that automates the setup of multi-agent teams and TDD pipelines.', 'bootstrap, claude-code, tdd, automation, project-setup', 'Automated agent team spawning, strict TDD pipeline enforcement, existing codebase tech-stack detection, pre-configured domain skills.'),
    ('https://github.com/amantus-ai/vibetunnel', 'Infrastructure & Proxy Layers', 'VibeTunnel: Local-to-Cloud', 'A secure tunneling utility that turns local terminal sessions into web-accessible dashboard links for remote AI agent control.', 'tunneling, remote-access, cli, dashboard, infrastructure', 'Secure browser-based terminal, Git worktree synchronization, native mobile push notifications, mobile image upload support.'),
    ('https://github.com/automazeio/vibeproxy', 'Infrastructure & Proxy Layers', 'VibeProxy Subscription Hub', 'A macOS utility that acts as a unified proxy for sharing AI subscriptions across multiple third-party agent tools without separate API keys.', 'proxy, infrastructure, subscription-sharing, macos, automation', 'OAuth token management, Vercel AI Gateway integration, multi-account load balancing, menu bar control interface.'),
    ('https://github.com/badrisnarayanan/antigravity-claude-proxy', 'Infrastructure & Proxy Layers', 'Antigravity API Bridge', "A persistence-focused API bridge that enables the official Claude Code CLI to run on top of Antigravity's cloud-hosted model endpoints.", 'proxy, bridge, claude-code, antigravity, persistence', 'Persistent OAuth session storage, intelligent model load balancing, "Gemini Thinking" budget clamping, local management dashboard.')
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
print('Successfully injected batch 37.')
