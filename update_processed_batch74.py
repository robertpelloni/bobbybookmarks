import sqlite3

data = [
    ('https://github.com/infiniflow/ragflow', 'Memory & Persistence Architecture', 'RAGFlow: Deep Document RAG', 'A next-generation RAG engine built on vision-based "Deep Document Understanding," ensuring high-accuracy retrieval from complex PDFs and tables.', 'rag, document-understanding, ocr, indexing, enterprise-ai', 'Vision-based layout/table recognition, template-based chunking, traceable citation engine, human-in-the-loop chunk visualization.'),
    ('https://github.com/hiyouga/LlamaFactory', 'Infrastructure & Proxy Layers', 'LlamaFactory: Unified Tuning', 'A comprehensive and efficient fine-tuning framework supporting 100+ models with integrated SFT, RLHF, and DPO workflows.', 'fine-tuning, llm, mlops, optimization, hf', 'Support for 100+ models (LLaMA/Qwen/DeepSeek), LlamaBoard all-in-one Web UI, efficient training algorithms (Unsloth/DoRA), integrated reward modeling.'),
    ('https://github.com/iOfficeAI/AionUi', 'Interface & Developer UX', 'AionUi: Unified Agent GUI', 'An open-source desktop application that provides a unified graphical interface for terminal-based AI agents like Gemini CLI and Claude Code.', 'gui, desktop-app, orchestration, agent-ui, productivity', 'Multi-agent mode (auto-detects CLIs), zero-setup agent engine, full filesystem operations, professional task assistants (PPTX/Data).'),
    ('https://github.com/khoj-ai/khoj', 'Memory & Persistence Architecture', 'Khoj: AI Second Brain', 'An open-source personal AI application that indexes private data (Notion/Obsidian/GitHub) to provide a private, context-aware digital assistant.', 'personal-ai, second-brain, search, privacy, context-management', 'Multi-source semantic indexing, local-first private storage, cross-platform access (Desktop/WhatsApp), custom knowledge-based agents.')
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
print('Successfully injected batch 40.')
