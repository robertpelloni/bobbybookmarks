import sqlite3

data = [
    ('https://algorithmicsuperintelligence.ai/blog/openevolve-overview/index.html', 'Agent Orchestration & Workflow', 'OpenEvolve: Evolution Core', 'An open-source evolutionary coding agent that automates the discovery of optimized algorithms using a Quality-Diversity (QD) search framework.', 'algorithm-discovery, evolution, optimization, deepmind, research', 'MAP-Elites search framework, Island Model diversity maintenance, multi-model ensemble (Gemini/Claude), artifact-side-channel feedback loops.'),
    ('https://alirezarezvani.medium.com/30-claude-code-subagents-you-need-in-2026-with-templates-you-can-use-today-part-1-2-127a11f473b1', 'Agent Orchestration & Workflow', 'Claude Code: 30 Subagents', 'A multi-agent architecture library for Claude Code that reduces context pollution by delegating specialized tasks to isolated worker agents.', 'orchestration, multi-agent, claude-code, specialization, efficiency', '30 domain-specific YAML subagents, Orchestrator-Worker delegation model, 60-70% token usage reduction, automated PR issue catching.'),
    ('https://alternativeto.net/software/activitywatch/about', 'Infrastructure & Proxy Layers', 'ActivityWatch: Local-First Tracking', 'A privacy-first, local-first time tracking tool that records system activity without cloud data exfiltration, featuring a high-performance Rust core.', 'privacy, local-first, time-tracking, rust, open-source', 'Local-only data storage, modular window/editor watchers, Rust-native server implementation (aw-server-rust), idle time AFK detection.'),
    ('https://aistudio.google.com/prompts/1Njd5MCPJGVDF4MLmSS-cT8_ZVKW26rgG', 'AI Agents & Frameworks', 'Google AI Studio: MCP Pattern', 'A structured Model Context Protocol (MCP) prompt pattern for Gemini models, utilizing XML delimiters and front-loaded behavioral constraints.', 'mcp, gemini, prompting, architecture, structured-output', 'Structured XML reasoning delimiters, JSON schema visual editing, native Google Search grounding, function calling integration.')
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
print('Successfully injected batch 106.')