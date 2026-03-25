# MEMORY.md: Ongoing Observations and Preferences

## Architectural Insights
- **Dual-Backend Reality**: The project uses both **Flask (Python)** and **Express (Node.js)**. Flask handles heavy research and database logic, while Express provides a high-speed data layer for the modern React/Vite UI.
- **Database Unification**: Initially, the Flask app used a separate database in `instance/`. We have since unified the system to point all components to the root `bookmarks.db` for consistency.
- **Master Sync Pulse**: We created a central `master_sync.py` to coordinate submodules, deduplication, and database maintenance. This should be the "source of truth" for system updates.
- **Process Persistence**: On `win32`, background processes started via `Start-Process` can be "invisible" to standard status tools. Using the Gemini CLI `is_background` flag is more reliable.

## Codebase Preferences
- **Universal Normalization**: Always use `deduplicator.normalize_url` or `get_project_url` instead of local regex/parsing logic to ensure deduplication works across the entire stack.
- **No Stop the Party**: The user explicitly requested **never terminating active background processes** (workers, servers) during a session unless absolutely necessary for an update.
- **Documentation First**: All new features and major changes must be reflected in `CHANGELOG.md`, `ROADMAP.md`, and `TODO.md` immediately.

## Discovery Notes
- **LLM Quota Management**: Quota exhaustion (429) is a recurring reality. The `GeminiModelPool` logic is crucial for continuous background operation.
- **Borg Taxonomy**: The specific categories in `deep_research.py` (e.g., "Connectivity & Interoperability (MCP/A2A)") are the primary schema for high-quality intelligence.
- **Skills Directory**: `skills/` is the location for universally usable model instructions. We have a robust collection integrated from various community sources.
