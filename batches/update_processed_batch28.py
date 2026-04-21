
import os

links = [
    ('https://github.com/takltc/gemini-router', 'AI Agents & Frameworks', 'Gemini-Router Proxy', 'A Cloudflare Worker that translates between the Anthropic and Google Gemini APIs, allowing Claude-optimized tools to use Gemini models.', 'proxy, gemini, anthropic, cloudflare-worker', 'API Translation, Response Mapping, Streaming support, Tool compatibility.'),
    ('https://github.com/theblazehen/mcp-server-stripe', 'MCP', 'Stripe MCP Server', 'An MCP server that exposes core Stripe API functionalities, including customer management, payment processing, and subscription billing.', 'mcp, stripe, tools, finance', 'Customer CRUD, PaymentIntents, Subscription lifecycle, Product management.'),
    ('https://github.com/theblazehen/mcp-server-paypal', 'MCP', 'PayPal MCP Server', 'A Model Context Protocol server providing an interface for the PayPal REST API, enabling AI agents to manage orders and process payments.', 'mcp, paypal, tools, payments', 'Order Authorization, Payment capture, Subscription profiles, Transaction history.'),
    ('https://github.com/theblazehen/mcp-server-shopify', 'MCP', 'Shopify MCP Server', 'An MCP server for Shopify store interaction, allowing AI agents to perform administrative tasks like product management and order fulfillment.', 'mcp, shopify, tools, e-commerce', 'Product/Inventory CRUD, Order processing, Customer insights, Store config.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
