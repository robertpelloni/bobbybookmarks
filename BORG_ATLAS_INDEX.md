# Borg Intelligence Atlas v7.1 — Master Index

> **13,376** tools · **3,555** standout 🏆⭐ · Domain-classified · Signal-scored · 2026-05-17

## What Changed in v7.1

| Area | v7 | v7.1 |
|------|----|----|
| Entry count | 6,805 | **6,301** (removed 504 noise/spam/duplicates) |
| Duplicate repos | 20 groups (92 entries) | **0** (merged, best metadata kept) |
| Google search URLs | 123 | **0** (removed noise) |
| Low-signal Reddit | 448 entries (avg ⚡67) | **160** (kept signal ≥ 70) |
| Tag normalization | Mixed `space`/`hyphen` | **All kebab-case** |
| Quality computation | Bimodal Q1.0/Q0.6 | **Graduated** 0-1 with 6 signal components |
| Signal spread | 47% at ⚡85+ | **44% at ⚡85+**, 52% at ⚡70-84 |
| Standout threshold | 40.6% | **24.8%** (stricter: innov≥9 AND quality≥0.8) |

## The 7 Borg Categories

| # | Layer | Tools | Standout | Avg Signal | Description |
|---|-------|-------|----------|------------|-------------|
| 1 | 🧠 [Agent Orchestration & Workflow](AGENT_ORCHESTRATION_WORKFLOW.md) | **2,678** | 683 | ⚡83 | Multi-agent swarms, workflows, planning, loops, verification |
| 2 | 👁 [Context Engineering & Isolation](CONTEXT_ENGINEERING_ISOLATION.md) | **995** | 260 | ⚡84 | Context compression, codebase indexing, RAG, isolation, ingestion |
| 3 | 🧬 [Memory & Persistence Architecture](MEMORY_PERSISTENCE_ARCHITECTURE.md) | **396** | 131 | ⚡84 | Graph memory, episodic, semantic, MCP memory, second brain, memory OS |
| 4 | 🤳 [Interface & Developer UX](INTERFACE_DEVELOPER_UX.md) | **860** | 204 | ⚡83 | Computer-use agents, terminal UIs, IDEs, web dashboards, voice, canvas |
| 5 | ⚡ [Connectivity / MCP / A2A](CONNECTIVITY_MCP_A2A.md) | **1,740** | 477 | ⚡85 | MCP infrastructure, A2A, gateways, tool discovery, registries |
| 6 | 🦴 [Infrastructure & Proxy Layers](INFRASTRUCTURE_PROXY_LAYERS.md) | **789** | 223 | ⚡84 | AI OSes, inference engines, sandboxes, security, deployment, LLM routers |
| 7 | 🗺 [Guides & Industry Trends](GUIDES_INDUSTRY_TRENDS.md) | **1,090** | 226 | ⚡82 | Awesome lists, tutorials, architecture patterns, benchmarks |

## Cross-Cutting Domains

| # | Domain | Tools | Standout | Avg Signal | Description |
|---|--------|-------|----------|------------|-------------|
| 8 | 🛠 [Coding Harness Tools](CODING_HARNESS_TOOLS.md) | **431** | 143 | ⚡84 | Agent harnesses, skills, governance, spec-driven dev, bridges |
| 9 | 🤖 [AI Agents & Frameworks](AI_AGENTS_FRAMEWORKS.md) | **267** | 82 | ⚡83 | Coding agents, GUI agents, research agents, AI OS, security agents |
| 10 | 🔍 [Search & Discovery](SEARCH_DISCOVERY.md) | **540** | 152 | ⚡85 | Semantic search, web APIs, code search, MCP registries |
| 11 | 💻 [Coding Tools & IDEs](CODING_TOOLS_IDES.md) | **892** | 241 | ⚡86 | AI editors, autocomplete, code review, refactoring, testing |
| 12 | 🔧 [Developer Workflow & Tools](DEVELOPER_WORKFLOW_TOOLS.md) | **1,976** | 554 | ⚡86 | Git, CI/CD, project management, documentation |
| 13 | 📐 [Vector Databases & Embeddings](VECTOR_DATABASES_EMBEDDINGS.md) | **226** | 50 | ⚡81 | Vector DBs, embedding models, ANN indexes, RAG frameworks |
| 14 | 🛡 [Security & Red Teaming](SECURITY_RED_TEAMING.md) | **496** | 129 | ⚡85 | AI guardrails, LLM red teaming, vulnerability scanning, pentesting |

---

## Signal Strength (⚡)

**Signal** (0-100) answers: *"Is this tool actually worth my time?"*

| Component | Weight | Measures |
|-----------|--------|----------|
| Innovation × 4 | 0-40 | Raw innovation from LLM analysis |
| Quality × 30 | 0-30 | Description depth, feature count, tags, verdict, owner |
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

## Quality Score (Q)

**Quality** (0-1) measures *data richness* — how much we know about this tool.

| Component | Max | Measures |
|-----------|-----|----------|
| Description depth | 30 | 500+ch=30, 300+=25, 150+=20, 50+=12, 10+=6 |
| Feature richness | 25 | 5+=25, 4+=22, 3+=18, 2+=12, 1+=6 |
| Tag richness | 15 | 6+=15, 4+=12, 2+=8, 1+=4 |
| Has page title | 10 | Meaningful title=10, any=5 |
| Has GitHub owner | 10 | Known repo owner |
| Verdict quality | 10 | 50+ch=10, 20+=7, 5+=4 |

## Classification Method

1. **Domain-first scoring**: Each entry scored against all 14 layers using weighted keywords
2. **LLM category as signal**: The LLM-assigned category provides a +5 bonus (not sole determinant)
3. **Anti-signals**: Keywords that REDUCE a layer's score prevent misclassification
4. **MCP = protocol, not domain**: MCP servers classified by WHAT THEY DO, not that they speak MCP
5. **Primary flag**: Each entry has one primary layer plus cross-listings in other layers
6. **Match score**: Stored confidence level for each classification
7. **Subcategory scoring**: Subcategories also keyword-scored, no 'Other' buckets
