
import os

links = [
    ('https://github.com/NeuralNomadsAI/CodeNomad', 'AI Agents & Frameworks', 'CodeNomad Cockpit', 'A high-performance command center for OpenCode power users, enabling side-by-side session management and keyboard-first control.', 'codenomad, opencode, gui, orchestration', 'Multi-instance Tabs, Command Palette, Native Performance, Asset Previews, Tauri App.'),
    ('https://github.com/anthropics/claude-agent-sdk-typescript/tree/main/packages/sdk/src/memory', 'AI Agents & Frameworks', 'Claude Agent SDK Memory System', 'Detailed memory implementations within the TypeScript SDK, covering short-term working memory, persistent long-term storage, and context management.', 'anthropic, memory, state-management, persistence', 'Short-term Memory, Long-term Storage, Context Windowing, Session Persistence.'),
    ('https://github.com/asimov-platform', 'AI Agents & Frameworks', 'ASIMOV Project Organization', 'A polyglot development platform for neurosymbolic AI, featuring a Rust-based CLI and SDKs for multi-agent coordination and module management.', 'asimov, neurosymbolic, rust, platform', 'ASIMOV CLI, Rust SDK (asimov.rs), Python SDK, Modular Architecture.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
