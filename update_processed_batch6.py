
import os

links = [
    ('https://github.com/CopilotKit/CopilotKit', 'AI Agents & Frameworks', 'CopilotKit Core Framework', 'An open-source frontend stack for building agent-native applications with generative UI, shared state, and seamless human-in-the-loop workflows.', 'copilotkit, frontend-stack, generative-ui, agent-native', 'AG-UI Protocol, Generative UI, useAgent Hook, Shared State Layer, HITL.'),
    ('https://docs.copilotkit.ai/', 'Guides & Articles', 'CopilotKit Documentation', 'Central portal for building in-app copilots and AI agents, providing tutorials for React integration and connecting various AI backends.', 'copilotkit, documentation, react, agents', 'In-App Copilots, AI Agents setup, Copilot Runtime, Generative UI guides.'),
    ('https://www.copilotkit.ai/blog/generative-ui-agentic-interfaces', 'Guides & Articles', 'Generative UI and Agentic Interfaces', 'Research and conceptual overview of Generative UI patterns (Controlled, Declarative, Open-Ended) and the shift to bidirectional AI interfaces.', 'blog, generative-ui, gen-ui, ux-design', 'UI Orchestration, AG-UI Spec, Co-Agents pattern, High-bandwidth AI.'),
    ('https://github.com/CopilotKit/CopilotKit/tree/main/examples', 'Guides & Articles', 'CopilotKit Examples & Showcases', 'A collection of reference applications demonstrating CopilotKit\'s capabilities, including RAG chatbots, spreadsheet copilots, and MCP demos.', 'examples, showcases, use-cases, templates', 'RAG Demo, Spreadsheet Copilot, MCP Integration Demo, Next.js Templates.'),
    ('https://mcp.copilotkit.ai', 'MCP', 'CopilotKit MCP Server', 'A specialized Model Context Protocol server that provides AI editors (Cursor, Claude) with expert knowledge and tool-use for CopilotKit APIs.', 'mcp, documentation-tool, cursor, claude', 'API Expert, Tool-use, Remote Connection, Editor Integration.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
