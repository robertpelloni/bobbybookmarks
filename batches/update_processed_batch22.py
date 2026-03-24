
import os

links = [
    ('https://github.com/zhu327/gemini-openai-proxy', 'AI Agents & Frameworks', 'Gemini-OpenAI Proxy (zhu327)', 'A Docker-deployable proxy that translates OpenAI API requests to the Google Gemini protocol, allowing existing OpenAI tools to use Gemini models.', 'proxy, gemini, openai, api-compat', 'Chat Completions, Embeddings support, Docker Deployment, Model Mapping.'),
    ('https://github.com/exa-labs/exa-mcp-server', 'MCP', 'Exa Search MCP Server', 'An MCP server that provides AI agents with high-quality, neural search and crawling capabilities using the Exa AI API.', 'mcp, search, exa, neural-search', 'Web Search, Code Context search, Company Research, URL Crawling, Deep Research reports.'),
    ('https://github.com/kshern/mcp-server-tavily', 'MCP', 'Tavily Search MCP Server', 'A Model Context Protocol server that integrates the Tavily API for AI-optimized web search and content extraction for RAG systems.', 'mcp, search, tavily, rag', 'Context-aware Search, Q&A focus, Website Mapping, URL extraction, Caching.'),
    ('https://github.com/theblazehen/mcp-server-brave', 'MCP', 'Brave Search MCP Server', 'An MCP server that bridges AI hosts with the Brave Search API, providing privacy-focused real-time web, local, and news information.', 'mcp, search, brave, privacy', 'Web Search, Local Search, Image/Video Search, Brave native summarization.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
