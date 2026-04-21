import sqlite3

data = [
    ('https://framework.beeai.dev/introduction/welcome', 'Agent Orchestration & Workflow', 'BeeAI: Constraint Reasoning', 'An open-source multi-agent framework (IBM Research) that enforces deterministic rules and multi-strategy memory management for production-grade agent systems.', 'orchestration, framework, multi-agent, ibm, constraint-reasoning', 'Constraint-based reasoning, Python/TS feature parity, 4 distinct memory strategies, OpenTelemetry observability integration.'),
    ('https://genesis-embodied-ai.github.io/', 'Infrastructure & Proxy Layers', 'Genesis: 43M FPS Physics', 'A generative, fully differentiable physics engine for Embodied AI capable of 43 million FPS simulations, outperforming MuJoCo MJX by up to 80x.', 'embodied-ai, robotics, physics-engine, simulation, differentiation', '43 million FPS simulation speed, universal solver (rigid/soft/cloth/fluid), VLM-based dynamic world generation, fully differentiable architecture.'),
    ('https://frame.work/products/framework-desktop-mainboard-amd-ryzen-ai-max-300-series?v=FRAFMK0006', 'Infrastructure & Proxy Layers', 'Ryzen AI Max: 50 TOPS', 'The high-end AMD "Strix Halo" SoC series featuring a 50 TOPS XDNA 2 NPU and up to 40 RDNA 3.5 CUs for workstation-class integrated AI performance.', 'hardware, amd, strix-halo, npu, performance', '50 TOPS AI compute (XDNA 2), 40 RDNA 3.5 Compute Units, 256-bit memory interface, up to 128GB LPDDR5X-8000 support.'),
    ('https://ghost.oxen.ai/no-hype-deepseek-r1-reading-list', 'Guides & Industry Trends', 'DeepSeek-R1: Core Pillars', 'A technical deconstruction of DeepSeek-R1, highlighting its GRPO algorithm, R1-Zero reasoning emergence, and Multi-Head Latent Attention (MLA) efficiency.', 'deepseek, research, r1, grpo, mla', 'GRPO (Group Relative Policy Optimization), R1-Zero reasoning emergence (no SFT), Multi-Head Latent Attention (MLA) efficiency, reasoning distillation patterns.')
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
print('Successfully injected batch 123.')