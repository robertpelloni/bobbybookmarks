# CHANGELOG.md: BobbyBookmarks Evolution

## [0.1.0] - 2026-03-25
### Added
- **Project Structure**: Created `batches/` and `logs/` directories to clean up the root.
- **Submodules**: Integrated 14 registries and skill repositories (anthropics, openai, stared, etc.).
- **Skills**: Installed 25 specialized skills and agents including `A2A Protocol` and `TaskSync`.
- **Intelligent Deduplication**: New `deduplicator.py` with project-level normalization for GitHub and documentation.
- **Database Unification**: Unified Flask and Express backends to share the root `bookmarks.db`.
- **Master Sync Pulse**: Created `master_sync.py` to automate submodule updates and data cleanup.
- **Auto-Pulse Daemon**: Created `auto_pulse.py` to trigger system syncs hourly in the background.
- **Gemini Research Engine**: Integrated native Gemini support in `tagger.py` and enabled auto-start in `config.py`.
- **Health Monitoring**: Created `health_check.py` for real-time status reporting.
- **UI Stack**: Launched the React/Vite frontend and Express API layers.
- **Core Documentation**: Initialized `VISION.md`, `MEMORY.md`, `ROADMAP.md`, `TODO.md`, `DEPLOY.md`, and `VERSION.md`.

### Fixed
- **Logging**: Resolved log file locks and updated pathing to `logs/borg_research.log`.
- **URL Normalization**: Fixed over-aggressive normalization for non-project sites like Reddit.
- **Database Consistency**: Resolved discrepancies between the root and instance databases via `sync_dbs.py`.

### Changed
- **Config**: Migrated default `LLM_BACKEND` from `mock` to `gemini`.
- **Root Directory**: Restructured scripts and logs for a professional workspace layout.
