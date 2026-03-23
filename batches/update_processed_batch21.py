
import os

links = [
    ('https://github.com/PublicAffairs/openai-gemini', 'AI Agents & Frameworks', 'OpenAI-to-Gemini API Proxy', 'A serverless proxy that translates OpenAI API requests into Gemini API calls, enabling OpenAI-compatible tools to work with Google\'s models.', 'proxy, gemini, openai, api-compat', 'Chat Completions, Embeddings, Vision/Audio support, Serverless Deploy (Vercel/CF).'),
    ('https://github.com/theblazehen/mcp-server-wolfram-alpha', 'MCP', 'Wolfram Alpha MCP Server', 'An MCP server that connects LLMs to the Wolfram|Alpha API for precise mathematical and scientific computations.', 'mcp, wolfram-alpha, tools, computation', 'complex math, factual data retrieval, unit conversions, precision query.'),
    ('https://github.com/theblazehen/mcp-server-playwright', 'MCP', 'Playwright Browser MCP', 'An MCP server enabling AI agents to perform browser automation and web scraping using Playwright.', 'mcp, browser-automation, scraping, playwright', 'Live Web Browsing, Element Clicking, Form Filling, Content Extraction.'),
    ('https://github.com/theblazehen/mcp-get', 'Development Tools & Libraries', 'mcp-get Installer', 'A command-line installer for Model Context Protocol (MCP) servers, acting as a package manager for the MCP ecosystem.', 'cli, mcp, package-manager, installer', 'Server Discovery, Automated Config, One-click Install, Version Management.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
