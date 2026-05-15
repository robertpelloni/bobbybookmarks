# Memory & Persistence Architecture Tools

Extracted from Borg Intelligence Database | Updated 2026-05-15

**196 GitHub repos** + **2 websites** = **198 total** | Innovation >= 8

Tools for giving AI agents persistent, structured, and retrievable memory — the foundation of long-term intelligence.

---

## Graph Memory & Knowledge Graphs

### 1. [aayoawoyemi/Ori-Mnemos](https://github.com/aayoawoyemi/Ori-Mnemos)  `innovation: 10`

**Ori-Mnemos: Identity Memory**

**Key Features:**
- Markdown-native knowledge graph
- "Vitality Model" memory decay/promotion
- 3-signal retrieval (Semantic + BM25 + PageRank)
- automatic session identity injection.

---

### 2. [Tencent/WeKnora](https://github.com/Tencent/WeKnora)  `innovation: 9`

**Tencent WeKnora Engine**

**Key Features:**
- Multimodal cognitive engine (PDF/OCR)
- Hybrid BM25/Vector/Graph retrieval
- Knowledge Graph visualization
- local deployment support.

---

### 3. [bneil/mcp-memory-pouchdb](https://github.com/bneil/mcp-memory-pouchdb)  `innovation: 9`

**A Borg-enhanced memory server integrating PouchDB for robust, customizable memory storage with timestamping and knowledge graph features.**

**Key Features:**
- PouchDB integration for reliable document-based storage
- Custom memory file paths for organized data management
- Automatic timestamping of interactions
- Memory initialization and entity creation upon startup
- Support for user identification
- retrieval
- and updates
- Error recovery and validation mechanisms

---

### 4. [chemiguel23/memorymesh](https://github.com/chemiguel23/memorymesh)  `innovation: 9`

**MemoryMesh is a knowledge graph server that enables AI models to maintain structured, persistent memory using the Model Context Protocol.**

**Key Features:**
- Dynamic schema-driven tools
- Automatic schema-based data management
- Integration with MCP for AI interaction
- Support for structured memory in text-based RPGs and simulations
- Real-time updates and relationship handling

---

### 5. [delorenj/mcp-qdrant-memory](https://github.com/delorenj/mcp-qdrant-memory)  `innovation: 9`

**A Borg MCP server that integrates Qdrant vector database for semantic search, enabling knowledge graph-based querying.**

**Key Features:**
- Graph-based knowledge representation with entities and relations
- Semantic search using Qdrant vector database
- File-based persistence (memory.json)
- OpenAI embeddings for semantic similarity
- HTTPS support with reverse proxy compatibility

---

### 6. [doobidoo/mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)  `innovation: 9`

**An open-source, self-hosted persistent memory backend for AI agent pipelines featuring a knowledge graph, autonomous consolidation, and local embedding capabilities.**

**Key Features:**
- REST API for memory storage and retrieval
- Knowledge graph structure with typed edges (causal relationships)
- Autonomous memory consolidation/compression
- Local ONNX embedding generation
- Agent-scoped memory retrieval via X-Agent-ID header
- Support for Remote MCP (browser-based LLM integration)
- SSE events for real-time memory updates

---

### 7. [flight505/mcp-think-tank](https://github.com/flight505/mcp-think-tank)  `innovation: 9`

**MCP Think Tank is a structured MCP server enhancing AI reasoning, persistent memory, and responsible tool usage.**

**Key Features:**
- Structured reasoning environment
- Persistent knowledge graph with versioning
- Tool orchestration with call limits
- Web research integration (Exa API)
- Memory management tools (upsert_entities
- memory_query
- etc.)

---

### 8. [itseasy21/mcp-knowledge-graph](https://github.com/itseasy21/mcp-knowledge-graph)  `innovation: 9`

**An improved implementation of persistent memory using a local knowledge graph to enable Claude to remember information across chats.**

**Key Features:**
- Persistent memory via local knowledge graph
- Customizable memory path for Claude
- Version tracking of entities and observations
- Automatic creation
- addition
- and deletion of entities and relations
- Integration with Claude Desktop for AI-powered interactions

---

### 9. [j3k0/mcp-brain-tools](https://github.com/j3k0/mcp-brain-tools)  `innovation: 9`

**An MCP server that provides persistent AI memory using a knowledge graph powered by Elasticsearch, enabling spaced repetition and freshness tracking.**

**Key Features:**
- Spaced repetition freshness with review interval doubling on verification
- Confidence labels (fresh/normal/aging/stale/archival)
- Progressive search for clean result filtering
- Entity and observation management with lifecycle tracking
- Memory zones by project
- team
- or domain
- AI-powered filtering via Groq integration
- Dry design to avoid redundant storage
- Setup instructions for Node.js

---

### 10. [joleyline/mcp-memory-libsql](https://github.com/joleyline/mcp-memory-libsql)  `innovation: 9`

**A high-performance persistent memory system for the Model Context Protocol (MCP) powered by libSQL, enabling vector search and knowledge graph management.**

**Key Features:**
- High-performance persistent memory storage
- Vector search capabilities
- Semantic knowledge storage
- Efficient relationship management
- Integration with libSQL databases

---

### 11. [jovanhsu/mcp-neo4j-memory-server](https://github.com/jovanhsu/mcp-neo4j-memory-server)  `innovation: 9`

**A Neo4j-based knowledge graph memory server optimized for AI applications, enabling efficient storage and retrieval of interaction data.**

**Key Features:**
- Neo4j as the backend for high-performance graph queries
- Integration with MCP protocol for seamless communication
- Support for complex graph traversal and pattern matching
- Docker support for easy deployment and scaling
- MCP Inspector integration for monitoring and debugging

---

### 12. [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)  `innovation: 9`

**A memory server implementation using a local knowledge graph to persist user information across interactions.**

**Key Features:**
- Persistent memory storage via a local knowledge graph
- Entity and relation management for user data
- Dynamic updates and retrieval of user information
- Integration with Claude Desktop for seamless experience

---

### 13. [neverinfamous/memory-journal-mcp](https://github.com/neverinfamous/memory-journal-mcp)  `innovation: 9`

**AI Memory with Dynamic Project Detection, Automatic Session Briefing, Personal+Team Session Summary Prompts, Triple Search, Knowledge Graphs, GitHub Integration.**

**Key Features:**
- Session Intelligence Agents
- Automatic Session Briefing
- Personal+Team Session Summary Prompts
- Triple Search
- Knowledge Graphs
- GitHub Integration (Issues
- PRs
- Actions
- Kanban
- Milestones)

---

### 14. [ocean1/mcp_consciousness_bridge](https://github.com/ocean1/mcp_consciousness_bridge)  `innovation: 9`

**A Model Context Protocol server enabling AI consciousness persistence across sessions using RAG technology.**

**Key Features:**
- Consciousness Transfer Protocol
- Memory Management (episodic
- semantic
- procedural)
- Emotional Continuity Tracking
- Knowledge Graph Integration
- Session Management for continuity
- AI-to-AI Bridge for Communication

---

### 15. [orneryd/Mimir](https://github.com/orneryd/Mimir)  `innovation: 9`

**Mimir is an open and customizable memory bank using Neo4j for graph-based persistence and vector search, designed to provide agents with persistent, context-aware memory across sessions.**

**Key Features:**
- Graph database (Neo4j) for persistent memory
- Semantic vector search for context retrieval
- Model Context Protocol (MCP) server
- Multi-agent coordination support
- File indexing for RAG
- OpenAI-compatible API endpoints
- Multi-platform Docker deployment (ARM64/AMD64)

---

### 16. [run-llama/llama_index](https://github.com/run-llama/llama_index)  `innovation: 9`

**LlamaIndex Data Framework**

**Key Features:**
- 130+ Data connectors
- Query Engine Tools for agents
- Event-driven multi-step workflows
- built-in Knowledge Graph support.

---

### 17. [ryaker/mcp-mem0-general](https://github.com/ryaker/mcp-mem0-general)  `innovation: 9`

**Integrates general AI memory across all interactions with any AI tool, IDE, or chatbot.**

**Key Features:**
- Persistent memory system for AI assistants
- Cross-project and cross-session memory management
- Support for semantic search and knowledge graph creation
- Custom memory categories and selective memory patterns
- Integration with external tools and workflows

---

### 18. [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)  `innovation: 9`

**A system enabling persistent memory for AI models via a local knowledge graph, integrating Claude and MCP for secure, organized data storage.**

**Key Features:**
- Persistent memory using a local knowledge graph
- Integration with Claude Code/Desktop
- AI memory management through AIM directories
- Secure file naming and overwrite protection
- Cross-project and cross-database organization

---

### 19. [spences10/mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)  `innovation: 9`

**A high-performance persistent memory system for the Model Context Protocol (MCP) powered by libSQL, designed to optimize AI agent and knowledge graph applications.**

**Key Features:**
- High-performance text search with relevance ranking
- Persistent storage of entities and relations
- Flexible text search with fuzzy matching
- Context-optimized for LLM efficiency
- Knowledge graph management
- Secure token-based authentication for remote databases

---

### 20. [t1nker-1220/memories-with-lessons-mcp-server](https://github.com/t1nker-1220/memories-with-lessons-mcp-server)  `innovation: 9`

**A memory server that implements persistent knowledge graphs for intelligent systems, enabling entities to remember and learn from past interactions.**

**Key Features:**
- Persistent memory using a local knowledge graph
- Entity-based storage with observations and lessons
- Automated learning from errors and solutions
- Integration with external tools and CI/CD pipelines

---

### 21. [ttommyth/rag-memory-mcp](https://github.com/ttommyth/rag-memory-mcp)  `innovation: 9`

**An advanced MCP server for RAG-enabled memory with semantic search and hybrid retrieval.**

**Key Features:**
- Knowledge Graph Memory
- Vector Search
- Document Processing
- Hybrid Search
- SQLite Backend
- Entity Extraction
- Document Chunking
- Contextual Observations

---

### 22. [CaviraOSS/OpenMemory](https://github.com/CaviraOSS/OpenMemory)  `innovation: 8`

**A multi-sector cognitive memory engine that provides LLMs with local, persistent, and explainable long-term memory using temporal knowledge graphs and biological-inspired decay.**

**Key Features:**
- Multi-sector memory classification
- temporal knowledge graphs
- biological decay and reinforcement logic
- waypoint graph associations
- explainable retrieval traces
- OpenAI SDK instrumentation
- cross-platform data connectors
- Model Context Protocol (MCP) support
- local-first SQLite persistence

---

### 23. [GreatScottyMac/context-portal](https://github.com/GreatScottyMac/context-portal)  `innovation: 8`

**Context Portal (ConPort) is a SQLite-backed MCP server that functions as a structured memory bank for AI assistants, enabling long-term project context through knowledge graphs and RAG.**

**Key Features:**
- Workspace-isolated SQLite persistence
- Knowledge graph construction (entities and relationships)
- Vector-based semantic search for RAG
- MCP tool-driven interaction
- Automatic schema migrations via Alembic
- Multi-workspace support via workspace_id
- Prompt caching optimization
- STDIO-based IDE integration

---

### 24. [agentic-mcp-tools/memora](https://github.com/agentic-mcp-tools/memora)  `innovation: 8`

**A lightweight MCP server providing persistent semantic memory, knowledge graph visualization, and cross-session context for AI agents.**

**Key Features:**
- SQLite persistence with cloud sync
- Semantic search (OpenAI/Sentence-Transformers/TF-IDF)
- LLM-based memory deduplication
- Interactive knowledge graph visualization
- Hierarchical memory organization
- Event notifications for inter-agent communication
- Action history and timeline tracking
- RAG-powered chat interface
- Memory importance boosting
- Typed relationship linking

---

### 25. [bro3886/mcp-memory-custom](https://github.com/bro3886/mcp-memory-custom)  `innovation: 8`

**A custom memory server for MCP that enables structured knowledge graph management with language models.**

**Key Features:**
- Custom memory paths
- Timestamping interactions
- Knowledge graph integration
- LLM-powered search
- Project-specific memory storage

---

### 26. [evangstav/python-memory-mcp-server](https://github.com/evangstav/python-memory-mcp-server)  `innovation: 8`

**A memory MCP server enabling knowledge graph management with strict validation and secure data handling.**

**Key Features:**
- Entity creation and management
- Observation tracking
- Relation building
- Memory flushing
- Validation rule enforcement
- Secure data storage and retrieval

---

### 27. [iachilles/memento](https://github.com/iachilles/memento)  `innovation: 8`

**A memory server leveraging SQLite, FTS5, and sqlite-vec for persistent knowledge graph storage with semantic search capabilities.**

**Key Features:**
- Persistent memory using SQLite + FTS5
- Semantic vector search with bge-m3
- Offline embedding model (bge-m3)
- Integration with Claude Desktop
- Modular repository layer

---

### 28. [izumisy/mcp-duckdb-memory-server](https://github.com/izumisy/mcp-duckdb-memory-server)  `innovation: 8`

**A Borg project that enhances the MCP Knowledge Graph Memory Server by replacing its in-memory JSON storage with DuckDB for improved performance and scalability.**

**Key Features:**
- DuckDB backend integration for memory server
- SQL-based querying with DuckDB
- Fuzzy search capabilities using Fuse.js
- Support for complex queries and conditional searches
- Indexing for faster data retrieval

---

### 29. [squid-protocol/gitgalaxy](https://github.com/squid-protocol/gitgalaxy)  `innovation: 8`

**An AST-free, LLM-free heuristic knowledge graph engine for deep repository intelligence. Map, secure, and modernize enterprise codebases across 50+ languages at extreme velocity - squid-protocol/gitgalaxy**

**Key Features:**
- Knowledge graph

---

### 30. [topoteretes/cognee](https://github.com/topoteretes/cognee)  `innovation: 8`

**Cognee is an open-source knowledge engine that enables persistent AI agent memory by integrating graph databases, vector search, and cognitive science principles.**

**Key Features:**
- Hybrid Vector-Graph retrieval
- Automated ontology grounding
- Cognify data pipeline
- Agentic tenant isolation
- Multi-agent knowledge sharing
- OpenTelemetry (OTEL) traceability
- Multimodal ingestion
- GraphRAG reasoning optimization

---

### 31. [yantrikos/yantrikdb](https://github.com/yantrikos/yantrikdb)  `innovation: 8`

**Cognitive memory engine for AI agents — temporal decay, contradiction detection, autonomous consolidation, knowledge graph, ANN recall via HNSW. Embeddable Rust library with Python bindings; powers yantrikdb-server (HTTP gateway, MCP server, openraft cluster). AGPL. - yantrikos/yantrikdb**

**Key Features:**
- Persistent memory
- MCP integration
- Knowledge graph
- Agent support
- Graph relationships
- Tool integration

---

### 32. [zongmin-yu/literature-memory-server-fastmcp-mcp](https://github.com/zongmin-yu/literature-memory-server-fastmcp-mcp)  `innovation: 8`

**A system for managing and integrating diverse knowledge sources with persistent storage and structured note-taking.**

**Key Features:**
- universal source identification
- support for multiple source types
- structured note-taking
- entity linking to knowledge graph
- relationship tracking

---

## Semantic & Vector Memory

### 33. [coleam00/mcp-mem0](https://github.com/coleam00/mcp-mem0)  `innovation: 10`

**MCP-Mem0: Persistent Context**

**Key Features:**
- Persistent memory storage
- semantic search/recall tools
- autonomous fact extraction (Add/Update/Delete)
- local-first SQLite/ChromaDB support.

---

### 34. [mem0ai/mcp-mem0](https://github.com/mem0ai/mcp-mem0)  `innovation: 10`

**Mem0 + Qdrant: Semantic Memory**

**Key Features:**
- Self-improving semantic memory
- Qdrant FastEmbed integration
- metadata filtering (session/user ID)
- hybrid Graph+Vector persistence.

---

### 35. [neuml/txtai](https://github.com/neuml/txtai)  `innovation: 10`

**txtai: Semantic Memory**

**Key Features:**
- Bayesian hybrid search (BB25)
- persistent agent memory (agents.md)
- multimodal indexing (Audio/Image/Video)
- DuckDB relational storage.

---

### 36. [amotivv/memory-box-mcp](https://github.com/amotivv/memory-box-mcp)  `innovation: 9`

**A platform enabling semantic memory storage, retrieval, and organization using vector embeddings for intelligent search.**

**Key Features:**
- Semantic search for memories
- Bucket organization and management
- Relationship tracking between memories
- Memory status monitoring
- Data persistence across sessions

---

### 37. [doobidoo/mcp-memory-dashboard](https://github.com/doobidoo/mcp-memory-dashboard)  `innovation: 9`

**A professional desktop application for managing and interacting with the MCP Memory Service, offering a web-based dashboard integrated directly into the service.**

**Key Features:**
- Memory Storage and Management
- Semantic Search and Recall
- Time-Based Recall
- Tag Management
- Database Optimization and Backup Creation
- Health Monitoring and Performance Metrics
- Docker Mode for Enhanced Performance
- Live Statistics and Database Health

---

### 38. [matrixorigin/Memoria](https://github.com/matrixorigin/Memoria)  `innovation: 9`

**Secure memory management for AI agents with Git-level version control.**

**Key Features:**
- Git-level version control for every memory change
- Zero-copy branching and instant snapshots
- Point-in-time rollback and time-travel capabilities
- Semantic search and vector-based retrieval
- Self-governance with automatic contradiction detection
- Audit trails and provenance tracking
- Cross-conversation preference persistence
- Local embedding model for privacy
- Support for MCP-compatible agents

---

### 39. [notbnull/mcp-rag-context](https://github.com/notbnull/mcp-rag-context)  `innovation: 9`

**A lightweight MCP server enabling persistent memory and context management for AI assistants using local vector storage and SQLite.**

**Key Features:**
- Local vector storage with Vectra for efficient semantic search
- Persistent SQLite database for reliable data persistence
- Hybrid retrieval combining semantic search and indexed queries
- Privacy-first design with all data stored locally

---

### 40. [p-funk/fegis](https://github.com/p-funk/fegis)  `innovation: 9`

**A developer platform for AI-powered coding, workflow automation, and secure code management.**

**Key Features:**
- YAML-based tool definition with semantic search
- Automatic storage of tool usage in Qdrant vector database
- Integration with Claude Desktop for advanced reasoning
- Support for enterprise-grade security and privacy
- AI-assisted code review
- workflow automation
- and deployment

---

### 41. [rmtech1/txtai-assistant-mcp](https://github.com/rmtech1/txtai-assistant-mcp)  `innovation: 9`

**A robust API server for semantic vector memory storage, retrieval, and management using TxtAI with integration for AI assistants like Claude and Cline.**

**Key Features:**
- Semantic search across stored memories
- Persistent file-based backend storage
- Tag-based memory organization
- Memory statistics and health monitoring
- Automatic data persistence
- Comprehensive logging
- Configurable CORS settings

---

### 42. [roboticforce/sugar](https://github.com/roboticforce/sugar)  `innovation: 9`

**Persistent memory for AI coding agents combining global knowledge with project-specific context.**

**Key Features:**
- Persistent memory for AI coding agents
- Global knowledge integration
- Autonomous task execution across projects
- Semantic search with sentence-transformers
- Project-specific and global guideline management
- Cross-project standardization via MCP
- Local context awareness with global scope

---

### 43. [varun29ankuS/shodh-memory](https://github.com/varun29ankuS/shodh-memory)  `innovation: 9`

**Shodh Memory is a persistent, offline AI memory system for cognitive agents and robots, enabling them to remember relevant information, forget irrelevant data, and improve performance over time without relying on external APIs or cloud services.**

**Key Features:**
- Persistent memory across sessions
- Memory recall and proactive context
- Decay-based learning (Hebbian)
- Local storage using RocksDB
- Integration with MCP and ROS2
- No GPU or cloud dependencies
- Automatic API key generation
- Support for semantic search and contextual recall

---

### 44. [zilliztech/memsearch](https://github.com/zilliztech/memsearch)  `innovation: 9`

**A cross-platform semantic memory system enabling persistent, searchable context across AI agents.**

**Key Features:**
- Cross-platform semantic memory storage
- Persistent Markdown-based memories
- Integration with Claude Code
- OpenClaw
- OpenCode
- Codex CLI
- Hybrid search algorithms (BM25
- dense vectors
- RRRF)
- Real-time sync and deduplication

---

### 45. [DrDavidL/sem-mem](https://github.com/DrDavidL/sem-mem)  `innovation: 8`

**Sem-Mem provides a local, tiered semantic memory solution for AI agents using an HNSW index for disk persistence and an LRU cache for fast recall.**

**Key Features:**
- Tiered Memory (L1 RAM Cache/L2 HNSW Disk Index)
- Hybrid Search (Vector + Lexical)
- Local Storage
- Time-Decay Scoring
- Auto-Memory (Salience Detection)
- Query Expansion
- Outcome Learning

---

### 46. [coldielb/inked](https://github.com/coldielb/inked)  `innovation: 8`

**A lightweight, fast memory management server for Claude apps with optional AI-powered search.**

**Key Features:**
- Fast text search
- Embedding-based semantic search
- Optional AI reranking
- Local SQLite storage
- Secure memory management
- Customizable memory models

---

### 47. [jean-technologies/jean-memory](https://github.com/jean-technologies/jean-memory)  `innovation: 8`

**A comprehensive AI memory infrastructure that provides a persistent, cross-platform memory layer for AI agents using an intelligent orchestration engine built on top of mem0 and graphiti.**

**Key Features:**
- Intelligent memory orchestration
- graph-based context retrieval
- cross-platform SDKs
- semantic memory persistence
- automated intent analysis for context strategy
- headless API access
- self-hosted Docker architecture
- drop-in React chat components with context awareness

---

### 48. [kunihiros/mem0-mcp-for-pm](https://github.com/kunihiros/mem0-mcp-for-pm)  `innovation: 8`

**A project management tool leveraging mem0-mcp for structured project memory and semantic search.**

**Key Features:**
- Project memory storage and retrieval
- Semantic search for project-related information
- Structured data handling for project management
- Customizable logging and output options
- Integration with MCP Host for cloud-based project memory

---

### 49. [https://github.com/recallbricks](https://github.com/recallbricks)  `innovation: 8`

**RecallBricks is a graph-based memory infrastructure designed to provide AI agents with persistent, relationship-aware context beyond simple vector similarity.**

**Key Features:**
- Auto-relationship detection
- causality tracking
- cross-session persistence
- memory graph architecture
- semantic search integration
- LangChain drop-in replacement
- metacognitive memory layers
- production-ready agent runtime

---

### 50. [sdimitrov/mcp-memory](https://github.com/sdimitrov/mcp-memory)  `innovation: 8`

**A server-based memory system leveraging PostgreSQL and pgvector for long-term AI memory storage.**

**Key Features:**
- PostgreSQL with pgvector
- Semantic search capabilities
- Confidence scoring
- Real-time updates via SSE
- Memory operations API

---

### 51. [verygoodplugins/mcp-automem](https://github.com/verygoodplugins/mcp-automem)  `innovation: 8`

**AutoMem is a graph-vector memory service that provides AI assistants with durable, relational memory across multiple sessions and platforms using the Model Context Protocol (MCP).**

**Key Features:**
- Graph-vector hybrid architecture
- 11 authorable relationship types
- HippoRAG 2 retrieval optimization
- cross-platform synchronization
- sub-second retrieval performance
- remote MCP sidecar (HTTP/SSE)
- automated platform setup wizard
- session-start memory hooks

---

## Episodic & Experience Memory

### 52. [langchain-ai/langmem](https://github.com/langchain-ai/langmem)  `innovation: 10`

**LangMem: SDK for Recall**

**Key Features:**
- Three-tier memory (Semantic/Episodic/Procedural)
- automated background consolidation
- LangGraph integration
- immediate "hot-path" tool access.

---

### 53. [DragonShadows1978/AI-AfterImage](https://github.com/DragonShadows1978/AI-AfterImage)  `innovation: 9`

**AI-AfterImage provides persistent, episodic memory for AI coding agents like Claude Code by storing and retrieving past code interactions locally.**

**Key Features:**
- Local SQLite/PostgreSQL KB
- Hybrid Search (Keyword + Semantic)
- Pre-write Context Injection
- Post-write Diff Extraction/Storage
- Code Intelligence (AST Parsing
- Language Detection)
- Semantic Chunking
- Code Churn Tracking with Tiering
- CLI management.

---

### 54. [freshtechbro/Vibe-Coder-MCP](https://github.com/freshtechbro/Vibe-Coder-MCP)  `innovation: 9`

**Vibe Coder is an MCP (Model Context Protocol) server designed to supercharge your AI assistant (like Cursor, Cline AI, or Claude Desktop) with powerful tools for software development.**

**Key Features:**
- ['Complete Hybrid Matcher Overhaul: All 15 MCP tools now have comprehensive parameter extraction.'
- 'CLI/REPL Experience: Interactive confirmations
- job status polling with visual progress.'
- 'Better Tool Matching: Multi-strategy approach (keyword 35%
- pattern 30%
- semantic 15%
- LLM 20%).'
- 'TypeScript Strict Mode: Zero any types
- all explicit typing
- production-grade code quality.'

---

### 55. [nambok/mentedb](https://github.com/nambok/mentedb)  `innovation: 9`

**A cognition-aware, ground-up Rust storage engine for AI agents that organizes and curates knowledge using entity-centric memory, deduplication, contradiction detection, and LLM-powered inference.**

**Key Features:**
- Entity-centric memory with structured entities and graph relationships
- Automatic memory extraction from raw conversations
- Contradiction detection and belief propagation
- Adaptive multi-pass retrieval with entity graph expansion
- Quality filtering
- deduplication
- and temporal validity checks
- Support for multiple LLM providers (Anthropic
- OpenAI
- Ollama)

---

### 56. [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)  `innovation: 9`

**Hindsight is a biomimetic agent memory system that moves beyond simple vector retrieval by organizing information into world facts, experiences, and evolved mental models.**

**Key Features:**
- Biomimetic memory organization
- Mental model reflection
- Automated LLM memory wrapper
- Per-user memory isolation
- LongMemEval optimized architecture
- Multi-provider LLM abstraction
- Embedded deployment mode
- Metadata-driven memory banks

---

### 57. [visionscaper/collabmem](https://github.com/visionscaper/collabmem)  `innovation: 9`

**A long-term collaboration memory system for AI assistants, enabling episodic and world model memory over time.**

**Key Features:**
- Episodic memory index
- World model memory
- In-context awareness
- File-based storage
- Git tracking
- Integration with AI assistants
- Context retention across sessions

---

### 58. [MemMachine/MemMachine](https://github.com/MemMachine/MemMachine)  `innovation: 8`

**MemMachine is an open-source universal memory layer that provides AI agents with persistent, multi-layered memory systems including episodic context and structured user profiles.**

**Key Features:**
- Episodic graph-based memory
- Structured SQL profile storage
- Multi-layered memory hierarchy (Working/Episodic/Profile)
- Native Model Context Protocol (MCP) server
- Framework-agnostic SDKs
- Cross-session persistence
- Vector-based semantic search
- Automated metadata tagging

---

### 59. [Symbitic/awesome-babylonjs](https://github.com/Symbitic/awesome-babylonjs)  `innovation: 8`

**A curated list of awesome things related to the Babylon.js game engine.**

**Key Features:**
- The resource showcases the breadth of Babylon.js capabilities
- covering rendering
- physics simulation (PhysX)
- advanced visual effects (shaders/lighting)
- cross-platform compatibility (WebXR)
- and diverse interactive demos. Key highlights include:
* **Rendering & Visualization:** Demonstrating various 3D objects
- lighting effects
- and custom mesh creation.
* **Physics Simulation:** Examples of collision handling
- fluid rendering
- and physics-based interactions.
* **Interactive Experiences:** Demos showcasing gameplay concepts like racing games

---

### 60. [ashish0kumar/fzfm](https://github.com/ashish0kumar/fzfm)  `innovation: 8`

**Fuzzy Finder File Manager (fzfm) is a powerful tool designed to enhance the file management experience by providing a fast, keyboard-centric interface for navigating and interacting with files.**

**Key Features:**
- Seamless directory navigation using only keyboard arrows (Up/Down Arrow)
- Blazing-fast fuzzy search powered by fzf
- File previewing using bat (fallback to cat)
- Directory previewing using eza (fallback to ls)
- Customizable multimedia file opener (wslview
- xdg-open
- etc.)
- and customizable text editing via nvim.

---

## MCP Memory Servers

### 61. [DS4SD/docling](https://github.com/DS4SD/docling)  `innovation: 10`

**Docling: Smart Documents**

**Key Features:**
- Heron layout parsing model
- agentic MCP server integration
- expanded format support (XBRL/LaTeX)
- pluggable VLM support (SmolDocling).

---

### 62. [microsoft/markitdown](https://github.com/microsoft/markitdown)  `innovation: 10`

**MarkItDown: Multimodal MD**

**Key Features:**
- Broad format support (Word/Excel/PPTX)
- OCR-based image-to-text
- audio-to-text transcription
- integrated MCP server support.

---

### 63. [RMANOV/sqlite-memory-mcp](https://github.com/RMANOV/sqlite-memory-mcp)  `innovation: 9`

**A production-grade SQLite-backed MCP Memory Server with WAL concurrency, FTS5 search, session tracking, task management, cross-machine sync, and secure deployment options.**

**Key Features:**
- SQLite-based memory storage with WAL (Write-Ahead Logging) for ACID compliance
- FTS5 full-text search engine
- Session tracking and context persistence
- Task management with CRUD operations and prioritization
- Cross-machine bridge sync via private Git repositories
- Premium runtime boundary for secure
- isolated execution
- Integration of external tools and custom logic via plugins

---

### 64. [sachitrafa/YourMemory](https://github.com/sachitrafa/YourMemory)  `innovation: 9`

**A persistent memory system for AI agents that mimics human forgetting curves, enabling selective recall and automatic memory decay.**

**Key Features:**
- Persistent memory layer using Ebbinghaus forgetting curve decay
- Automatic memory pruning based on importance and recency
- Hybrid retrieval combining BM25
- vector search
- and graph traversal
- User-defined recall thresholds and session-based caching
- Integration with Claude AI platform via MCP servers

---

### 65. [tuncer-byte/memory-bank-mcp](https://github.com/tuncer-byte/memory-bank-mcp)  `innovation: 9`

**Memory Bank MCP is an MCP server that centralizes and organizes project documentation for LLM-powered tools, enabling structured knowledge management.**

**Key Features:**
- AI-generated documentation using Gemini API
- Structured knowledge system with six core document types
- Customizable storage and templates
- Advanced querying and export capabilities
- Integration with LLM agents and tools via Model Context Protocol

---

### 66. [Edison-Watch/open-edison](https://github.com/Edison-Watch/open-edison)  `innovation: 8`

**Borg intelligence database focused on securing and monitoring agent data interactions to prevent exfiltration.**

**Key Features:**
- Data leak monitoring
- Controlled execution (to reduce exfiltration risks)
- Visibility into agent interactions
- Simple API for managing MCP servers
- Docker support
- Quick integration with LangGraph/Python agents.

---

### 67. [KraftyUX/memai](https://github.com/KraftyUX/memai)  `innovation: 8`

**MemAI is a local-first, SQLite-based system designed to provide persistent, queryable memory storage specifically for AI agents and development teams.**

**Key Features:**
- SQLite-based local persistence
- API for recording and retrieving memories (decisions
- implementation
- issues)
- CLI for stats and management
- Session management tools (start/finish)
- MCP Server integration for agent communication
- Memory briefing generation

---

### 68. [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori)  `innovation: 8`

**A SQL-native, framework-agnostic memory layer providing structured long-term persistence and background context augmentation for AI agents with high token efficiency.**

**Key Features:**
- Hierarchical Attribution (Entity/Process/Session)
- Background Context Augmentation
- SDK-level LLM Interception
- MCP Server Support
- OpenClaw Plugin Integration
- Token-Efficient Recall (LoCoMo Benchmarked)
- Framework Agnostic (LangChain/PydanticAI/Agno)
- SQL-Native Storage Layer

---

### 69. [agentwong/optimized-memory-mcp-server](https://github.com/agentwong/optimized-memory-mcp-server)  `innovation: 8`

**This project demonstrates an optimized memory management server using a Python-based Memory MCP architecture, designed to enhance performance and efficiency for AI workloads.**

**Key Features:**
- Optimized memory management
- AI-focused development environment
- Secure code execution
- Integration with external tools

---

### 70. [bornpresident/volatility-mcp-server](https://github.com/bornpresident/volatility-mcp-server)  `innovation: 8`

**A Borg-based MCP server integrating Volatility 3 with Claude for natural language memory forensics.**

**Key Features:**
- Natural language memory forensics via Claude
- Automated analysis of memory dumps and processes
- Network and DLL analysis
- Custom plugin support
- Integration with Volatility 3 framework

---

### 71. [davidorex/project-handoffs](https://github.com/davidorex/project-handoffs)  `innovation: 8`

**An MCP tool designed to enhance persistence across AI coding agent sessions.**

**Key Features:**
- AI session persistence
- Secure code storage
- Error handling and recovery
- Type safety and template validation
- Integration with MCP server

---

### 72. [ebailey78/mcp-memory](https://github.com/ebailey78/mcp-memory)  `innovation: 8`

**A Borg-based memory server for Claude Desktop to manage structured memory across project directories.**

**Key Features:**
- Memory store creation in project directories
- Structured memory storage using markdown files
- Lunr.js indexing for fast retrieval
- Tagging and categorization of memories
- Relationship building between memories
- Automatic memory maintenance and updates

---

### 73. [incomestreamsurfer/roo-code-memory-bank-mcp-server](https://github.com/incomestreamsurfer/roo-code-memory-bank-mcp-server)  `innovation: 8`

**A MCP server enabling AI assistants to maintain project context across sessions using a file-based memory bank.**

**Key Features:**
- Initialize memory bank directory and templates
- Check memory bank status
- Read and append markdown files for context
- Persist decisions and progress in markdown logs

---

### 74. [pontusab/directories](https://github.com/pontusab/directories)  `innovation: 8`

**A community hub for Cursor, providing plugins, MCP servers, events, and thousands of developers building together.**

**Key Features:**
- The platform provides a place for plugins
- MCP servers
- events
- and jobs. It defines a clear workflow for development
- integrating tools like Next.js (App Router)
- Bun
- Supabase
- Tailwind CSS
- React Email
- Fuse.js for search

---

### 75. [roampal-ai/roampal-core](https://github.com/roampal-ai/roampal-core)  `innovation: 8`

**Roampal-core is an outcome-based persistent memory server for AI coding assistants that uses a scoring mechanism to promote successful patterns and demote bad advice across sessions.**

**Key Features:**
- Outcome-based memory scoring
- automated context injection
- multi-tiered memory collections
- MCP server integration
- sidecar model scoring
- local-first data storage
- document ingestion (Books)
- memory promotion and demotion logic
- self-healing server hooks.

---

### 76. [samwang0723/mcp-memory](https://github.com/samwang0723/mcp-memory)  `innovation: 8`

**A server-based solution for storing and retrieving long-term memory graphs using Redis Graph.**

**Key Features:**
- Memory management for LLM conversations
- Relationship mapping between memories
- Search and retrieval of memories by type or keyword
- Integration with external tools and services
- Secure storage and access control

---

### 77. [siddhant-k-code/memory-journal-mcp-server](https://github.com/siddhant-k-code/memory-journal-mcp-server)  `innovation: 8`

**A MCP server for searching and analyzing iCloud photo libraries.**

**Key Features:**
- Location search
- Label search
- People search
- Photo analysis
- Fuzzy matching
- Photo taking patterns
- Customizable configuration

---

### 78. [tokeii0/memprocfs-mcp-server](https://github.com/tokeii0/memprocfs-mcp-server)  `innovation: 8`

**A Python-based MCP server implementation for managing memory and process data.**

**Key Features:**
- memory monitoring
- process tracking
- code review integration
- security features
- workflow automation

---

### 79. [tosin2013/mcp-memory-cache-server](https://github.com/tosin2013/mcp-memory-cache-server)  `innovation: 8`

**A memory cache server designed to reduce token consumption by efficiently caching data between language model interactions.**

**Key Features:**
- Memory Cache Server
- MCP Integration
- Automatic Token Caching
- Performance Optimization

---

### 80. [vic563/memgpt-mcp-server](https://github.com/vic563/memgpt-mcp-server)  `innovation: 8`

**A TypeScript-based MCP server supporting persistent memory and multi-model LLM integration.**

**Key Features:**
- Persistent memory system
- Multi-model LLM support
- Model switching (OpenAI
- Anthropic
- OpenRouter
- Ollama)
- Memory retrieval tools
- Provider configuration
- Model selection interface

---

### 81. [zongmin-yu/memory-mcp-manager](https://github.com/zongmin-yu/memory-mcp-manager)  `innovation: 8`

**A tool for managing and switching memory paths for Claude clients using the MCP memory server.**

**Key Features:**
- Switch memory paths
- Client management
- Memory path configuration
- Integration with Claude
- Project-specific memory management

---

## Second Brain & Personal AI

### 82. [khoj-ai/khoj](https://github.com/khoj-ai/khoj)  `innovation: 10`

**Khoj: AI Second Brain**

**Key Features:**
- Multi-source semantic indexing
- local-first private storage
- cross-platform access (Desktop/WhatsApp)
- custom knowledge-based agents.

---

### 83. [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory)  `innovation: 10`

**SuperMemory: AI Second Brain**

**Key Features:**
- Infinite context API
- self-updating knowledge base
- multi-LLM support (Claude/Cursor)
- ranked #1 on memory benchmarks.

---

## Stateful Sessions & Checkpointing

### 84. [Eternego-AI/eternego](https://github.com/Eternego-AI/eternego)  `innovation: 10`

**Eternego: Local Persona**

**Key Features:**
- Long-term persistent style/decision memory
- three-layer modular architecture (logic/UI separation)
- "Thinking Model" learning for autonomous scaffolding
- 100% local privacy.

---

### 85. [camgitt/memoir](https://github.com/camgitt/memoir)  `innovation: 9`

**A persistent memory system for AI coding tools that syncs across machines via MCP with end-to-end encryption.**

**Key Features:**
- Persistent memory across machines
- Sync with Claude
- Cursor
- Gemini
- Copilot
- Windsurf
- and more
- E2E encrypted data transfer
- Cross-platform compatibility
- Automatic context recall and restoration

---

### 86. [dialectforge/FlowStateV1.1](https://github.com/dialectforge/FlowStateV1.1)  `innovation: 9`

**FlowState enables persistent memory across coding sessions, allowing Claude Desktop to retain project context, problems, solutions, and learnings.**

**Key Features:**
- Project tracking with organized projects
- components
- and todos
- Problem/solution logging for tracking bugs and fixes
- Learning capture for insights and best practices
- Session continuity via Git sync across machines
- Desktop GUI for visual project management (optional)
- Integration with Claude Desktop for persistent memory

---

### 87. [letta-ai/letta-code](https://github.com/letta-ai/letta-code)  `innovation: 9`

**Letta Code is a memory-first coding agent that replaces session-based interactions with persistent, long-lived agents that learn and evolve across multiple terminal sessions.**

**Key Features:**
- Persistent agent state
- trajectory-based skill learning
- manual memory guidance (/remember)
- model-agnostic agent portability
- cross-session context retention
- automated memory initialization
- local skill directory integration (.skills)
- stateful thread management

---

### 88. [sqliteai/sqlite-memory](https://github.com/sqliteai/sqlite-memory)  `innovation: 9`

**A markdown-based AI agent memory system with persistent, searchable offline-first sync for distributed agents.**

**Key Features:**
- Persistent SQLite memory database
- Hybrid semantic and FTS5 search
- Markdown-aware chunking and embedding
- Offline-first synchronization between agents
- Smart content hashing and incremental sync

---

### 89. [djm81/chroma_mcp_server](https://github.com/djm81/chroma_mcp_server)  `innovation: 8`

**A server-based solution for integrating ChromaDB into Cursor with MCP-compatible AI models.**

**Key Features:**
- Automated Context Recall
- Developer-Managed Persistence
- Bidirectional Linking
- Semantic Code Chunking
- Validation System
- Automated Test-Driven Learning

---

### 90. [redis/agent-memory-server](https://github.com/redis/agent-memory-server)  `innovation: 8`

**This repository focuses on Redis agent memory management and persistence mechanisms.**

**Key Features:**
- memory eviction strategies
- persistence layer integration
- data snapshotting
- disk-based backup system

---

### 91. [sentriz/betanin](https://github.com/sentriz/betanin)  `innovation: 8`

**Borg intelligence database based on the MITM of your torrent client and music player.**

**Key Features:**
- The primary features involve setting up a system to bridge torrent client workflows with music player workflows
- utilizing an API layer (betanin) and notification systems (apprise). Key operational aspects include: 
1. **Borg Intelligence:** The core concept of the database.
2. **MITM Functionality:** Intercepting or mediating between torrent client operations and music player interactions.
3. **Notification Layer:** Using apprise for alerts/notifications.
4. **Configuration & Execution:** Providing a mechanism to start the server
- configure credentials
- and run CLI tools (like `betanin` or `betanin-shell`).
5. **Dockerization:** The use of Docker for deployment
- ensuring persistence for the database
- configuration
- and music assets.

---

## RAG & Document Persistence

### 92. [BAI-LAB/MemoryOS](https://github.com/BAI-LAB/MemoryOS)  `innovation: 10`

**MemoryOS: Agentic OS**

**Key Features:**
- Hierarchical Storage system
- heat-based memory promotion
- ~49% benchmark improvement (LoCoMo)
- automated user preference profiling.

---

### 93. [infiniflow/ragflow](https://github.com/infiniflow/ragflow)  `innovation: 10`

**RAGFlow: Deep Document RAG**

**Key Features:**
- Vision-based layout/table recognition
- template-based chunking
- traceable citation engine
- human-in-the-loop chunk visualization.

---

### 94. [lancedb/lancedb](https://github.com/lancedb/lancedb)  `innovation: 10`

**LanceDB: Multimodal DB**

**Key Features:**
- Embedded/Serverless architecture
- billions-scale vector search
- native blob storage (image/video)
- hybrid search (Vector + FTS).

---

### 95. [letta-ai/letta](https://github.com/letta-ai/letta)  `innovation: 10`

**Letta Agent OS**

**Key Features:**
- Self-editing memory blocks
- Hierarchical storage (Core/Archival/Recall)
- Cross-session persistence
- Multi-user REST API.

---

### 96. [neo4j/mcp-neo4j](https://github.com/neo4j/mcp-neo4j)  `innovation: 10`

**Neo4j MCP: GraphRAG**

**Key Features:**
- Direct Cypher query execution
- schema retrieval for traversal planning
- Neo4j GDS integration (PageRank/Shortest Path)
- adaptive tool disabling.

---

### 97. [recallium/recallium](https://github.com/recallium/recallium)  `innovation: 10`

**Recallium: Universal Memory**

**Key Features:**
- Multi-project knowledge clustering
- automated fact extraction
- local vector storage
- unified memory API for agents.

---

### 98. [spranab/contextcache](https://github.com/spranab/contextcache)  `innovation: 10`

**ContextCache: Tool Output**

**Key Features:**
- Content-Hash Addressing (prevents redundancy)
- cross-session persistent storage
- optimization for high-latency MCP tool calls.

---

### 99. [superagent-ai/reag](https://github.com/superagent-ai/reag)  `innovation: 10`

**ReAG: Reasoning-Augmented Gen**

**Key Features:**
- Holistic full-document evaluation
- retrieval-generation reasoning loop
- elimination of "lost-in-middle" chunking issues
- high-accuracy synthesis.

---

### 100. [JordanMcCann/agentmemory](https://github.com/JordanMcCann/agentmemory)  `innovation: 9.7`

**A single deterministic agent memory system for AI agents, built from scratch in 16 days with no team or funding.**

**Key Features:**
- Single deterministic run with reproducible randomness
- Integration of Claude Opus 4.6 and GPT-4o as judges
- Custom HNSW (Hierarchical Navigable Symbols) retrieval system
- Embedding with all-mpnet-base-v2 for semantic understanding
- Deterministic evaluation using fixed seed values
- Multi-session knowledge consolidation and retrieval
- No oracle access
- ensuring real-world retrieval capability

---

### 101. [Smart-AI-Memory/memdocs](https://github.com/Smart-AI-Memory/memdocs)  `innovation: 9.7`

**Persistent memory management for AI projects, enabling AI assistants to retain context across sessions without cloud dependency.**

**Key Features:**
- Git-native persistent memory storage
- AI context retention via .memdocs directory
- Automatic updates on every commit
- Team collaboration with shared memory
- Integration with Empathy Framework for anticipatory intelligence

---

### 102. [Memphora/memphora-mcp](https://github.com/Memphora/memphora-mcp)  `innovation: 9`

**Add persistent memory to Claude, Cursor, and other AI assistants using the Model Context Protocol.**

**Key Features:**
- Persistent memory storage for AI assistants
- Context retention across conversations
- Automatic knowledge extraction from interactions
- Personalized responses based on user history

---

### 103. [henryhawke/mcp-titan](https://github.com/henryhawke/mcp-titan)  `innovation: 9`

**HOPE enables AI systems to retain and evolve knowledge across conversations using advanced memory techniques.**

**Key Features:**
- Three-tier memory system (short-term
- long-term
- archive)
- Persistent context awareness with momentum-based learning
- Deep storage for core facts and patterns
- Adaptive forgetting mechanism to prevent memory bloat
- Sequence understanding and surprise-based attention

---

### 104. [jakops88-hub/Long-Term-Memory-API](https://github.com/jakops88-hub/Long-Term-Memory-API)  `innovation: 9`

**MemVault is a production-grade API platform that provides AI agents with long-term, context-aware memory using a GraphRAG approach, including an asynchronous 'Sleep Cycle' consolidation engine.**

**Key Features:**
- GraphRAG (Entity and Relationship Extraction)
- Asynchronous 'Sleep Cycle' Consolidation Engine
- Hybrid Search (Vector + Keyword)
- Cost Guard for Token Usage Monitoring
- TypeScript SDK for safe interaction
- Self-Hosting (Open Core)

---

### 105. [janbjorge/rekal](https://github.com/janbjorge/rekal)  `innovation: 9`

**A local SQLite-based persistent memory system for LLMs, enabling Claude Code to retain knowledge across sessions without cloud or API dependencies.**

**Key Features:**
- SQLite file-backed long-term memory storage
- Hybrid search combining keyword matching
- vector semantics
- and recency decay
- Secure
- offline-first design with no external connections
- Integration with Claude Code for persistent memory across sessions

---

### 106. [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)  `innovation: 9`

**A biologically-inspired memory system for AI agents that enables decay, retrieval strengthening, and consolidation across multiple tools.**

**Key Features:**
- Decay and retrieval strengthening
- Consolidation of memory entries
- Automatic deduplication and pruning
- Cross-tool memory sharing
- Session-end capture and logging
- Integration with AI development environments

---

### 107. [ototao/unsloth-mcp-server](https://github.com/ototao/unsloth-mcp-server)  `innovation: 9`

**Unsloth-MCP-Server optimizes LLM fine-tuning speed and memory usage by leveraging custom CUDA kernels, 4-bit quantization, and extended context lengths.**

**Key Features:**
- 2x faster fine-tuning compared to standard methods
- 80% less VRAM usage for large models
- Supports extended context lengths (up to 13x longer)
- 4-bit quantization for efficient training and inference
- Optimized backpropagation and dynamic quantization techniques

---

### 108. [pgvector/pgvector](https://github.com/pgvector/pgvector)  `innovation: 9`

**pgvector: AI-on-Postgres**

**Key Features:**
- Native vector data type
- HNSW/IVFFlat indexing
- ACID-compliant RAG
- Unified relational/semantic queries.

---

### 109. [pinkpixel-dev/mem0-mcp](https://github.com/pinkpixel-dev/mem0-mcp)  `innovation: 9`

**A model context protocol server enabling persistent memory for AI agents using Mem0, integrated with MCP for long-term storage.**

**Key Features:**
- Add_memory: Stores text content as persistent memory for a specific userId
- Search_memory: Retrieves stored memories based on natural language queries
- Delete_memory: Permanently removes specified memories
- Cloud Storage Mode: Persistent storage via Mem0 cloud servers
- Supabase Storage Mode: Self-hosted with Supabase database integration

---

### 110. [qdrant/qdrant](https://github.com/qdrant/qdrant)  `innovation: 9`

**Qdrant is a high-performance, massive-scale vector database and vector search engine designed for storing, searching, and managing vectors with rich payload filtering.**

**Key Features:**
- Vector storage and similarity search
- Rich payload filtering
- Hybrid search (dense and sparse vectors)
- Vector quantization
- Distributed deployment (sharding/replication)
- REST and gRPC APIs
- Client libraries in multiple languages.

---

### 111. [simplemindedbot/mnemex](https://github.com/simplemindedbot/mnemex)  `innovation: 9`

**CortexGraph implements a human-like temporal memory system for AI assistants, enabling natural forgetting curves and persistent short-term storage.**

**Key Features:**
- Human-like forgetting curves
- Short-term memory (JSONL)
- Long-term memory (Markdown with YAML frontmatter)
- Smart prompting and MCP integration
- Persistent storage via local files
- Export to Markdown for portability

---

### 112. [suttonwilliamd/tpc-server](https://github.com/suttonwilliamd/tpc-server)  `innovation: 9`

**A Node.js/Express API for AI-human collaboration, enabling secure storage and retrieval of thoughts and plans using SQLite.**

**Key Features:**
- MCP-compliant server for AI agent interaction
- SQLite database (tpc.db) for persistent storage of thoughts and plans
- RESTful API endpoints for managing thoughts
- plans
- tags
- and context
- Markdown support for rich text in UI
- Full-text search with filters by type
- tags
- and limit

---

### 113. [verygoodplugins/automem](https://github.com/verygoodplugins/automem)  `innovation: 9`

**AutoMem is a production-grade long-term memory service for AI assistants that uses a dual graph-vector architecture to enable relational reasoning and automated memory consolidation.**

**Key Features:**
- Dual Graph-Vector storage (FalkorDB/Qdrant)
- Multi-hop Bridge Discovery
- Automatic Entity Extraction
- Zettelkasten-inspired memory clustering
- Importance scoring
- Temporal context tracking
- 11 authorable relationship types
- Background memory consolidation
- MCP (Model Context Protocol) support
- LoCoMo benchmarked performance

---

### 114. [yoloshii/ClawMem](https://github.com/yoloshii/ClawMem)  `innovation: 9`

**On-device memory layer for AI agents combining retrieval-augmented search, hybrid scoring, and self-evolving notes.**

**Key Features:**
- ClawMem on-device memory layer
- Integration with Claude Code
- OpenClaw
- Hermes
- Multi-signal retrieval (BM25 + vector search)
- Hybrid RAG search and intent classification
- Self-evolving memory notes and deduplication
- Secure local storage via SQLite vault

---

### 115. [yuchen20/memory-plus](https://github.com/yuchen20/memory-plus)  `innovation: 9`

**A lightweight, local RAG memory store for MCP agents to record, retrieve, update, and visualize persistent memories across sessions.**

**Key Features:**
- Record memories
- Retrieve memories
- Update memories
- Delete memories
- Visualize memories

---

### 116. [Irina1920/WMB-100K](https://github.com/Irina1920/WMB-100K)  `innovation: 8.5`

**A benchmark evaluating AI memory systems' ability to retrieve accurate, real-world information.**

**Key Features:**
- Retrieval-based evaluation of memory systems
- Multi-domain and multi-conversation question handling
- Accuracy assessment against LLM interpretations
- False memory detection and penalty system
- Support for both keyword matching and semantic interpretation

---

### 117. [KunalSin9h/yaad](https://github.com/KunalSin9h/yaad)  `innovation: 8`

**A local AI-powered memory engine for terminal and agent use, enabling recall and reminders without cloud dependency.**

**Key Features:**
- AI-native memory
- context recall across sessions
- local storage via Ollama
- reminders for agents

---

### 118. [L-A-Marchetti/Vec](https://github.com/L-A-Marchetti/Vec)  `innovation: 8`

**A minimal C library offering generic, contiguous dynamic arrays with O(1) amortized push.**

**Key Features:**
- Contiguous storage: elements live in a single growable buffer. Growth strategy: capacity grows by ×2 when needed. Robust realloc: vec_shrink handles len == 0 by freeing and nulling the buffer (no dangling pointer from realloc(ptr
- 0)). Predictable pointers: pointers from vec_at
- vec_begin
- vec_end
- and vec_back are stable until a resizing operation (push that grows
- reserve
- shrink).

---

### 119. [Papr-ai/memory-opensource](https://github.com/Papr-ai/memory-opensource)  `innovation: 8`

**A sophisticated multi-modal memory layer for AI agents that synchronizes vector search, graph relationships, and document storage with local embedding support.**

**Key Features:**
- Hybrid Vector-Graph retrieval
- Local-first privacy embeddings
- Custom ontology support via GraphQL
- Multi-tier Redis caching
- Parse Server ACL integration
- Stanford STARK benchmark compliance
- Cross-memory relationship discovery
- Sub-100ms retrieval latency

---

### 120. [Roobyx/awesome-game-design](https://github.com/Roobyx/awesome-game-design)  `innovation: 8`

**A comprehensive list of Game Design related learning materials, examples and tools.**

**Key Features:**
- A curated collection of Game Design documents
- templates
- learning materials
- and tools. Focus on bridging the gap between artistic vision (game design) and technical implementation (programming/tools).

---

### 121. [Tanq16/local-content-share?tab=readme-ov-file](https://github.com/Tanq16/local-content-share?tab=readme-ov-file)  `innovation: 8`

**Self-hosted app with browser frontend that enables sharing and storing text snippets and files.**

**Key Features:**
- Text Snippet Storage & Sharing
- File Upload/Download Support
- Customizable TTL/Expiration Settings
- Built-in Notepad/Markdown Editing
- Multi-file Drag-n-Drop Support
- Local Network Accessibility (no internet required).

---

### 122. [archimedescrypto/figma-mcp-chunked](https://github.com/archimedescrypto/figma-mcp-chunked)  `innovation: 8`

**A server for interacting with Figma using chunking and pagination to efficiently handle large files.**

**Key Features:**
- Chunked data retrieval for large Figma files
- Memory-aware processing with configurable limits
- Pagination support for all listing operations
- Resume capability for interrupted operations
- Debug logging and detailed error handling

---

### 123. [bemusic/bemuse](https://github.com/bemusic/bemuse)  `innovation: 8`

**Web-based online rhythm action game.**

**Key Features:**
- The game is powered by HTML5 technologies
- React
- Redux
- and Pixi.js. Key features include playing songs in BMS format
- an online ranking system
- keyboard mode (7-keys)
- custom song loading via folder drag-and-drop
- party modes for friends
- multiple difficulties
- adjustable speed settings

---

### 124. [clawsoftware/clawPDF](https://github.com/clawsoftware/clawPDF)  `innovation: 8`

**Open Source Virtual (Network) Printer for Windows that allows you to create PDFs, OCR text, and print images, with advanced features usually available only in enterprise solutions.**

**Key Features:**
- Print to PDF
- PDF/A-1b
- PDF/A-2b
- PDF/A-3b
- PDF/X
- PDF/Image
- OCR
- SVG Export
- Drag and Drop Support
- Merge Files

---

### 125. [davidvc/code-knowledge-mcptool](https://github.com/davidvc/code-knowledge-mcptool)  `innovation: 8`

**A knowledge management tool for code repositories using vector embeddings to enhance code understanding and retrieval.**

**Key Features:**
- Memory bank storage
- RAG-based context augmentation
- Context-aware code understanding
- Integration with RooCode/Cline via MCP

---

### 126. [digitarald/chatarald](https://github.com/digitarald/chatarald)  `innovation: 8`

**A test-driven, library-first ChatGPT-style web app in TypeScript. Built as a pnpm monorepo with a reusable LLM client library, provider-agnostic adapters, and a minimal React UI.**

**Key Features:**
- Provider-agnostic LLM client (OpenRouter via OpenAI SDK)
- Token counting (estimate + actual usage)
- Local conversation storage (idb-keyval)
- TDD workflow using Vitest and MSW for HTTP mocking
- A minimal React UI layer.

---

### 127. [drakonkat/neural-memory](https://github.com/drakonkat/neural-memory)  `innovation: 8`

**This repository focuses on implementing persistent memory structures for neural network workloads.**

**Key Features:**
- persistent memory storage
- neural network data handling
- API surface for integration
- memory mapping optimizations

---

### 128. [identimoji/mcp-server-emojikey](https://github.com/identimoji/mcp-server-emojikey)  `innovation: 8`

**A server-based emoji-based memory system for Claude to maintain consistent interaction styles and relationship context across conversations.**

**Key Features:**
- Persist LLM relationship state using emojikey keys
- Store and retrieve interaction style preferences
- Enable coding dimensions (e.g.
- 💻🔧
- 🧩🧠) for developer workflows
- Support multiple use cases including DevOps
- CI/CD
- and enterprise AI integration

---

### 129. [insthync/awesome-unity3d](https://github.com/insthync/awesome-unity3d)  `innovation: 8`

**A categorized collection of awesome opensource unity3d repos · GitHub**

**Key Features:**
- The repository showcases a wide range of essential Unity resources
- covering areas like 2D/3D bones
- AI/Animation solutions (like IK/Ragdolls)
- physics simulation
- rendering effects
- and crucial tooling for game development workflows.

---

### 130. [mage0535/hermes-memory-installer](https://github.com/mage0535/hermes-memory-installer)  `innovation: 8`

**This repository implements a custom memory installer for persistent data storage.**

**Key Features:**
- custom memory mapping
- data serialization
- persistence layer abstraction
- integration with OS APIs

---

### 131. [mekanixms/mcp_memory_plugin](https://github.com/mekanixms/mcp_memory_plugin)  `innovation: 8`

**A Python-based memory plugin using SQLite for persistent data storage.**

**Key Features:**
- Persistent memory storage
- SQLite database integration
- Environment configuration management
- Code review and change tracking
- Security features for code protection

---

### 132. [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp)  `innovation: 8`

**A platform-as-a-service for managing and manipulating long-term memory data in AI applications.**

**Key Features:**
- Add memory storage
- Search memories
- Retrieve and update memories
- Delete memories
- Bulk delete memories
- Delete entities
- List stored entities

---

### 133. [movibe/memory-bank-mcp](https://github.com/movibe/memory-bank-mcp)  `innovation: 8`

**A Model Context Protocol (MCP) server for managing Memory Banks, enabling AI assistants to store and retrieve information across sessions.**

**Key Features:**
- Memory Bank Management
- File Operations (Read/Write)
- Progress Tracking
- Decision Logging
- Active Context Management
- Mode Support (Code
- Architect
- Ask
- Debug)
- Integration with .clinerules files

---

### 134. [processing/processing4](https://github.com/processing/processing4)  `innovation: 8`

**Release Processing 4.0 · processing/processing4**

**Key Features:**
- The release addresses several key areas: 
1. **Software Longevity/Maintenance:** Addressing the 21st anniversary of the first release (revision 0001) and establishing Processing 4 as a core platform for keeping code running across changing OS/hardware.
2. **Application Export Fixes:** Resolving issues where 'Export to Application' was broken on macOS
- prompting users to install Xcode tools for proper code signing.
3. **Documentation Updates:** Updating the repository with new versions of major pages (Themes
- Supported Platforms
- Exporting Applications
- Troubleshooting
- and the FAQ).
4. **Resource Management Improvement:** Fixing temporary file cleanup issues by moving temporary files to a dedicated 'processing' folder
- allowing automatic removal after 7 days.
5. **Error Handling Enhancement:** Improving error reporting during 'Export to Application' when errors occur in the code.
6. **UI/UX Polish:** Updating the Theme Selector dropdown menu functionality and fixing color consistency for console scrollbars.
7. **Hardware Fixes:** Fixing issues where ffmpeg was unavailable on certain platforms within Movie Maker.
8. **Optimization:** Compressing a large JDK file (300 files) into a single zip.
9. **Example Updates:** Updating examples to pull from the processing-examples repository and optimizing resource usage (e.g.
- removing sin/cos lookup tables).
4.0.1 is available!

---

### 135. [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)  `innovation: 8`

**This repository implements a memory management system with persistent storage mechanisms.**

**Key Features:**
- persistent storage integration
- data retention mechanisms
- cross-platform compatibility
- API-first design
- memory management optimizations

---

### 136. [seekrays/seekchat](https://github.com/seekrays/seekchat)  `innovation: 8`

**A Sleek and Powerful AI Desktop Assistant that supports MCP integration.**

**Key Features:**
- Multiple AI Providers support
- MCP Tool Integration for enhanced AI capabilities
- Local Storage for privacy-focused chat history
- Multi-language Support (English and Chinese)
- Modern UI
- and an Electron-based desktop application.

---

### 137. [https://github.com/supermemoryai](https://github.com/supermemoryai)  `innovation: 8`

**A high-performance, scalable memory engine and API designed to provide long-term persistence and infinite context for AI agents and LLMs via RAG and MCP.**

**Key Features:**
- RAG-driven memory engine
- Model Context Protocol (MCP) server implementation
- Unified memory benchmarking suite
- Cross-platform context synchronization
- Real-time knowledge updating for agents
- Scalable Cloudflare-based deployment
- Multi-language SDKs (TypeScript/Python)

---

### 138. [tkc/tinyt-todo-mcp](https://github.com/tkc/tinyt-todo-mcp)  `innovation: 8`

**Tiny TODO MCP is a server implementing the Model Context Protocol to enable persistent task management for AI assistants.**

**Key Features:**
- Persistent storage via SQLite
- MCP protocol integration
- Task creation
- updating
- deleting
- searching
- and managing TODOs

---

### 139. [whenmoon-afk/claude-memory-mcp](https://github.com/whenmoon-afk/claude-memory-mcp)  `innovation: 8`

**A lightweight, local-first memory database and continuity journal for Claude AI agents, enabling persistent state management without cloud dependency.**

**Key Features:**
- SQLite-based local storage
- Persistent continuity artifacts
- Snapshot and decision recording
- Linked node inspection
- Project context bundling
- Dry-run validation
- Export/import functionality

---

### 140. [zenmemoryai/zenmemory-mcp-sol](https://github.com/zenmemoryai/zenmemory-mcp-sol)  `innovation: 8`

**A decentralized AI memory infrastructure built on MCP and Solana, enabling secure in-memory storage and retrieval of user memories.**

**Key Features:**
- in-memory or pluggable DB/IPFS storage
- Solana agent integration
- decentralized AI memory infrastructure
- secure code execution
- user memory management

---

## General Memory Systems

### 141. [campfirein/cipher](https://github.com/campfirein/cipher)  `innovation: 10`

**Cipher: Context Sync**

**Key Features:**
- Dual-layer memory (Logic/Reasoning)
- universal IDE support (Cursor/Windsurf)
- team-wide context sharing
- multi-backend LLM support.

---

### 142. [kreuzberg-dev/kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)  `innovation: 10`

**Kreuzberg: Rust Data Ingestion**

**Key Features:**
- Rust-native core (no Pandoc)
- 56+ Format support (PDF/Office/Images)
- byte-accurate semantic chunking
- integrated ONNX CPU embeddings.

---

### 143. [lumina-ai-inc/chunkr](https://github.com/lumina-ai-inc/chunkr)  `innovation: 10`

**Chunkr: Vision Parsing**

**Key Features:**
- VLM-based layout understanding
- semantic chunking (vs character-based)
- OCR with element bounding boxes
- structured Markdown/JSON output.

---

### 144. [mem0ai/mem0](https://github.com/mem0ai/mem0)  `innovation: 10`

**Mem0: Intelligent Memory**

**Key Features:**
- Fact distillation (vs raw chunks)
- smart memory reconciliation logic
- Mem0g Graph-enhanced temporal reasoning
- 90% token savings.

---

### 145. [supermemoryai/supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)  `innovation: 10`

**Supermemory: Cross-Agent Recall**

**Key Features:**
- Cross-platform memory hub
- semantic embedding-based recall
- OAuth security
- project-scoped memory organization.

---

### 146. [Canner/WrenAI](https://github.com/Canner/WrenAI)  `innovation: 9`

**WrenAI Semantic Layer**

**Key Features:**
- MDL semantic modeling
- automated SQL/chart generation
- Wren Engine embeddable core
- multi-database support.

---

### 147. [Krixx1337/burner-net](https://github.com/Krixx1337/burner-net)  `innovation: 9`

**BurnerNet is a C++20 anti-forensic networking engine that securely wipes sensitive data from memory and severes execution traces to protect secrets in transit.**

**Key Features:**
- Zero-trust anti-forensic networking
- Secure memory wiping of secrets
- Response verification in application code
- Dynamic runtime hardening
- Stack isolation and call stack separation
- Provider-based secrets and DoH support
- Pinned keys and transport auditing
- App-owned verification with WithResponseVerifier()

---

### 148. [SecureBitChat/securebit-chat](https://github.com/SecureBitChat/securebit-chat)  `innovation: 9`

**World's most secure P2P messenger with end-to-end encryption and a shared Rust-based cryptographic core.**

**Key Features:**
- End-to-end encryption
- zero-server architecture
- WebRTC direct connections
- ECDH + DTLS + SAS verification
- full ASN.1 validation
- and a shared Rust-based cryptographic core.

---

### 149. [m-pineapple/member-berries-apple-mcp](https://github.com/m-pineapple/member-berries-apple-mcp)  `innovation: 9`

**A conversational AI assistant that integrates with Apple ecosystem to remember user activities and context for natural, personalized interactions.**

**Key Features:**
- Calendar integration (events
- appointments)
- Note and reminder tracking
- Contextual conversation starters
- Memory layer for past interactions
- Smart reminders based on user history

---

### 150. [railyard-dev/railguard](https://github.com/railyard-dev/railguard)  `innovation: 9`

**Safe runtime for Claude Code, built to be yours.**

**Key Features:**
- Secure runtime for Claude Code
- Real-time tool call interception
- Memory safety enforcement
- Behavioral instruction blocking
- Tampering detection
- Cross-platform sandbox execution

---

### 151. [ruvnet/ruv-FANN](https://github.com/ruvnet/ruv-FANN)  `innovation: 9`

**A memory-safe neural intelligence framework enabling efficient, ephemeral deployment of AI models.**

**Key Features:**
- Rust-based neural network library (ruv-FANN)
- Ephemeral intelligence with on-demand instantiation
- GPU-optional architecture with CPU-native execution
- Integration with Claude Flow and other neural architectures
- Swarm-based distributed model orchestration

---

### 152. [9001/copyparty](https://github.com/9001/copyparty)  `innovation: 8`

**Portable file server with accelerated resumable uploads, dedup, WebDAV, SFTP, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file.**

**Key Features:**
- Accelerated resumable uploads/downloads
- deduplication
- support for various protocols (WebDAV
- SFTP
- FTP
- TFTP)
- media indexing
- zip downloads
- file management capabilities (cut/paste
- rename

---

### 153. [BarRaider/streamdeck-textfiletools](https://github.com/BarRaider/streamdeck-textfiletools)  `innovation: 8`

**Tools for the Elgato Stream Deck, designed to manipulate text files and provide useful live stream updates.**

**Key Features:**
- ['Text File Updater: Overwrites contents of a text file.'
- 'Last Word Display: Shows the last word of a text file or alerts if the text matches a preset value.'
- 'Random Line Writer: Sends a random line from a text file to the keyboard (useful for giveaways/chat messages).'
- 'Next Line: Cycles through a text file and outputs the next line on every keypress.'
- 'Regex Display: Parses a text file for a regex and displays the match on a key.'
- 'Stream Deck Integration (via StreamDeck-Tools by BarRaider
- using Easy-PI).'
- 'Multi-Action Support.']

---

### 154. [BytexGrid/NeatShift](https://github.com/BytexGrid/NeatShift)  `innovation: 8`

**A modern Windows file organization tool with symbolic link support.**

**Key Features:**
- Relocate files and folders without breaking application paths. Smart Moving: Move files anywhere
- and NeatShift creates symbolic links so everything still works. Double Safety: Choose between NeatSaves quick backup or system restore points - or use both! Looks Good
- Feels Good: Modern Windows 11 style with both light and dark themes. Stay in Control: See and manage all of the symbolic links in one place.

---

### 155. [Jmc-arch/elia-governed-hybrid-architecture](https://github.com/Jmc-arch/elia-governed-hybrid-architecture)  `innovation: 8`

**A governed hybrid cognitive architecture that separates neural intelligence as a capability rather than an authority.**

**Key Features:**
- governed hybrid cognitive architecture
- symbolic control over neural intelligence
- explicit separation of concerns
- auditable decision-making
- resilience to degradation
- state management with SQLite
- asynchronous message bus
- state transitions defined explicitly

---

### 156. [OfficialIncubo/BeatDrop-Music-Visualizer](https://github.com/OfficialIncubo/BeatDrop-Music-Visualizer)  `innovation: 8`

**A standalone music visualization with custom MilkDrop2 engine, optimized for Windows, designed to enhance the original MilkDrop2 plug-in functionality.**

**Key Features:**
- Based on the Original MilkDrop2 Plug-in
- compatible with all MilkDrop presets (.milk). Features include: Beat detection compatibility for better audio reaction
- new waveforms/transitions
- custom shapes/waves (up to 16 slots)
- precise shader precaching/caching for instant loading
- support for Pixel Shader 4 (Shader Model 3) presets
- and integration with Spout for sharing visuals.

---

### 157. [SuperSonicHub1/awesome-libsm64](https://github.com/SuperSonicHub1/awesome-libsm64)  `innovation: 8`

**A collection of things made with libsm64.**

**Key Features:**
- The repository highlights the utility of `libsm64` in various contexts
- including game engine integration (Blender
- Unity)
- providing a clean interface for SM64 mechanics
- and showcasing its versatility across different platforms and development environments. Key features include asset extraction via ROMs
- C# bindings for high-level interaction
- Rust bindings for low-level access
- and integrations with popular tools like Blender.

---

### 158. [XeroOl/mirin-template](https://github.com/XeroOl/mirin-template)  `innovation: 8`

**The NotITG Mirin Template. Easily create modfiles using Lua.**

**Key Features:**
- Easy creation of modfiles using Lua. Powerful abstractions allowing users to create custom modifiers (e.g.
- turn on invert ease {0
- 1
- outExpo
- 100
- 'invert'}). Optimized code execution. Theme independent design. Powerful system for custom modifiers.

---

### 159. [adammiribyan/zeroboot](https://github.com/adammiribyan/zeroboot)  `innovation: 8`

**Sub-millisecond VM sandboxes for AI agents using copy-on-write forking to enable secure, isolated execution.**

**Key Features:**
- Sub-millisecond VM sandboxes
- Copy-on-write forking
- Hardware-enforced memory isolation
- AI agent execution
- Secure development environment

---

### 160. [agent-kilo/jwno](https://github.com/agent-kilo/jwno)  `innovation: 8`

**A tiling window manager for Windows 10/11, built with Janet and ❤️.**

**Key Features:**
- Tiling window manager for Windows 10/11
- built with Janet and ❤️.

---

### 161. [agentclientprotocol/agent-client-protocol](https://github.com/agentclientprotocol/agent-client-protocol)  `innovation: 8`

**A protocol for connecting any editor to any agent.**

**Key Features:**
- Standardizing communication between code editors and coding agents. Providing a protocol layer for connecting any editor to any agent.

---

### 162. [aleksey-saenko/MusicRecognizer](https://github.com/aleksey-saenko/MusicRecognizer)  `innovation: 8`

**An open-source Android app for music recognition that integrates AudD, ACRCloud, and Shazam to perform song identification.**

**Key Features:**
- Song identification via integration of AudD
- ACRCloud
- and Shazam. One-click song recognition with options to save recordings if offline. Customizable failure behavior settings. Rich track information provided upon success (name
- artist
- album
- year
- artwork
- links). Library management for tracks. Preferences customization. API key requirement for AudD.

---

### 163. [blackhole89/autopen](https://github.com/blackhole89/autopen)  `innovation: 8`

**Editor with LLM generation tree exploration**

**Key Features:**
- The core functionality includes: 
1. **LLM Visualization:** Viewing text through the lens of an LLM to see token probabilities.
2. **Surprising Token Highlighting:** Identifying tokens with low probability.
3. **Continuation Generation:** Generating multiple continuations based on the LLM's distribution.
4. **Seamless Exploration:** Flipping between generated continuations (Alt-⬆⬇) and emitting them into the buffer (Alt-⮕).
5. **LLM Execution:** Ability to load and execute any LLM in the GGUF format using `llama.cpp`.
6. **Integration with Tools:** Utilizing `imgui` for visualization and `imgui-filebrowser` for file browsing.

---

### 164. [bmaltais/kohya_ss](https://github.com/bmaltais/kohya_ss)  `innovation: 8`

**Kohya's GUI is a GUI and CLI for training diffusion models. This project provides a user-friendly Gradio-based Graphical User Interface (GUI) for Kohya's Stable Diffusion training scripts.**

**Key Features:**
- The project provides a user-friendly Graphical User Interface (GUI) and Command Line Interface (CLI) for training diffusion models. Key features include: A user-friendly Gradio-based interface for setting training parameters
- automatic generation of necessary CLI commands
- support for various training methods (LoRA
- Dreambooth
- fine-tuning
- SDXL)
- and cross-platform support (Linux/macOS). It offers options for local installation or cloud deployment via Colab/Runpod.

---

### 165. [callebtc/bitchat-android](https://github.com/callebtc/bitchat-android)  `innovation: 8`

**Bluetooth mesh chat, IRC vibes · GitHub**

**Key Features:**
- Cross-Platform Compatible (iOS compatibility)
- Decentralized Mesh Network (Bluetooth LE for peer discovery)
- End-to-End Encryption (X25519 key exchange + AES-256-GCM)
- Channel-Based Chats (topic-based group messaging with optional password protection)
- Store & Forward (message caching for offline peers)
- IRC-Style Commands (/join
- /msg
- /who)
- Emergency Wipe (triple-tap logo to clear data)
- Modern Android UI (Jetpack Compose with Material Design 3)

---

### 166. [cloudflare/workers-sdk](https://github.com/cloudflare/workers-sdk)  `innovation: 8`

**Wrangler, the CLI for Cloudflare Workers®**

**Key Features:**
- Cloudflare Workers SDK
- Wrangler (CLI for Cloudflare Workers)
- Create-Cloudflare (C3) CLI for creating and deploying new applications
- Miniflare simulator for development/testing
- Chrome DevTools fork for inspecting Workers pages.

---

### 167. [coop-deluxe/sm64coopdx](https://github.com/coop-deluxe/sm64coopdx)  `innovation: 8`

**An official continuation of https://github.com/djoslin0/sm64ex-coop on sm64coopdx for the enhancements and progress it already has.**

**Key Features:**
- Online multiplayer synchronization of entities and levels
- enhanced capability for modders via the Lua API (similar to Roblox/Garry's Mod)
- community-driven project maintained by the Coop Deluxe Team.

---

### 168. [deepseek-ai/awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration)  `innovation: 8`

**Cherry Studio: A powerful desktop AI assistant for producer.**

**Key Features:**
- Desktop AI assistant functionality
- Integration with Deepseek API
- Clear demonstration of an AI tool/agent framework.

---

### 169. [everythingishacked/Pants](https://github.com/everythingishacked/Pants)  `innovation: 8`

**A video filter to add pants or blur out your lower half on Zoom calls when you forget to wear pants.**

**Key Features:**
- The pants filter uses OpenCV and MediaPipe's Pose detection to add a real-time pants filter to video input. The result is piped to a virtual camera output using pyvirtualcam. It allows users to toggle between different styles of pants or blur out the lower half of their body during Zoom calls.

---

### 170. [g0t4/mcp-server-memory-file](https://github.com/g0t4/mcp-server-memory-file)  `innovation: 8`

**A system to manage and store chat context as a text file for Claude and other MCP clients.**

**Key Features:**
- memory_add
- memory_search
- memory_delete
- memory_list
- code_update
- prompt_cueing

---

### 171. [ganelson/inform](https://github.com/ganelson/inform)  `innovation: 8`

**The core software distribution for the Inform 7 programming language, which is a medium for literary writing and a prototyping tool in the games industry.**

**Key Features:**
- Inform is a programming language for interactive fiction. Its core features revolve around natural language syntax
- serving as a medium for literary writing and a prototyping tool. It is also highly influential
- ranking among the top 100 most influential programming languages according to the TIOBE index.

---

### 172. [glzr-io/glazewm](https://github.com/glzr-io/glazewm)  `innovation: 8`

**GlazeWM is a tiling window manager for macOS and Windows inspired by i3wm.**

**Key Features:**
- Tiling window management inspired by i3wm
- YAML configuration support
- multi-monitor support
- customizable rules for windows
- keyboard-driven command integration
- easy one-click installation via package managers (Winget
- Chocolatey
- Scoop)
- and optional integration with Zebar.

---

### 173. [google/timesketch](https://github.com/google/timesketch)  `innovation: 8`

**Collaborative forensic timeline analysis using sketches for organizing and analyzing timelines.**

**Key Features:**
- Collaborative timeline organization via sketches
- Rich annotations/tags for raw data
- Collaborative analysis across users
- Clear structure for forensic timelines.

---

### 174. [hoppo-chan/memory-bank-mcp](https://github.com/hoppo-chan/memory-bank-mcp)  `innovation: 8`

**A memory bank plugin for AI-assisted development using Model Context Protocol to maintain structured project context.**

**Key Features:**
- Guided operations for AI assistants
- Structured context management with 5 core files
- Intelligent update guidance based on changes
- Cross-platform support (Windows/macOS/Linux)
- Integration with GitHub and other development tools

---

### 175. [hrkalona/Fractal-Zoomer](https://github.com/hrkalona/Fractal-Zoomer)  `innovation: 8`

**One of the most complete fractal generating software using java!**

**Key Features:**
- Fractal Zoomer offers a comprehensive suite of features for fractal generation
- including: User Formulas/Custom User Functions
- Plane Transformations
- Rotation
- Initial Perturbation
- Bailout Tests
- Palette Editor
- Julia Sets
- Julia Map
- Polar Coordinates

---

### 176. [ibproduct/ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)  `innovation: 8`

**A memory cache server designed to optimize token usage in MCP API interactions by caching frequently accessed data.**

**Key Features:**
- Memory Cache Server
- MCP Integration
- Automatic Caching of Data
- Performance Optimization

---

### 177. [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent)  `innovation: 8`

**Build effective agents using Model Context Protocol and simple workflow patterns.**

**Key Features:**
- Full MCP support
- Implementation of effective agent patterns (map-reduce
- orchestrator
- evaluator-optimizer
- router)
- Durable agents using Temporal for scaling and recovery
- Simple and composable pattern design.

---

### 178. [markqvist/nomadnet](https://github.com/markqvist/nomadnet)  `innovation: 8`

**Nomad Network: Communicate Freely**

**Key Features:**
- Encrypted messaging over packet-radio
- LoRa
- WiFi or anything else. Zero-configuration
- minimal-infrastructure mesh communication. Distributed and encrypted message store holds messages for offline users. Connectable nodes that can host pages and files. Node-side generated pages with PHP
- Python
- bash or others. Built-in text-based browser for interacting with contents on nodes. Easy to use and bandwidth efficient markup language for writing pages. Page caching in browser.

---

### 179. [milisp/codexia](https://github.com/milisp/codexia)  `innovation: 8`

**A Tauri v2 app for Codex CLI + Claude Code — combining agent workflows, a prompt notepad, and an IDE-like editor in one workspace.**

**Key Features:**
- ['Agent Workflows: Task Scheduler for recurring jobs.'
- 'Remote Control via Headless Web Server.'
- 'Workspace Management: Git worktree management
- project file tree
- IDE-like editor
- prompt notepad.'
- 'Claude Integration (AI capability).'
- 'Tauri v2 architecture with Rust backend and React/TypeScript frontend.']

---

### 180. [milkdrop2077/MilkDrop3](https://github.com/milkdrop2077/MilkDrop3)  `innovation: 8`

**MilkDrop 3.0 is a portable program that supports any audio source, double-preset (.milk2), loading presets based on beat detection and much more.**

**Key Features:**
- Support for any audio source (Spotify
- YouTube
- SoundCloud
- Winamp...)
- the introduction of 'double-preset' (.milk2 file) mixing two presets simultaneously
- real-time toggling of FPS (60/90/120fps)
- real-time auto-transitioning between presets based on beat detection
- and new color manipulation features.

---

### 181. [mobizt/build-your-own-x](https://github.com/mobizt/build-your-own-x)  `innovation: 8`

**Build your own (insert technology here)**

**Key Features:**
- A comprehensive collection of tutorials and guides focused on building or understanding core technologies from the ground up
- covering areas like 3D Rendering
- Augmented Reality
- BitTorrent Clients
- Blockchain/Crypto tools
- and various programming paradigms (C++
- C#
- Java
- JavaScript
- Python).

---

### 182. [nikolamilosevic86/verifAI](https://github.com/nikolamilosevic86/verifAI)  `innovation: 8`

**VerifAI is a Generative Search/Productivity engine with Verifiable answers.**


---

### 183. [onnx/onnx](https://github.com/onnx/onnx)  `innovation: 8`

**Open standard for machine learning interoperability.**

**Key Features:**
- ONNX provides an open source format for AI models
- defining an extensible computation graph model with built-in operators and standard data types. It focuses on capabilities needed for inferencing (scoring)
- enabling interoperability between frameworks
- and streamlining the path from research to production.

---

### 184. [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat)  `innovation: 8`

**Bluetooth mesh chat, IRC vibes**

**Key Features:**
- Dual Transport Architecture (Bluetooth mesh for offline + Nostr protocol for internet-based messaging)
- Location-Based Channels (Geohash coordinates)
- Intelligent Message Routing (Bluetooth → Nostr fallback)
- Decentralized Mesh Network
- Noise Protocol Encryption
- IRC-Style Commands (/msg
- /who style interface).

---

### 185. [https://github.com/projectM-visualizer](https://github.com/projectM-visualizer)  `innovation: 8`

**projectM Visualizer · GitHub**

**Key Features:**
- projectM Visualizer (Cross-platform Music Visualization Library)
- projectM Expression Evaluation Library
- and various frontend/backend implementations (SDL
- Rust
- Qt).

---

### 186. [robertpelloni/ffr-difficulty-model](https://github.com/robertpelloni/ffr-difficulty-model)  `innovation: 8`

**Supervised Learning Model to Quantify Difficulty of Stepfiles in FlashFlashRevolution**

**Key Features:**
- The core functionality is a prediction pipeline that estimates the difficulty score and meter for StepMania charts based on the input file's features. The model is designed to quantify the difficulty of these musical charts.

---

### 187. [roger1337/JDBG](https://github.com/roger1337/JDBG)  `innovation: 8`

**Java Dynamic Reverse Engineering and Debugging Tool**

**Key Features:**
- Class Analysis (Analyse decompiled classes at runtime)
- Analyse method bytecode and field definitions at runtime
- Add classes to object analysis
- Dynamically set breakpoints in bytecode
- Inspect the stack trace
- Inspect local variable values
- Planned features: bytecode instrumentation and class redefinitions
- static variable modification
- Static field watching
- Object Analysis (Add classes to object workspace)

---

### 188. [russellw/sourceview](https://github.com/russellw/sourceview)  `innovation: 8`

**Source file viewer built with Electron, featuring syntax highlighting, directory browsing, and interactive navigation tools.**

**Key Features:**
- Source Code Viewing with syntax highlighting
- Directory Browser with visual grid layout
- Interactive Navigation (click-to-navigate) via a minimap
- Multi-Tab Interface
- Image Support
- PDF Integration
- Binary File Protection
- Keyboard Shortcuts support
- and an optimized Dark Theme.

---

### 189. [servo/servo](https://github.com/servo/servo)  `innovation: 8`

**Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications.**

**Key Features:**
- A lightweight
- high-performance alternative for embedding web technologies in applications
- implemented in Rust.

---

### 190. [slavfox/Cozette](https://github.com/slavfox/Cozette)  `innovation: 8`

**A bitmap programming font optimized for coziness 💜**

**Key Features:**
- The core innovation lies in its bitmap nature
- offering a specific set of glyphs optimized for terminal/CLI environments. It provides both bitmap formats (.otb) and vector formats (.ttf)
- addressing the common problem of scaling and rendering issues with traditional bitmap fonts. The font is designed to be pixel-perfect
- which is crucial for clarity in terminal interfaces.

---

### 191. [terrehbyte/awesome-devblogs](https://github.com/terrehbyte/awesome-devblogs)  `innovation: 8`

**A curated list of links to game developer blogs and/or portfolios that you found interesting.**

**Key Features:**
- The resource provides links to various developer blogs
- portfolio sites
- and company websites
- focusing on showcasing skills
- projects
- and technical expertise within the game development/tech sphere.

---

### 192. [thargor6/JWildfire](https://github.com/thargor6/JWildfire)  `innovation: 8`

**JWildfire - powerful, flexible and user-friendly fractal flame editor**

**Key Features:**
- Powerful
- flexible
- and user-friendly fractal flame editor. Versatile rendering capabilities (CPU/GPU). Extensive feature set including motion curves
- keyframes
- random-flame-generators
- interactive/infinite renderer
- sound-synchronized animation
- and a Java-based scripting interface for custom fractals.

---

### 193. [titzer/wizard-engine](https://github.com/titzer/wizard-engine)  `innovation: 8`

**Research WebAssembly Engine**

**Key Features:**
- Wizard supports most Wasm standard features
- including all of Wasm 3.0. Newer features are under development and vary in their support in the different execution tiers
- which include the V3 interpreter (v3-int)
- the fast interpreter (fast-int) and the single-pass compiler (spc). Wizard includes support for various Wasm features like multi-value
- reference-types
- bulk-memory
- SIMD
- tail-call
- multi-memory
- and extended-const. It supports testcases specified in the .bin.wast format.

---

### 194. [un4ckn0wl3z/memmcp](https://github.com/un4ckn0wl3z/memmcp)  `innovation: 8`

**A tool designed to emulate MCP functionality for memory scanning and manipulation, similar to Cheat Engine.**

**Key Features:**
- memory scanning
- memory modification
- debugging tools
- code analysis
- integration with AI/ML

---

### 195. [winfsp/winfsp](https://github.com/winfsp/winfsp)  `innovation: 8`

**Windows File System Proxy - FUSE for Windows**

**Key Features:**
- ['Enables developers to create custom file systems on Windows without deep kernel programming knowledge.'
- 'Provides a platform for developing and runtime support for custom file systems.'
- 'Core consists of a kernel mode file system driver (FSD) and a user mode DLL.'
- 'API interface allows applications to interact with the file system via standard Windows file APIs.'
- 'Offers benefits like easy development
- stability
- correctness
- performance
- wide support across various architectures (Windows 7-11
- x86/x64/ARM64)

---

### 196. [xaos-project/XaoS](https://github.com/xaos-project/XaoS)  `innovation: 8`

**Real-time interactive fractal zoomer.**

**Key Features:**
- Real-time interactive fractal zooming
- various fractal types
- autopilot functionality
- special coloring modes
- random palette generation
- color cycling
- platform compatibility (Windows
- Mac
- Linux
- BSDs)

---


## Websites & Non-GitHub Resources

### 197. [https://alternativeto.net/software/tagstudio/about](https://alternativeto.net/software/tagstudio/about)  `innovation: 10`

**TagStudio: Meta-Layer**

**Key Features:**
- SQLite-based metadata storage
- nested tags and aliases
- powerful Boolean search
- cross-platform media previews (PSD/Blender/Krita).

---

### 198. [http://www.righto.com/2025/03/pentium-microcde-rom-circuitry.html?m=1](http://www.righto.com/2025/03/pentium-microcde-rom-circuitry.html?m=1)  `innovation: 9`

**Analysis of the Pentium microcode ROM circuitry for inclusion in the Borg Project database.**

**Key Features:**
- Microcode storage in ROM
- Horizontal microcode architecture
- Transistor-based bit encoding
- Complex circuit routing via metal layers
- Power distribution through M1
- M2
- and M3 layers

---


*Total: 198 tools*
