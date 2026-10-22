# bobbybookmarks — Borg Intelligence Atlas / Harvester

A personal research pipeline that ingests bookmarks and URLs about AI and developer
tools, enriches them with LLM classification and scoring, and publishes the result
as a categorized "atlas" of tools. It is the working tree behind the Borg /
TormentNexus research effort, not a packaged product: the repository contains the
pipeline scripts, the generated atlas documents, and the live SQLite databases
themselves.

## What it does

- **Ingest** — URLs queued in `incoming_resources.txt` (and the various
  `*_to_process` / backlog files) are fetched and parsed into SQLite
  (`_ingest2.py`, `_ingest3.py`, `deep_research.py`).
- **Enrich** — research workers (`_research_worker*.py`) classify each entry,
  generate descriptions, and assign signal scores using a local LLM (LM Studio,
  via `llm_pool.py` / `gemini_pool.py`).
- **Deduplicate / hygiene** — `deduplicator.py` and the scripts under `scripts/`
  keep the stores clean (e.g. Jaccard-similarity dedup at a 90% threshold).
- **Export** — `_gen_atlas_v8.py` regenerates the atlas: `atlas.html`,
  `atlas.json`, `BORG_ATLAS_INDEX.md`, and one Markdown file per category layer
  (agent orchestration, MCP/connectivity, memory architecture, coding tools,
  security/red teaming, and nine more). The atlas index in the repo reports
  7,607 entries across 14 layers.

## Contents

- Python pipeline and worker scripts at the root (`deep_research.py`,
  `borg_deep_v4.py`, `borg_memory.py`, `borg_skills.py`, `borg_selfhealing.py`,
  `phase3_mcp_catalog.py`, `phase4_links_backlog*.py`, …)
- `backend/` — a Go API (`backend/cmd/api`, `backend/internal/`) with a compiled
  `bobby-api` binary checked in
- SQLite databases checked into git: `bookmarks.db` (~64 MB), `atlas.db`
  (~23 MB), `tormentnexus.db` (~61 MB), `borg.db`, `metamcp.db`
- Generated layer documents (`AGENT_ORCHESTRATION_WORKFLOW.md`,
  `AI_AGENTS_FRAMEWORKS.md`, `CONNECTIVITY_MCP_A2A.md`, etc. — several MB each)
- Governance/ops docs: `VISION.md`, `ROADMAP.md`, `RUNBOOK.md`, `HANDOFF.md`,
  `CHANGELOG.md`, `TODO.md`

## Running it

There is no installer or packaged entry point; the pipeline is run as loose
scripts from the repo root, per `RUNBOOK.md`:

```bash
python3 deep_research.py &            # ingestion/enrichment worker (background)
cd backend && go build -buildvcs=false ./cmd/api
cd backend && go test -buildvcs=false ./internal/...
sqlite3 atlas.db "PRAGMA integrity_check;"
```

## Status

Personal research working tree, snapshotted by automated checkpoint commits —
the most recent commit (2026-07-21) is literally "auto: commit dirty working
directory before reconciliation". Expect large binary databases, generated
documents, session markers from several agent harnesses (`.tormentnexus/`,
`.chunkhound/`, `.pi/`), and in-progress queues rather than a clean release.
`HANDOFF.md` documents a past data-loss/recovery incident for some of the
databases; treat the DBs here as the surviving copies, not backups.
