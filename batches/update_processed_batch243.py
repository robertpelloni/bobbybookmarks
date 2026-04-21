import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1rvu5vs/10_mcp_servers_that_together_give_your_ai_agent/', 'Connectivity & Interoperability (MCP/A2A)', 'Agent Power Stack 2026', 'A curated "power stack" of 10 MCP servers (including Context7, Browserbase, and GibsonAI) that transforms basic chatbots into autonomous system operators.', 'mcp, stack, orchestration, browser-automation, database', 'Context7 (Docs RAG), Browserbase (web vision), GibsonAI (Serverless SQL), Notion/Docker/GitHub integrations.'),
    ('https://www.reddit.com/r/better_claw/comments/1rw4vo9/your_opencclaw_agent_isnt_forgetting_things_sorry/', 'Memory & Persistence Architecture', '3-Layer Memory Architecture', 'A solution to OpenClaw "amnesia" utilizing a three-tier memory architecture (Identity, Recall, Reference) coupled with `@mem0` to ensure persistent context.', 'memory, openclaw, architecture, context-management, persistence', 'Layer 1: Core Identity (`soul.md`), Layer 2: Long-Term Recall (`YYYY-MM-DD.md` logs), Layer 3: Deep Reference (specs/docs), `memory_flush: on` configuration.'),
    ('https://www.reddit.com/r/ClaudeCode/comments/1rw5g7c/claude_code_recursive_selfimprovement_of_code_is/', 'Agent Orchestration & Workflow', 'Claude: Recursive R&D', 'Discussions on moving Recursive Self-Improvement (RSI) from theory to practice, detailing how Anthropic uses Claude Code to write its own successor.', 'recursion, claude-code, self-improvement, orchestration, architecture', 'Prevention of "Death Spirals" via codebase metrics (`sentrux`), autonomous "Skill-Creator" loop, partial Recursive Self-Improvement (RSI) in production.'),
    ('https://www.reddit.com/r/AIMemory/comments/1rw9omd/tired_of_ai_rate_limits_midcoding_session_i_built/', 'Memory & Persistence Architecture', 'AIMemory: Context Offload', 'A local vector database layer that intercepts and offloads chat history to drastically reduce token usage and bypass API rate limits during coding sessions.', 'memory, rate-limits, optimization, vector-db, persistence', 'Context offloading via local vector DB, Just-in-Time snippet retrieval, cross-provider persistence (switch Claude to GPT-4 without losing context).')
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
print('Successfully injected batch 203.')