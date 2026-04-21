import sqlite3

data = [
    ('https://alternativeto.net/software/jwildfire/about', 'Interface & Developer UX', 'JWildfire: GPU Fractals', 'A premier open-source flame fractal generator featuring the JWildfireSwan GPU engine for near-real-time rendering of complex mathematical art.', 'fractals, mathematics, gpu-rendering, open-source, generative-art', 'JWildfireSwan GPU backend, painterly aesthetic variations, solid rendering overhaul, background transforms for complex layering.'),
    ('https://alternativeto.net/software/super-productivity/about', 'Agent Orchestration & Workflow', 'Super Productivity: Agentic', 'A privacy-first, local-first task manager that integrates with local LLMs (Ollama) to autonomously generate sub-tasks and schedule focus blocks.', 'productivity, local-llm, ollama, orchestration, task-management', 'Local LLM (Ollama) sub-task generation, autonomous scheduling blocks, cross-platform (Win/Mac/Linux), privacy-focused offline core.'),
    ('https://alternativeto.net/software/visions-of-chaos', 'Development Tools & Libraries', 'Visions of Chaos: ML GUI', 'The most comprehensive Windows GUI for local machine learning, automating the setup of complex Python environments for SD, LoRA, and fluid simulations.', 'ml, simulations, generative-art, windows, automation', 'Automated ML environment setup (TensorFlow/PyTorch), 100+ built-in ML/GAN/CLIP models, LoRA training support, thousands of mathematical simulations.'),
    ('https://alternativeto.net/software/vibe-transcribe/about', 'Infrastructure & Proxy Layers', 'Vibe: Local Transcription', 'A privacy-first desktop app for local audio/video transcription using Whisper, featuring Ollama integration for instant summaries and MCP support.', 'transcription, privacy, whisper, mcp, local-first', '100% offline Whisper transcription, Ollama-powered local summaries, speaker diarization (120+ languages), native MCP server support.')
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
print('Successfully injected batch 116.')