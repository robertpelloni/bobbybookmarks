import sqlite3

data = [
    ('https://www.reddit.com/r/DeepSeek/comments/1ri6nvh/deepseek_v4_is_finally_out/', 'Guides & Industry Trends', 'DeepSeek v4: Engram Memory', 'A trillion-parameter MoE model introducing the "Engram" memory system which decouples static knowledge from logical processing for O(1) context lookup.', 'deepseek, moe, engram-memory, vram-optimization, sw-bench', 'Engram O(1) knowledge lookup, 45% VRAM reduction vs v3, 83.7% SWE-bench Verified score, Manifold-Constrained Hyper-Connections (mHC).'),
    ('https://www.reddit.com/r/ExperiencedDevs/comments/1rkri1n/how_are_you_upskilling_yourself_for_working_with/', 'Guides & Industry Trends', 'Intentional Engineering Upskilling', 'A strategic shift for senior engineers toward "delegation over collaboration," focusing on failure mode design and observability at tool boundaries.', 'upskilling, intentional-engineering, delegation, observability, trends', 'Failure mode design priority, tool-boundary observability instincts, micro-automation project focus, transition from implementer to orchestrator.'),
    ('https://www.reddit.com/r/FactoryAi/comments/1puk4bq/factory_cli_v0400_released_custom_models_from/', 'Infrastructure & Proxy Layers', 'Factory AI: BYOK Framework', 'Version 0.4.0 of the Factory CLI introducing a provider-agnostic framework for running agents using local keys from Ollama, Groq, and OpenRouter.', 'factory, byok, model-agnostic, security, local-keys', 'Provider-agnostic agent execution (BYOK), local-first API key storage, native Ollama/Groq integration, /model model-switching command.'),
    ('https://www.reddit.com/r/FactoryAi/comments/1qatsme/factory_cli_v0460_released_createskill_command/', 'AI Agents & Frameworks', 'Factory Skill Wizard', 'A structured guided-flow for creating specialized agent capabilities (SKILL.md) with built-in verification-driven development gates.', 'factory, skill-creation, sdd, workflow, automation', '/create-skill guided wizard, SKILL.md auto-generation, verification-driven development gates, droid exec mode integration.')
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
print('Successfully injected batch 65.')
