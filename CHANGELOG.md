# CHANGELOG.md: BobbyBookmarks Evolution


## [0.2.0] - 2026-04-19
### Added
- **Multi-Provider Fallback**: Added OpenRouter and LM Studio integrations with adaptive exponential backoffs in `multi_pool.py`.
- **Public Registry**: Exposed a read-only endpoint for accessing the `borg` innovation index, integrated directly into the dashboard.
- **Deep Research Automation**: Fully ingested the 7,725 raw bookmarks into the AI indexing engine to tag, evaluate, and map out concepts.
- **Cluster Analysis**: Added `rebuild_clusters.py` to automatically cluster related findings using K-Means and TF-IDF.
- **Visual Intelligence**: Added the missing Recharts and D3.js Knowledge Nebula and Borg Consciousness Map graph endpoints to the React frontend.
- **Raw Download Export**: Added the `api/bookmarks/download-txt` feature so users can retrieve their initial text file payloads directly from the dashboard.

### Fixed
- **API Loop Bug**: Stopped the `gemini_pool.py` from continuously slamming endpoints when API limits were exhausted, using proper handling.
- **Security Check Failures**: Removed hardcoded and accidental development API keys pushed into the SQLite database resulting in `GitGuardian` build failures. Rebased Git history to completely purge them from origin memory.

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
