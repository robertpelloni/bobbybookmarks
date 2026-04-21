import sqlite3

data = [
    ('https://www.reddit.com/r/AgentsOfAI/comments/1py9zy4/i_killed_rag_hallucinations_almost_completely/', 'Memory & Persistence Architecture', 'Multi-Agent Verification RAG', 'A "Debate & Verify" RAG pattern that uses specialized searcher, critic, and synthesizer agents to achieve near-zero hallucination rates.', 'rag, multi-agent, verification, hallucinations, accuracy', 'Exact character-offset citations, character-level verification loops, multi-agent "Debate" protocol, automated "Critic" rejection logic.'),
    ('https://www.reddit.com/r/AgentsOfAI/comments/1q62fro/memory_persistence_problem_in_ai_agents_is_worse/', 'Memory & Persistence Architecture', 'Memory Persistence & Drift Analysis', 'A critical analysis of "Recursive Summarization Decay" and why vector-based long-term memory leads to agentic intent loss over time.', 'memory-drift, summarization-decay, vector-db, context-engineering, persistence', 'Identification of summarization decay, intent-loss analysis, shift toward Graph-based memory, task-relevance filtering protocols.'),
    ('https://www.reddit.com/r/Anthropic/comments/1r56egp/how_i_structure_claude_code_projects_claudemd/', 'AI Agents & Frameworks', 'CLAUDE.md: Project Constitution', 'A standardized "Project Constitution" file that provides persistent, session-stable architectural mandates and workflow rules for AI agents.', 'claude-code, documentation, constitution, workflow, standardization', 'Persistent architectural mandates, tech-stack version locking, step-by-step workflow definitions, SKILL/MCP integration definitions.'),
    ('https://www.reddit.com/r/AmpCode/comments/1q8crv1/context_compression_layer/', 'Context Engineering & Isolation', 'AmpCode: Contextual Pruning', 'A specialized management layer that automatically prunes boilerplate and "noise" from files to maximize LLM context window efficiency.', 'context-compression, optimization, token-reduction, pruning, terminal-ai', 'Automated contextual pruning, ACP (Agent Communication Protocol) support, token-aware semantic diffing, high-efficiency context management.')
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
print('Successfully injected batch 62.')
