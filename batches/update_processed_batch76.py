import sqlite3

data = [
    ('https://github.com/microsoft/OmniParser', 'Interface & Developer UX', 'OmniParser: Screen-as-Context', 'A comprehensive screen parsing framework that converts screenshots into structured interactable elements for "Pure Vision" agent control.', 'omniparser, vision-agent, gui-automation, computer-use, microsoft', 'Visual icon/element recognition, pixel-exact coordinate grounding, model-agnostic UI mapping, support for mobile and desktop screens.'),
    ('https://github.com/microsoft/markitdown', 'Memory & Persistence Architecture', 'MarkItDown: Multimodal MD', 'A Python utility for converting diverse file formats (PDF/Office/Images) into structured Markdown optimized for AI context and RAG.', 'markitdown, markdown, rag, data-ingestion, preprocessing', 'Broad format support (Word/Excel/PPTX), OCR-based image-to-text, audio-to-text transcription, integrated MCP server support.'),
    ('https://github.com/microsoft/promptflow', 'Agent Orchestration & Workflow', 'Microsoft Prompt Flow', 'A suite of tools for "GenAIOps" that enables the visual design, tracing, evaluation, and deployment of complex AI agentic workflows.', 'prompt-flow, llmops, workflow, orchestration, tracing', 'Visual executable flows, detailed interaction tracing, built-in quality evaluation tools, streamlined endpoint deployment.'),
    ('https://github.com/microsoft/semanticworkbench', 'Agent Orchestration & Workflow', 'Semantic Workbench', 'A production-grade infrastructure for prototyping multi-agent systems, managing state, conversation history, and collaborative workspaces.', 'semantic-workbench, infrastructure, multi-agent, collaboration, sandbox', 'State management for agents, shared semantic workspaces, conversation history persistence, file attachment orchestration.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 10) for d in data]:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level, innovation_score)
        VALUES (?, ?, ?, ?, ?, ?, 'borg', ?)
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='borg',
            innovation_score=excluded.innovation_score
    ''', (url, cat, sd, ld, tags, mf, score))
conn.commit()
conn.close()
print('Successfully injected batch 42.')
