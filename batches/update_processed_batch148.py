import sqlite3

data = [
    ('https://www.reddit.com/r/speckit/comments/1rccoqu/lazyspeckit_speckit_without_babysitting/', 'Agent Orchestration & Workflow', 'LazySpecKit: Auto-Spec', 'A community fork of Spec Kit designed to automate the full spec-to-code lifecycle, featuring autonomous review loops and an "--auto-clarify" mode.', 'workflow, speckit, automation, spec-driven, lazy-dev', 'Autonomous Specify-Plan-Implement cycle, automated multi-agent review loops, --auto-clarify ambiguity resolution, zero-babysitting engineering.'),
    ('https://www.reddit.com/r/unsloth/comments/1r2soh5/run_glm5_locally_guide/', 'Infrastructure & Proxy Layers', 'GLM-5: Local Execution', 'A guide for running the frontier-class GLM-5 model locally using Unsloth\'s 2-bit quantization, shrinking it to 241GB for high-VRAM Linux/Mac environments.', 'glm-5, unsloth, local-llm, quantization, performance', '744B sparse model support, Dynamic 2-bit quantization, 241GB VRAM footprint, 9-13 tokens/sec on H200 hardware.'),
    ('https://www.reddit.com/r/tui/comments/1pxm1gf/pnana_a_modern_tui_text_editor_inspired_by_nano/', 'Interface & Developer UX', 'pNana: Modern TUI Editor', 'A modern C++17 terminal text editor that blends Nano\'s simplicity with Sublime-inspired features like three-pane layouts and smart status bars.', 'tui, editor, cpp, ftxui, terminal', 'C++17/FTXUI core, zero learning curve shortcuts (Ctrl+S), three-pane layout, no-dependency portable executable.'),
    ('https://www.reddit.com/r/tauri/comments/1qzaqfy/switched_from_electron_to_tauri_v2_for_my/', 'Interface & Developer UX', 'Tauri v2: Desktop Agent Hub', 'An analysis of switching to Tauri v2 for local-first AI apps, achieving 58% less memory usage and 96% smaller bundle sizes than Electron.', 'tauri, rust, desktop-app, performance, optimization', 'Rust-native backend performance, 58% memory reduction, mobile platform support (iOS/Android), modular plugin system.')
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
print('Successfully injected batch 98.')