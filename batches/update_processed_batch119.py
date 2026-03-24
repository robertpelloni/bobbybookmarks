import sqlite3

data = [
    ('https://www.reddit.com/r/LocalLLaMA/comments/1q6sp4b/sopro_a_169m_parameter_realtime_tts_model_with/', 'Interface & Developer UX', 'SoPro: CPU-Native TTS', 'A 169M parameter Text-to-Speech model that achieves 4x real-time generation on CPU with zero-shot voice cloning from 3s of audio.', 'tts, voice-cloning, low-latency, edge-ai, cpu-native', '0.25 RTF on standard CPU, 3-12s zero-shot cloning, <1GB VRAM footprint, Apache 2.0 open-weights.'),
    ('https://www.reddit.com/r/LocalLLaMA/comments/1pze13o/exploring_a_158bit_ternary_llm_core_inspired_by/', 'Infrastructure & Proxy Layers', 'Trion: 1.58-bit Ternary Core', 'An extreme-quantization LLM core that uses {-1, 0, +1} ternary weights to achieve massive throughput on low-end hardware.', 'quantization, ternary-llm, bitnet, cuda, optimization', 'Straight-Through Estimator (STE) training, Sign+Mask CUDA kernels, zero-softmax attention, high-throughput low-power reasoning.'),
    ('https://www.reddit.com/r/LocalLLaMA/comments/1qb034t/github_deepseekaiengram_conditional_memory_via/', 'Memory & Persistence Architecture', 'DeepSeek Engram Memory', 'A conditional memory system that uses hashed token n-grams to offload static knowledge to system RAM, enabling O(1) context lookup.', 'memory-architecture, deepseek, engram, optimization, ram-offloading', 'Hashed n-gram deterministic lookup, 45% VRAM reduction, O(1) knowledge recall, persistent factual memory axis.'),
    ('https://www.reddit.com/r/LocalLLaMA/comments/1qcuerc/nvidias_new_8b_model_is_orchestrator8b_a/', 'Agent Orchestration & Workflow', 'NVIDIA Orchestrator-8B', 'A specialized "Middle Manager" model fine-tuned for high-reliability tool-calling and multi-agent task delegation.', 'orchestration, middle-manager, tool-calling, nvidia, routing', 'Extreme delegation focus, sub-agent task routing, native tool-invocation preference, low-latency coordination core.')
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
print('Successfully injected batch 68.')
