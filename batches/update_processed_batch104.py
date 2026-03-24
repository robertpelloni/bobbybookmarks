import sqlite3

data = [
    ('https://www.reddit.com/r/ChatGPTCoding/comments/1pyxqjt/agent_skills_have_arrived_in_roo_code_roo_code/', 'AI Agents & Frameworks', 'Roo Code Modular Skills', 'A transition from monolithic custom instructions to a modular skill framework using individual .roo/SKILL.md files for specialized agent behaviors.', 'roo-code, skills, modularity, context-efficiency, documentation', 'Individual SKILL.md files, dynamic activation triggers, project-specific instruction scope, YAML-based activation logic.'),
    ('https://www.reddit.com/r/ChatGPTCoding/comments/1q9ize8/finally_got_true_multiagent_group_chat_working_in/', 'Agent Orchestration & Workflow', 'Multi-Agent "Main Context" Pattern', 'A swarm coordination strategy that uses a "Main Context Document" (MCD) as a shared ground-truth to prevent conflicting agent actions.', 'swarm, orchestration, mcd, multi-agent, ground-truth', 'Main Context Document (MCD) pattern, Router-Agent delegation loops, cross-agent artifact sharing, conflict resolution protocols.'),
    ('https://www.reddit.com/r/ChatGPTPro/comments/1qzbdwb/openai_has_now_acknowledged_that_pro_lacks_memory/', 'Guides & Industry Trends', 'ChatGPT Pro Memory Limitations', 'Official acknowledgment that GPT-5.2 Pro lacks persistent memory features, necessitating manual memory injection strategies for long-term projects.', 'openai, memory-drift, limits, chatgpt-pro, persistence', 'Loss of saved memories in Pro tier, manual Markdown memory injection workarounds, session-stable vs cross-session memory bifurcation.'),
    ('https://www.reddit.com/r/ChatGPTPromptGenius/comments/1qjweoq/i_reverseengineered_chatgpts_reasoning_and_found/', 'AI Agents & Frameworks', 'Hidden "Reasoning Trace" Loops', 'Reverse-engineering research revealing that response quality jumps 10x when models are forced through a 5-step internal loop (Understand -> Analyze -> Reason -> Synthesize -> Conclude).', 'reasoning-chains, reverse-engineering, logic-engine, chain-of-thought, prompt-engineering', '5-Step internal reasoning loop, invisible Constitutional AI layers, RLHF pattern-matching detection, high-fidelity reasoning trace extraction.')
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
print('Successfully injected batch 66.')
