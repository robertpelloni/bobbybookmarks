# bobbybookmarks — Borg Intelligence Atlas & Unified HUD (`v1.2.0`)

A unified AI/developer-tools intelligence harvester, capability atlas, and dual-HUD web application backing the Borg / TormentNexus research ecosystem. The repository tracks the Python ingestion/enrichment pipeline, the pure-Go Fiber API backend, the React 19 / TypeScript Dual-HUD frontend, generated category layer documents, agent memory/session stores, and the live SQLite databases themselves.

## Architecture & Core Components

- **Ingestion & Enrichment Pipeline (Python)** — URLs queued in `incoming_resources.txt`, `reddit_hn_urls.txt`, and `*_to_process.txt` are scraped and classified via `_ingest2.py`, `_ingest3.py`, `deep_research.py`, and `_research_worker_v3.py` (with quota rotation via `llm_pool.py` / `gemini_pool.py` and deduplication via `deduplicator.py`).
- **Unified API & Static Server (`backend/`, Go 1.25 + Fiber v2)** — Pure-Go SQLite (`modernc.org/sqlite`, `CGO_ENABLED=0`) backend serving `/api/*` analytics, search, D3 force-graph, semantic `nebula_map` coordinates, Phase 2 `skill_executions` (`/api/skills`), Capability Atlas telemetry (`/api/atlas/summary`), `/atlas.html`, and the compiled React SPA (`dist/`) on port `5000`.
- **Dual-HUD Frontend (`src/`, React 19 + Vite + Tailwind v4)** — Reconciled web interface preserving both the **Cyber Intelligence Kinetic HUD** (`src/CyberKineticHud.tsx`) and the **Clean Utility Interface** (`src/CleanUtilityHud.tsx`) with live runtime mode switching.
- **Capability Atlas & Public Registry Exports** — `_gen_atlas_v8.py` generates `atlas.html`, `atlas.json`, `BORG_ATLAS_INDEX.md`, and 14 category Markdown reports; `scripts/generate_public_registry.py` exports Borg-enriched bookmarks to `exports/public_registry.html`.

## Tracked SQLite Stores

| Database | Contents |
| :--- | :--- |
| `bookmarks.db` (~60.8 MB) | `10,820` bookmarks (`10,811` Borg-enriched), `3,942` embeddings & `nebula_map` points, `17` clusters, `22` debates, L2/L3 tiered memory |
| `tormentnexus.db` (~57.8 MB) | `687` imported sessions, `57,144` session memories, `17,341` `links_backlog` URLs, `65` MCP servers |
| `atlas.db` (~22.3 MB) | `17,533` entries across `14` capability layers (`24,248` memberships) |
| `borg.db` (~3.4 MB) | `65` MCP servers, `548` sessions, `1,620` memories, Phase 2 `skill_executions` |
| `catalog.db` (~1.08 MB) | `3,984` parsed MCP catalog entries |
| `metamcp.db` (~356 KB) | MetaMCP server configuration schema |
| `data/prompt_library.db` (~6.4 MB) | Deduplicated prompt library rebuilt via `scripts/rebuild_prompts.py` |

## Build & Run

```bat
:: Full frontend + Go backend build & test suite (keeps all built binaries)
build.bat

:: Launch unified server on http://localhost:5000 (Atlas at /atlas.html)
start.bat

:: Launch hot-reload dev mode (Vite :3000 + Go API :5000)
start.bat --dev
```

Manual Go verification (per `RUNBOOK.md`):
```bash
cd backend && CGO_ENABLED=0 go build -buildvcs=false -o bobby-api.exe ./cmd/api
cd backend && CGO_ENABLED=0 go test -buildvcs=false ./internal/...
```

## Governance & Memory
See [VERSION.md](./VERSION.md) (`v1.2.0`), [RUNBOOK.md](./RUNBOOK.md), [AGENTS.md](./AGENTS.md), [ROADMAP.md](./ROADMAP.md), [TODO.md](./TODO.md), [SUBMODULE_INVENTORY.md](./SUBMODULE_INVENTORY.md), [CHANGELOG.md](./CHANGELOG.md), and [HANDOFF.md](./HANDOFF.md).
