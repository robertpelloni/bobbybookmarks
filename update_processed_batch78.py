import sqlite3

data = [
    ('https://github.com/runtm-ai/runtm-coding-agent-runtime-control-plane', 'Infrastructure & Proxy Layers', 'runtm: Agent Control Plane', 'A runtime and control plane designed specifically for software built by agents, enabling rapid Generate-Deploy-Observe-Repeat loops.', 'infrastructure, deployment, control-plane, flyio, firecracker', 'Ephemeral app lifecycle (init/deploy/destroy), human-in-the-loop infra approvals, tight feedback loops for coding agents, Firecracker VM support.'),
    ('https://github.com/runvnc/mindroot', 'AI Agents & Frameworks', 'Mindroot Framework', 'A plugin-based Python framework for creating and sharing AI agents with customizable 3D graph visualizations of agent reasoning chains.', 'framework, python, 3d-visualization, agent-hub, rag', 'Hook-based extensible architecture, 3D Graph UI for reasoning, integrated RAG knowledge sharing, community persona registry.'),
    ('https://github.com/samuel-vitorino/sopro', 'Interface & Developer UX', 'SoPro: Efficiency-First TTS', 'A lightweight (169M) Text-to-Speech model optimized for CPU-based real-time voice cloning and low-latency agent interaction.', 'tts, voice-cloning, optimization, cpu-native, interaction', 'Zero-shot 3-12s voice cloning, 0.25 RTF on Apple Silicon, non-Transformer convolution architecture, real-time streaming support.'),
    ('https://github.com/shekohex/opencode-pty', 'Interface & Developer UX', 'OpenCode PTY Manager', 'A specialized plugin for interactive Pseudo-Terminal (PTY) management, allowing agents to control background processes and paginated CLI output.', 'pty, cli, interactive-terminal, opencode, automation', 'Interactive background process control, regex-based terminal filtering, persistent terminal sessions, automated input/output paginations.')
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
print('Successfully injected batch 44.')
