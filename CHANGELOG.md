# Changelog

All notable changes to this project will be documented in this file.

## [v1.0.1] - 2026-06-18
### Added
- Created `HANDOFF.md` to document the catastrophic data loss of the backup database `db_v1_28413952.db`, `catalog.db`, and missing codebase sub-trees (like `go/internal/tools` and `packages/core`).
- Created `.github/workflows/deploy-landing.yml` to support automated deployments of Cloudflare Pages for `tormentnexus.site` and `hypernexus.site` when they exist.
- Created `scripts/rebuild_prompts.py` to re-fetch prompts from the `awesome-chatgpt-prompts` repository into `data/prompt_library.db`, fulfilling Phase 3a data recovery.
- Re-initialized structural governance documents `VISION.md`, `ROADMAP.md`, `TODO.md`, and `CHANGELOG.md` to adhere to the core instruction standards.
- Re-initialized global `VERSION.md` file at `v1.0.1`.
