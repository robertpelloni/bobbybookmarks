import sqlite3

data = [
    ('https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md', 'Guides & Industry Trends', 'Agentic AI Foundation (AAIF)', 'A Linux Foundation consortium (Anthropic, OpenAI, Microsoft, etc.) focused on building vendor-neutral open-source infrastructure like MCP and AGENTS.md.', 'consortium, standard, mcp, goose, foundation', 'Model Context Protocol (MCP) support, goose local-first framework, AGENTS.md standardized conventions, cross-vendor interoperability.'),
    ('https://agentclientprotocol.com/overview/introduction', 'Connectivity & Interoperability (MCP/A2A)', 'Agent Client Protocol (ACP)', 'An open standard developed by JetBrains and Zed to standardize communication between IDEs and coding agents, replacing bespoke plugins with a single protocol.', 'standard, acp, ide, integration, connectivity', 'JSON-RPC 2.0 communication, editor-agnostic agent workflows, standardized diff/permission handling, local/remote agent support.'),
    ('https://ai.google.dev/gemini-api/docs/prompting-strategies#agentic-si-template', 'AI Agents & Frameworks', 'Gemini Agentic SI Template', 'Google\'s structured prompting framework for enabling autonomous reasoning in Gemini, using XML tags and front-loaded behavioral constraints.', 'gemini, prompting, reasoning, architecture, best-practices', 'Structured XML reasoning tags, front-loaded behavioral roles, explicit goal-to-subtask parsing, self-critique loop instructions.'),
    ('https://aider.chat/', 'Agent Orchestration & Workflow', 'Aider: AI Pair Programming', 'A leading terminal-based AI pair programmer that uses deep Git integration and Architect Mode to autonomously plan and implement complex features.', 'pair-programming, git, architect-mode, automation, workflow', 'Architect/Implementation dual-mode, automatic descriptive git commits, repository-scale semantic mapping, autonomous test/lint validation loops.')
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
print('Successfully injected batch 105.')