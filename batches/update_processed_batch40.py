import sqlite3

data = [
    ('https://github.com/sst/opencode', 'AI Agents & Frameworks', 'SST OpenCode Rebuild', 'A 100% open-source and provider-agnostic rebuild of the OpenCode CLI, enabling developers to use any LLM with deep LSP integration.', 'opencode, sst, open-source, model-agnostic, lsp', 'Multi-model support (75+ models), specialized Plan/Coder agents, AST-aware refactoring, reusable Skill.md support.'),
    ('https://github.com/charmbracelet/crush', 'AI Agents & Frameworks', 'Crush Agentic CLI', 'A high-performance, glamorous agentic coding assistant from the Charm team, featuring deep MCP integration and a premium TUI experience.', 'crush, charm, tui, mcp, bubble-tea', 'Unified MCP gateway, Docker-based tool catalog, multi-session task management, LSP-enhanced codebase understanding.'),
    ('https://github.com/factory-ai/factory', 'AI Agents & Frameworks', 'Factory Enterprise Droids', 'An enterprise-grade platform utilizing specialized AI "Droids" to automate end-to-end software engineering workflows within corporate CI/CD cycles.', 'factory, enterprise, droids, automation, workflows', 'Autonomous file execution and PR submission, SOC 2/GDPR compliance, deep integration with Linear/Jira/Sentry, usage-based token billing.'),
    ('https://github.com/CodebuffAI/codebuff', 'AI Agents & Frameworks', 'Codebuff Coordinated Intelligence', 'A multi-agent system designed for high-accuracy codebase editing by coordinating specialized picking, planning, and editing agents.', 'codebuff, multi-agent, accuracy, openrouter, sdk', '61% task success rate, model-agnostic (via OpenRouter), TypeScript generator support, embeddable SDK.'),
    ('https://github.com/moazbuilds/CodeMachine-CLI', 'AI Agents & Frameworks', 'CodeMachine Orchestration', 'A structured engine for orchestrating and managing long-running workflows across multiple AI coding CLIs like Claude Code and Cursor.', 'codemachine, orchestration, manager, workflow, persistence', 'Engine-agnostic management, Ali 5-step workflow builder, Autonomous "Clone" controller agent, BMad story-based task breakdown.'),
    ('https://github.com/MoonshotAI/kimi-cli', 'AI Agents & Frameworks', 'Kimi-CLI Shell Agent', 'A terminal-native AI agent powered by Kimi K2.5, blending traditional shell operations with massive multi-agent swarm capabilities.', 'kimi, moonshot-ai, cli, swarm, visual-intelligence', '100-agent Swarm mode, native Zsh/shell integration, visual UI screenshot analysis, low-cost flagship performance.'),
    ('https://github.com/openai/codex', 'AI Agents & Frameworks', 'OpenAI Codex Digital Employee', 'The evolved autonomous software engineering agent from OpenAI, designed for long-horizon autonomy and independent issue resolution.', 'codex, openai, digital-employee, autonomy, gpt-5', 'GPT-5.2-Codex architecture, AGENTS.md instruction support, secure sandbox testing, native GitHub comment triggering.'),
    ('https://ampcode.com/', 'AI Agents & Frameworks', 'Amp Frontier Agent', 'A frontier coding agent platform built for high-performance teams, prioritizing high-quality outcomes through multi-agent orchestration.', 'amp, frontier-ai, oracle, productivity, document-generation', 'Oracle/Search/Librarian sub-agents, Deep Mode reasoning (GPT-5.3), built-in Mermaid diagram generation, outcome-oriented autonomy.'),
    ('https://qoder.com/referral', 'AI Agents & Frameworks', 'Qoder Agentic Platform', "Alibaba's agentic coding platform featuring autonomous 'Quest Mode' and automated repository wiki maintenance.", 'qoder, alibaba, quest-mode, wiki, automation', 'Autonomous Quest execution, automated Repo Wiki documentation, Intelligent task scheduling, multi-line edit predictions.'),
    ('https://github.com/block/goose', 'AI Agents & Frameworks', 'Goose Open Agent', 'An open-source, extensible AI agent from Block Inc. that serves as a reference implementation for the Model Context Protocol (MCP).', 'goose, block, open-source, mcp, hackable', 'MCP-native extensibility, local filesystem/terminal access, cross-project session tracking, multi-model config support.')
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
print('Successfully injected batch 7.')
