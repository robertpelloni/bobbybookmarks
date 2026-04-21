
import os

links = [
    ('https://github.com/starbased-co/ccproxy', 'AI Agents & Frameworks', 'ccproxy Model Router', 'A LiteLLM-based proxy for Claude Code that enables intelligent request routing to Gemini or Perplexity and supports custom \"mods\" for request lifecycle hooks.', 'proxy, claude-code, routing, litellm', 'Model-switching rules, Custom Hook/Mod system, Token-aware routing, Feature injection.'),
    ('https://github.com/theblazehen/mcp-server-vercel', 'MCP', 'Vercel MCP Server', 'An MCP server providing administrative control over Vercel deployments and projects, enabling project creation, env var management, and domain updates.', 'mcp, vercel, tools, deployment', 'Deployment CRUD, Env Var management, Domain control, Project configuration tools.'),
    ('https://github.com/theblazehen/mcp-server-datadog', 'MCP', 'Datadog MCP (Read-only)', 'A high-utility MCP server with 116 tools providing read-only visibility into Datadog Logs, Metrics, Traces, Alerts, and Dashboards for troubleshooting.', 'mcp, datadog, tools, observability', '116 Observability Tools, Zero-write policy, Logs/Trace search, Incident retrieval.'),
    ('https://github.com/theblazehen/mcp-server-sentry', 'MCP', 'Sentry MCP Server', 'An MCP server that bridges AI assistants with Sentry for error retrieval and issue analysis, featuring Seer AI integration for automated fixes.', 'mcp, sentry, tools, debugging', 'Issue Retrieval, Stack Trace analysis, Seer AI integration, Natural Language Search.'),
    ('https://github.com/theblazehen/mcp-server-pagerduty', 'MCP', 'PagerDuty MCP Server', 'A Model Context Protocol server for PagerDuty integration, enabling AI agents to manage incidents, schedules, and on-call rotations autonomously.', 'mcp, pagerduty, tools, sre', 'Incident CRUD, On-call scheduling, Service health checks, User/Team management.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
