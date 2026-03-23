import sqlite3

data = [
    ('https://news.ycombinator.com/item?id=43103484', 'Guides & Industry Trends', 'DeepSeek-R1: HN Analysis', 'Hacker News analysis of DeepSeek-R1 focusing on its GRPO reasoning efficiency, MLA attention compression, and the industry-disrupting training cost breakthrough.', 'deepseek, research, grpo, mla, benchmarks', 'GRPO reasoning optimization, MLA KV-compression (VRAM savings), 1/10th training cost parity, reasoning distillation transparency.'),
    ('https://news.ycombinator.com/item?id=42400349', 'Connectivity & Interoperability (MCP/A2A)', 'MCP: The AI "USB-C"', 'Hacker News discussion defining the Model Context Protocol (MCP) as a solution to the NxM integration chaos via standardized Resources, Prompts, and Tools.', 'mcp, protocol, standard, connectivity, orchestration', 'Universal tool interface, Resources/Prompts/Tools primitives, elimination of bespoke bridges, low-level "HTTP for agents" layer.'),
    ('https://news.ycombinator.com/item?id=44147359', 'Agent Orchestration & Workflow', 'Ouroboros: Self-Evolution', 'A controversial discussion on recursive AI self-improvement, debating the technical reality of agents that rewrite their own core logic and the associated alignment risks.', 'autonomy, self-evolving, ouroboros, risk-analysis, research', 'Recursive code/prompt rewriting, "Fast Takeoff" takeoff debate, statistical vs architectural evolution, paperclip-maximizer risk analysis.'),
    ('https://news.ycombinator.com/item?id=42487072', 'Agent Orchestration & Workflow', 'Claude Code: Terminal Flow', 'Hacker News community feedback on Claude Code, highlighting the speed of terminal-first workflows and the productivity of solo devs using "thinking" tokens.', 'claude-code, cli, productivity, workflow, terminal', 'Terminal-first agentic "flow," effective Sonnet 3.5 "Thinking" tokens, solo dev productivity multiplier, TDD-focused implementation loops.')
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
print('Successfully injected batch 139.')