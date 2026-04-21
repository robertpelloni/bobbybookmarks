import sqlite3

data = [
    ('https://www.reddit.com/r/voiceaii/comments/1pgalns/microsoft_ai_releases_vibevoicerealtime_a', 'AI Agents & Frameworks', 'VibeVoice: Realtime TTS', 'Microsoft\'s open-source 0.5B parameter voice AI model designed for real-time text-to-speech, featuring ultra-low 300ms latency and 7.5 Hz continuous tokenization.', 'voice-ai, tts, microsoft, real-time, inference', 'Ultra-low 300ms first-sound latency, 7.5 Hz continuous speech tokenizers, streaming text-input support, lightweight 0.5B parameter architecture.'),
    ('https://www.roboratings.com/', 'Guides & Industry Trends', 'RoboRatings: 2026 SOTA', 'A 2026 benchmark leaderboard tracking frontier models, highlighting Claude Opus 4.6 (Reasoning), Sonnet 5 (Coding), and Gemini 3.1 Pro (Multimodal) as industry leaders.', 'benchmarks, leaderboard, claude, gemini, evaluation', 'Claude Opus 4.6 (91.9% GPQA Reasoning), Claude Sonnet 5 (82.1% SWE-bench Coding), Gemini 3.1 Pro (1M+ Multimodal), Kimi K2.5 (Cost/Performance ratio).'),
    ('https://www.rtrvr.ai/', 'Interface & Developer UX', 'Retriever AI: Vibe Scraping', 'A web automation platform that replaces CSS selectors with natural language "Vibe Scraping," featuring a remote MCP server for cross-agent browser control.', 'browser-automation, scraping, mcp, stealth, automation', 'Natural language "Vibe Scraping" (no CSS selectors), Remote MCP Server for agentic browser control, native Extension API execution (stealth), 1,000+ parallel cloud instances.'),
    ('https://www.reddit.com/r/VibeCodingSaaS/comments/1p6crpw/we_aggregated_all_top_genai_models_into_one_api', 'Infrastructure & Proxy Layers', 'MegaLLM: API Gateway', 'An enterprise-grade AI API gateway aggregating 70+ LLMs into a single OpenAI-compatible endpoint, featuring sub-100ms latency and semantic caching.', 'gateway, api, proxy, infrastructure, optimization', '70+ models unified under OpenAI API format, Semantic Caching (80% latency reduction), smart geo-routing/fallbacks, team budget/rate-limit governance.')
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
print('Successfully injected batch 175.')