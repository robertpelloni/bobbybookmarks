import sqlite3

data = [
    ('https://github.com/BerriAI/litellm', 'Infrastructure', 'LiteLLM Proxy Server', 'A universal Python SDK and AI Gateway that enables calling 100+ different LLM APIs using a unified, OpenAI-compatible format.', 'litellm, proxy, gateway, infrastructure, multi-model', 'Unified API completion, load balancing across providers, cost tracking and spend management, built-in guardrails and observability.'),
    ('https://github.com/sigoden/aichat', 'Development Tools & Libraries', 'AIChat TUI Assistant', 'An all-in-one terminal-based LLM assistant written in Rust, featuring a shell assistant, RAG-based document chat, and agent capabilities.', 'aichat, rust, tui, shell-assistant, rag', 'OS-specific shell command generation, multi-provider model support, local document indexing (RAG), custom agent roles.'),
    ('https://github.com/plandex-ai/plandex', 'AI Agents & Frameworks', 'Plandex AI Coder', 'An open-source AI coding agent designed for long-horizon autonomy and managing complex refactors across large codebases with smart context mapping.', 'plandex, agent, autonomous, code-refactoring, context-management', '2M+ token context window, diff review sandbox, tree-sitter project mapping, automated terminal/test execution.'),
    ('https://github.com/shareAI-lab/Kode-cli', 'AI Agents & Frameworks', 'Kode-cli Workbench', 'A high-performance AI coding assistant built for post-human workflows, featuring multi-model orchestration and parallel subagent delegation.', 'kode-cli, agent, orchestration, sub-agents, workflow', 'Native AGENTS.md support, TaskTool subagent system, fuzzy matching completion, Option+G editor integration.'),
    ('https://www.reddit.com/r/Qodercoding/comments/1oxmdb6/qoder_pro_for_2_only/', 'AI Agents & Frameworks', 'Qoder PRO Analysis', "Community analysis of Alibaba's Qoder AI coding service, highlighting its aggressive pricing and technical challenges with token efficiency.", 'qoder, alibaba, reddit, analysis, pricing', 'Quest Mode vs Agent Mode,Repo Wiki generation, Intelligent task scheduling, multi-line edit predictions.'),
    ('https://app.augmentcode.com/onboard', 'AI Agents & Frameworks', 'Augment Code Platform', 'An enterprise-grade software agent platform powered by a proprietary context engine that maintains a live semantic map of entire codebases.', 'augment-code, enterprise, context-engine, agent, swe-bench', '#1 SWE-Bench Pro ranking, live semantic codebase mapping, Auggie CLI interface, precise code reuse auditing.')
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
print('Successfully injected batch 8.')
