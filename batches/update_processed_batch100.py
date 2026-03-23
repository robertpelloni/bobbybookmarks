import sqlite3

data = [
    ('https://www.reddit.com/r/AskVibecoders/comments/1qwyg3n/claude_opus_46_how_to_monetize_5_system_workflows/', 'Guides & Industry Trends', 'Vibe Coding Monetization', 'A 5-step framework for turning AI-orchestrated workflows into revenue, focusing on niche research, automated asset generation, and droid-based implementation.', 'vibe-coding, monetization, business-model, orchestration, autonomous-dev', 'Step 1: Deep Niche Research, Step 2: Automated Asset Gen, Step 3: Vibe PRD standard, Step 4: Autonomous Droid Config, Step 5: Automated Social Outreach.'),
    ('https://www.reddit.com/r/AskVibecoders/comments/1rkqviv/how_to_finetune_llms_in_2026/', 'Guides & Industry Trends', 'Fine-Tuning Agents (2026)', 'A consensus analysis on the shift from SFT to Reinforcement Fine-Tuning (RFT) using GRPO and RULER for training reasoning-aware agents.', 'fine-tuning, rft, grpo, agent-training, unsloth', 'GRPO (Group Relative Policy Optimization), RULER LLM-Elicited Rewards, 5GB VRAM 7B tuning via Unsloth, ART (Agent Reinforcement Trainer) framework.'),
    ('https://www.reddit.com/r/AugmentCodeAI/comments/1q65fqq/factory_droid_is_an_immensly_better_augmentcode/', 'AI Agents & Frameworks', 'Factory Droid: Orchestration', 'A comparison of autonomous "Droids" vs legacy copilots, highlighting the shift toward specialized, multi-model agent teams for end-to-end tasks.', 'factory-droid, multi-agent, enterprise-automation, orchestration, benchmarks', 'Specialized Code/Review/Reliability droids, Multi-model subscription access, "Set and Forget" handoff workflow, #1 Terminal-Bench ranking.'),
    ('https://www.reddit.com/r/AugmentCodeAI/comments/1q7tilw/auggie_wiggum_a_ralph_wiggum_loop_for_auggie_cli/', 'Agent Orchestration & Workflow', 'Auggie Wiggum: Self-Healing Loop', 'An implementation of the "Ralph Wiggum Loop" that uses exit code interception and completion promises to drive 14+ hour autonomous coding sessions.', 'self-healing, autonomous-coding, feedback-loops, build-automation, persistence', 'Stop Hook exit interception, <promise> completion checking, 14+ hour autonomous execution, automated context re-feeding on failure.')
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
print('Successfully injected batch 64.')
