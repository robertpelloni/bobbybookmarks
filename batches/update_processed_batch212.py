import sqlite3

data = [
    ('https://www.reddit.com/r/mcp/comments/1p287ou/reducing_mcp_token_usage_by_100x_you_dont_need', 'Agent Orchestration & Workflow', 'MCP Code Execution', 'A paradigm shift in MCP orchestration where agents write and execute Python/TS scripts to handle intermediate JSON payloads, reducing token usage by up to 98.7%.', 'mcp, code-execution, optimization, tokens, orchestration', 'Sandboxed script execution (Python/TS), up to 98.7% token reduction, elimination of multi-turn JSON payload ping-pong, progressive tool discovery.'),
    ('https://www.reddit.com/r/mcp/comments/1phupt8/built_a_simple_metamcp_server_code_mode_to', 'Infrastructure & Proxy Layers', 'MetaMCP: Code Mode Proxies', 'Implementations of MCP proxy servers (like Bifrost) that generate `.d.ts` type declarations and execute agent-written TypeScript within Goja VM sandboxes.', 'mcp, proxy, code-mode, sandboxing, typescript', 'Goja VM sandboxing, automated `.d.ts` type generation for MCP tools, lazy-loaded MCP definitions, chained execution blocks.'),
    ('https://www.reddit.com/r/mcp/comments/1pj3icd/implemented_anthropics_programmatic_tool_calling', 'Agent Orchestration & Workflow', 'Programmatic Tool Calling', 'Open-source implementations (Open PTC Agent, Zypher) of Anthropic\'s Programmatic Tool Calling, treating MCP tools as importable functions within Deno/Python scripts.', 'mcp, tool-calling, orchestration, lang-chain, deno', 'Tool-as-importable-function paradigm, Deno Worker sandboxing, local LLM support via LangChain, complex logic chaining (loops/conditionals).'),
    ('https://www.reddit.com/r/newAIParadigms/comments/1og97zw/breakthrough_for_continual_learning_lifelong', 'AI Agents & Frameworks', 'Meta: Continuous Learning', 'A breakthrough training method by Meta utilizing Sparse Attention to finetune models on new data without catastrophic forgetting, enabling lifelong learning agents.', 'research, continual-learning, sparse-attention, meta, finetuning', 'Continuous Learning via Sparse Memory Finetuning, prevention of catastrophic forgetting, targeted parameter updates, lifelong agent memory integration.')
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
print('Successfully injected batch 172.')