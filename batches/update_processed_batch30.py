
import os

links = [
    ('https://github.com/Dhatchinamoorthy/GoogleGeminiRouter', 'AI Agents & Frameworks', 'Xcode 26 Gemini Router', 'A FastAPI-based proxy designed to integrate Google\'s Gemini API with Xcode 26, handling model mapping and bearer token authentication.', 'proxy, gemini, xcode, fastapi', 'Chat Completions, model listing, real-time streaming, CORS-enabled async.'),
    ('https://github.com/HenkDz/postgresql-mcp-server', 'MCP', 'Advanced PostgreSQL MCP', 'A redesigned MCP server that consolidates 46 granular tools into 18 intelligent meta-tools for database management and data manipulation.', 'mcp, postgresql, database, henkdz', 'Consolidated CRUD, Data Manipulation meta-tool, Transaction Control, Performance Inspection.'),
    ('https://github.com/theblazehen/mcp-redis-cloud', 'MCP', 'Redis Cloud MCP Server', 'An MCP server providing a natural language interface for managing Redis Cloud infrastructure, including subscriptions and databases.', 'mcp, redis, cloud-infrastructure, admin', 'Pro/Essential Subscription CRUD, Cloud Region listing, Database module checks.'),
    ('https://github.com/pinecone-database/mcp', 'MCP', 'Pinecone Developer MCP', 'A Model Context Protocol implementation for managing Pinecone indexes and searching documentation, optimized for integrated inference models.', 'mcp, pinecone, vector-database, rag', 'Index CRUD, Stats retrieval, Semantic record search, Reranking, Docs search.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
