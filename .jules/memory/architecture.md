# Project Memory: Borg Intelligence Harvester (BobbyBookmarks)

## Architecture & Systems
- **Core Purpose**: The system functions as an AI/developer tools database with automated ingestion, LLM-powered enrichment, and data hygiene processes (Borg Intelligence Harvester). It uses ecosystem saturation analysis, gap detection, and mechanism enrichment to formulate recommendations.
- **Database Architecture**: The project heavily relies on SQLite databases. The main data stores include `bookmarks.db` (~61MB) for unified, centralized data, `atlas.db` (~23MB), `borg.db` (~3.4MB), `tormentnexus.db` (~2.8MB), and `metamcp.db`. Deduplication is handled centrally. Data isolation is a core tenant (using partition databases where appropriate).
- **Backend Infrastructure**: 
  - *Python/Flask Backend*: Manages heavy research and database logic (`deep_research.py`, workers, deduplicators).
  - *Go Backend*: Contains an API for various endpoints and workers (located in `backend/internal/api`, `backend/internal/database`, etc.).
  - *TypeScript/Express*: Typically provides a high-speed data layer for the frontend (though some parts of `packages/core` were found missing in the current worktree/repo state).
- **Ingestion Pipeline**: The data ingest uses tools like `_ingest3.py` and `deep_research.py` to process incoming resources. A MultiProviderPool and GeminiModelPool manage LLM request quotas and fallbacks. 
- **Continuous Execution**: Follows a "Don't Stop the Party" directive, ensuring background processes run continuously and autonomously.
- **Frontend / Landing**: Static sites `tormentnexus.site` and `hypernexus.site` are to be deployed using Cloudflare Pages via `.github/workflows/deploy-landing.yml`.

## Patterns & Decisions
- **Unified State & Strict Versioning**: Version strings are stored centrally in `VERSION.md`. Every build/commit must explicitly reference this version string. State is synchronized across databases, maintaining a unified architecture without fragmented contexts.
- **Data Hygiene First**: Deduplication is actively enforced at the script level. For example, `rebuild_prompts.py` enforces a 90% Jaccard similarity deduplication to avoid DB bloat.
- **Data Loss Handling**: When expected files (like `db_v1_28413952.db`, `catalog.db`) or code directories are completely lost and irrecoverable from Git history or local disk, the procedure is to document the loss explicitly in `HANDOFF.md` and rebuild what is viable programmatically (like regenerating the prompt library from external sources).
- **Documentation Standards**: Documentation governance is extremely strict. Important files include `VISION.md`, `ROADMAP.md`, `TODO.md`, `IDEAS.md`, `MEMORY.md`, `DEPLOY.md`, `HANDOFF.md`, and `CHANGELOG.md`. These files act as the system's "memory" to guide autonomous sessions across context resets.
- **Code Comments & Testing**: Code must be heavily commented regarding the *why* and structural side-effects. Testing relies on ensuring build success (e.g., `cd backend && go build -buildvcs=false ./cmd/api` and `cd backend && go test -buildvcs=false ./internal/...`) and verification checks prior to commits.