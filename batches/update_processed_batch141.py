import sqlite3

data = [
    ('https://www.reddit.com/r/opencodeCLI/comments/1qadc07/remote_code_execution_in_opencode_update_now/', 'Infrastructure & Proxy Layers', 'OpenCode RCE Vulnerability', 'A critical security flaw in OpenCode allowing arbitrary command execution via local server hijacking; users must update to v1.1.10 or newer.', 'security, vulnerability, opencode, rce, update', 'Critical RCE fix, v1.1.10 mandatory update, local server hijacking prevention, community-driven security audit.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1qaflua/i_built_an_obsidian_plugin_that_embeds_opencode/', 'Interface & Developer UX', 'OpenCode Obsidian Plugin', 'A sidebar plugin for Obsidian that embeds a full OpenCode terminal emulator (xterm.js), allowing agents to operate directly within the vault context.', 'obsidian, plugin, terminal, ui, opencode', 'Full xterm.js terminal emulation, vault-aware working directory, image pasting support, multi-tabbed instances.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1qbbsfg/one_reviewer_three_lenses_building_a_multiagent/', 'Agent Orchestration & Workflow', 'open-artisan: Multi-Lens Review', 'A structured AI orchestration plugin using a state machine to drive a self-review loop across design, architecture, and user vision lenses.', 'orchestration, state-machine, review-loop, workflow, opencode', 'One Reviewer Three Lenses framework, autonomous state-machine loops, design/architecture/vision alignment, readiness validation.'),
    ('https://www.reddit.com/r/opencodeCLI/comments/1qbqn96/openpackage_a_better_universal_open_source/', 'Infrastructure & Proxy Layers', 'OpenPackage: Universal Assets', 'A universal, open-source package system for AI coding assets (rules, skills, agents) that provides proper dependency management and cross-platform portability.', 'openpackage, plugin-system, modularity, registry, assets', 'Universal asset portability, npm-style dependency management, openpackage.dev registry, single-command cross-tool installation.')
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
print('Successfully injected batch 91.')