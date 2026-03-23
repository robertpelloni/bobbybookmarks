import sqlite3

data = [
    ('https://news.ycombinator.com/item?id=46036878', 'Guides & Industry Trends', 'DeepSeek-V3: Economic SOTA', 'A technical deconstruction of DeepSeek-V3, highlighting its $5.5M training cost, 53x cheaper inference vs Claude, and successful FP8 quantized MoE training.', 'deepseek, research, economics, moe, benchmarks', '53x cheaper inference, FP8 quantized training, 37B active / 671B total params, Multi-token prediction core.'),
    ('https://news.ycombinator.com/item?id=45554240', 'Interface & Developer UX', 'Claude: Computer Use GA', 'Hacker News discussion on the general availability of Claude 3.5 Sonnet Computer Use, focusing on the security implications of prompt-injected GUI hijacking.', 'anthropic, computer-use, security, vision, vulnerability', 'Native screen pixel counting, autonomous GUI interaction, Docker-sandbox requirement, Prompt Injection risk analysis.'),
    ('https://news.ycombinator.com/item?id=46207464', 'Guides & Industry Trends', 'Llama 4: Benchmark Audit', 'A controversial report on Llama 4 leaked benchmarks and internal Meta resignations, alleging training data contamination and ELO manipulation.', 'llama, meta, benchmarks, security, audit', 'Llama-4-Maverick (400B MoE) specs, training set leakage allegations, ELO manipulation controversy, internal Meta AI team churn.'),
    ('https://news.ycombinator.com/item?id=46037343', 'Guides & Industry Trends', 'Gemini 3 Pro: Logic Jump', 'Hacker News feedback on Gemini 3 Pro, noting a step-change in math/logic reasoning and superior long-context tracking compared to the 3.0 series.', 'gemini, google, reasoning, logic, benchmarks', 'Superior math/logic reasoning, 200K+ token stable context, complex SVG generation (Pelican test), "Senior Developer" persona archetypes.')
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
print('Successfully injected batch 145.')