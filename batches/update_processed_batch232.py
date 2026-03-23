import sqlite3

data = [
    ('https://github.com/PatrickSys/codebase-context', 'Context Engineering & Isolation', 'CodeGraphContext: CGC', 'A leading codebase indexing MCP server that treats code as a symbol-level graph, allowing agents to query caller/callee hierarchies using natural language.', 'mcp, context-engineering, codebase-indexing, graph-rag, search', 'Symbol-level graph querying (callers/callees), pre-indexed `.cgc` repository bundles, live file watching (`cgc watch`), 10x faster than traditional vector indexing.'),
    ('https://www.verdent.ai/', 'Agent Orchestration & Workflow', 'Verdent AI: Verification', 'A production-grade agentic coding platform emphasizing systematic planning over autocomplete, achieving a 76.1% single-attempt resolution rate on SWE-bench Verified.', 'orchestration, autonomy, verification, testing, multi-agent', 'Plan Mode (think-before-code), Parallel Agent Git Worktrees, Review Subagent (3-model cross-validation), Diff Lens "Why" analysis.'),
    ('https://www.reddit.com/r/BMAD_Method/comments/1rpt753/i_built_bmalph_bmad_for_deep_planning_ralph_for/', 'Agent Orchestration & Workflow', 'BMALPH: SDLC Integration', 'A CLI integration layer bridging the "thinking" phase of the BMAD Method (Product Briefs/PRDs) with the "doing" phase of the Ralph autonomous bash loop.', 'orchestration, bmad, ralph, tdd, workflow', 'Automated PRD to Task-List conversion, `/bmalph-implement` bridge command, Test-Driven Development (TDD) execution loop, zero context-drift handoffs.'),
    ('https://www.reddit.com/r/BMAD_Method/comments/1rpywka/plugin_ralphmad_autonomous_sdlc_workflows/', 'Agent Orchestration & Workflow', 'RalphMAD: Claude Plugin', 'A specialized Claude Code plugin automating the full Software Development Life Cycle (SDLC) by executing 12+ pre-built BMAD workflows autonomously.', 'claude-code, plugins, sdlc, bmad, automation', '12+ pre-built autonomous workflows, YAML-driven `{{placeholder}}` templating, isolated concurrent state management, `/plugin install ralphmad` deployment.')
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
print('Successfully injected batch 192.')