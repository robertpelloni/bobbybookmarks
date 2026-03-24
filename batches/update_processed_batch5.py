
import os

links = [
    ('https://www.crewai.com/', 'AI Agents & Frameworks', 'CrewAI Enterprise Platform', 'A comprehensive platform for building, managing, and scaling teams of collaborative AI agents using a visual editor or a powerful API.', 'crewai, multi-agent, enterprise-ai, orchestration', 'Role-based Agents, Visual Workflow Editor, Serverless Scaling, Tracing & Monitoring.'),
    ('https://github.com/crewAIInc/crewAI', 'AI Agents & Frameworks', 'CrewAI Core Framework', 'Official Python framework for orchestrating role-playing autonomous AI agents, enabling collaborative intelligence through Crews, Tasks, and Agents.', 'crewai, python, agents, collaboration', 'Sequential/Hierarchical Processes, Role-playing, Memory Management, Tool Use.'),
    ('https://docs.crewai.com/', 'Guides & Articles', 'CrewAI Documentation', 'The official documentation portal for CrewAI, featuring quickstart guides, core concept explanations, and deployment instructions.', 'crewai, documentation, tutorials, api-ref', 'Getting Started, Agent/Task/Crew Docs, Flow Orchestration, CLI Commands.'),
    ('https://github.com/crewAIInc/crewAI-examples', 'Guides & Articles', 'CrewAI Examples Repository', 'A collection of real-world examples and project templates demonstrating how to use CrewAI for various automated workflows.', 'examples, use-cases, crewai, templates', 'Trip Planner, Job Posting, Markdown Validation, Stock Analysis.'),
    ('https://www.crewai.com/mcp', 'AI Agents & Frameworks', 'CrewAI MCP Integration', 'First-class support for the Model Context Protocol (MCP) in CrewAI, allowing agents to dynamically discover and use external tools.', 'mcp, crewai, tool-use, interoperability', 'DSL Integration (mcps=[]), Stdio/SSE/HTTP Transports, Tool Filtering, Caching.'),
    ('https://docs.crewai.com/how-to/cli/', 'Development Tools & Libraries', 'CrewAI CLI', 'The official command-line tool for scaffolding projects, running crews, training agents with feedback, and deploying to production.', 'cli, deployment, crewai, project-management', 'crewai create, crewai run, crewai chat, crewai train, crewai deploy.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
