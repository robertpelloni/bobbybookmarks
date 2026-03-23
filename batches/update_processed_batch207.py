import sqlite3

data = [
    ('https://www.reddit.com/r/ChatGPTCoding/comments/1njm3z9/gpt5codex_high_vs_gpt5pro_refactoring', 'Guides & Industry Trends', 'GPT-5.3 Codex vs Pro', 'A community analysis of OpenAI\'s 2026 models, highlighting GPT-5.3 Codex High as the superior choice for massive, reliable codebase refactoring over the "Thinking" Pro models.', 'codex, gpt-5, refactoring, benchmarks, openai', 'GPT-5.3 Codex High for production-grade architectural refactoring, GPT-5.2 Pro for quick abstract reasoning/prototyping, "zero AI slop" output from Codex.'),
    ('https://www.reddit.com/r/ChatGPTCoding/comments/1nmxq1o/do_you_use_codex_dont_forget_this', 'Context Engineering & Isolation', 'Codex: The 30% Context Rule', 'A viral workflow pattern establishing that LLMs begin to degrade at 30% of their context limit, advocating for strict README.md and HANDOFF.md grounding files to allow safe session restarts.', 'context-engineering, codex, workflow, optimization, grounding', 'The 30% degradation rule, HANDOFF.md session-restart state tracking, explicit environment-locking prompts ("do not invent tools").'),
    ('https://www.reddit.com/r/ChatGPTCoding/comments/1nwe5nz/my_agentsmd', 'Agent Orchestration & Workflow', 'AGENTS.md: Autonomy Standard', 'An emerging open standard file format (AGENTS.md) used to provide vendor-agnostic instructions (Claude/Gemini/Codex) dictating how autonomous agents should behave in a repository.', 'orchestration, standard, agents.md, workflow, autonomy', 'Vendor-agnostic instruction format, "Dogged Autonomy" directives, Progressive Disclosure via subdirectory inheritance, Command Safety locking (e.g., forcing `uv run`).'),
    ('https://www.reddit.com/r/ChatGPTCoding/comments/1pi4ojr/gemini_30_pro_has_been_out_for_long_enough_for', 'Guides & Industry Trends', 'Gemini 3.0 Pro: Multimodal SOTA', 'A community review declaring Gemini 3.0 Pro a "downgrade" for logic/reasoning compared to 2.5 Pro, but acknowledging it as the absolute State-of-the-Art for Multimodal UI (screenshot-to-code) generation.', 'gemini, google, multimodal, ui-generation, benchmarks', 'SOTA visual screenshot-to-code generation (beats Codex-Max), regression in large-scale codebase reasoning (vs 2.5 Pro), unreliable web search citation issues.')
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
print('Successfully injected batch 167.')