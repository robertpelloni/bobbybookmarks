# TODO.md: Immediate Actions

## UI & Visualization
- [x] **Port Stats Tab**: Re-implemented "Research Status Breakdown" with Recharts in `App.jsx`.
- [x] **Port Domain Patterns**: Integrated "Harvest Velocity" timeline into the "Insights" view.
- [x] **Port Tag Frequency**: Re-implemented "Trending Tags" cloud with visual frequency bars.
- [x] **Intelligence Clusters**: Created a new "Clusters" view to show automated groupings of bookmarks.
- [x] **Semantic Search UI**: Integrated "Semantic Mode" toggle and vector search result handling.
- [x] **Peer Review Viewer**: Created a new tab to visualize the Advocate vs Critic intellectual duels.
- [x] **A2A Consensus Scoring**: Subjected the first 16 high-innovation projects to rigorous agentic peer review.
- [x] **Network Health Monitor**: Live "Network" tab showing real-time agent heartbeats and tasks.
- [x] **Live Research Feed**: Added a "terminal-style" log in the UI to watch the worker's real-time thoughts.
- [x] **Automated Reports**: Dashboard now features a "Reports" tab rendering the auto-generated Daily Intelligence Briefing.
- [x] **Add Version Display**: Dashboard now displays `v0.1.0` in the header.
- [x] **Nebula Interactivity**: Added real-time concept search and domain filters to the 2D Knowledge Nebula.


## Data & Backend
- [x] **Consolidate `requirements.txt`**: Added `psutil`, `pandas`, and `tabulate` for system analysis.
- [x] **Clean Redundant Files**: Removed `temp_processed.txt` and `bookmarks.txt.bak`.
- [x] **Refine `GeminiModelPool`**: Implemented an aggressive cooldown and per-model rotation for 429 errors.
- [x] **Vector Indexing**: Reached 100% coverage of Borg entries.
- [x] **100% Vector Coverage**: Finalized remaining batches to index all researched intelligence.
- [x] **Automated Reports**: Script `generate_intelligence_report.py` is generating automated daily briefings.


## Documentation
- [x] **Universal Instructions**: Created `GLOBAL_RULES.md`.
- [x] **Submodules Dashboard**: Created `SUBMODULES.md` with registry and skill repo details.
- [x] **Deployment Manual**: Created `DEPLOY.md` with local and cloud stack guides.
- [x] **Unified Export Engine**: Dashboard data can now be exported to 1,244 high-fidelity Markdown dossiers.

## Testing & Validation
- [x] **Health Check Enhancement**: Implemented `--fix` flag to auto-restart stopped background services.
- [ ] **API Unit Tests**: Add tests for the new database unification and deduplication logic.
