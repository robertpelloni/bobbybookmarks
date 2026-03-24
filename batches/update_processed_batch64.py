import sqlite3

data = [
    ('https://build.nvidia.com/nvidia/multi-agent-intelligent-warehouse', 'Agent Orchestration & Workflow', 'NVIDIA Warehouse Intelligence', 'An open-source AI command layer that orchestrates specialized agent fleets to unify warehouse operations and telemetry.', 'nvidia, orchestration, warehouse-automation, iot, langgraph', 'Centralized Warehouse Assistant, specialized Equipment/Safety agents, real-time telemetry unification, Natural Language operational queries.'),
    ('https://build.nvidia.com/nvidia/safety-for-agentic-ai', 'Guides & Industry Trends', 'NVIDIA Agentic Safety Framework', 'A comprehensive "Safety Recipe" for hardening agentic workflows against misalignment, hallucinations, and prompt injections.', 'security, guardrails, nvidia, nemo, ai-safety', 'Inference-time Topic Control, Jailbreak detection microservices, build-time garak vulnerability scanning, specialized safety datasets.'),
    ('https://build.nvidia.com/nvidia/vulnerability-analysis-for-container-security', 'Infrastructure & Proxy Layers', 'NVIDIA Container Security Agent', 'An automated triage agent that uses RAG and SBOM analysis to distinguish between genuine container risks and false positives.', 'security, container, cve, sbom, automation', 'Automated SBOM (Syft) generation, RAG-based CVE cross-referencing, VEX (Vulnerability Exploitability) generation, sub-second security triage.'),
    ('https://build.nvidia.com/nvidia/llm-router', 'Infrastructure & Proxy Layers', 'NVIDIA NIM LLM Router', 'A high-performance framework that dynamically routes prompts to optimal models based on intent, cost, and latency requirements.', 'routing, model-selection, nvidia, nim, optimization', 'Intent-based semantic classification, multimodal text/image routing, OpenAI API compliance, automated cost-quality-latency balancing.')
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
print('Successfully injected batch 30.')
