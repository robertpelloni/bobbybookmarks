# TODO.md: Immediate Actions

## UI & Visualization
- [ ] **Port Stats Tab**: Re-implement "Research Status Breakdown" bars in `App.jsx` using Recharts.
- [ ] **Port Domain Patterns**: Re-implement "Top Domains" list with filtering.
- [ ] **Port Tag Frequency**: Re-implement "Top Tags" and "Tag Co-occurrence" visualizations.
- [ ] **Add Version Display**: Show `v0.1.0` (from `VERSION.md`) in the UI header.

## Data & Backend
- [ ] **Consolidate `requirements.txt`**: Ensure all submodules' dependencies are represented.
- [ ] **Clean Redundant Files**: Archive or delete legacy `temp_processed.txt` and `bookmarks.txt.bak` after verifying the latest sync.
- [ ] **Refine `GeminiModelPool`**: Add a more robust cooldown period for "Resource Exhausted" errors.

## Documentation
- [ ] **Universal Instructions**: Create `GLOBAL_RULES.md` and update `AGENTS.md` / `GEMINI.md` to reference it.
- [ ] **Submodules Dashboard**: Create `SUBMODULES.md` listing versions, locations, and purposes.
- [ ] **Deployment Manual**: Fill out `DEPLOY.md` with step-by-step local and cloud instructions.

## Testing & Validation
- [ ] **Health Check Enhancement**: Add a `--fix` flag to `health_check.py` to auto-restart stopped workers.
- [ ] **API Unit Tests**: Add tests for the new database unification and deduplication logic.
