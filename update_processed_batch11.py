
import os

links = [
    ('https://platform.iflow.cn/models', 'AI Agents & Frameworks', 'iFlow Open Platform', 'A developer-centric AI ecosystem providing high-performance MoE models (iFlow-ROME) and infrastructure for autonomous agents.', 'iflow, models, infrastructure, developer-platform', 'MoE Architectures, iFlow-ROME, Long-context (1M), API/CLI access.'),
    ('https://github.com/iflow-ai/iflow-cli', 'AI Agents & Frameworks', 'iFlow CLI', 'A Rust-based terminal intelligence for repository analysis and autonomous coding, featuring multiple safety modes and sub-agent delegation.', 'cli, rust, autonomous-coding, acp', 'YOLO Mode, Plan Mode, Sub-agent Market, GitHub Action integration.'),
    ('https://github.com/iflow-ai/iflow-cli-action', 'AI Agents & Frameworks', 'iFlow CLI Action', 'An official GitHub Action that automates repository maintenance and coding tasks using the iFlow agentic ecosystem.', 'github-actions, automation, maintenance, ci-cd', 'Automated Refactoring, Bug Fixing, Pull Request Automation.'),
    ('https://github.com/iflow-ai/AgentFlow', 'AI Agents & Frameworks', 'AgentFlow Optimization', 'A framework for optimizing agentic systems using Flow-based Group Refined Policy Optimization (Flow-GRPO) to improve tool-calling reliability.', 'optimization, grpo, reasoning, tool-use', 'Flow-GRPO, Policy Optimization, Reliable Reasoning, Tool Reliability.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
