
import os

links = [
    ('https://github.com/MadAppGang/claude-code', 'AI Agents & Frameworks', 'MadAppGang Claude Code Fork', 'A production-focused fork of Claude Code designed as a \"Plugins Marketplace,\" adding multi-model support, 8-phase workflows, and specialized frontend/backend agents.', 'fork, claude-code, marketplace, multi-model', 'Plugin Marketplace, 8-Phase /implement, Multi-model (OpenRouter), Team-wide Sync.'),
    ('https://github.com/MadAppGang/claude-code/tree/main/plugins', 'AI Agents & Frameworks', 'MadAppGang Plugins Ecosystem', 'A robust ecosystem of opinionated plugins for Claude Code, including specialized frontend design, Bun backend, and semantic analysis tools.', 'plugins, extensibility, frontend-design, bun-stack', 'Frontend Designer agent, Bun/Hono/Prisma support, Semantic Search Skill, Figma sync.'),
    ('https://github.com/MadAppGang/claudish', 'AI Agents & Frameworks', 'Claudish CLI', 'A standalone proxy tool within the MadAppGang ecosystem that enables running Claude Code with any model from OpenRouter (Grok, GPT-5, etc.).', 'cli, proxy, openrouter, multi-model', 'Universal LLM Support, OAuth Proxy, Profile management, low-latency routing.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
