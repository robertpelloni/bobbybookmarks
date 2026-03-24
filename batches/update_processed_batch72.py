import sqlite3

data = [
    ('https://github.com/bytedance/UI-TARS-desktop', 'Interface & Developer UX', 'UI-TARS: Native GUI Agent', 'A multimodal AI agent stack that "sees" the screen and emulates human mouse/keyboard input to operate any software without specialized APIs.', 'ui-tars, gui-agent, computer-use, multimodal, vision-agent', 'Vision-based UI recognition, cross-platform (Win/Mac/Browser) control, Seed-1.5-VL model backbone, natural language command grounding.'),
    ('https://github.com/browser-use/browser-use', 'Interface & Developer UX', 'Browser-use Framework', 'A Python library designed to make the entire web accessible to agents via high-level navigation, interaction, and data extraction tools.', 'browser-use, automation, playwright, web-agent, python', 'Multi-step web tasking, Stealth Mode bot-bypass, Browser Use Cloud scaling, integrated Claude Code skill support.'),
    ('https://github.com/boxlite-labs/boxlite', 'Infrastructure & Proxy Layers', 'BoxLite: Stateful Sandboxes', 'A lightweight, local-first micro-VM platform written in Rust that provides secure and persistent execution environments for AI agents.', 'boxlite, microvm, rust, security, stateful-execution', 'Hardware-level isolation (KVM/Hypervisor), 200ms instant boot, persistent state snapshots, async-first API for agents.'),
    ('https://github.com/clawdbot/clawdbot', 'Connectivity & Interoperability (MCP/A2A)', 'OpenClaw Personal AI OS', 'A multi-channel personal AI gateway that connects a single agent session to 20+ messaging platforms including WhatsApp, iMessage, and Slack.', 'openclaw, gateway, omnichannel, personal-ai, nodejs', '20+ Platform connectors, native iOS/Android companion apps, "Talk Mode" wake-word support, Live Canvas visual workspace.')
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
print('Successfully injected batch 38.')
