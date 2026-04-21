
import os

links = [
    ('https://github.com/a2aproject/A2A', 'AI Agents & Frameworks', 'A2A (Agent-to-Agent) Protocol', 'An open standard for interoperability between diverse AI agents, enabling them to discover capabilities and collaborate using JSON-RPC 2.0.', 'a2a, protocol, interoperability, standards', 'Agent Cards, JSON-RPC 2.0, HTTP(S) Transport, Task Lifecycle, Opacity Preservation.'),
    ('https://github.com/a2anet/a2a-ui', 'AI Agents & Frameworks', 'A2A Reference UI', 'A Next.js based web interface that acts as a universal \"browser\" for A2A-compatible agents, supporting rich message rendering and task management.', 'a2a, ui, nextjs, agent-client', 'Next.js App Router, A2A JS SDK, Session Context, Artifact Rendering, Tool Call Visibility.'),
    ('https://github.com/a2anet/a2a-mcp', 'MCP', 'A2A-to-MCP Bridge', 'An MCP server that allows Model Context Protocol hosts (like Claude) to discover and interact with remote A2A agents as tools.', 'mcp, a2a, bridge, agent-collaboration', 'Agent Discovery tool, Message Routing, Artifact Handling, Claude Desktop integration.'),
    ('https://www.a2aprotocol.ai/', 'Guides & Articles', 'A2A Official Portal', 'The central documentation and resources site for the A2A protocol, featuring the spec, SDK links, and educational materials.', 'a2a, portal, documentation, standards', 'Protocol Spec, SDK Links, DeepLearning.AI Course, Community Resources.'),
    ('https://www.copilotkit.ai/blog/build-with-googles-new-a2a-spec-agent-to-agent-interoperability-with-a2a', 'Guides & Articles', 'A2A Interoperability Overview', 'Research post on how A2A enables a \"backend mesh\" of collaborative agents while AG-UI handles the frontend \"human-in-the-loop\" experience.', 'blog, a2a, interoperability, architecture', 'Backend Mesh, Agent Cards, Coordination Patterns, Framework Agnosticism.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
