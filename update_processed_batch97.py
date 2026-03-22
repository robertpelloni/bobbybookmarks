import sqlite3

data = [
    ('https://www.reddit.com/r/AI_Operator/comments/1q0vsvi/ace_the_real_time_computer_autopilot/', 'Interface & Developer UX', 'ACE: Real-Time Autopilot', 'A foundational AI model optimized for direct computer interaction, bypassing traditional vision-latency to achieve human-equivalent speed (~15s workflows).', 'computer-use, autopilot, low-latency, foundational-model, automation', 'Native OS/Browser token space, sub-second reaction times, human-equivalent execution speed, API-less software interaction.'),
    ('https://www.reddit.com/r/AI_Agents/comments/1rfwt3p/i_built_an_orchstrator_that_manages_30_agent/', 'Agent Orchestration & Workflow', '30-Agent "Team Lead" Orchestrator', 'A massive parallel agent management system that uses Git Worktrees and reactive context injection to coordinate 30+ independent Claude Code/Codex sessions.', 'orchestration, multi-agent, git-worktrees, reactive-context, automation', 'Git Worktree isolation for 30+ sessions, "Reaction" engine for CI/PR log injection, automated Team Lead coordination, tmux/docker persistent runtimes.'),
    ('https://www.reddit.com/r/AI_Tips_Tricks/comments/1q2x5gl/reverse_prompt_engineering_trick_everyone_should/', 'AI Agents & Frameworks', 'Reverse Prompt Engineering', 'An "output-first" methodology where LLMs analyze gold-standard artifacts to reverse-engineer the precise system instructions needed to reproduce them.', 'prompt-engineering, system-prompts, optimization, reverse-engineering, benchmarking', 'Latent variable extraction (tone/pacing), automated system prompt generation, gold-standard reproduction, objective instruction refinement.'),
    ('https://www.reddit.com/r/AgentsOfAI/comments/1puwboa/i_built_a_team_of_7_ai_agents_that_collaborate_to/', 'Agent Orchestration & Workflow', 'Studio Culture Agent Swarm', 'A creative/technical orchestration platform that decomposes complex tasks into a "Studio" of specialized agents communicating via a shared MCP backbone.', 'swarm, mcp, collaboration, specialized-agents, multi-agent', 'Specialized Scout/Curator/Critic roles, Remote MCP communication layer, agent-agnostic collaboration, unified multi-framework conversation threads.')
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
print('Successfully injected batch 61.')
