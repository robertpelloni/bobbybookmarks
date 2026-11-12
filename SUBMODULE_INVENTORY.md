# Repository & Submodule Structural Map (`v1.2.0`)

## Root Repository
| Repository | Branch | Version | Remote (`origin` / `upstream`) | Layout Role |
| :--- | :--- | :--- | :--- | :--- |
| `bobbybookmarks` | `main` | `v1.2.0` | `https://github.com/robertpelloni/bobbybookmarks` | Standalone root repository (also tracked as submodule `#11` inside parent `robertpelloni/workspace`) |

## Active Branches Reconciled
| Branch | Direction | Status |
| :--- | :--- | :--- |
| `main` | Primary target | Reconciled at `v1.2.0` (includes forward-merged `jules-5781053154188114867-382e86c1`, Dependabot PRs #4/#5/#7, cherry-picked PR #1 `scripts/generate_public_registry.py` + `AGENTS.md`, restored dual-HUD `src/`, and restored `catalog.db` + `.jules/`) |
| `jules-5781053154188114867-382e86c1` | Forward & Reverse merged | Synced with `main` (`v1.2.0`) so zero branch drift remains |

## Nested Submodules Inside `bobbybookmarks`
* **Active Git Submodules (`.gitmodules`)**: **None (`0`)**.
* **Historical Consolidation Note**: Fourteen external reference submodules formerly under `submodules/*` (`4regab-TaskSync`, `a2aproject-A2A`, `anthropics-skills`, `awesome-ai-apps`, `awesome-mcp-servers-appcypher`, `awesome-mcp-servers-punkpeye`, `awesome-mcp-servers-wong2`, `bkircher-skills`, `dotfiles`, `openai-skills`, `robertpelloni-metamcp`, `stared-gemini-claude-skills`, `toolsdk-mcp-registry`, `ykdojo-claude-code-tips`) were intentionally absorbed into the tracked SQLite databases (`bookmarks.db`, `atlas.db`, `catalog.db`, `metamcp.db`) and `.tormentnexus/skills/` + `skills/` in commits `2fcda409` and `ebb4b6d5`.

## Directory & Database Layout
| Path | Description |
| :--- | :--- |
| `backend/` | Pure-Go (`modernc.org/sqlite`, `CGO_ENABLED=0`) Fiber v2 unified API & static SPA server (`cmd/api`, `internal/api`, `internal/database`, `internal/models`, `internal/worker`) |
| `src/` | Reconciled React 19 + TypeScript + Tailwind v4 Dual-HUD frontend (`App.tsx`, `CyberKineticHud.tsx`, `CleanUtilityHud.tsx`) |
| `dist/` | Production Vite bundle served at `/` by `backend/bobby-api.exe` |
| `scripts/` | Operational utilities (`rebuild_prompts.py`, `build_skill_tracker.py`, `generate_public_registry.py`, `lower-priority.ps1`, `lower-priority-run.js`) |
| `bookmarks.db` | Primary Borg intelligence store (`10,820` bookmarks, `3,942` embeddings & `nebula_map` coordinates, tiered memory tables) |
| `atlas.db` / `atlas.html` | Capability Atlas v8 (`17,533` entries across `14` layers, `24,248` memberships) |
| `tormentnexus.db` | Session & link backlog store (`687` sessions, `57,144` memories, `17,341` `links_backlog` URLs, `65` MCP servers) |
| `catalog.db` | Restored MCP server catalog (`3,984` `catalog_entries`) |
| `borg.db` / `metamcp.db` | Phase 2 `skill_executions`, MCP registry (`65` servers), and MetaMCP configuration |
| `data/` | `prompt_library.db` + LanceDB vector store (`data/lancedb/memories.lance`) |
| `.tormentnexus/`, `.pi/`, `.pi-lens/`, `.jules/` | Tracked agent memory blocks, handoffs, skills, and session transcripts |
