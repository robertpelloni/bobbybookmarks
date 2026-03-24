
import os

links = [
    ('https://github.com/zuisong/gemini-openai-proxy', 'AI Agents & Frameworks', 'Gemini-OpenAI Proxy (zuisong)', 'A portable proxy tool that translates OpenAI API calls to Google Gemini Pro, supporting completions, embeddings, and vision with serverless deployment options.', 'proxy, gemini, openai, api-compat', 'Docker/Node/Bun support, serverless (Vercel/CF), OpenAI TTS compatibility.'),
    ('https://github.com/theblazehen/mcp-server-github', 'MCP', 'GitHub MCP Server', 'A Model Context Protocol server that provides a comprehensive interface for AI agents to manage GitHub repositories, issues, and PRs autonomously.', 'mcp, github, tools, automation', 'Repo Management, File Ops, Issue Tracking, PR creation/merge, Code Search.'),
    ('https://github.com/theblazehen/mcp-server-gitlab', 'MCP', 'GitLab MCP Server', 'An MCP server that enables AI assistants to interact programmatically with GitLab (Cloud/Self-managed) for repository and project management.', 'mcp, gitlab, tools, devops', 'File CRUD, Issue/Merge Request management, Label/Milestone control.'),
    ('https://github.com/theblazehen/mcp-server-bitbucket', 'MCP', 'Bitbucket MCP Server', 'A bridge between the Bitbucket API and MCP clients, allowing AI agents to perform Git operations, code reviews, and PR management on Bitbucket Cloud/Server.', 'mcp, bitbucket, tools, code-review', '27+ Tools, PR Lifecycle, Diff Retrieval, Inline Commenting, Repo Browsing.'),
    ('https://github.com/microsoft/azure-devops-mcp', 'MCP', 'Azure DevOps MCP Server', 'The official Microsoft-maintained MCP server for Azure DevOps, enabling AI agents to manage work items, pipelines, and repositories natively.', 'mcp, azure-devops, microsoft, agentic-ai', 'Work Item CRUD, Pipeline monitoring, Wiki management, Team operations.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
