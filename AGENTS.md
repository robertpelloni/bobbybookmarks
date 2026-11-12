# AGENTS.md — Universal Model & Agent Directives

All autonomous and interactive agents operating in `bobbybookmarks` must follow [RUNBOOK.md](./RUNBOOK.md), [VISION.md](./VISION.md), and [MEMORY.md](./MEMORY.md).

## Core Invariants
1. **"Don't Stop the Party"**: Never blanket-kill background processes (`python`, `go`, `node`) or touch external agent sessions. Only manage specific child processes spawned by your own session.
2. **Preserve Data, Memory & Sessions**: Never gitignore or delete SQLite databases (`bookmarks.db`, `atlas.db`, `tormentnexus.db`, `borg.db`, `catalog.db`, `metamcp.db`, `data/prompt_library.db`), URL queues (`incoming_resources.txt`, `reddit_hn_urls.txt`), or agent memory/session directories (`.pi/`, `.pi-lens/`, `.jules/`, `.tormentnexus/`).
3. **Pure-Go SQLite & VCS Flag**: Always build/test the Go backend with `CGO_ENABLED=0` and `-buildvcs=false`:
   ```bash
   cd backend && go build -buildvcs=false -o bobby-api.exe ./cmd/api
   cd backend && go test -buildvcs=false ./internal/...
   ```
4. **Dual-HUD Frontend**: `src/App.tsx` hosts both reconciled React interfaces (`CyberKineticHud.tsx` and `CleanUtilityHud.tsx`) plus links to the static Capability Atlas (`/atlas.html`). Build via `node build-render.js` (or `build.bat`).
5. **Version Governance**: Centralized in [VERSION.md](./VERSION.md) and mirrored in `package.json`, `index.html`, [CHANGELOG.md](./CHANGELOG.md), and [HANDOFF.md](./HANDOFF.md).

## Model-Specific Guidance (Reconciled from PR #1)
- **Claude / Architecture & Docs**: Prioritize schema backwards-compatibility across Borg (`research_level`, `short_description`, `innovation_score`) and legacy bookmark columns, and keep `HANDOFF.md` / `CHANGELOG.md` thorough.
- **Gemini / High-Velocity Pipelines & Vectors**: Leverage `gemini_pool.py` / `llm_pool.py` quota rotation when running `deep_research.py` or `_research_worker_v3.py`, and preserve `embeddings` / `nebula_map` integrity in `bookmarks.db`.
- **GPT / Synthesis & SQLite Hygiene**: Use read-only SQLite URI connections (`?mode=ro`) for inspections/exports (`scripts/generate_public_registry.py`) and enforce Jaccard/URL deduplication (`deduplicator.py`, `scripts/rebuild_prompts.py`).
