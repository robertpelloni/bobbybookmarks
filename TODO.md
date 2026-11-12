# Immediate Short-Term Tasks & Bug Fixes (v1.2.0)

## Data Recovery & Retention
- [x] Restore `tormentnexus.db` (687 sessions, 57,144 memories, 17,341 `links_backlog` URLs) and `catalog.db` (3,984 MCP entries).
- [x] Recover stashed `.jules/` architecture memory and session transcripts (`stash@{0}`) and ensure `.pi/`, `.pi-lens/`, `.jules/`, `.tormentnexus/`, and all primary `.db` / queue files are tracked in Git.
- [x] Implement Phase 3a (`scripts/rebuild_prompts.py` -> `data/prompt_library.db`) and PR #1 Public Registry exporter (`scripts/generate_public_registry.py` -> `exports/public_registry.html`).
- [x] Implement Phase 9 (`.github/workflows/deploy-landing.yml` CI/CD for Cloudflare Pages).

## Codebase Reconciliation & Maintenance
- [x] Restore missing React 19 / TypeScript frontend (`src/`, `package.json`, Vite/Tailwind v4 configs) and retain both `CyberKineticHud` and `CleanUtilityHud` implementations with live mode switching.
- [x] Upgrade `backend/internal/api` and `backend/internal/database` for full dual-schema compatibility (Borg + Legacy), `/api/skills`, `/api/atlas/summary`, and `/api/analytics/nebula`.
- [x] Fix `start.bat`, `Dockerfile`, and add `build.bat` for unified Go + Vite builds without purging existing binaries.

## Next Up
- [ ] Drain newly queued links in `incoming_resources.txt`, `_new_to_process.txt`, and `reprocess_queue.txt` via `deep_research.py` / `_research_worker_v3.py` and regenerate `atlas.html` (`_gen_atlas_v8.py`).
- [ ] Record live `borg_skills.py` execution telemetry directly into `borg.db:skill_executions` so win-rates populate in the HUD `Terminal` tab.
- [ ] Port active Python LLM scraping/enrichment logic into `backend/internal/worker/main.go` as an optional native Go worker mode.
