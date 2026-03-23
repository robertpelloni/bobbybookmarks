import sqlite3

data = [
    ('https://www.reddit.com/r/Bard/comments/1qon7ia/introducing_agentic_vision_in_gemini_3_flash/', 'Interface & Developer UX', 'Gemini Agentic Vision', 'A multimodal paradigm shift where agents use a "visual scratchpad" to actively crop, zoom, and annotate screenshots for high-accuracy UI grounding.', 'gemini, vision-agent, visual-grounding, computer-use, automation', 'Active "Think-Act-Observe" visual loops, iterative image manipulation (crop/zoom), character-offset visual grounding, 10% quality boost in high-density data tasks.'),
    ('https://www.reddit.com/r/Bard/comments/1qwwt86/53codex_blows_gemini_3_out_of_the_water/', 'Guides & Industry Trends', 'GPT-5.3-Codex vs Gemini 3', "A strategic performance comparison highlighting GPT-5.3-Codex's role as a 'Workflow Assistant' vs. Gemini 3's lead in 'Hacker Mind' bug-hunting.", 'benchmarks, codex, gemini, sw-bench, research', '74.2% Verified lead for Gemini 3 Pro, GPT-5.3 workflow-level reliability, 1M+ token context dominance for Flash, distinct implementer vs architect model personas.'),
    ('https://www.reddit.com/r/BeyondThePromptAI/comments/1raglxo/your_ai_companion_isnt_safe_on_someone_elses/', 'Infrastructure & Proxy Layers', 'Sovereign AI Infrastructure', 'A movement advocating for independent, locally-hosted AI companions to protect users from the "moral failure" and military integration of major tech providers.', 'sovereignty, local-host, privacy, infrastructure, compliance', 'Control over inference-layer sovereignty, domestic hardware priority, local data-model coupling, mitigation of " foreign plug-pull" risks.')
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
