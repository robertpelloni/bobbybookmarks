
import os

links = [
    ('https://github.com/vishalveerareddy123/Lynkr', 'AI Agents & Frameworks', 'Lynkr LLM Proxy', 'A universal LLM proxy server that decouples AI coding tools from their backends, enabling them to run on any provider (AWS, local, etc.) with significant cost savings.', 'lynkr, proxy, llm-gateway, cost-optimization', 'Provider Agility, 60-80% Cost Reduction, Semantic Caching, Long-term Memory, Local-first support.'),
    ('https://gist.github.com/theblazehen/ae0ba6faec0060909990cc9be000bbbf', 'Guides & Articles', 'MCP Client Implementation Gist', 'A \"gold standard\" technical snippet providing a complete implementation of an MCP Client with dynamic tool discovery and a robust tool-calling loop.', 'gist, mcp, python-sdk, tool-calling', 'Stdio Transport, ClientSession Init, Dynamic Sync, Multiturn Loop Logic.'),
    ('https://github.com/anthropics/claude-agent-sdk-demos', 'AI Agents & Frameworks', 'Claude Agent SDK Demo Suite', 'A collection of full-featured demo applications built with the Claude Agent SDK, including multi-agent research systems and email managers.', 'anthropic, demos, agent-sdk, use-cases', 'Research Agent, Email Assistant, Resume Generator, Web Chat UI.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
