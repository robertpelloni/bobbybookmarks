import sqlite3

data = [
    ('https://www.google.com/search?q=what+are+the+hardware+options+available+for+running+large+llm+locally', 'Infrastructure & Proxy Layers', '2026 Local LLM Hardware', 'An overview of the 2026 hardware landscape for local LLM inference, highlighting the shift toward high-memory APUs and multi-GPU configurations.', 'hardware, local-llm, inference, vram, amd-strix', 'AMD Ryzen AI Max+ (Strix Halo) 128GB APUs, NVIDIA Blackwell (RTX 50) bandwidth upgrades, Mac Studio M5 Ultra (192GB unified memory), high-quantization offloading.'),
    ('https://www.google.com/search?q=compile+c%2B%2B+code+in+java', 'Development Tools & Libraries', 'Java Panama: C++ Interop', 'A shift in Java ecosystem standards replacing legacy JNI with Project Panama (Foreign Function & Memory API) for near-native C/C++ execution.', 'java, cpp, jni, project-panama, interoperability', 'Project Panama Foreign Function & Memory API, JExtract automatic C/C++ binding generation, GraalVM Native Image compilation, zero-overhead ABI access.'),
    ('https://electricsheep.org/', 'Interface & Developer UX', 'Electric Sheep: 2026', 'The modern evolution of the classic distributed fractal screensaver, utilizing neural style transfer and latent space exploration mixed with traditional mathematical algorithms.', 'fractals, distributed-compute, generative-art, screensaver, genetic-algorithm', 'Distributed genetic breeding algorithm, 4K/8K "Gold" resolution, AI-hybrid neural style transfer, cross-platform distributed rendering.'),
    ('https://www.google.com/search?q=add+c%2B%2B+syntax+support+to+java+language', 'Development Tools & Libraries', 'Polyglot C++/Java Support', 'The 2026 evolution of IDE and build tool integration allowing seamless cross-compilation and unified debugging of C++ code embedded within Java projects.', 'ide, polyglot, java, cpp, tooling', 'Visual Studio 2026 Polyglot Notebooks, JetBrains Remote Development C++ offloading, C++26 Reflection integration, Eclipse CDT unified debugging.')
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
print('Successfully injected batch 161.')