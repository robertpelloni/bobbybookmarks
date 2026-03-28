# ROADMAP.md: Future Intelligence Capabilities

## Phase 1: Visualization & UX (Current Focus)
- [ ] **Legacy View Porting**: Bring back the statistical bar charts and timelines from the vanilla JS version into the React/Vite UI using **Recharts**.
- [x] **The Pulse**: Implemented a real-time "Harvest Velocity" timeline showing cumulative discovery progress.
- [x] **Borg Feature Matrix 2.0**: Enhanced the feature matrix with drill-down capabilities to see source bookmarks for each feature.

## Phase 2: Relationship Mapping
- [x] **The Borg Consciousness Map**: Integrated **D3.js** force-directed node graph linking projects, categories, and tags.
- [x] **Project Clusters**: Automatically grouping related tools using TF-IDF and K-Means clustering, visualized in a dedicated Clusters view.

## Phase 3: Semantic Intelligence
- [x] **Vector Search**: Integrated Gemini text-embeddings and cosine similarity to enable real-time semantic search across the Borg corpus.
- [ ] **Knowledge Nebula**: A 2D semantic landscape visualization where bookmarks are plotted based on conceptual similarity.

## Phase 4: Agentic Peer Review
- [x] **The A2A Debate**: Implemented a background protocol where an Advocate and a Critic persona debate project innovation to establish a consensus score.
- [ ] **Automated Briefs**: Generate daily "Intelligence Reports" summarizing the latest discoveries in Markdown.

## Phase 5: Ecosystem Integration
- [x] **Unified Export**: Implemented `unified_export.py` to generate high-fidelity Markdown technical dossiers for all researched intelligence (Obsidian-ready).
- [ ] **Public Registry**: A read-only public version of the Borg database for community sharing.
