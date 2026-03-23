import sqlite3

data = [
    ('https://www.ideabrowser.com/', 'Agent Orchestration & Workflow', 'IdeaBrowser: Startup OS', 'A comprehensive AI "startup toolkit" that transforms market trends into validated business opportunities via an autonomous research agent and AI builder prompts.', 'orchestration, market-research, automation, ideas, workflow', 'Automated market/keyword trend research, business framework mapping (Value Equation), query-chain conversational analysis, pre-filled cursor/bolt prompts.'),
    ('https://www.kavout.com/investgpt', 'AI Agents & Frameworks', 'InvestGPT: Finance Swarm', 'An institutional-grade AI investment assistant that routes queries to a swarm of specialized agents (Technical, Fundamental, Sentiment, Trade Spotter) for deep market analysis.', 'finance, investing, multi-agent, swarm, research', 'Specialized financial agent swarm, real-time tracking (11k+ assets), congressional/insider trade monitoring, dual-mode (Quick/Deep Research).'),
    ('https://www.keyshot.com/keyshot-studio-ai', 'Interface & Developer UX', 'KeyShot Studio AI: 3D', 'The 2026 evolution of the industry-standard 3D rendering suite, featuring local GPU-based generative AI for instant moodboarding and environment generation.', '3d-rendering, generative-ai, local-first, vision, workflow', '100% local processing (protects CAD IP), Imagine Mode instant concepting, Restyle Mode scene modification, generative background projection.'),
    ('https://www.helicone.ai/blog/llm-api-providers', 'Guides & Industry Trends', 'LLM Provider Meta 2026', 'Helicone\'s 2026 industry analysis highlighting the shift from model size to "Reasoning Models" (DeepSeek R1/Opus 4.5) and the rise of massive context windows (Grok 4.1).', 'benchmarks, economics, api-providers, trends, reasoning', 'Cost deflation ("The Great Token Deflation"), DeepSeek R1 reasoning efficiency, Grok 4.1 Fast 2M token context, inference platform benchmarks (Together/Fireworks).')
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
print('Successfully injected batch 162.')