import sqlite3

data = [
    ('https://docs.letta.com/guides/agents/agent-file/', 'AI Agents & Frameworks', 'Letta Agent-File (.af)', 'An open standard for serializing the complete state of an AI agent, enabling "Agent-as-Code" workflows and version-controlled persistence.', 'letta, agent-as-code, persistence, serialization, standard', 'Portable .af file format, system prompt & tool versioning, persistent memory block capture, git-backed agent CI/CD support.'),
    ('https://docs.letta.com/guides/agents/human-in-the-loop/', 'Interface & Developer UX', 'Letta HITL Patterns', 'A set of collaborative interaction patterns designed to keep humans informed and in control of autonomous agent actions.', 'hitl, human-in-the-loop, security, governance, ux', 'Tool-Gate approvals, live memory editing (ADE), adaptive clarification questioning, supervisor sign-off nodes.'),
    ('https://docs.molt.bot/gateway', 'Infrastructure & Proxy Layers', 'Moltbot Multi-Channel Gateway', 'A centralized messaging hub that bridges self-hosted AI agents to WhatsApp, Telegram, Discord, and Slack via a unified WebSocket API.', 'messaging, gateway, moltbot, infrastructure, omnichannel', 'Multi-channel hub (6 platforms), local WebSocket API, proactive agent "heartbeats," session-based message routing.'),
    ('https://docs.openhands.dev/sdk/guides/hello-world', 'AI Agents & Frameworks', 'OpenHands ACI Standard', 'A software agent SDK that defines the Agent-Computer Interface (ACI), providing agents with direct, sandboxed access to terminals and filesystems.', 'openhands, aci, sdk, automation, computer-use', 'Conversation-Workspace pattern, Docker-sandboxed execution, native terminal/editor toolset, multi-model backend abstraction.')
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
print('Successfully injected batch 32.')
