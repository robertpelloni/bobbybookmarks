import sqlite3

data = [
    ('https://www.zenable.app/dashboard', 'Infrastructure & Proxy Layers', 'Zenable: AI Guardrails', 'An AI governance platform that monitors and enforces security standards in real-time as AI coding assistants (Cursor/Claude Code) generate code.', 'security, governance, dev-tools, compliance, orchestration', 'Real-time AI code security scanning, auto-fix vulnerability remediation, custom architectural policy enforcement, PR/Commit hook integration.'),
    ('https://www.zine.ai/', 'Interface & Developer UX', 'Zine (Dzine.ai): Gen Editing', 'An AI-powered image generation suite functioning as a professional non-destructive editor with stable character generation across multiple prompts.', 'generative-ai, design, image-editing, multimodal, ux', 'Layer-based non-destructive workflow, consistent character generation (branding), generative fill/expansion, 6144x6144 high-res output.'),
    ('https://yapnotes.com/', 'Interface & Developer UX', 'Yapnotes: Voice Summaries', 'An AI-powered audio application that transcribes "messy" unstructured voice memos and converts them into polished, structured notes and action items.', 'voice-ai, transcription, productivity, ios, memory', 'Filler-word removal (um/ah filtering), structured Markdown summarization, "Chat with recording" semantic retrieval, iOS Dynamic Island support.'),
    ('https://yodaplus.com/blog/mcp-vs-langchain-agents-vs-autogen-which-protocol-wins-where', 'Guides & Industry Trends', 'Orchestrator Comparison', 'A 2026 architectural breakdown comparing MCP (Enterprise Standardization), LangChain (Rapid Prototyping), and AutoGen (Multi-agent Simulation).', 'mcp, langchain, autogen, orchestration, architecture', 'MCP positioned as Enterprise Data Standardization, LangChain for rapid MVPs, AutoGen for complex "Human-in-the-loop" multi-agent simulations.')
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
print('Successfully injected batch 178.')