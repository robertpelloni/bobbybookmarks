# Borg Intelligence — Definitive Feature Roadmap

Current Version: **v1.2.0**

## Phase 1: MEMORY & UNIFIED DATA LAYER (Completed / Active)
- [x] Unified SQLite Intelligence Stores: `bookmarks.db` (10,820 tools), `atlas.db` (17,533 entries across 14 layers), `tormentnexus.db` (687 sessions, 57,144 memories, 17,341 backlog links), `catalog.db` (3,984 MCP entries), `borg.db`, `metamcp.db`, and `data/prompt_library.db`.
- [x] Tiered Memory implementation (`memory_l2_warm`, `memory_l3_cold`, `memory_access_log` in `bookmarks.db`, plus LanceDB semantic vectors in `data/lancedb/`).
- [x] Cross-session persistence across `.tormentnexus/`, `.pi/`, `.pi-lens/`, and `.jules/` tracked directly in Git.

## Phase 2: SKILL ENGINE & UNIFIED DUAL-HUD INTERFACE (Completed in v1.2.0)
- [x] `SKILL.md` template systems (`.tormentnexus/skills/` and `skills/*.json`) for extraction and task resolution strategies.
- [x] Execution win-rate tracking schema (`skill_executions` in `borg.db`) wired to `GET /api/skills` in the Go Fiber backend.
- [x] Dual-HUD React 19 / TypeScript Frontend (`CyberKineticHud` + `CleanUtilityHud`) reconciled and served alongside static Capability Atlas (`/atlas.html`) and Public Registry exporter (`scripts/generate_public_registry.py`).
- [ ] Automated skill retirement & DSPy-style prompt evolution loop triggered by live worker telemetry.

## Phase 3: CONTEXT MANAGER (Budget Control)
- [ ] Progressive schema disclosure (lazy-loading MCP tools from `catalog.db` and `borg_tool_registry` on demand).
- [ ] Context re-injection hooks after compaction events to preserve high-signal architectural invariants.
- [ ] Dynamic token budget allocation assigned per active tool.

## Phase 4: VERIFICATION (Safety & Autonomy)
- [x] Automated Go backend unit/integration test suite (`backend/internal/api/routes_test.go`) and SQLite `PRAGMA integrity_check` verification.
- [ ] Closed-loop self-healing (`borg_selfhealing.py` -> Build -> Fail -> LLM Error Resolution -> Retry).
- [ ] Multi-model cross-validation pipelines (`debates` table advocate/critic consensus scoring).

## Phase 5: THE RECURSIVE LOOP (Continuous Improvement)
- [ ] Self-modification informed by historical graph memory and `nebula_map` semantic clusters.
- [ ] Triggers linking verification failure/success directly to skill evolution in `skill_executions`.
