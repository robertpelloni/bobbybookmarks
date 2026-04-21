
import os

links = [
    ('https://github.com/ag-ui-protocol/ag-ui', 'AI Agents & Frameworks', 'AG-UI (Agent-User Interaction) Protocol', 'An open, event-based standard for connecting AI agents to frontends, enabling real-time chat, state sync, and generative UI.', 'ag-ui, protocol, generative-ui, frontend', 'Real-time Chat, State Sync, Middleware Transports, Multi-framework support.'),
    ('https://ag-ui.org/', 'Guides & Articles', 'AG-UI Official Portal', 'The central documentation and demo site for the AG-UI protocol, featuring the \"AG-UI Dojo\" interactive playground.', 'ag-ui, portal, dojo, documentation', 'Live Demo, Integration Guides, Protocol Specs, SDK links.'),
    ('https://github.com/theblazehen/react-ag-ui', 'Development Tools & Libraries', 'react-ag-ui Components', 'Lightweight, unopinionated React components (MessageList, ChatHeader) designed to build interfaces for AG-UI compliant backends.', 'react, ag-ui, ui-components, chat', 'ChatProvider, Typed Store Sync, Generative UI support, CopilotKit integration.'),
    ('https://github.com/anthropics/claude-agent-sdk-typescript', 'AI Agents & Frameworks', 'Claude Agent SDK for TypeScript', 'Official SDK for building autonomous agents with Claude Code\'s capabilities, including file editing and command execution.', 'anthropic, typescript, agent-sdk, claude-code', 'Codebase Analysis, File Editing (edit.ts), Command Execution (bash.ts), Workflow Hooks.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
