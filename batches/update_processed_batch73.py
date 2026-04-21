import sqlite3

data = [
    ('https://github.com/divyenduz/incus-sandbox-sdk', 'Infrastructure & Proxy Layers', 'Incus Sandbox SDK', 'A software development kit for managing secure, system-level containers and virtual machines using the Incus (LXD fork) hypervisor.', 'sandboxing, incus, virtualization, infrastructure, security', 'Programmatic VM/Container lifecycle, hardware-level isolation for agents, secure secret injection, OCI image support.'),
    ('https://github.com/fiatrete/OpenDAN-Personal-AI-OS', 'AI Agents & Frameworks', 'OpenDAN Personal AI OS', 'A comprehensive AI operating system designed to orchestrate multiple specialized agents into a unified, interoperable personal assistant.', 'ai-os, personal-ai, orchestration, interoperability, local-first', 'Consolidated AI Kernel, group-based agent collaboration, local privacy-first storage, native IoT and web service integration.'),
    ('https://github.com/github/spec-kit', 'AI Agents & Frameworks', 'GitHub Spec-Kit', 'A structured framework for automated specification-driven development, turning requirements into executable blueprints for AI agents.', 'spec-driven, blueprint, automated-specification, quality-gate, standard', 'Executable technical specs, /specify and /plan commands, Project Constitution enforcement, iterative requirements refinement.'),
    ('https://github.com/gsd-build/get-shit-done', 'Agent Orchestration & Workflow', 'GSD Orchestration Framework', 'A production-grade context engineering and multi-agent system designed to make AI development reliable via rigorous planning and verification.', 'gsd, orchestration, verification, cdd, workflow', 'Planner-Checker-Revise loops, automated codebase mapping, sub-agent task delegation, interactive verification gates.')
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
print('Successfully injected batch 39.')
