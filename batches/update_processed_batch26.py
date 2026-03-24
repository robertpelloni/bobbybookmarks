
import os

links = [
    ('https://github.com/zhifac/gemini-cli-router', 'AI Agents & Frameworks', 'Gemini-CLI-Router (zhifac)', 'A Node.js proxy that routes Gemini CLI requests to OpenAI-compatible APIs (OpenAI, Azure, OpenRouter) with built-in debug logging and passthrough modes.', 'proxy, gemini-cli, routing, api-compat', 'Multi-provider support, Azure OpenAI integration, Request Logging, Passthrough mode.'),
    ('https://github.com/theblazehen/mcp-server-gmail', 'MCP', 'Gmail MCP Server', 'A Model Context Protocol server enabling AI assistants to manage Gmail tasks like searching, reading, drafting, and downloading attachments using OAuth2.', 'mcp, gmail, tools, productivity', 'Advanced Email Search, Draft creation, Attachment download, Label management.'),
    ('https://github.com/theblazehen/mcp-server-google-drive', 'MCP', 'Google Drive MCP Server', 'An MCP server that integrates Google Drive into AI workflows, automatically converting Docs/Sheets/Slides into AI-friendly Markdown and CSV formats.', 'mcp, google-drive, tools, cloud-storage', 'Full-text Search, Auto-format conversion (Doc->MD, Sheet->CSV), File reading.'),
    ('https://github.com/theblazehen/mcp-server-notion', 'MCP', 'Notion MCP Server', 'A lightweight Python-based MCP server focused on Notion task management and todo list integration, converting block structures to clean Markdown.', 'mcp, notion, tools, task-management', 'Todo management, Database integration, Markdown support, CRUD operations.'),
    ('https://github.com/theblazehen/mcp-server-obsidian', 'MCP', 'Advanced Obsidian MCP', 'A specialized MCP server for structural vault intelligence, allowing AI agents to map note hierarchies and analyze connections between ideas.', 'mcp, obsidian, tools, knowledge-graph', 'Vault Hierarchy Mapping, Graph Analysis (NetworkX), Simple Search, Note patching.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
