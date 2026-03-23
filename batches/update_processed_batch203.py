import sqlite3

data = [
    ('https://www.letta.com/', 'Memory & Persistence Architecture', 'Letta: Stateful Agents', 'The evolution of MemGPT into a production platform for stateful AI agents, featuring an OS-inspired memory hierarchy and self-improving memory blocks.', 'memory, persistence, letta, memgpt, stateful-agents', 'Core/Archival/Recall memory hierarchy, self-improving memory blocks, Letta Code local execution CLI, graphical Agent Development Environment (ADE).'),
    ('https://www.marktechpost.com/2025/09/13/google-ai-releases-vaultgemma-the-largest-and-most-capable-open-model-1b-parameters-trained-from-scratch-with-differential-privacy', 'AI Agents & Frameworks', 'VaultGemma: Private SLM', 'A 1B parameter Small Language Model by Google designed specifically for Differential Privacy (DP), preventing the memorization of sensitive training data.', 'privacy, differential-privacy, google, gemma, slm', 'Differential Privacy (DP) ground-up training, Poisson Sampling algorithm, 1B parameter efficiency, designed for healthcare/finance regulatory compliance.'),
    ('https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks', 'Agent Orchestration & Workflow', 'Magentic-One: Generalist', 'Microsoft\'s generalist multi-agent system utilizing a Lead Orchestrator and specialized sub-agents (WebSurfer, FileSurfer, Coder) for open-ended tasks.', 'orchestration, multi-agent, microsoft, autogen, framework', 'Lead Orchestrator with Task/Progress ledgers, specialized sub-agents (Web/File/Coder), plug-and-play heterogeneous model support, dynamic error re-planning.'),
    ('https://www.lesswrong.com/posts/cnj9tXk3okFPsXzmD/llms-suck-at-deep-thinking-part-3-trying-to-prove-it-fixed', 'Guides & Industry Trends', 'Shallow vs Deep Thinking', 'A critical analysis from LessWrong arguing that LLMs excel at heuristic "shallow thinking" but structurally fail at computationally expensive "deep thinking" exploration.', 'philosophy, reasoning, limitations, research, agi', 'Shallow (heuristic) vs Deep (exploration) reasoning definitions, critique of the "Chess" analogy for LLMs, predictive architecture limitations.')
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
print('Successfully injected batch 163.')