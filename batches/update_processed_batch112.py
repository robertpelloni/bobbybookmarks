import sqlite3

data = [
    ('https://www.reddit.com/r/DeepSeek/comments/1qkoc53/deepseekv32_matches_gpt5_at_10x_lower_cost_introl/', 'Guides & Industry Trends', 'DeepSeek-V3.2: Sparse MoE', 'A performance breakthrough demonstrating GPT-5 level reasoning at 10x lower cost via a highly optimized Sparse Attention and Mixture of Experts (MoE) architecture.', 'deepseek, moe, sparse-attention, benchmarking, cost-reduction', 'Sparse Attention parameter activation, $0.028/M token pricing, math/logic reasoning dominance, efficient $5.5M training budget.'),
    ('https://www.reddit.com/r/CodexAutomation/comments/1qn9g8w/codex_cli_updates_0900_0910_network_sandbox_proxy/', 'Infrastructure & Proxy Layers', 'Codex CLI Sandbox Proxy', 'A policy-enforced network proxy for autonomous agents that restricts outbound calls to approved endpoints and implements sub-agent fan-out guardrails.', 'security, sandboxing, proxy, guardrails, orchestration', 'Policy-enforced outbound network proxy, sub-agent fan-out limits (recursive protection), secure API endpoint whitelisting, autonomous task safety.'),
    ('https://www.reddit.com/r/ContextEngineering/comments/1pwe9my/the_context_layer_ai_agents_actually_need/', 'Memory & Persistence Architecture', 'The Unified Context Layer', 'A proposal for a structured state management system that strips JSON bloat and formats history with system instructions for high-fidelity active memory.', 'context-engineering, state-management, memory-architecture, optimization, instruction-wrapping', 'JSON-bloat stripping, instruction-wrapped history, active memory substrate, multi-agent context synchronization.'),
    ('https://www.reddit.com/r/ContextEngineering/comments/1pt2oxf/you_can_now_move_your_entire_history_and_context/', 'Memory & Persistence Architecture', 'Inter-Agent State Porting', 'A mechanism for seamless context transfer between different agent providers (e.g., Claude to Codex) using vector-ready state files.', 'interop, context-porting, state-transfer, memory-forge, cross-platform', 'Vector-ready state file generation, seamless history porting, instruction-stable context migration, provider-agnostic memory forge.')
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
print('Successfully injected batch 71.')
