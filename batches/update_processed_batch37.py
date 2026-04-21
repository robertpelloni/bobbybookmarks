import sqlite3

data = [
    ('https://github.com/anthropics/claude-code/blob/main/plugins/README.md', 'AI Agents & Frameworks', 'Claude Code Plugin Architecture', 'Official documentation for the Claude Code plugin system, allowing teams to bundle slash commands, agents, and hooks into shared, versioned packages.', 'claude-code, plugins, architecture, teamwork, standard', 'Formal plugin.json manifest, Namespaced slash commands, Automated hook system, Team-wide deployment support.'),
    ('https://github.com/musistudio/claude-code-router', 'Infrastructure', 'Claude Code Router', 'A smart request dispatcher that allows Claude Code to utilize alternative LLM providers (DeepSeek, Gemini, local) based on task complexity.', 'claude-code, routing, infrastructure, multi-model, cost-optimization', 'Dynamic model dispatching, GitHub Actions support, regional block bypass, local model (Ollama) integration.'),
    ('https://github.com/farion1231/cc-switch', 'Development Tools & Libraries', 'cc-switch Control Center', 'A cross-platform desktop GUI for managing and hot-switching configurations for multiple AI CLI tools like Claude Code, Codex, and Gemini CLI.', 'gui, control-center, configuration, switching, productivity', 'One-click provider swapping, system tray integration, proxy takeover mechanism, WebDAV configuration sync.'),
    ('https://github.com/vishalveerareddy123/Lynkr', 'Infrastructure', 'Lynkr Universal Proxy', 'A self-hosted universal LLM proxy that acts as a drop-in replacement for Anthropic backends, enabling AI coding tools to run on 100+ different models.', 'proxy, infrastructure, self-hosted, gateway, open-source', 'Drop-in replacement for Anthropic API, 100+ model support (Bedrock/Azure/local), built-in prompt caching, Prometheus observability.'),
    ('https://github.com/generalaction/emdash', 'AI Agents & Frameworks', 'Emdash ADE', 'An open-source Agentic Development Environment designed to run multiple coding agents in parallel using isolated git worktrees.', 'ade, agentic-ide, parallel-agents, git-worktrees, automation', 'Multi-agent parallelism, Linear/Jira ticket integration, Worktree isolation, Full PR lifecycle management from UI.'),
    ('https://github.com/Chat2AnyLLM/code-assistant-manager', 'Development Tools & Libraries', 'Code Assistant Manager (CAM)', 'A unified Python-based CLI for orchestrating and managing configurations for over 17 different AI coding assistants.', 'cli, orchestration, manager, multi-assistant, productivity', 'Support for 17+ assistants, Centralized provider management, interactive TUI menu, shared Skill/Plugin system.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level)
        VALUES (?, ?, ?, ?, ?, ?, 'deep')
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='deep'
    ''', (url, cat, sd, ld, tags, mf))
conn.commit()
conn.close()
print('Successfully injected batch 5.')
