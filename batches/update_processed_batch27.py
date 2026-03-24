
import os

links = [
    ('https://github.com/derek-larson14/claude-code-openrouter', 'AI Agents & Frameworks', 'Claude-Code-OpenRouter Proxy', 'A bridge enabling Claude Code to use external models (Grok, Gemini, GPT-5) via OpenRouter, with custom model configuration and local context support.', 'proxy, claude-code, openrouter, multi-model', 'Multi-Model access, Custom models.conf, Context Injection, Output directory management.'),
    ('https://github.com/theblazehen/mcp-server-twitter', 'MCP', 'Twitter (X) MCP Server', 'An MCP server providing AI agents with tools to search tweets, post updates, manage mentions, and interact with accounts (like/retweet/follow).', 'mcp, twitter, tools, social-media', 'Tweet Posting, Keyword Search, Mention fetching, Profile retrieval.'),
    ('https://github.com/theblazehen/mcp-server-reddit', 'MCP', 'Reddit MCP Server', 'A Model Context Protocol server enabling AI agents to browse subreddits, search content, submit posts, reply to comments, and vote.', 'mcp, reddit, tools, community', 'Subreddit Browsing, Post Submission, Comment trees, Voting tools.'),
    ('https://github.com/theblazehen/mcp-server-linkedin', 'MCP', 'LinkedIn MCP Server', 'An MCP server for professional networking, allowing AI agents to post updates, search for people and companies, and retrieve user profiles.', 'mcp, linkedin, tools, networking', 'Professional Updates, People Search, Company Search, Profile data retrieval.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
