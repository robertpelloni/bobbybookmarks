
import os

links = [
    ('https://github.com/musistudio/claude-code-router', 'AI Agents & Frameworks', 'Musistudio Claude Code Router', 'A foundational tool for routing Claude Code CLI requests to various LLM providers (AWS Bedrock, Vertex AI, local models) using a flexible transformer system.', 'claude-code, routing, infrastructure, llm-gateway', 'Provider Switching, Payload Transformers, ccr CLI, GitHub Actions integration.'),
    ('https://github.com/musistudio/claude-code-router-action', 'AI Agents & Frameworks', 'Claude Code Router Action', 'A general-purpose GitHub Action that integrates Claude Code\'s autonomous engineering capabilities directly into PRs and Issues.', 'github-actions, automation, ci-cd, agentic-workflows', 'PR Implementation, Issue Answering, @claude Trigger support.'),
    ('https://github.com/musistudio/mcp-music-studio', 'MCP', 'Musistudio MCP Server', 'A specialized Model Context Protocol server that enables AI agents to compose music, supporting multiple instruments and style presets.', 'mcp, music, creativity, tools', '30+ Instruments, Style Presets, Sheet Music generation, Composition API.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
