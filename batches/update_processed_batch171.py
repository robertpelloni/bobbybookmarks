import sqlite3

data = [
    ('https://en.wikipedia.org/wiki/GraalVM', 'Infrastructure & Proxy Layers', 'GraalVM: ML-Static Analysis', 'A polyglot high-performance runtime featuring ML-powered profile inference (GraalNN) to bridge the performance gap between Native Image and JIT.', 'java, graalvm, native-image, machine-learning, performance', 'ML-powered profile inference (GraalNN), sub-100ms CLI startup, zero-overhead polyglot data sharing (GraalPy/JS), FFM API C-library integration.'),
    ('https://en.wikipedia.org/wiki/Jikes_RVM', 'Guides & Industry Trends', 'Jikes RVM: Meta-Circular', 'A foundational meta-circular research JVM written in Java, known for its MMTk modular memory framework and AOS adaptive optimization system.', 'jvm, research, meta-circular, architecture, memory-management', 'Java-in-Java meta-circular core, MMTk (Memory Management Toolkit), AOS (Adaptive Optimization System), "VM Magic" raw memory access.'),
    ('https://en.wikipedia.org/wiki/Fractal-generating_software', 'Development Tools & Libraries', '2026 Fractal Ecosystem', 'A summary of state-of-the-art fractal engines (Chaotica, Mandelbulb 3D) utilizing GPU-acceleration for real-time VFX and architectural design.', 'fractals, vfx, architecture, gpu-acceleration, mathematical-art', 'Real-time GPU flame rendering (Chaotica 2026), 3D landscape hybridization (Mandelbulber), 100k-pixel high-res print support (Ultra Fractal), WebGL browser exploration.'),
    ('https://en.wikipedia.org/wiki/History_of_writing', 'Guides & Industry Trends', 'Writing: Data Abstraction', 'A 10,000-year history of writing viewed as a progression of data abstraction, from physical accounting tokens to high-density phonetic alphabets.', 'information-theory, history, abstraction, tokenization, language', '10,000-year abstraction timeline, accounting-to-language evolution, information density shifts (Logographic vs Alphabetic), material bandwidth expansion (Clay to Papyrus).')
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
print('Successfully injected batch 121.')