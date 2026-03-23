import sqlite3

data = [
    ('https://huggingface.co/Qwen/Qwen3-Coder-Next', 'AI Agents & Frameworks', 'Qwen3-Coder-Next', 'The 2026 gold standard for local agentic coding, an 80B MoE model (3B active) optimized for long-horizon reasoning and failure recovery.', 'qwen, coder, moe, local-llm, agents', '80B total / 3B active parameters, 256K native context (131K validated YaRN), optimized execution-failure recovery, 30GB+ VRAM required (2-bit XL).'),
    ('https://www.google.com/search?q=ChatGPT+vs+Claude+vs+Gemini+coding+benchmarks+2026', 'Guides & Industry Trends', '2026 Frontier Agent Wars', 'An analysis of the 2026 Big Three: Claude Opus 4.5 dominates SWE-bench (80.9%), GPT-5.2 leads in abstract logic, and Gemini 3 Pro excels in 1M+ context ingestion.', 'benchmarks, swe-bench, claude, gpt-5, gemini', 'Claude Opus 4.5 (80.9% SWE-bench Verified), GPT-5.2 (best all-rounder / competitive programming), Gemini 3 Pro (1M+ context "Speed Demon").'),
    ('https://github.com/sitbon/magg', 'Connectivity & Interoperability (MCP/A2A)', 'Magg: Meta-MCP Proxy', 'A meta-MCP server acting as a "package manager" that allows LLMs to autonomously discover, install, and orchestrate other MCP servers at runtime.', 'mcp, package-manager, orchestration, dynamic-discovery, proxy', 'Runtime autonomous tool discovery, automatic prefix proxying (avoids conflicts), MCP sampling-based config generation, dual stdio/SSE support.'),
    ('https://www.google.com/search?q=best+llm+model+for+256gb+ram+2026', 'Infrastructure & Proxy Layers', '256GB Hardware SOTA', 'A 2026 guide for high-end local inference (256GB RAM), highlighting 400B+ class models like Llama 4 Maverick and DeepSeek-V3.', 'local-llm, hardware, 256gb, llama4, deepseek-v3', 'Llama 4 Maverick 400B (Q4_K_M support), DeepSeek-V3 671B (MoE offloading Q4/Q5), Llama 4 Scout (10M token context support).')
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
print('Successfully injected batch 160.')