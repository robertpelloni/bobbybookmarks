# Borg Intelligence Atlas v7 — Master Index

> **14,261** tools · **5,946** standout 🏆⭐ · Domain-classified · Signal-scored · 2026-05-16

## What Changed in v7

| Problem | v5 | v6 | v7 |
|---------|----|----|----|
| MCP = Connectivity | 3,776 in one bucket | 3,776 in one bucket | **Domain-first**: MCP memory→Memory, MCP code→Harness, MCP infra→Infra |
| Agent Orchestration catch-all | 3,616 entries | 3,616 entries | **2,902** (764 misfit MCP servers re-homed) |
| Quality score | 99.9% = 1.0 | Computed (flat) | **Computed** with 7 real signals |
| Category chaos | 92 unique strings | Normalized | **Scoring-based** with LLM as signal (not sole source) |
| 'Other' subcategories | 36% | 0% (wrong subcats) | **0%** (keyword-scored subcategories) |
| No signal metric | None | ⚡ Signal 0-100 | **⚡ Signal 0-100** with innovation+quality+features+depth+trust |
| No primary flag | None | 📍 Primary | **📍 Primary** + match_score confidence |

## The 7 Borg Categories

| # | Layer | Tools | Standout | Avg Signal | Description |
|---|-------|-------|----------|------------|-------------|
| 1 | 🧠 [Agent Orchestration & Workflow](AGENT_ORCHESTRATION_WORKFLOW.md) | **2,902** | 1,174 | ⚡82 | Multi-agent swarms, workflows, planning, loops, verification |
| 2 | 👁 [Context Engineering & Isolation](CONTEXT_ENGINEERING_ISOLATION.md) | **1,028** | 390 | ⚡82 | Context compression, codebase indexing, RAG, isolation, ingestion |
| 3 | 🧬 [Memory & Persistence Architecture](MEMORY_PERSISTENCE_ARCHITECTURE.md) | **418** | 272 | ⚡83 | Graph memory, episodic, semantic, MCP memory, second brain, memory OS |
| 4 | 🤳 [Interface & Developer UX](INTERFACE_DEVELOPER_UX.md) | **937** | 327 | ⚡82 | Computer-use agents, terminal UIs, IDEs, web dashboards, voice, canvas |
| 5 | ⚡ [Connectivity / MCP / A2A](CONNECTIVITY_MCP_A2A.md) | **1,783** | 673 | ⚡83 | MCP infrastructure, A2A, gateways, tool discovery, registries |
| 6 | 🦴 [Infrastructure & Proxy Layers](INFRASTRUCTURE_PROXY_LAYERS.md) | **812** | 420 | ⚡84 | AI OSes, inference engines, sandboxes, security, deployment, LLM routers |
| 7 | 🗺 [Guides & Industry Trends](GUIDES_INDUSTRY_TRENDS.md) | **1,277** | 465 | ⚡80 | Awesome lists, tutorials, architecture patterns, benchmarks |

## Cross-Cutting Domains

| # | Domain | Tools | Standout | Avg Signal | Description |
|---|--------|-------|----------|------------|-------------|
| 8 | 🛠 [Coding Harness Tools](CODING_HARNESS_TOOLS.md) | **443** | 279 | ⚡84 | Agent harnesses, skills, governance, spec-driven dev, bridges |
| 9 | 🤖 [AI Agents & Frameworks](AI_AGENTS_FRAMEWORKS.md) | **272** | 177 | ⚡85 | Coding agents, GUI agents, research agents, AI OS, security agents |
| 10 | 🔍 [Search & Discovery](SEARCH_DISCOVERY.md) | **651** | 277 | ⚡83 | Semantic search, web APIs, code search, MCP registries |
| 11 | 💻 [Coding Tools & IDEs](CODING_TOOLS_IDES.md) | **940** | 362 | ⚡85 | AI editors, autocomplete, code review, refactoring, testing |
| 12 | 🔧 [Developer Workflow & Tools](DEVELOPER_WORKFLOW_TOOLS.md) | **2,044** | 807 | ⚡84 | Git, CI/CD, project management, documentation |
| 13 | 📐 [Vector Databases & Embeddings](VECTOR_DATABASES_EMBEDDINGS.md) | **229** | 112 | ⚡83 | Vector DBs, embedding models, ANN indexes, RAG frameworks |
| 14 | 🛡 [Security & Red Teaming](SECURITY_RED_TEAMING.md) | **525** | 211 | ⚡84 | AI guardrails, LLM red teaming, vulnerability scanning, pentesting |

---

## Signal Strength (⚡)

**Signal** (0-100) answers: *"Is this tool actually worth my time?"*

| Component | Weight | Measures |
|-----------|--------|----------|
| Innovation × 4 | 0-40 | Raw innovation from LLM analysis |
| Quality × 30 | 0-30 | Description depth, feature count, tags |
| Feature richness | 0-15 | Concrete features listed |
| Description depth | 0-10 | How detailed the description is |
| GitHub trust | 0-5 | Open-source repo bonus |

| Range | Meaning |
|-------|----------|
| ⚡85+ | 🏆 Must-know — world-class |
| ⚡70-84 | ⭐ Excellent — highly recommended |
| ⚡50-69 | ✓ Solid — worth exploring |
| ⚡30-49 | ○ Adequate — has useful features |
| ⚡0-29 | ⚠ Thin — limited data |

## Classification Method (v7)

1. **Domain-first scoring**: Each entry scored against all 14 layers using weighted keywords
2. **LLM category as signal**: The LLM-assigned category provides a +5 bonus (not sole determinant)
3. **Anti-signals**: Keywords that REDUCE a layer's score prevent misclassification
4. **MCP = protocol, not domain**: MCP servers classified by WHAT THEY DO, not that they speak MCP
5. **Primary flag**: Each entry has one primary layer plus cross-listings in other layers
6. **Match score**: Stored confidence level for each classification
7. **Subcategory scoring**: Subcategories also keyword-scored, no 'Other' buckets
