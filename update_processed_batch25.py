
import os

links = [
    ('https://github.com/Jasonzhangf/gemini-cli-router', 'AI Agents & Frameworks', 'Gemini CLI Router', 'A zero-modification proxy system that intercepts Google Gemini CLI requests and routes them to alternative providers like OpenAI or Claude.', 'proxy, gemini-cli, routing, api-compat', 'Multi-provider support, OAuth Proxy, Model Overrides, Zero-mod installation.'),
    ('https://github.com/theblazehen/mcp-server-slack', 'MCP', 'Slack MCP Server', 'An MCP server that bridges AI assistants with Slack workspaces for reading history, posting messages, and managing channel metadata.', 'mcp, slack, tools, communication', 'Channel History, Message Posting, Thread Retrieval, CSV directory resources.'),
    ('https://github.com/theblazehen/mcp-server-discord', 'MCP', 'Discord MCP Server', 'A secure MCP server for Discord integration featuring JWT Bearer Token authentication to protect bot credentials during agent sessions.', 'mcp, discord, tools, security', 'JWT Auth, Message Sending, History Retrieval, Content Moderation tools.'),
    ('https://github.com/theblazehen/mcp-server-telegram', 'MCP', 'Telegram MTProto MCP', 'An MCP server using the MTProto protocol to allow AI agents to interact with Telegram as the user (reading chats, sending as self).', 'mcp, telegram, tools, mtproto', 'Personal Account sync, Dialog Listing, Message Reading, 2FA support.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
