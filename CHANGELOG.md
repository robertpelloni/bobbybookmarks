# Changelog

All notable changes to this project will be documented in this file.

## [v1.2.0] - 2026-11-12
### Added
- **Dual-HUD React 19 / TypeScript Frontend Restored (`src/`)**: Restored and reconciled both overlapping frontend implementations dropped during an earlier branch merge — `src/CyberKineticHud.tsx` (Cyber Intelligence Kinetic HUD) and `src/CleanUtilityHud.tsx` (Clean Utility Interface) — behind a live HUD mode switcher in `src/App.tsx`, plus a complete `Terminal` view displaying real-time kernel logs, Capability Atlas v8 layer metrics, and Phase 2 Skill Engine stats.
- **PR #1 Public Registry Exporter & Multi-Model Agent Directives**: Ported `scripts/generate_public_registry.py` (exports `bookmarks.db` Borg-enriched entries to `exports/public_registry.html`) and reconciled `AGENTS.md` from `origin/pr/1` (`fcdc2862`).
- **New Go Unified API Endpoints & Tests**: Added `GET /api/skills` (Phase 2 `skill_executions`), `GET /api/atlas/summary` (`atlas.db` layer telemetry), `GET /api/analytics/nebula` (3,942 semantic 2D vectors from `nebula_map`), `POST /api/bookmarks` (URL queue ingestion), `/atlas` + `/atlas.html` static routes, and automated tests in `backend/internal/api/routes_test.go`.
- **Root Build & Launch Scripts**: Added `build.bat` for full-stack Vite + pure-Go builds/tests and overhauled `start.bat` and `Dockerfile` (`golang:1.25-alpine`, `CGO_ENABLED=0`).

### Fixed
- **Go API Dual-Schema Compatibility**: Updated `backend/internal/database/db.go`, `models.go`, and `routes.go` to auto-detect and query the live Borg SQLite schema (`research_level`, `short_description`, `category`, `innovation_score`, `created_at`) while retaining backwards compatibility with legacy bookmark schemas and resolving database/static paths from either repo root or `backend/`.
- **Restored `catalog.db` & Stashed `.jules/` Memory/Sessions**: Restored the 1.08 MB `catalog.db` (`3,984` MCP entries) from commit `4f65f1d3` (previously overwritten by a 0-byte file in `1ed90f9f`) and recovered `.jules/memory/architecture.md` and `.jules/sessions/5781053154188114867.md` from `stash@{0}`.
- **Repository Tracking Hygiene (`.gitignore`)**: Un-ignored all SQLite databases, URL queues (`reddit_hn_urls.txt`, `incoming_resources_backup.txt`), and agent memory/session stores (`.pi/`, `.pi-lens/`, `.jules/`, `.tormentnexus-session.json`) while keeping `.env` secrets, raw `*.log` streams, `/node_modules/`, and compiled `.exe` binaries ignored on disk without purging binaries.

## [v1.1.0] - 2026-11-08
### Added
- Added heavyweight app priority management (`scripts/lower-priority.ps1` and `scripts/lower-priority-run.js`) and bumped `VERSION.md` to `v1.1.0`.
- Rewrote `README.md` (`7bcff343`) and merged Go module dependency updates (`fe7b47fd`, `dd7908a6`).

## [1.0.3] - Phase 2 Skill Engine Rebuild
- Created `SKILL.md` base template for extraction and task resolution strategies.
- Initialized execution win-rate tracking schemas in `borg.db`.
- Added Go database handler for skill engine initialization.

## [v1.0.1] - 2026-06-18
### Added
- Created `HANDOFF.md` to document initial recovery investigation and verified Go API build/tests.
- Created `.github/workflows/deploy-landing.yml` for Cloudflare Pages deployment (`tormentnexus.site` and `hypernexus.site`).
- Created `scripts/rebuild_prompts.py` to populate `data/prompt_library.db`.
- Re-initialized governance documents `VISION.md`, `ROADMAP.md`, `TODO.md`, `CHANGELOG.md`, and `VERSION.md`.
