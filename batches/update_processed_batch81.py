import sqlite3

data = [
    ('https://github.com/xfey/MCP-Zero', 'Connectivity & Interoperability (MCP/A2A)', 'MCP-Zero: Active Discovery', 'A framework enabling agents to autonomously discover and request specific tools on-demand, reducing context usage by 98%.', 'mcp, active-discovery, context-efficiency, optimization, tool-calling', 'Autonomous capability gap identification, on-demand schema fetching, 98% token reduction, zero-overhead context manager.'),
    ('https://xpipe.io/', 'Infrastructure & Proxy Layers', 'XPipe: Remote Shell Orchestrator', 'A unified connection hub and MCP server that manages remote shells and file systems across SSH, Docker, and K8s without remote setup.', 'remote-access, shell, file-manager, mcp, infrastructure', 'Zero-setup remote management, unified SSH/Docker/K8s interface, integrated MCP server, secure credential handling.'),
    ('https://instavm.io/blog/anthropic-skills-can-be-optimized-using-dspy', 'Guides & Industry Trends', 'InstaVM: Skill Optimization', 'A methodological guide on using DSPy to programmatically optimize Anthropic SKILL.md files for higher agent accuracy and reliability.', 'dspy, prompt-engineering, optimization, anthropic, skill-synthesis', 'Automated SKILL.md to DSPy conversion, algorithmic instruction phrasing, few-shot example optimization, verifiable performance gains.'),
    ('https://jules-autopilot.vercel.app/', 'Agent Orchestration & Workflow', 'Jules: Autonomous Autopilot', "Google's autonomous AI coding agent platform designed for unsupervised, long-horizon tasks and self-healing deployment loops.", 'jules, google, autopilot, self-healing, orchestration', 'Scheduled recurring tasks (maintenance/updates), self-healing deployment integration, asynchronous cloud VM execution, GitHub/Jira auto-sync.')
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
print('Successfully injected batch 47.')
