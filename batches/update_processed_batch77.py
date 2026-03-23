import sqlite3

data = [
    ('https://github.com/open-webui/open-webui', 'Interface & Developer UX', 'Open WebUI: Local-First Chat', 'A feature-rich, self-hosted AI interface designed for entirely offline operation, serving as a universal frontend for Ollama and OpenAI APIs.', 'local-first, ollama, self-hosted, gui, privacy', 'Full offline support, built-in local RAG, integrated Whisper/TTS, multi-user management, seamless Ollama integration.'),
    ('https://github.com/papercomputeco/stereOS', 'Infrastructure & Proxy Layers', 'stereOS: Agentic NixOS', 'A minimal, NixOS-based operating system purpose-built and hardened for hosting autonomous AI agents with a restricted execution footprint.', 'ai-os, nixos, security, hardening, orchestration', 'Restricted binary PATH, specialized stereosd/agentd daemons, declarative agent machine images (mixtapes), minimal attack surface.'),
    ('https://github.com/postrv/forgemax', 'Infrastructure & Proxy Layers', 'ForgeMax: Sandboxed Gateway', 'A local MCP gateway that consolidates multiple tool servers into search/execute tools and runs LLM-generated code in a Deno-based V8 isolate.', 'mcp, gateway, sandboxing, deno, context-efficiency', 'Consolidated search/execute interface, Deno-core V8 isolation, context-efficient tool loading, opaque credential protection.'),
    ('https://github.com/qodo-ai/pr-agent', 'Agent Orchestration & Workflow', 'Qodo PR-Agent', 'An open-source AI agent that automates the pull request lifecycle, providing auto-descriptions, code reviews, and actionable improvements.', 'autonomous-pr, code-review, automation, github, gitlab', 'Automated PR descriptions, interactive slash-command reviews, smart hunk-compression for context, multi-platform git integration.')
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
print('Successfully injected batch 43.')
