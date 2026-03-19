
import os

links = [
    ('https://github.com/Hk-Gosuto/vercel-ai-proxy', 'AI Agents & Frameworks', 'Vercel Edge AI Proxy', 'A lightweight API proxy running on Vercel\'s edge network, supporting multiple providers (Gemini, Groq, Claude) to bypass regional restrictions.', 'proxy, vercel, edge, multi-provider', 'Serverless Routing, Vercel Edge integration, Multi-LLM support, Custom domains.'),
    ('https://github.com/emmett.deen/linear-mcp-server', 'MCP', 'Linear MCP Server', 'A Model Context Protocol server that bridges AI assistants with the Linear platform for managing issues, projects, and cycles via natural language.', 'mcp, linear, tools, project-management', 'Issue CRUD, Workspace Metadata, Batch actions, Human-readable feedback.'),
    ('https://github.com/theblazehen/mcp-server-jira', 'MCP', 'Jira MCP Server', 'An MCP server providing AI agents with direct access to Jira Cloud/Server for issue tracking, status transitions, and bulk operations.', 'mcp, jira, tools, issue-tracking', 'JQL Search, Status Transitions, Markdown-to-ADF conversion, Custom Field support.'),
    ('https://github.com/theblazehen/mcp-server-asana', 'MCP', 'Asana MCP Server', 'A Model Context Protocol server that exposes the Asana API as a set of tools for task management, project organization, and status auditing.', 'mcp, asana, tools, collaboration', 'Task/Project CRUD, Read-only mode, Subtask management, Status auditing prompts.'),
    ('https://github.com/delorenj/mcp-server-trello', 'MCP', 'Trello MCP Server', 'A comprehensive MCP server implementation for Trello, allowing AI agents to manage boards, lists, and cards with built-in rate limiting.', 'mcp, trello, tools, task-management', 'Board/List/Card management, Attachment support, Member listing, Bun runtime optimized.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
