import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1rnj35s/10_mcps_that_genuinely_made_me_quicker_and_can', 'Connectivity & Interoperability (MCP/A2A)', '10 Practical MCPs 2026', 'A curated list of high-utility MCP servers including Context7 (Docs RAG), Docker runtime inspection, and Arachne (98% token-saving codebase indexing).', 'mcp, utility, optimization, context-engineering, tools', 'Context7 framework documentation RAG, Docker runtime visibility, Browser DevTools DOM exposure, Arachne 98% token reduction.'),
    ('https://www.reddit.com/r/mcp/comments/1rno9pu/i_built_44_mcp_tools_for_my_own_cognitive_system', 'Memory & Persistence Architecture', 'Cognitive MCP Tools', 'Insights from building a Firestore-backed knowledge graph (Cortex) with 44 MCP tools, highlighting the "Wander" pattern and the necessity of a "Forget" tool.', 'mcp, memory, knowledge-graph, reflection, architecture', 'Firestore-backed knowledge graph (Cortex), "Wander" random traversal pattern, "Forget" tool for noise reduction, simple logbook-append primacy.'),
    ('https://github.com/jaehongpark-agent/claude-code-spinner-verbs', 'Interface & Developer UX', 'Claude Spinner Customizer', 'A utility that allows users to extract and replace the default "spinner" processing verbs in Claude Code (e.g., changing "Thinking" to "Cooking").', 'claude-code, cli, customization, ux, tooling', 'Replaces default processing verbs, modifies `~/.claude/settings.json`, native language (e.g., Korean) translation support.'),
    ('https://github.com/terpinedream/Bashd', 'Interface & Developer UX', 'Bashd: File MCP TUI', 'A script toolkit and Terminal User Interface (TUI) that provides fuzzy search navigation, update tracking, and a built-in MCP server for automated file categorization.', 'cli, tui, bash, mcp, file-management', 'Fuzzy search navigation (`fzf`), "Plumber\'s Safety" interactive `rm` wrapper, GitHub release update tracking, MCP-driven file categorization.')
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
print('Successfully injected batch 182.')