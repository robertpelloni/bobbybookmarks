import sqlite3

data = [
    ('https://sebgnotes.com/blog/2025-02-05-llms-as-vector-program-databases-a-new-mental-model', 'Guides & Industry Trends', 'LLMs: Vector Program DBs', 'A paradigm shift where LLMs are used as queryable databases of executable logic (vectorized code snippets) for Retrieval-Augmented Software Engineering.', 'programming, vector-db, architecture, logic-engine, software-engineering', 'Vectorized program storage, NL-to-Intent mapping, Retrieval-Augmented Software Engineering (RASE), executable logic synthesis.'),
    ('https://research.phospho.ai/phospho_embeddingalign_rag.pdf', 'Memory & Persistence Architecture', 'Phospho: EmbeddingAlign', 'A research breakthrough introducing a linear transformation layer to align vector spaces to specific datasets, optimizing RAG without fine-tuning.', 'rag, embeddings, research, optimization, vector-search', 'Linear transformation alignment layer, <10ms retrieval latency overhead, trained on single CPU, significant hit rate improvement (0.89 to 0.95).'),
    ('https://servo.org/blog/2025/01/31/servo-in-2024', 'Infrastructure & Proxy Layers', 'Servo Browser Engine 2025', 'A reboot of the Rust-based parallel browser engine focusing on thread splitting for non-blocking JS and modern web standards (Shadow DOM/CSS Grid).', 'browser-engine, rust, performance, standards, web-platform', 'Parallel script/layout thread splitting, Shadow DOM/CSS Grid support, Apple Silicon native support, 79% WPT pass rate (2025).'),
    ('https://rlama.dev/blog/building-local-rag-with-rlama', 'Memory & Persistence Architecture', 'rLama: Private Local RAG', 'A streamlined CLI and visual playground for building private, offline RAG systems that integrate directly with Ollama and support hybrid vector storage.', 'rag, local-llm, ollama, privacy, cli', 'One-command RAG setup (`rlama rag`), visual chunking strategy playground, direct Ollama model integration, hybrid vector/keyword storage.')
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
print('Successfully injected batch 148.')