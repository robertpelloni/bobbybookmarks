# Context Engineering & Isolation Tools

Extracted from Borg Intelligence Database | Updated 2026-05-15

**734 GitHub repos** + **1 websites** = **735 total** | Innovation >= 8

Tools for managing, compressing, indexing, and isolating LLM context windows — the critical bottleneck for agent capabilities.

---

## Codebase Indexing & Repository Intelligence

### 1. [PatrickSys/codebase-context](https://github.com/PatrickSys/codebase-context)  `innovation: 10`

**CodeGraphContext: CGC**

**Key Features:**
- Symbol-level graph querying (callers/callees)
- pre-indexed `.cgc` repository bundles
- live file watching (`cgc watch`)
- 10x faster than traditional vector indexing.

---

### 2. [Donnyb369/mcp-spine](https://github.com/Donnyb369/mcp-spine)  `innovation: 9`

**MCP Spine addresses security and efficiency challenges in LLM tooling by providing a secure, context-preserving proxy between client and MCP servers.**

**Key Features:**
- Token waste reduction through schema compression
- Context rotation to prevent file version overwrites
- Secure secret scrubbing and protection against injection attacks
- Semantic routing for intelligent tool selection
- Schema minification with configurable aggression levels
- State guard to maintain file state integrity
- Human-in-the-loop for destructive operations
- Audit logging and secure audit trails

---

### 3. [ast-grep/ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)  `innovation: 9`

**An experimental MCP server enabling AI assistants to search and analyze codebases using Abstract Syntax Tree (AST) pattern matching for precise structural code analysis.**

**Key Features:**
- AST-based code search
- Pattern matching for programming constructs
- Visualization of AST structures
- Rule creation and validation via MCP
- Integration with AI assistants

---

### 4. [crazyrabbitltc/mcp-ethers-server](https://github.com/crazyrabbitltc/mcp-ethers-server)  `innovation: 9`

**A full implementation of Ethers.js as an AI tool for the model context protocol.**

**Key Features:**
- Ethers.js v6 integration
- Wallet operations (eth
- usdc)
- Contract interaction and inspection
- Secure transaction broadcasting
- Gas optimization and estimation
- Hardhat-based development environment
- Comprehensive testing suite
- Custom ABI support
- Multi-chain compatibility (ethereum

---

### 5. [datalab-to/chandra](https://github.com/datalab-to/chandra)  `innovation: 9`

**A state-of-the-art OCR model that accurately interprets complex tables, forms, and handwriting while preserving layout information.**

**Key Features:**
- Handles complex tables and forms with high layout fidelity
- Supports multilingual OCR with strong performance across 90+ languages
- Preserves mathematical content
- tables
- and structured data
- Offers both local (HuggingFace) and remote (vLLM) inference options
- Includes a hosted API for faster and more accurate results
- Provides detailed output formats: markdown
- html
- and JSON with metadata

---

### 6. [elusznik/mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)  `innovation: 9`

**This project implements a discovery-first MCP bridge that executes Python code in isolated rootless containers to drastically reduce tool definition context bloat.**

**Key Features:**
- Discovery-first architecture
- Rootless container execution (Podman/Docker)
- Stdio MCP server proxying
- Runtime schema hydration
- Fuzzy tool search
- Capability dropping for security isolation
- Python-centric execution environment

---

### 7. [gleicon/mcp-osv](https://github.com/gleicon/mcp-osv)  `innovation: 9`

**A MCP server integrating with OSV.dev to enable secure code reviews and vulnerability analysis.**

**Key Features:**
- MCP protocol support for AI assistant integration
- Secure code analysis using AST-based Go code inspection
- Secret detection via Gitleaks v8 with 100+ rules
- Dependency vulnerability checks against OSV.dev database
- Comprehensive security audit including pattern matching and entropy analysis

---

### 8. [9001/copyparty](https://github.com/9001/copyparty)  `innovation: 8`

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

### 9. [BarRaider/streamdeck-textfiletools](https://github.com/BarRaider/streamdeck-textfiletools)  `innovation: 8`

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

### 10. [CursorWP/ai-project-journal](https://github.com/CursorWP/ai-project-journal)  `innovation: 8`

**A simple template to help AI coding assistants maintain context across sessions.**

**Key Features:**
- ['Context Retention: The core feature that allows AI assistants to remember past decisions and context.'
- 'Progress Tracking: Documenting what has been built.'
- "Decision Log: Recording the 'why' behind certain technical choices."
- 'Session Continuity: Ensuring a smooth transition between sessions.'
- 'Team Friendly: Onboarding new developers or AIs instantly.'
- 'Quick Start: Providing an easy way to start and end sessions by updating the journal.']

---

### 11. [GoneTone/mcp-server-taiwan-weather](https://github.com/GoneTone/mcp-server-taiwan-weather)  `innovation: 8`

**Model Context Protocol server for accessing Taiwan Central Meteorological Bureau API data.**

**Key Features:**
- Access Taiwan weather forecasts via MCP Server
- Integrate external tools and APIs
- Support for AI model context management
- Secure authentication with API keys

---

### 12. [alefcastelo/archai-static-analyzer-mcp](https://github.com/alefcastelo/archai-static-analyzer-mcp)  `innovation: 8`

**Static analysis tool for identifying vulnerabilities and security issues in codebases.**

**Key Features:**
- static analysis
- vulnerability detection
- code review integration
- security scanning

---

### 13. [alexandreroman/mcp-location](https://github.com/alexandreroman/mcp-location)  `innovation: 8`

**A MCP server providing user location data for integration into enterprise applications.**

**Key Features:**
- MCP server integration
- User location data retrieval
- Context-aware application enhancements
- Secure data handling protocols
- Scalable infrastructure design

---

### 14. [allthatjazzleo/mantrachain-mcp](https://github.com/allthatjazzleo/mantrachain-mcp)  `innovation: 8`

**Mantrachain MCP server for interacting with Cosmos SDK blockchain, enabling secure token management and protocol operations.**

**Key Features:**
- Send and receive tokens via MCP protocol
- Delegate/Stake tokens to validators
- Query account balances
- Get validator information
- Sign and broadcast transactions
- Manage mnemonics and network settings

---

### 15. [ananddtyagi/copy-paste-mcp](https://github.com/ananddtyagi/copy-paste-mcp)  `innovation: 8`

**A tool for extracting precise lines from text content, enabling focused data retrieval without altering original material.**

**Key Features:**
- Extract specific line ranges
- Preserve formatting and newlines
- Integrate with AI tools

---

### 16. [ashish0kumar/fzfm](https://github.com/ashish0kumar/fzfm)  `innovation: 8`

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

### 17. [beyond-network-ai/beyond-mcp-server](https://github.com/beyond-network-ai/beyond-mcp-server)  `innovation: 8`

**An extensible Model Context Protocol (MCP) server enabling secure, standardized access to social platform data for AI applications.**

**Key Features:**
- MCP compliant model context server
- Multi-platform support (Farcaster
- Twitter placeholder)
- Extensible architecture for new social platforms
- Secure handling of user profiles and wallet balances
- Integration with Claude Desktop for LLM interaction

---

### 18. [bingal/fastdomaincheck-mcp-server](https://github.com/bingal/fastdomaincheck-mcp-server)  `innovation: 8`

**A Model Context Protocol implementation for checking domain registration status in bulk.**

**Key Features:**
- Bulk domain registration status checking
- Dual verification (WHOIS & DNS)
- Input validation
- Error handling
- Performance optimization

---

### 19. [farukalpay/hormuz-tectonochemical-engine](https://github.com/farukalpay/hormuz-tectonochemical-engine)  `innovation: 8`

**A MCP-first tectonochemical forecasting engine for the Strait of Hormuz, integrating real-time data and reproducible modeling.**

**Key Features:**
- MCP-first tectonochemical forecasting engine
- Reproducible hydrocarbon-nitrogen-water modeling
- Real-time data ingestion from multiple sources
- TensorFlow LSTM with temporal attention mechanism
- Multi-stress index monitoring (shipping risk
- insurance
- grid stability)
- Optimization of process windows for feed gas and desalination processes
- Secure code execution and artifact publishing
- Integration with external monitoring APIs and dashboards

---

### 20. [freedanfan/mcp_server](https://github.com/freedanfan/mcp_server)  `innovation: 8`

**A Python-based MCP server enabling standardized context interaction between AI models and development environments.**

**Key Features:**
- Standardized context interaction via MCP
- JSON-RPC 2.0 support
- Server-sent events (SSE) for real-time updates
- Modular architecture for easy extension
- Asynchronous processing with FastAPI
- Client test implementation

---

### 21. [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent)  `innovation: 8`

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

### 22. [manimohans/farcaster-mcp](https://github.com/manimohans/farcaster-mcp)  `innovation: 8`

**A platform for interacting with the Farcaster network to fetch casts, channels, and user data using APIs.**

**Key Features:**
- Retrieve user casts by FID
- Get username casts
- Fetch channel casts
- View user profile details
- List channels with search filtering
- Show user following relationships
- Display user followers
- Analyze cast reactions

---

### 23. [manimohans/verge-news-mcp](https://github.com/manimohans/verge-news-mcp)  `innovation: 8`

**A server that integrates The Verge's RSS feed into Claude Desktop for news fetching and search.**

**Key Features:**
- Fetch daily or weekly tech news
- Search articles by keyword
- Get random news selections from the past week

---

### 24. [marcusbai/caiyun-weather-mcp](https://github.com/marcusbai/caiyun-weather-mcp)  `innovation: 8`

**A cloud-based weather API service providing real-time and forecasted weather data for various applications.**

**Key Features:**
- Real-time weather data (temperature
- humidity
- wind speed
- etc.)
- Minute-level precipitation forecasts
- Hourly and daily weather predictions
- Air quality trend analysis
- Detailed life index for lifestyle suggestions
- Weather alert notifications

---

### 25. [markqvist/nomadnet](https://github.com/markqvist/nomadnet)  `innovation: 8`

**Nomad Network: Communicate Freely**

**Key Features:**
- Encrypted messaging over packet-radio
- LoRa
- WiFi or anything else. Zero-configuration
- minimal-infrastructure mesh communication. Distributed and encrypted message store holds messages for offline users. Connectable nodes that can host pages and files. Node-side generated pages with PHP
- Python
- bash or others. Built-in text-based browser for interacting with contents on nodes. Easy to use and bandwidth efficient markup language for writing pages. Page caching in browser.

---

### 26. [nerfels/mind-map](https://github.com/nerfels/mind-map)  `innovation: 8`

**A model context protocol server for intelligent code and project analysis, leveraging AI-driven pattern recognition and memory caching.**

**Key Features:**
- Context-aware caching
- Brain-inspired learning patterns
- Code pattern detection
- Document and file analysis
- Multi-language AST parsing
- Automated CI/CD integration
- Memory optimization techniques

---

### 27. [nickbaumann98/everart-forge-mcp](https://github.com/nickbaumann98/everart-forge-mcp)  `innovation: 8`

**An advanced MCP server for Cline that integrates with EverArt's AI models to generate vector and raster images, supporting multiple styles and formats.**

**Key Features:**
- Vector graphics generation using Recraft-Vector model
- Raster image generation in PNG
- JPEG
- WebP formats
- Support for multiple AI models (5000
- 6000
- 7000
- 8000
- 9000)
- Custom output paths and filenames

---

### 28. [probelabs/probe](https://github.com/probelabs/probe)  `innovation: 8`

**Probe is an AST-aware context engine that provides LLMs with complete, syntactically coherent code blocks using zero-indexing structural search and MCP integration.**

**Key Features:**
- AST-aware structural search
- zero-indexing semantic retrieval
- MCP server integration
- token budget management
- session-based context deduplication
- boolean query language support
- complete code block extraction
- multi-language tree-sitter parsing

---

### 29. [rooking-oss/zipcode-search-mcp](https://github.com/rooking-oss/zipcode-search-mcp)  `innovation: 8`

**A Python-based MCP server that provides Japanese postal code to address lookup functionality using the Model Context Protocol.**

**Key Features:**
- Search Japanese addresses by 7-digit postal codes
- Integrate with AI assistants and other MCP clients
- Fast and lightweight implementation

---

### 30. [rossshannon/weekly-weather-mcp](https://github.com/rossshannon/weekly-weather-mcp)  `innovation: 8`

**A weather forecasting server that provides detailed forecasts and integrates with the Model Context Protocol.**

**Key Features:**
- Global weather forecasts with detailed hourly and daily data
- Integration with MCP (Model Context Protocol) for seamless API usage
- Support for multiple time zones and location inputs
- Secure API key management via environment variables
- Automated deployment and CI/CD support
- Comprehensive documentation and community resources

---

### 31. [sammcj/mcp-data-extractor](https://github.com/sammcj/mcp-data-extractor)  `innovation: 8`

**A model context protocol server that extracts embedded data from TypeScript/JavaScript source code into structured JSON configuration files.**

**Key Features:**
- Data Extraction
- SVG Extraction
- Configuration Replacement
- Custom AST Traversal
- Integration with MCP Client

---

### 32. [sinedied/grumpydev-mcp](https://github.com/sinedied/grumpydev-mcp)  `innovation: 8`

**A tool for grumpy senior developers to review and critique code with MCP, focusing on context, style, and quality.**

**Key Features:**
- Code review with sarcastic feedback
- Model configuration suggestions
- Contextual guidance for AI model integration
- Automated security checks and vulnerability detection

---

### 33. [spences10/mcp-jinaai-reader](https://github.com/spences10/mcp-jinaai-reader)  `innovation: 8`

**A tool for parsing websites using the Jina.ai Reader API to extract structured web content.**

**Key Features:**
- Advanced web content extraction
- Fast and efficient content retrieval
- Complete text extraction with structure preservation
- Clean format optimized for LLMs

---

### 34. [spences10/mcp-jinaai-search](https://github.com/spences10/mcp-jinaai-search)  `innovation: 8`

**A unified platform for integrating Jina.ai Search API with LLMs to deliver clean, LLM-friendly web content.**

**Key Features:**
- Advanced web search via Jina.ai
- Fast and efficient content retrieval
- Clean text extraction preserving structure
- Content optimized for large language models
- Support for various content types
- Localization support
- Token budget control

---

### 35. [spences10/mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)  `innovation: 8`

**MCP server for Svelte documentation with caching and search.**

**Key Features:**
- Svelte 5 definitions (runes)
- TypeScript-first documentation
- Integrated caching & fast searches
- Event handling & component communication
- Migration guidance from Svelte 4 to 5

---

### 36. [t3ta/sql-mcp-server](https://github.com/t3ta/sql-mcp-server)  `innovation: 8`

**A secure TypeScript implementation of a Model Context Protocol server enabling language models to query PostgreSQL databases via SSH tunnels.**

**Key Features:**
- SSH bastion tunnel support
- PostgreSQL read-only query engine
- STDIO-based MCP protocol transport
- Environment variable configuration
- Jest testing framework
- Clear commit history and documentation

---

### 37. [the-focus-ai/mastodon-mcp](https://github.com/the-focus-ai/mastodon-mcp)  `innovation: 8`

**A tool for interacting with Mastodon using model context protocol, enabling secure and customizable toot creation.**

**Key Features:**
- Create toots with customizable visibility
- Upload and attach media files
- Add alt text/descriptions
- Schedule toots for future times

---

### 38. [titzer/wizard-engine](https://github.com/titzer/wizard-engine)  `innovation: 8`

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

## Context Compression & Token Optimization

### 39. [kayba-ai/agentic-context-engine](https://github.com/kayba-ai/agentic-context-engine)  `innovation: 10`

**Agentic Context Engine (ACE)**

**Key Features:**
- Autonomous success/failure pattern extraction
- 49% browser automation token reduction
- dynamic "Skillbook" system prompt evolution
- multi-framework plug-and-play support.

---

### 40. [Apofenic/globalmcp](https://github.com/Apofenic/globalmcp)  `innovation: 9`

**A modular MCP server that compresses context and intelligently routes prompts to appropriate models for efficient long-session development.**

**Key Features:**
- Context Compression using DCT
- Smart Routing based on complexity analysis
- Model chaining with multiple compression techniques
- Integration with GitHub Copilot and external tools
- Fallback mechanisms for unavailability

---

### 41. [Lucenor/mnesis](https://github.com/Lucenor/mnesis)  `innovation: 9`

**A Python library designed to address context window degradation in long-running LLM agents by offloading memory management to a deterministic engine.**

**Key Features:**
- Lossless Context Management (LCM) architecture
- Active Context handling with deterministic memory engine
- Context trigger and summarization without model intervention
- Three-level compaction for efficient token budget usage
- Support for parallel LLMMap and AgenticMap operators

---

### 42. [cdgaete/token-scope-mcp](https://github.com/cdgaete/token-scope-mcp)  `innovation: 9`

**TokenScope provides intelligent directory structure analysis and token-aware file content exploration for LLMs like Claude, helping developers understand codebases efficiently.**

**Key Features:**
- Token-Aware Directory Exploration
- Automatic Summarization for Large Directories
- Respect for Token Limits to Maximize Information
- Smart Filtering with Default Patterns and .gitignore Support
- Accurate Directory Statistics for Large Repositories

---

### 43. [haasonsaas/deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)  `innovation: 9`

**A platform that integrates Claude Code with Google Gemini AI to enable advanced, context-aware code analysis and reasoning across distributed systems.**

**Key Features:**
- Deep code analysis using multi-model workflow
- Distributed system debugging with 1M token context window
- AI-to-AI conversational reasoning for iterative problem-solving
- Cross-system impact analysis across services
- Hypothesis testing and validation with evidence-based results

---

### 44. [ogoldberg/gemini-context-mcp-server](https://github.com/ogoldberg/gemini-context-mcp-server)  `innovation: 9`

**A MCP server leveraging Gemini's large context window to enhance AI capabilities.**

**Key Features:**
- Context management up to 2M tokens
- Session-based conversational state maintenance
- Smart context tracking and cleanup
- Automatic context expiration
- Semantic search and metadata retrieval

---

### 45. [66julienmartin/mcp-server-qwen_max](https://github.com/66julienmartin/mcp-server-qwen_max)  `innovation: 8`

**A server implementation for deploying and managing the Qwen Max language model via MCP protocol.**

**Key Features:**
- MCP server integration
- Model selection (Qwen-Max
- Qwen-Plus
- Qwen-Turbo)
- Token context window management
- API authentication support

---

### 46. [ai-1st/deepview-mcp](https://github.com/ai-1st/deepview-mcp)  `innovation: 8`

**DeepView MCP enables IDEs to analyze large codebases using Gemini's context window.**

**Key Features:**
- Load entire codebase from a single text file
- Query with Gemini's extensive context window
- Integrate with IDEs like Cursor and Windsurf
- Support for multiple Gemini models

---

### 47. [portofcontext/pctx](https://github.com/portofcontext/pctx)  `innovation: 8`

**pctx Context Porter**

**Key Features:**
- 58% token reduction
- 56% cost efficiency
- isolated Deno sandboxing
- unified multi-server authentication.

---

### 48. [voicetreelab/lazy-mcp](https://github.com/voicetreelab/lazy-mcp)  `innovation: 8`

**Lazy-MCP is a proxy server that minimizes context window bloat by implementing a hierarchical, on-demand discovery system for Model Context Protocol (MCP) tools.**

**Key Features:**
- Hierarchical tool discovery
- Lazy-loading tool activation
- Context window token optimization
- Proxy-based tool execution
- Automatic structure generation
- Custom permission hooks
- Claude Code integration
- Support for stdio and SSE transports

---

## RAG & Retrieval Systems

### 49. [upstash/context7](https://github.com/upstash/context7)  `innovation: 10`

**Context7: Doc RAG**

**Key Features:**
- Server-side reranking (65% token saving)
- automated SKILL.md generation
- llms.txt standard support
- dual stdio/HTTP transport.

---

### 50. [stagsz/unconventional-thinking](https://github.com/stagsz/unconventional-thinking)  `innovation: 9.7`

**A context-efficient MCP server for generating and tracking unconventional solutions using advanced note-taking.**

**Key Features:**
- Key Context-Saving Features
- Resource-based Thought Storage
- Metadata-First API
- Persistent File-Based Storage
- Server-Side Filtering
- Context-Efficient Thought Retrieval

---

### 51. [BrokkAi/brokk?tab=readme-ov-file](https://github.com/BrokkAi/brokk?tab=readme-ov-file)  `innovation: 9`

**Brokk is an AI-native code platform focusing on managing context at the fragment level, enabling LLMs to operate effectively within massive codebases.**

**Key Features:**
- Fragment-level context management
- Agentic context collection and pruning (ContextAgent/SearchAgent)
- Persistent and branchable history
- Dependency decompilation to source
- Structured task execution (Lutz Mode)
- Brokk Power Ranking (BPR) for model fitness assessment.

---

### 52. [Muvon/octocode](https://github.com/Muvon/octocode)  `innovation: 9`

**Octocode is a local-first semantic code indexer and graph builder that facilitates deep code understanding and intelligent assistance via a knowledge graph and MCP integration.**

**Key Features:**
- Semantic Code Search
- Knowledge Graph (GraphRAG)
- Multi-Language Support
- AI-Powered Git Workflow Integration
- Local/Cloud Embedding Model Support
- Model Context Protocol (MCP) Server
- LanceDB Optimization
- Respects .gitignore for security.

---

### 53. [alex-feel/mcp-context-server](https://github.com/alex-feel/mcp-context-server)  `innovation: 9`

**A high-performance Model Context Protocol server enabling persistent multimodal context storage for LLM agents.**

**Key Features:**
- Multimodal Context Storage
- Thread-Based Scoping
- Flexible Metadata Filtering
- Date Range Filtering
- Tag-Based Organization
- Summary Generation
- Full-Text Search
- Semantic Search
- Hybrid Search
- Cross-Encoder Reranking

---

### 54. [augmented-nature/pubchem-mcp-server](https://github.com/augmented-nature/pubchem-mcp-server)  `innovation: 9`

**A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database.**

**Key Features:**
- Comprehensive chemical compound search
- Extensive molecular property analysis
- Bioassay data retrieval
- Structural similarity and similarity search
- Safety and toxicity information
- Integration with external databases (ChEMBL
- DrugBank
- etc.)
- Batch processing for multiple compounds
- Comprehensive error handling and validation

---

### 55. [brysontang/deltatask](https://github.com/brysontang/deltatask)  `innovation: 9`

**A task management application with Model Context Protocol integration, SQLite storage, and Obsidian visualization.**

**Key Features:**
- Task prioritization engine
- Smart task decomposition
- Tagging system for categorization
- Local SQLite database storage
- Obsidian bidirectional sync
- MCP server for structured data management

---

### 56. [cyreslab-ai/exploitdb-mcp-server](https://github.com/cyreslab-ai/exploitdb-mcp-server)  `innovation: 9`

**A platform-powered AI assistant for cybersecurity research, enabling secure and efficient exploitation data analysis.**

**Key Features:**
- AI-driven exploit search and details retrieval
- Real-time statistics and trend analysis
- Advanced filtering by platform
- type
- CVE
- date
- etc.
- Integration with Claude and other MCP-compatible assistants
- Automated database updates and maintenance

---

### 57. [ergodiclabs/twotruthsandatwist](https://github.com/ergodiclabs/twotruthsandatwist)  `innovation: 9`

**A pioneering Model Context Protocol game that leverages AI to deliver interactive trivia experiences.**

**Key Features:**
- Model Context Protocol (MCP) integration
- AI-generated trivia rounds
- Interactive gameplay with twist reveals
- Customizable game settings
- Cross-platform compatibility

---

### 58. [getzep/graphiti](https://github.com/getzep/graphiti)  `innovation: 9`

**Graphiti enables the creation and management of temporal context graphs for AI agents, allowing them to maintain accurate, up-to-date knowledge over time.**

**Key Features:**
- Temporal fact management with validity windows
- Episodes and provenance tracking
- Custom entity and edge types via Pydantic models
- Hybrid retrieval combining semantic
- keyword
- and graph-based search
- Real-time incremental updates without full recomputation

---

### 59. [getzep/zep](https://github.com/getzep/zep)  `innovation: 9`

**Zep is an end-to-end context engineering platform designed to assemble comprehensive, relationship-aware context for AI agents with low latency.**

**Key Features:**
- End-to-end context assembly
- Temporal knowledge graph (Graphiti)
- Relationship-aware retrieval
- Sub-200ms latency context delivery
- SDKs for Python/TypeScript/Go
- Integration examples with LangChain/LlamaIndex/AutoGen
- SOC2 Type 2 / HIPAA compliance (Zep Cloud).

---

### 60. [jonnoc/coderag](https://github.com/jonnoc/coderag)  `innovation: 9`

**Advanced graph-based code analysis platform for AI-assisted software development.**

**Key Features:**
- Automated Code Analysis
- Remote Repository Analysis
- Intelligent Language Detection
- Quality Assessment
- Semantic Code Search
- Multi-Project Management
- Architectural Analysis
- Pattern Detection
- Documentation and Insights

---

### 61. [jurasofish/mcpunk](https://github.com/jurasofish/mcpunk)  `innovation: 9`

**MCPunk enables context-aware code exploration and intelligent search within GitHub repositories.**

**Key Features:**
- File chunking (functions
- classes
- markdown sections)
- LLM-powered search across file chunks
- Contextual insights for code review and analysis
- Integration with GitHub and CI/CD pipelines
- Security-focused code inspection and vulnerability detection

---

### 62. [mizchi/lsmcp](https://github.com/mizchi/lsmcp)  `innovation: 9`

**A unified MCP server enabling advanced code manipulation and analysis across multiple programming languages via Language Server Protocol integration.**

**Key Features:**
- Multi-language support for TypeScript
- JavaScript
- Rust
- F#
- Go
- Haskell
- OCaml
- AI-optimized semantic code analysis with Claude integration
- Comprehensive code search and symbol inspection across files and workspaces
- Detailed diagnostics

---

### 63. [spences10/mcp-tavily-search](https://github.com/spences10/mcp-tavily-search)  `innovation: 9`

**A model context protocol tool for integrating Tavily API into LLM search workflows.**

**Key Features:**
- Advanced web search using Tavily API
- AI-generated summaries and direct question answering
- Context generation for RAG applications
- Customizable search depth
- parameters
- and response formats
- Support for domain filtering and source inclusion/exclusion

---

### 64. [sreedeep-ss/docret-mcp-server](https://github.com/sreedeep-ss/docret-mcp-server)  `innovation: 9`

**A Model Context Protocol server enabling AI assistants to access up-to-date documentation for Python libraries.**

**Key Features:**
- Dynamic documentation retrieval from official sources
- Asynchronous web searches using SERPER API
- HTML parsing with BeautifulSoup
- Extensible configuration for new libraries
- Integration with AI assistants like Claude and custom models
- API endpoints for external integrations

---

### 65. [stass/exif-mcp](https://github.com/stass/exif-mcp)  `innovation: 9`

**A model context protocol server for extracting and managing image metadata offline.**

**Key Features:**
- EXIF extraction
- GPS coordinate retrieval
- XMP and ICC data parsing
- IPTC metadata access
- JFIF and IHDR support
- Image orientation and rotation detection
- Thumbnail generation
- Integration with Claude Desktop for advanced analysis

---

### 66. [super-i-tech/mcp_plexus](https://github.com/super-i-tech/mcp_plexus)  `innovation: 9`

**MCP Plexus enables secure, multi-tenant deployment of MCP applications with isolated environments and persistent user authentication.**

**Key Features:**
- Multi-tenant architecture with isolated environments
- Secure external service integration via OAuth 2.1
- Persistent user authentication and token storage
- API key management for tools and external services
- Standardized decorators for defining MCP components
- Extensible design for custom authentication providers

---

### 67. [zxfgds/mcp-code-indexer](https://github.com/zxfgds/mcp-code-indexer)  `innovation: 9`

**An AI-powered code indexing tool for intelligent code retrieval and analysis.**

**Key Features:**
- Intelligent code retrieval
- Semantic understanding of code
- Cross-language support
- Code structure analysis
- Code quality evaluation
- Documentation extraction
- Similar code detection
- Dependency analysis
- Contextual token management

---

### 68. [dasein108/mcp-cw-graph](https://github.com/dasein108/mcp-cw-graph)  `innovation: 8.5`

**MCP Server for interacting with the CW-Social smart contract on Cosmos-based blockchains, enabling creation, management, and querying of cyberlinks.**

**Key Features:**
- Create
- read
- update
- and delete cyberlinks
- Batch operations for efficient processing
- Rich query capabilities with filtering and pagination
- Transaction Management with real-time monitoring
- Semantic embedding generation via Hugging Face transformers
- Cosine similarity calculations for semantic matching
- Flexible ID system with formatted IDs (fids) and global IDs (gids)

---

### 69. [L-A-Marchetti/Vec](https://github.com/L-A-Marchetti/Vec)  `innovation: 8`

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

### 70. [Symbitic/awesome-babylonjs](https://github.com/Symbitic/awesome-babylonjs)  `innovation: 8`

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

### 71. [Tanq16/local-content-share?tab=readme-ov-file](https://github.com/Tanq16/local-content-share?tab=readme-ov-file)  `innovation: 8`

**Self-hosted app with browser frontend that enables sharing and storing text snippets and files.**

**Key Features:**
- Text Snippet Storage & Sharing
- File Upload/Download Support
- Customizable TTL/Expiration Settings
- Built-in Notepad/Markdown Editing
- Multi-file Drag-n-Drop Support
- Local Network Accessibility (no internet required).

---

### 72. [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)  `innovation: 8`

**A specialized implementation of Vision-based Retrieval-Augmented Generation (RAG) that uses PageIndex to process and retrieve visual document context for multimodal LLMs.**

**Key Features:**
- Vision-based document indexing
- layout-aware chunking
- multimodal context retrieval
- PDF-to-image pipeline for RAG
- spatial relationship preservation
- VLM context injection
- multimodal vector search
- automated document visualization.

---

### 73. [alizdavoodi/mcpdocsearch](https://github.com/alizdavoodi/mcpdocsearch)  `innovation: 8`

**A toolset for crawling documentation sites, generating Markdown, and enabling searchable indexing via MCP protocol.**

**Key Features:**
- Web crawler (crawler_cli) with configurable depth and URL patterns
- Markdown document generator with HTML cleaning options
- MCP server for semantic search and vector embedding generation
- Integration with Cursor and other MCP clients via stdio transport
- Cache-based performance optimization to speed up subsequent runs

---

### 74. [alxspiker/ai-meta-mcp-server](https://github.com/alxspiker/ai-meta-mcp-server)  `innovation: 8`

**A dynamic MCP server enabling AI to create and execute custom tools via a meta-function architecture.**

**Key Features:**
- Dynamic tool creation
- Multiple runtime environments (JavaScript
- Python
- Shell)
- Sandboxed execution
- Persistent storage of tools
- Human approval workflow

---

### 75. [alxspiker/windows-command-line-mcp-server](https://github.com/alxspiker/windows-command-line-mcp-server)  `innovation: 8`

**A secure Windows Command Line MCP Server enabling safe AI model interaction with Windows CLI.**

**Key Features:**
- Secure bridge between AI models and Windows CLI
- Safe command execution with predefined allowlists
- Project creation for React
- Node.js
- Python
- System information retrieval (info
- network
- processes)
- Process management and service interaction
- Integration with development tools and IDEs

---

### 76. [amanasmuei/mcp-server-malaysia-prayer-time](https://github.com/amanasmuei/mcp-server-malaysia-prayer-time)  `innovation: 8`

**A Model Context Protocol server providing accurate Islamic prayer times for Malaysia via real-time API integration.**

**Key Features:**
- Location-based prayer time retrieval
- Coordinate-based prayer time lookup
- Zone code access (JAKIM)
- Integration with Claude Desktop
- API-driven schedule generation

---

### 77. [arborist-ai/claudehopper](https://github.com/arborist-ai/claudehopper)  `innovation: 8`

**A macOS application that manages Model Context Protocol (MCP) servers for Claude Desktop, enabling AI-driven interaction with construction documents.**

**Key Features:**
- MCP server management
- AI-powered document analysis
- Visual and vector-based search
- Secure local processing
- Integration with Claude Desktop

---

### 78. [atilioa/tesouro-direto-mcp](https://github.com/atilioa/tesouro-direto-mcp)  `innovation: 8`

**A MCP server enabling natural language queries for Brazilian treasury bond data.**

**Key Features:**
- Natural language query support
- Smart caching mechanism
- API integration with Tesouro Direto
- Market data retrieval
- Bond details and search functionality

---

### 79. [baidu/mochow-mcp-server-python](https://github.com/baidu/mochow-mcp-server-python)  `innovation: 8`

**A context protocol server enabling integration with Mochow and supporting advanced AI model interactions.**

**Key Features:**
- MCP Server for accessing Baidu Cloud Vector Database
- Supports multiple AI models via Context Protocol
- Integration with Claude Desktop and Cursor
- Secure API key management
- Database operations including list
- describe
- create
- delete
- etc.

---

### 80. [bankless/onchain-mcp](https://github.com/bankless/onchain-mcp)  `innovation: 8`

**Borg provides a secure, isolated environment for interacting with blockchain data via the Bankless API.**

**Key Features:**
- Secure API integration with Bankless
- Support for contract operations (read
- write
- events)
- Proxy contract management
- Event topic generation
- Transaction history retrieval
- AI model integration via MCP

---

### 81. [bemusic/bemuse](https://github.com/bemusic/bemuse)  `innovation: 8`

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

### 82. [bielacki/igdb-mcp-server](https://github.com/bielacki/igdb-mcp-server)  `innovation: 8`

**Borg intelligence database server enabling seamless access to IGDB API for AI assistants.**

**Key Features:**
- IGDB API access via Model Context Protocol
- Game metadata retrieval (titles
- descriptions
- ratings)
- Trending and popular game discovery
- Custom query support with flexible search syntax
- Integration with AI assistants for intelligent queries

---

### 83. [https://github.com/campfirein](https://github.com/campfirein)  `innovation: 8`

**This GitHub profile is focused on developing and leveraging tools related to AI coding agents, particularly emphasizing memory layers and context management.**

**Key Features:**
- Open-source memory layer for coding agents
- Benchmark suite for context retrieval evaluation
- Compatibility with multiple coding agents and IDEs
- Model Context Protocol (MCP) implementation
- Autonomous program improvement capabilities.

---

### 84. [clawsoftware/clawPDF](https://github.com/clawsoftware/clawPDF)  `innovation: 8`

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

### 85. [crazyrabbitltc/mcp-morpho-server](https://github.com/crazyrabbitltc/mcp-morpho-server)  `innovation: 8`

**A morpho server for the model context protocol enabling interaction with Morpho's GraphQL API.**

**Key Features:**
- morpho api integration
- market data retrieval
- vault management
- historical apy data
- schema validation

---

### 86. [cskwork/keyword-rag-mcp](https://github.com/cskwork/keyword-rag-mcp)  `innovation: 8`

**BM25 기반 문서 검색을 위한 MCP 서버로, 토스 결제 연동 MCP 프로젝트를 활용하여 마크다운 문서를 검색하고 지식 검색을 제공합니다.**

**Key Features:**
- BM25 알고리즘 기반 문서 검색
- 토스 결제 연동 지원
- Claude Desktop 연동
- 자동 설정 및 구성 파일 생성
- 문서 및 MDX 파일 관리
- 명확한 검색 및 컨텍스트 기반 결과 제공

---

### 87. [dazeb/markdown-downloader](https://github.com/dazeb/markdown-downloader)  `innovation: 8`

**A MCP server that converts webpages into markdown instantly, enabling seamless integration with AI development environments.**

**Key Features:**
- Webpage to markdown conversion
- Configurable download directories
- Automatic filename sanitization and date-stamped filenames
- Persistent configuration storage
- Integration with AI development tools like Jina.ai

---

### 88. [dcspark/mcp-server-helius](https://github.com/dcspark/mcp-server-helius)  `innovation: 8`

**A model context protocol server enabling Claude to interact with Solana blockchain data.**

**Key Features:**
- Basic blockchain operations
- Wallet balance checks
- Block height retrieval
- Transaction and account information
- NFT and digital asset details
- Program account management

---

### 89. [dedeveloper23/codebase-mcp](https://github.com/dedeveloper23/codebase-mcp)  `innovation: 8`

**Model Context Protocol implementation for retrieving codebases using RepoMix.**

**Key Features:**
- Codebase retrieval in multiple formats
- Remote repository support
- Customizable analysis options
- Integration with AI assistants
- File saving and preservation

---

### 90. [devhub/devhub-cms-mcp](https://github.com/devhub/devhub-cms-mcp)  `innovation: 8`

**Integration of Claude Desktop with DevHub CMS via Model Context Protocol for LLM-based content management.**

**Key Features:**
- Model Context Protocol integration
- LLM-powered content management
- Business and location data retrieval
- Hours of operation management
- Nearest location lookup

---

### 91. [digitarald/chatarald](https://github.com/digitarald/chatarald)  `innovation: 8`

**A test-driven, library-first ChatGPT-style web app in TypeScript. Built as a pnpm monorepo with a reusable LLM client library, provider-agnostic adapters, and a minimal React UI.**

**Key Features:**
- Provider-agnostic LLM client (OpenRouter via OpenAI SDK)
- Token counting (estimate + actual usage)
- Local conversation storage (idb-keyval)
- TDD workflow using Vitest and MSW for HTTP mocking
- A minimal React UI layer.

---

### 92. [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server)  `innovation: 8`

**A model context protocol server for interacting with Quran.com API to search verses, translations, and tafsirs.**

**Key Features:**
- Quran verse search
- Translation integration
- Tafsir information retrieval
- API v4.0 integration
- Docker-based production deployment

---

### 93. [dmontgomery40/mcp-local-server](https://github.com/dmontgomery40/mcp-local-server)  `innovation: 8`

**A local server for integrating BirdNET-Pi with MCP, enabling secure and isolated context management for AI-driven applications.**

**Key Features:**
- MCP Server Integration
- BirdNET-Pi Local Detection
- Data Retrieval & Statistics
- Audio Recording Access
- Activity Pattern Reporting
- Secure Context Isolation
- Customizable Configuration
- Docker-based Deployment

---

### 94. [excoriate/mcp-terragrunt-docs](https://github.com/excoriate/mcp-terragrunt-docs)  `innovation: 8`

**A Deno/TypeScript MCP server that provides contextual information and documentation for Terragrunt, enhancing AI assistant accuracy.**

**Key Features:**
- MCP Server Provisioning
- Dependency Management
- AI Integration for Documentation
- Issue Tracking & Monitoring
- Security & Code Quality Tools

---

### 95. [fkesheh/code-context-mcp](https://github.com/fkesheh/code-context-mcp)  `innovation: 8`

**A model context protocol server that enables semantic code search from local Git repositories, enhancing development workflows with contextual insights.**

**Key Features:**
- Local git repository processing
- Semantic code chunk embedding generation
- Context-aware search using Ollama
- Integration with Claude Desktop for AI-assisted code review

---

### 96. [grovesjosephn/pokemcp](https://github.com/grovesjosephn/pokemcp)  `innovation: 8`

**A monorepo-based system for managing and processing Pokémon data via Model Context Protocol (MCP) server and SQLite database.**

**Key Features:**
- MCP server for standardized Pokemon data access
- Data ingestion service using PokeAPI
- SQLite database for persistent storage
- Comprehensive search and filtering capabilities
- Integration with Claude Desktop for GUI testing

---

### 97. [hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs)  `innovation: 8`

**An MCP server implementation that enables AI assistants to retrieve and process documentation via vector search, enhancing contextual responses.**

**Key Features:**
- Vector-based documentation search
- Semantic search capabilities
- Automated documentation processing
- Real-time context augmentation for LLMs

---

### 98. [hardik-id/azure-resource-graph-mcp-server](https://github.com/hardik-id/azure-resource-graph-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling access to Azure Resource Graph queries across subscriptions.**

**Key Features:**
- Azure Resource Graph query support
- Resource ID
- name
- type
- and location retrieval
- Custom Resource Graph queries
- Integration with Azure CLI and Azure DevOps
- Support for secure authentication via DefaultAzureCredential

---

### 99. [henkdz/selfhosted-supabase-mcp](https://github.com/henkdz/selfhosted-supabase-mcp)  `innovation: 8`

**A self-hosted Supabase MCP server enabling secure, isolated database interactions for developers.**

**Key Features:**
- Database schema introspection and management
- Migration tracking and application of changes
- Authentication and user management
- Integration with Supabase Storage
- Type definition generation
- Security auditing and vulnerability detection

---

### 100. [hloiseaufcms/mcp-gopls](https://github.com/hloiseaufcms/mcp-gopls)  `innovation: 8`

**mcp-gopls enables AI assistants to leverage Go's LSP for advanced navigation, diagnostics, testing, and code analysis.**

**Key Features:**
- Go-to-definition
- References
- Hover
- Completion
- Code actions
- Coverage analysis
- Go mod tidy
- Go vulncheck
- Workspace and file context
- Resource navigation (overview

---

### 101. [icraft2170/youtube-data-mcp-server](https://github.com/icraft2170/youtube-data-mcp-server)  `innovation: 8`

**A cloud-based YouTube Data API server enabling AI models to interact with YouTube content securely and efficiently.**

**Key Features:**
- YouTube video information retrieval
- Video search by keywords
- Transcript/caption management
- Channel statistics analysis
- Trend and comparison analytics
- Popular content discovery
- Automated data processing and insights

---

### 102. [insthync/awesome-unity3d](https://github.com/insthync/awesome-unity3d)  `innovation: 8`

**A categorized collection of awesome opensource unity3d repos · GitHub**

**Key Features:**
- The repository showcases a wide range of essential Unity resources
- covering areas like 2D/3D bones
- AI/Animation solutions (like IK/Ragdolls)
- physics simulation
- rendering effects
- and crucial tooling for game development workflows.

---

### 103. [jaldekoa/mcp-fredapi](https://github.com/jaldekoa/mcp-fredapi)  `innovation: 8`

**Integration of FRED API with Model Context Protocol for economic data retrieval.**

**Key Features:**
- FRED API integration
- Model Context Protocol support
- Economic data access

---

### 104. [janwilmake/uithub-mcp](https://github.com/janwilmake/uithub-mcp)  `innovation: 8`

**A MCP server for interacting with GitHub to analyze and retrieve code from repositories.**

**Key Features:**
- code retrieval
- smart filtering
- integration with Claude Desktop
- security features

---

### 105. [jbdamask/mcp-nih-reporter](https://github.com/jbdamask/mcp-nih-reporter)  `innovation: 8`

**A Model Context Protocol server enabling conversational interaction with NIH RePORTER API for research data retrieval.**

**Key Features:**
- Search NIH-funded projects by fiscal year
- principal investigator
- organization
- funding details
- and COVID-19 response status
- Search publications linked to NIH projects
- Combined search for both projects and publications
- Detailed project and publication information including abstracts
- Configurable result limits and filters
- Support for Python 3.12+ with UV package manager

---

### 106. [jean-technologies/mcp-writer-substack](https://github.com/jean-technologies/mcp-writer-substack)  `innovation: 8`

**A tool that bridges Substack and Medium writing to Claude, enabling semantic search and personalized assistance with published content.**

**Key Features:**
- Retrieves and caches blog posts from Substack and Medium
- Uses embeddings for semantic search across writings
- Generates individual essay resources for Claude
- Allows query-based retrieval of relevant essays
- Supports selective content refresh and caching

---

### 107. [jeong-sik/kakao-api-mcp-server](https://github.com/jeong-sik/kakao-api-mcp-server)  `innovation: 8`

**This project enables AI models to leverage Kakao Map and Daum APIs for location-based services, integrating geospatial data retrieval, route planning, and web search functionalities.**

**Key Features:**
- Kakao Map API integration for location search
- Daum API for web document and webpage searches
- Geospatial data handling (coordinates to addresses
- route finding)
- Traffic and transportation information retrieval
- Image and blog content extraction from web sources

---

### 108. [jjlabsio/korea-stock-mcp](https://github.com/jjlabsio/korea-stock-mcp)  `innovation: 8`

**A MCP Server for Korean stock analysis that integrates official APIs from DART and KRX to provide AI-powered insights on stock data.**

**Key Features:**
- Disclosure search by company and date
- Parsing of large XML disclosure documents (e.g.
- annual reports)
- AI-driven financial statement analysis using XBRL
- Real-time stock data retrieval (KRX
- KOSPI
- KONEX)
- Integration with Claude Desktop for advanced analysis

---

### 109. [jkingsman/qanon-mcp-server](https://github.com/jkingsman/qanon-mcp-server)  `innovation: 8`

**A sociological research tool for analyzing QAnon posts using the Model Context Protocol.**

**Key Features:**
- Model Context Protocol (MCP) server integration
- Post retrieval and analysis capabilities
- Data filtering and querying tools
- Timeline generation and visualization
- Word cloud and frequency analysis
- Customizable search parameters

---

### 110. [jlfwong/food-data-central-mcp-server](https://github.com/jlfwong/food-data-central-mcp-server)  `innovation: 8`

**A server-based platform for integrating and managing access to the USDA FoodData Central API, enabling food data retrieval and analysis.**

**Key Features:**
- Search for foods in USDA FoodData Central database
- Access food nutrient information
- Support multiple data types (Foundation
- SR Legacy
- Survey
- Branded)
- Paginated results with customizable page size and sorting
- Integration with Claude Desktop for AI-powered food search

---

### 111. [joesecurity/joesandboxmcp](https://github.com/joesecurity/joesandboxmcp)  `innovation: 8`

**A cloud-based MCP server for analyzing and extracting threat intelligence from sandboxed executions.**

**Key Features:**
- IOC extraction
- Signature detection
- Process tree visualization
- Unpacked binary analysis
- PCAP download
- Behavioral detections
- Memory dump retrieval

---

### 112. [jon-vii/canvas-student-mcp](https://github.com/jon-vii/canvas-student-mcp)  `innovation: 8`

**Integration of Canvas Student MCP with LLM clients via the MCP standard to enable intelligent interactions within a LMS.**

**Key Features:**
- Canvas Student MCP integration for LLM interaction
- PDF content preview and access
- PDF text extraction support
- Course assignment management
- Quiz information retrieval
- To-do list and assignment tracking

---

### 113. [jonathanfischer97/juliadoc-mcp](https://github.com/jonathanfischer97/juliadoc-mcp)  `innovation: 8`

**A MCP server designed to efficiently serve Julia documentation and source code, enabling seamless access for developers.**

**Key Features:**
- Contextual documentation retrieval
- Source code access
- Integration with Julia projects
- Error handling
- Development environment support

---

### 114. [jtucker/mcp-untappd-server](https://github.com/jtucker/mcp-untappd-server)  `innovation: 8`

**A Node.js server that interacts with the Untappd API to retrieve and display beer information.**

**Key Features:**
- untappd model context protocol server
- beer information retrieval
- API integration
- search functionality

---

### 115. [jumasheff/mcp-ragdoc-fork](https://github.com/jumasheff/mcp-ragdoc-fork)  `innovation: 8`

**A tool for retrieving and processing documentation to enhance AI responses with relevant context.**

**Key Features:**
- Vector-based documentation search
- Semantic search capabilities
- Automated documentation processing
- Real-time context augmentation

---

### 116. [kazuph/mcp-docs-rag](https://github.com/kazuph/mcp-docs-rag)  `innovation: 8`

**A Borg-based RAG server for local document retrieval and AI-driven document querying.**

**Key Features:**
- Local document storage via Git repositories or plain text files
- RAG-based AI querying with context from local documents
- Integration with Google Gemini API for enhanced search capabilities
- Automatic indexing and retrieval using llama-index.ts
- Support for adding custom document names and sparse checkout
- Development and deployment tools including Codespaces and CI/CD integration

---

### 117. [kiseki-technologies/kiseki-labs-readwise-mcp](https://github.com/kiseki-technologies/kiseki-labs-readwise-mcp)  `innovation: 8`

**A lightweight MCP server enabling seamless integration with Readwise API for language models.**

**Key Features:**
- MCP Server Integration
- Readwise API Access
- Language Model Interaction
- Highlight Retrieval
- Custom Commands via CLI

---

### 118. [kkjdaniel/bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)  `innovation: 8`

**Borg MCP enables secure, isolated access to BoardGameGeek data via the Model Context Protocol, supporting advanced filtering and retrieval of board game information.**

**Key Features:**
- Secure API integration with BoardGameGeek
- Real-time board game data retrieval
- User collection and profile management
- Filtering and searching capabilities
- Integration with AI tools for contextual insights

---

### 119. [koki-develop/esa-mcp-server.git](https://github.com/koki-develop/esa-mcp-server.git)  `innovation: 8`

**A Model Context Protocol (MCP) server for esa.io, enabling secure and isolated model context management.**

**Key Features:**
- Model Context Protocol (MCP) server integration
- Secure post and comment management
- Tag and post retrieval capabilities
- Read-only mode for non-modifying operations
- Support for nested inclusion of comments and tags

---

### 120. [kujenga/zotero-mcp](https://github.com/kujenga/zotero-mcp)  `innovation: 8`

**A Python-based server implementing the Model Context Protocol (MCP) for Zotero, enabling AI assistants to access and interact with Zotero libraries.**

**Key Features:**
- Zotero search items via text queries
- Metadata retrieval for specific Zotero items
- Full-text content retrieval for PDFs
- Integration with MCP clients and Inspector
- Local API access (requires Zotero Beta Build)
- Web API integration (requires Zotero Library ID)

---

### 121. [kwp-lab/mcp-fetch](https://github.com/kwp-lab/mcp-fetch)  `innovation: 8`

**A server-based solution for securely fetching web content with custom HTTP proxies, enabling secure and isolated data retrieval.**

**Key Features:**
- Web content retrieval with custom HTTP proxy support
- Secure handling of images and URLs
- Integration with Claude Desktop for seamless workflow
- Customizable proxy configuration via environment variables

---

### 122. [lishenxydlgzs/simple-files-vectorstore](https://github.com/lishenxydlgzs/simple-files-vectorstore)  `innovation: 8`

**A simple vector store that indexes file content for semantic search.**

**Key Features:**
- Semantic search via vector embeddings
- Real-time file content indexing
- Configurable chunk size and overlap
- Background processing of file changes
- Support for multiple file types

---

### 123. [microsoft/clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling secure, isolated access to Microsoft Clarity analytics and session data.**

**Key Features:**
- Session recording retrieval
- Real-time analytics access
- Natural language query support
- Integration with Claude for Desktop
- Custom data filtering and export

---

### 124. [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)  `innovation: 8`

**A server implementing the Model Context Protocol (MCP) for secure, dynamic filesystem operations with advanced file management and access control.**

**Key Features:**
- MCP-based directory access control
- Dynamic root-based access via Roots protocol
- Secure file read/write operations
- File metadata retrieval
- Directory listing with size information
- Dry-run editing capabilities
- Multi-file processing and pattern matching

---

### 125. [morphik-org/morphik-mcp](https://github.com/morphik-org/morphik-mcp)  `innovation: 8`

**Morphik MCP server enabling secure, isolated context management for AI assistants interacting with Morphik databases.**

**Key Features:**
- Document ingestion (text and files)
- Document retrieval with LLM-powered completions
- Document querying and management
- File system navigation and file ingestion
- Secure file operations via --allowed-dir parameter

---

### 126. [nattyraz/youtube-mcp](https://github.com/nattyraz/youtube-mcp)  `innovation: 8`

**A model context protocol server for YouTube videos enabling metadata extraction, caption handling, and markdown conversion.**

**Key Features:**
- Video metadata retrieval
- Automatic caption extraction
- Markdown template conversion
- Search within captions
- OAuth2 authentication support

---

### 127. [naveenbandarage/poke-mcp](https://github.com/naveenbandarage/poke-mcp)  `innovation: 8`

**A Model Context Protocol server enabling AI assistants to access Pokémon data via standardized APIs.**

**Key Features:**
- MCP server integration
- PokeDex API queries
- Real-time communication via SSE
- Natural language query support

---

### 128. [niledatabase/nile-mcp-server](https://github.com/niledatabase/nile-mcp-server)  `innovation: 8`

**Nile MCP Server enables secure, standardized interaction between LLM applications and the Nile database platform.**

**Key Features:**
- Database Management
- Credential Management
- Region Management
- SQL Query Support
- MCP Protocol Implementation
- Type Safety with TypeScript
- Comprehensive Error Handling
- Test Coverage and Validation

---

### 129. [olaxbt/solana-vault-mcp](https://github.com/olaxbt/solana-vault-mcp)  `innovation: 8`

**A Python-based Solana wallet management system enabling secure, isolated operations via Model Context Protocol.**

**Key Features:**
- Secure wallet operations
- SOL balance checking
- Transaction history retrieval
- Model Context Protocol compliance
- Flask web server support

---

### 130. [ompragash/isolator-mcp](https://github.com/ompragash/isolator-mcp)  `innovation: 8`

**A secure, containerized MCP server enabling safe execution of code in multiple languages via isolated environments.**

**Key Features:**
- Secure code execution sandbox for Python
- Go
- and JavaScript
- Supports Docker-based container isolation
- Configurable security defaults and resource limits
- Integration with MCP protocol for LLM interaction
- Automated deployment and management of code snippets

---

### 131. [openlinksoftware/mcp-jdbc-server](https://github.com/openlinksoftware/mcp-jdbc-server)  `innovation: 8`

**A Java-based Model Context Protocol (MCP) server for JDBC, enabling secure and efficient database connectivity.**

**Key Features:**
- Supports MCP protocol for seamless integration with Virtuoso DBMS
- Secure JDBC connection management with environment variables
- Comprehensive schema and table information retrieval
- Advanced querying capabilities including filtering
- searching
- and SPARQL support
- AI-assisted code generation and review through integrated tools

---

### 132. [paablolc/mcp-hacker-news](https://github.com/paablolc/mcp-hacker-news)  `innovation: 8`

**A MCP server bridging Hacker News API with AI tools for seamless integration.**

**Key Features:**
- Integration with Claude and Cursor for Model Context Protocol
- Fetching live Hacker News data (posts
- comments
- users)
- Support for advanced queries and custom parameters
- Real-time updates and latest content retrieval

---

### 133. [pangeacyber/pangea-mcp-server](https://github.com/pangeacyber/pangea-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling secure integration with Pangea APIs for intelligence data retrieval.**

**Key Features:**
- Model Context Protocol (MCP) server integration
- Secure storage of Pangea API tokens in Vault
- Audit logging with Secure Audit Log configuration
- Token management and extension across multiple Pangea services
- Support for AI Guard
- Domain Intel
- Embargo
- IP Intel
- Redact
- URL Intel

---

### 134. [pinkpixel-dev/npm-helper-mcp](https://github.com/pinkpixel-dev/npm-helper-mcp)  `innovation: 8`

**A Model Context Protocol server that enhances npm package management for AI applications, enabling seamless integration with LLMs and automated dependency updates.**

**Key Features:**
- Automated dependency checking and upgrading using Model Context Protocol
- Safe upgrade tools to prevent version conflicts
- Integration with LLMs like Claude for intelligent npm operations
- Comprehensive search and metadata retrieval for packages
- Support for secure
- isolated development environments

---

### 135. [pipedreamhq/pipedream](https://github.com/pipedreamhq/pipedream)  `innovation: 8`

**A reference implementation for managing MCP server connections, user authentication, and API interactions.**

**Key Features:**
- MCP server reference implementation
- User authentication and authorization
- Dynamic app discovery
- API request management
- Secure credential storage
- Integration with external tools

---

### 136. [pree-dew/mcp-bookmark](https://github.com/pree-dew/mcp-bookmark)  `innovation: 8`

**A MCP server enabling AI-powered bookmark saving, searching, and categorization using OpenAI RAG.**

**Key Features:**
- Save bookmarks with metadata
- Smart semantic search across bookmarks
- Integration with OpenAI for intelligent categorization

---

### 137. [prixyy/rag_based_mcp](https://github.com/prixyy/rag_based_mcp)  `innovation: 8`

**A model context protocol server that ingests documents and provides intelligent, context-aware answers.**

**Key Features:**
- Ingest new documents
- Answer questions based on documents
- Context-aware responses
- Integration with GroundX API

---

### 138. [qubaomingg/stock-analysis-mcp](https://github.com/qubaomingg/stock-analysis-mcp)  `innovation: 8`

**A tool for analyzing stock tickers using the Model Context Protocol to extract and process financial data.**

**Key Features:**
- stock-data analysis
- intraday and daily data retrieval
- price movement alerts
- data resource management
- code review and security features

---

### 139. [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp)  `innovation: 8`

**Connect and analyze Strava data using LLMs via a custom MCP server.**

**Key Features:**
- Connect Strava account via Claude Desktop
- Real-time activity data retrieval (distance
- time
- heart rate)
- Workout analysis with power
- speed
- and zone tracking
- Route exploration and GPX/TCX exports
- Profile management and club listings
- Integration with AI for contextual insights

---

### 140. [ramidecodes/mcp-server-notion](https://github.com/ramidecodes/mcp-server-notion)  `innovation: 8`

**A Model Context Protocol server that wraps the official Notion SDK, enabling AI models to interact with Notion workspaces.**

**Key Features:**
- Integration with Notion via MCP protocol
- Search
- query
- and manage Notion pages and databases
- Create
- retrieve
- and update content blocks (paragraphs
- lists
- etc.)
- Manage users and user information

---

### 141. [rossja/irtoolshed-mcp-server](https://github.com/rossja/irtoolshed-mcp-server)  `innovation: 8`

**A comprehensive Model Context Protocol (MCP) server for network incident response, enabling AI-driven security analysis.**

**Key Features:**
- ASN (Autonomous System Number) Lookup
- DNS Record Lookup
- WHOIS Record Retrieval
- IP Geolocation
- Network Port Scanning
- Threat Intelligence Integration
- Malware Hash Lookups
- URL Reputation Checking
- Email Security Analysis
- Passive DNS History

---

### 142. [seekrays/seekchat](https://github.com/seekrays/seekchat)  `innovation: 8`

**A Sleek and Powerful AI Desktop Assistant that supports MCP integration.**

**Key Features:**
- Multiple AI Providers support
- MCP Tool Integration for enhanced AI capabilities
- Local Storage for privacy-focused chat history
- Multi-language Support (English and Chinese)
- Modern UI
- and an Electron-based desktop application.

---

### 143. [servo/servo](https://github.com/servo/servo)  `innovation: 8`

**Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications.**

**Key Features:**
- A lightweight
- high-performance alternative for embedding web technologies in applications
- implemented in Rust.

---

### 144. [seym0n/tiktok-mcp](https://github.com/seym0n/tiktok-mcp)  `innovation: 8`

**Integrates TikTok access into AI platforms for enhanced context analysis.**

**Key Features:**
- TikTok video analysis
- Subtitle extraction
- Engagement metrics retrieval
- Virality factor identification

---

### 145. [shak2000/stockmcp](https://github.com/shak2000/stockmcp)  `innovation: 8`

**Integrates real-time financial data with LLaMA 3.2 3B to enhance AI responses with up-to-date market information.**

**Key Features:**
- Integrate Yahoo Finance API
- Real-time stock price retrieval
- Company information fetching
- Historical data access
- Market news integration
- Natural language processing for context enhancement

---

### 146. [shivay-couchbase/couchbase-mcp](https://github.com/shivay-couchbase/couchbase-mcp)  `innovation: 8`

**Implementation of a Model Context Protocol server for semantic search in Star Wars planet data using Couchbase vector search.**

**Key Features:**
- Model Context Protocol integration
- Vector search for similarity lookup
- Couchbase server setup with vector indexing
- TypeScript implementation with type safety

---

### 147. [shlomico-tr/etoroportfoliomcp](https://github.com/shlomico-tr/etoroportfoliomcp)  `innovation: 8`

**A platform providing MCP tools for interacting with eToro's public API, enabling portfolio fetching and instrument details retrieval.**

**Key Features:**
- fetch_etoro_portfolio
- fetch_instrument_details
- search_instruments
- get_tools

---

### 148. [showfive/playwright-mcp-server](https://github.com/showfive/playwright-mcp-server)  `innovation: 8`

**A server enabling Playwright web page content retrieval using the Model Context Protocol.**

**Key Features:**
- Page navigation
- Full page content retrieval
- Visible content extraction
- Interactive elements detection
- Mouse operation simulation
- Echo tool for testing
- Drag and drop support
- Interactive element positioning
- Error handling and timeout management

---

### 149. [sinco-lab/mcp-youtube-transcript](https://github.com/sinco-lab/mcp-youtube-transcript)  `innovation: 8`

**A tool for extracting and processing YouTube video transcripts, supporting multiple languages with advanced text normalization and error handling.**

**Key Features:**
- YouTube transcript extraction from videos
- Multi-language support
- Paragraph segmentation and normalization
- Robust error handling and timestamp detection
- Integration with Claude Desktop for analysis

---

### 150. [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone)  `innovation: 8`

**A Pinecone Model Context Protocol server enabling reading and writing operations from Pinecone, supporting rudimentary RAG.**

**Key Features:**
- Read from Pinecone index
- Write to Pinecone index
- Semantic search integration
- RAG capabilities

---

### 151. [slavfox/Cozette](https://github.com/slavfox/Cozette)  `innovation: 8`

**A bitmap programming font optimized for coziness 💜**

**Key Features:**
- The core innovation lies in its bitmap nature
- offering a specific set of glyphs optimized for terminal/CLI environments. It provides both bitmap formats (.otb) and vector formats (.ttf)
- addressing the common problem of scaling and rendering issues with traditional bitmap fonts. The font is designed to be pixel-perfect
- which is crucial for clarity in terminal interfaces.

---

### 152. [sociallayer-im/sola-mcp](https://github.com/sociallayer-im/sola-mcp)  `innovation: 8`

**A stateless HTTP server implementing the Model Context Protocol for social layer platform integrations.**

**Key Features:**
- Event retrieval
- Event listing and search
- Group information access
- Profile details
- Venue information
- Session-based HTTP transport

---

### 153. [spathodea-network/opencti-mcp](https://github.com/spathodea-network/opencti-mcp)  `innovation: 8`

**OpenCTI MCP Server enables integration with OpenCTI platform for threat intelligence management.**

**Key Features:**
- Fetch and search threat intelligence data
- Search for malware information
- Query indicators of compromise
- User and group management
- List attack patterns
- Campaign information retrieval
- System connectors listing
- File operations and file details
- Reference data access
- Marking definitions

---

### 154. [spences10/mcp-embedding-search](https://github.com/spences10/mcp-embedding-search)  `innovation: 8`

**A Borg-based search tool for efficiently querying transcript segments using vector similarity in a Turso database.**

**Key Features:**
- Vector similarity search
- Relevance scoring with cosine similarity
- Configurable search parameters
- Efficient database connection pooling

---

### 155. [stevenvo/slack-mcp-server](https://github.com/stevenvo/slack-mcp-server)  `innovation: 8`

**A Slack MCP server enabling secure, programmatic access to Slack workspaces for AI assistants like Claude.**

**Key Features:**
- Message operations (read/permalinks)
- Thread and channel management
- Metadata retrieval
- User and group information access
- Search capabilities
- Integration with Claude AI assistant

---

### 156. [strickvl/mcp-beeminder](https://github.com/strickvl/mcp-beeminder)  `innovation: 8`

**A server implementation enabling AI applications to securely interact with Beeminder's API using the Model Context Protocol.**

**Key Features:**
- MCP server implementation
- Secure access to Beeminder API
- Goal and datapoint management
- User information retrieval
- Support for multiple Beeminder goal types

---

### 157. [takumiy235/uniprot-mcp-server](https://github.com/takumiy235/uniprot-mcp-server)  `innovation: 8`

**MCP server for UniProt protein data access enabling AI assistants to fetch protein information.**

**Key Features:**
- Batch retrieval of multiple proteins
- Caching with 24-hour TTL
- Error handling and logging
- API integration using httpx
- Rate limiting and retries

---

### 158. [tejpalvirk/developer](https://github.com/tejpalvirk/developer)  `innovation: 8`

**A developer management system that maintains persistent context across coding sessions.**

**Key Features:**
- Persistent Development Context
- Session Management
- Dependency Tracking
- Project Status Insights
- Component Context Retrieval
- Decision History
- Milestone Progress Tracking
- Related Entity Discovery

---

### 159. [thesophiaxu/contextd](https://github.com/thesophiaxu/contextd)  `innovation: 8`

**An efficient macOS app that continuously captures screen activity, summarizes it with an LLM, and makes summaries available for integration with other local tools.**

**Key Features:**
- Screen recording every 2 seconds
- OCR on changed regions
- Local SQLite database storage
- Interactive API for summarization
- Integration with external LLM services via OpenRouter API

---

### 160. [v4lheru/trello-mcp-server](https://github.com/v4lheru/trello-mcp-server)  `innovation: 8`

**A secure, enterprise-grade Trello API integration server enabling secure credential management and workflow automation.**

**Key Features:**
- Secure credential storage using OS credential manager
- Comprehensive Trello API integration
- Full TypeScript support with type safety
- Robust error handling and migration tools
- Secure development environment setup

---

### 161. [veithly/rss-mcp](https://github.com/veithly/rss-mcp)  `innovation: 8`

**A TypeScript-based Model Context Protocol (MCP) server that enables structured parsing and retrieval of RSS/Atom feeds, with enhanced support for RSSHub feeds.**

**Key Features:**
- Universal feed parsing for RSS/Atom
- Specialized support for RSSHub feeds
- Multi-instance polling for reliable data fetching
- Customizable item count and priority instance selection
- Content cleaning and structured JSON output

---

### 162. [victoriametrics-community/mcp-victorialogs](https://github.com/victoriametrics-community/mcp-victorialogs)  `innovation: 8`

**Implementation of Model Context Protocol (MCP) server for VictoriaLogs to enable advanced observability and automation.**

**Key Features:**
- Access to all read-only VictoriaLogs APIs
- Comprehensive log querying and exploration
- Metrics UI with setup instructions
- Integration with external tools and documentation
- Support for Streamable HTTP mode
- Embedded documentation and search capabilities

---

### 163. [xuanwo/mcp-server-opendal](https://github.com/xuanwo/mcp-server-opendal)  `innovation: 8`

**A model context protocol server enabling integration with multiple storage services for Apache OpenDAL.**

**Key Features:**
- Model Context Protocol Server
- Integration with multiple storage services
- Environment variable-based configuration
- Support for S3
- Azure Blob Storage
- Google Cloud Storage

---

### 164. [xzq-xu/jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)  `innovation: 8`

**A lightweight JVM monitoring and diagnostic server built on native JDK tools, enabling AI agents to analyze Java applications without third-party dependencies.**

**Key Features:**
- Java process listing
- Thread information retrieval
- Memory usage monitoring
- Class structure analysis
- Method call path tracing
- Class decompilation and inspection
- Method invocation monitoring
- Logger level management
- System resource dashboard

---

### 165. [yassinetk/mcp-docs-provider](https://github.com/yassinetk/mcp-docs-provider)  `innovation: 8`

**Provides a documentation context provider for LLMs via MCP, enabling seamless access to local markdown technical documentation.**

**Key Features:**
- Integration with MCP for LLM context access
- Markdown file support
- Local documentation retrieval
- Automatic code generation and querying

---

## Context Isolation & Sandboxing

### 166. [jpmelos/agentcontainer](https://github.com/jpmelos/agentcontainer)  `innovation: 10`

**AgentContainer (jpmelos)**

**Key Features:**
- Standardized agent environment declaration
- Rust-native performance
- reproducible dependency isolation
- Docker-like standard for agents.

---

### 167. [chrishayuk/mcp-code-sandbox](https://github.com/chrishayuk/mcp-code-sandbox)  `innovation: 9`

**A secure, isolated sandbox environment for executing Python code safely.**

**Key Features:**
- Isolated sandbox environments
- Secure file operations
- Extensible architecture
- Code execution with abstraction
- Integration with MCP protocol
- Support for custom interpreters

---

### 168. [glassbead-tc/audius-mcp-atris](https://github.com/glassbead-tc/audius-mcp-atris)  `innovation: 9`

**A code-mode MCP server that enables LLMs to access Audius and Open Audio Protocol efficiently using search and execution capabilities.**

**Key Features:**
- Search and execute on Audius API endpoints
- Secure sandboxed execution with QuickJS WASM
- Integration with The Graph for on-chain protocol data
- No raw network calls or file system access

---

### 169. [mKeRix/toolscript](https://github.com/mKeRix/toolscript)  `innovation: 9`

**Toolscript is a tool execution layer that minimizes context bloat by dynamically generating and exposing only necessary tool types to an LLM via a semantic search interface.**

**Key Features:**
- Automatic TypeScript type generation from MCP tool schemas
- Semantic tool search interface
- Sandboxed Deno execution environment
- Selective tool exposure via include/exclude configurations
- Seamless Claude Code plugin integration
- Configuration file merging for server definitions.

---

### 170. [alfonsograziano/node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)  `innovation: 8`

**A Node.js sandbox MCP server that executes arbitrary JavaScript in ephemeral Docker containers, enabling secure and isolated development environments.**

**Key Features:**
- Disposable Docker container execution
- On-the-fly npm dependency installation
- Arbitrary shell command execution within containers
- File capture and saving capabilities
- Integration with VS Code for quick testing
- Detached mode for long-running processes

---

### 171. [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)  `innovation: 8`

**A Model Context Protocol (MCP) server supporting remote MCP connections with Cloudflare OAuth integration.**

**Key Features:**
- MCP server implementation
- Cloudflare OAuth integration
- Remote MCP connection support
- Secure authentication mechanisms
- Context isolation features

---

### 172. [d-kimuson/esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)  `innovation: 8`

**Model Context Protocol server implementation for secure and isolated context management in enterprise applications.**

**Key Features:**
- Model Context Protocol server
- Article search functionality
- Context isolation
- Secure API endpoints
- Modular architecture

---

### 173. [danilop/mcp2lambda](https://github.com/danilop/mcp2lambda)  `innovation: 8`

**MCP2Lambda enables AI models to securely interact with AWS Lambda functions as tools without code changes, enhancing isolation and control over external service access.**

**Key Features:**
- Run AWS Lambda functions as LLM tools
- Secure invocation via MCP protocol
- Access private AWS resources safely
- Integrate with other AWS services through Lambda

---

### 174. [engineer-man/piston](https://github.com/engineer-man/piston)  `innovation: 8`

**Piston is a containerized, high-performance code execution engine designed to securely run untrusted code across over 100 programming languages via a standardized API.**

**Key Features:**
- Multi-language runtime management
- secure sandboxing via cgroups v2
- resource usage limiting (CPU/Memory/Time)
- RESTful execution API
- CLI-based package management
- multi-file execution support
- stdin/stdout/stderr piping
- pre-built containerized language packages

---

### 175. [garc33/js-sandbox-mcp-server](https://github.com/garc33/js-sandbox-mcp-server)  `innovation: 8`

**A secure JavaScript execution environment for sandboxed code runs.**

**Key Features:**
- secure js-sandbox execution
- isolated environment
- execution time and memory limits
- debugging tools
- code sandboxing

---

### 176. [harjjotsinghh/mcp-server-postgres-multi-schema](https://github.com/harjjotsinghh/mcp-server-postgres-multi-schema)  `innovation: 8`

**A model context protocol server enabling read-only access to PostgreSQL databases with enhanced multi-schema support.**

**Key Features:**
- Multi-schema support
- Read-only database access
- Schema isolation
- Cross-schema discovery
- Metadata exposure
- Schema context management

---

### 177. [huoshuiai42/huoshui-file-converter](https://github.com/huoshuiai42/huoshui-file-converter)  `innovation: 8`

**A secure MCP server for document format conversion within a specified working directory.**

**Key Features:**
- Secure MCP integration
- Format conversion support (Markdown
- DOCX
- HTML
- PDF
- TXT)
- Intelligent file format detection
- Sandboxed execution within a working directory
- CLI and environment variable configuration
- Support for large files with limits and special handling

---

### 178. [jlucaso1/mcp-javascript-sandbox](https://github.com/jlucaso1/mcp-javascript-sandbox)  `innovation: 8`

**A server tool for securely executing arbitrary JavaScript code within a sandboxed environment using QuickJS and Node.js WASI.**

**Key Features:**
- Secure JavaScript execution in WASM sandbox
- Standard I/O capture (stdout/stderr)
- Error reporting and handling
- MCP integration via stdio
- Type safety with TypeScript

---

### 179. [johnnyoshika/mcp-server-sqlite-npx](https://github.com/johnnyoshika/mcp-server-sqlite-npx)  `innovation: 8`

**A Node.js implementation of the Model Context Protocol SQLite server for secure, isolated database operations.**

**Key Features:**
- SQLite Server Integration
- Node.js Runtime Support
- Claude Desktop Compatibility
- Context Isolation
- Secure Development Practices

---

### 180. [lauriewired/ghidramcp](https://github.com/lauriewired/ghidramcp)  `innovation: 8`

**GhidraMCP enables context engineering and isolation by integrating Ghidra's reverse engineering tools with MCP clients, allowing secure and automated analysis of complex applications.**

**Key Features:**
- Ghidra plugin integration
- MCP server support
- automated code analysis
- secure context isolation
- memory persistence handling

---

### 181. [layr-labs/eigenlayer-mcp-server](https://github.com/layr-labs/eigenlayer-mcp-server)  `innovation: 8`

**A server implementation for the Model Context Protocol (MCP) to enable secure, isolated communication between AI models and external services.**

**Key Features:**
- Model context protocol integration
- Secure communication channels
- Context isolation
- API management
- Developer tools

---

### 182. [lloydzhou/bitable-mcp](https://github.com/lloydzhou/bitable-mcp)  `innovation: 8`

**A platform enabling secure and isolated interaction with Bitable tables via the Model Context Protocol.**

**Key Features:**
- Secure access to Bitable tables
- Model Context Protocol integration
- Predefined interaction tools
- Isolation for sensitive operations

---

### 183. [maxim-saplin/mcp_safe_local_python_executor](https://github.com/maxim-saplin/mcp_safe_local_python_executor)  `innovation: 8`

**A secure Python runtime that wraps LLM-generated code execution via MCP, limiting operations to prevent malicious code execution.**

**Key Features:**
- Secure execution of Python code
- Restricted imports and collections
- No file I/O operations
- Sandboxed environment for LLM agents

---

### 184. [mohit-novo/mcp-lithic](https://github.com/mohit-novo/mcp-lithic)  `innovation: 8`

**A TypeScript implementation of a Model Context Protocol server for Lithic API, providing read-only access to banking and card services.**

**Key Features:**
- TypeScript implementation
- Docker support
- Read-only access to Lithic API
- Automated builds and deployments
- Enhanced error handling
- Context isolation

---

### 185. [mozicim/node-code-sandbox-mcp](https://github.com/mozicim/node-code-sandbox-mcp)  `innovation: 8`

**A Node.js sandbox server implementing the Model Context Protocol for secure JavaScript execution in isolated environments.**

**Key Features:**
- Dynamic JavaScript execution in isolated Docker containers
- On-the-fly npm package installation
- Interactive assistance for AI agents and LLMs
- Compliance with Model Control Protocol (MCP)

---

### 186. [nahmanmate/code-research-mcp-server](https://github.com/nahmanmate/code-research-mcp-server)  `innovation: 8`

**A platform designed to enhance context management and isolation for developers using AI tools.**

**Key Features:**
- Code search across multiple platforms
- Integration with Stack Overflow
- MDN Web Docs
- GitHub
- npm
- Caching for performance
- Error handling and debugging tools

---

### 187. [rayai-labs/agentic-ray](https://github.com/rayai-labs/agentic-ray)  `innovation: 8`

**A production-grade agent hosting platform providing isolated Firecracker microVMs with persistent workspaces and secure credential proxying.**

**Key Features:**
- Firecracker microVM isolation
- Persistent workspace filesystem
- Network-level credential proxying
- Sub-second cold starts
- Framework-agnostic deployment
- Real-time token streaming
- CLI-based session management
- Automated environment provisioning

---

### 188. [rgbkrk/rcon-mcp](https://github.com/rgbkrk/rcon-mcp)  `innovation: 8`

**A Minecraft server management tool enabling AI interaction via RCON protocol.**

**Key Features:**
- AI interaction via RCON
- Server management in Docker container
- Context isolation for secure operations

---

### 189. [svngoku/mcp-docker-code-interpreter](https://github.com/svngoku/mcp-docker-code-interpreter)  `innovation: 8`

**A secure sandbox for executing code via the Model Context Protocol (MCP) using Docker containers.**

**Key Features:**
- Secure Docker container execution
- Multi-language support (currently Python)
- Automatic setup for container creation and cleanup
- Integration with Model Context Protocol
- Resource limitations to prevent abuse

---

### 190. [tywenk/mcp-sol](https://github.com/tywenk/mcp-sol)  `innovation: 8`

**Model Context Protocol for Solana Client enabling secure, isolated communication between microservices.**

**Key Features:**
- Model Context Protocol
- Secure communication channels
- Context isolation
- Data flow management

---

## Context Distillation & Summarization

### 191. [Opencode-DCP/opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)  `innovation: 9`

**OpenCode DCP (Context Pruner)**

**Key Features:**
- Redundant tool-call deduplication
- automated stale error removal
- active agent-driven context discarding
- session summarization.

---

### 192. [ab498/code-context-provider-mcp](https://github.com/ab498/code-context-provider-mcp)  `innovation: 9`

**A tool that provides code context and analysis for AI assistants, extracting directory structures and code symbols using WebAssembly Tree-sitter parsers with zero native dependencies.**

**Key Features:**
- Code context extraction for AI assistants
- Directory structure analysis
- Symbol identification (functions
- variables
- classes
- imports
- exports)
- WebAssembly Tree-sitter parser integration
- Zero native dependencies for seamless deployment

---

### 193. [fenxer/steam-review-mcp](https://github.com/fenxer/steam-review-mcp)  `innovation: 8`

**A tool for retrieving and analyzing Steam game reviews using the Model Context Protocol.**

**Key Features:**
- Get game reviews
- Analyze game reviews
- Summarize pros and cons
- Install via Smithery
- Run service locally

---

### 194. [kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)  `innovation: 8`

**The kagimcp server enables secure, context-aware search across multiple tools and platforms using the Model Context Protocol (MCP).**

**Key Features:**
- Contextual search across multiple tools
- Integration with AI frameworks (e.g.
- OpenAI Codex)
- Custom summarization engine selection
- Secure API key management
- Developer workflow automation

---

### 195. [kazuph/mcp-youtube](https://github.com/kazuph/mcp-youtube)  `innovation: 8`

**A model-context protocol server for YouTube in Japanese, enabling integration with external AI services.**

**Key Features:**
- Model Context Protocol integration
- YouTube subtitle extraction
- AI-powered summarization
- Secure code deployment

---

### 196. [masonchow/source-map-parser-mcp](https://github.com/masonchow/source-map-parser-mcp)  `innovation: 8`

**A WebAssembly-based source map parser that maps JavaScript error stack traces back to source code, aiding developers in quickly identifying and resolving issues.**

**Key Features:**
- Source map parsing for JavaScript error stack traces
- Context extraction around error locations
- Batch processing of multiple stack traces
- Customizable context offset lines
- Integration with MCP server for enhanced functionality

---

### 197. [mcp-get/community-servers](https://github.com/mcp-get/community-servers)  `innovation: 8`

**A server that enables AI models to understand file structures and relationships for context-aware development.**

**Key Features:**
- Directory listing
- Context extraction
- Multi-query search
- Local caching
- Cross-platform support

---

### 198. [mondweep/youtube-music-mcp-server](https://github.com/mondweep/youtube-music-mcp-server)  `innovation: 8`

**A Model Context Protocol server enabling AI interaction with YouTube Music for playback control.**

**Key Features:**
- MCP server integration
- AI-powered song search
- Playback control via YouTube Music
- Error handling and logging
- Cross-platform support (macOS)
- Note creation and summarization

---

### 199. [shreyaskarnik/huggingface-mcp-server](https://github.com/shreyaskarnik/huggingface-mcp-server)  `innovation: 8`

**A server enabling secure, isolated access to Hugging Face APIs for LLM interactions.**

**Key Features:**
- Model access via custom URIs
- Prompt-based interactions (compare-models
- summarize-paper)
- Dataset and space exploration
- Integration with Hugging Face APIs
- Tool categories for model
- dataset
- space
- paper
- and collection management

---

## Prompt Engineering & Optimization

### 200. [abhichandra21/Promptheus.git](https://github.com/abhichandra21/Promptheus.git)  `innovation: 9`

**Automated prompt refinement and optimization for enterprise AI interactions.**

**Key Features:**
- Adaptive questioning to identify required information
- Multi-provider support (Google
- OpenAI
- Anthropic
- etc.)
- Interactive refinement through iterative Q&A
- Session history tracking and reuse for context preservation
- Integration with MCP server for advanced prompt optimization

---

### 201. [lumile/promptopia-mcp](https://github.com/lumile/promptopia-mcp)  `innovation: 9`

**A server for managing and reusing prompt templates with variable substitution and multi-message conversation structures.**

**Key Features:**
- Centralized prompt management
- Advanced multi-message support
- Intelligent variable substitution
- Seamless MCP integration
- Future-proof architecture

---

### 202. [rbonestell/ap-mcp-server](https://github.com/rbonestell/ap-mcp-server)  `innovation: 9`

**An AI-powered MCP server transforming AP Media API content into intelligent, conversational interfaces.**

**Key Features:**
- Natural language query processing
- Intelligent prompt templates
- Content recommendation engine
- Trend analysis and pattern detection
- Bulk data handling and caching
- Secure configuration and error recovery

---

### 203. [jjikky/dynamo-readonly-mcp](https://github.com/jjikky/dynamo-readonly-mcp)  `innovation: 8`

**A server enabling LLMs to query AWS DynamoDB using natural language.**

**Key Features:**
- Table Management Tools
- Data Query Tools
- Prompt Templates
- Resource Access
- Dynamic Prompt Generation

---

### 204. [raw391/coin_daemon_mcp](https://github.com/raw391/coin_daemon_mcp)  `innovation: 8`

**A beta MCP server enabling AI assistants to securely interact with cryptocurrency daemons for transaction management, monitoring, and data analysis.**

**Key Features:**
- Transaction Management
- Balance Checking
- Wallet Operations
- Daemon Status Monitoring
- Transaction History
- Prompt Templates
- Security Best Practices

---

## General Context Engineering

### 205. [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)  `innovation: 10`

**VoltAgent: 5k Skills Repo**

**Key Features:**
- 5
- 000+ audited `SKILL.md` runbooks
- Red-Team "Abaddon" mode skills
- YAML frontmatter dependency tracking
- active community malware filtering.

---

### 206. [clkao/agentlore](https://github.com/clkao/agentlore)  `innovation: 10`

**AgentLore: Persona Context**

**Key Features:**
- Dynamic "world-building" context injection
- role/boundary consistency enforcement
- behavioral state versioning (rollback capability)
- swarm-wide lore synchronization.

---

### 207. [context7/context7](https://github.com/context7/context7)  `innovation: 10`

**Context7: Real-time Doc Aggregator**

**Key Features:**
- Real-time documentation scraping
- automated version-aware indexing
- token-efficient context injection
- support for latest framework updates.

---

### 208. [cyclotruc/gitingest](https://github.com/cyclotruc/gitingest)  `innovation: 10`

**Gitingest: Repo Grounding**

**Key Features:**
- URL-to-digest conversion (replace hub with ingest)
- smart LLM-friendly formatting
- real-time token counting
- browser extension support.

---

### 209. [dennishavermans/agentfile](https://github.com/dennishavermans/agentfile)  `innovation: 10`

**agentfile: Agent Dockerfile**

**Key Features:**
- Standardized agent environment declaration
- MCP server dependency mapping
- cross-platform workflow portability
- deterministic system prompt injection.

---

### 210. [jkerdels/dependency-graph-mcp](https://github.com/jkerdels/dependency-graph-mcp)  `innovation: 10`

**Dependency-Graph-MCP**

**Key Features:**
- Multi-language support (TS/JS/C#/Python)
- DOT format visual rendering
- architectural debt scoring
- circular dependency deadlock detection.

---

### 211. [ryanreh99/skills-sync](https://github.com/ryanreh99/skills-sync)  `innovation: 10`

**Skills-Sync: Cross-Agent**

**Key Features:**
- AI-powered skill normalization
- cross-platform synchronization
- adaptive complexity scaling
- standardized SKILL.md management.

---

### 212. [toroleapinc/claude-brain](https://github.com/toroleapinc/claude-brain)  `innovation: 10`

**Claude Brain: State Sync**

**Key Features:**
- Automated Pre/Post session state sync
- LLM-powered semantic memory merging
- auto-evolution of repeated patterns into durable rules.

---

### 213. [yamadashy/repomix](https://github.com/yamadashy/repomix)  `innovation: 10`

**Repomix: Repo Packaging**

**Key Features:**
- AI-optimized XML/Markdown formatting
- Tree-sitter token compression (70%)
- Secretlint data stripping
- remote GitHub repo support.

---

### 214. [augmnt/augments-mcp-server](https://github.com/augmnt/augments-mcp-server)  `innovation: 9.7`

**A next-generation framework documentation platform for Claude Code, offering intelligent caching, multi-source integration, and context-aware assistance to accelerate development.**

**Key Features:**
- Documentation-first search with BM25 indexing
- Context-aware assistance and type inference
- Integration of multiple external data sources
- Real-time code examples and API documentation
- Error pattern recognition and diagnostics
- Version comparison and migration guides
- Secure
- production-grade environment setup

---

### 215. [demomagic/duckchain-mcp](https://github.com/demomagic/duckchain-mcp)  `innovation: 9.7`

**A blockchain MCP server enabling AI-driven deep analysis of blockchain data.**

**Key Features:**
- Blockchain data access via BlockScout API v2
- AI-powered transaction analysis and smart contract evaluation
- Comprehensive address and token management
- Secure development environment with automated workflows
- Integration with CI/CD pipelines and DevOps tools
- Advanced security features including vulnerability detection
- Real-time monitoring and state change tracking
- Token operations
- NFT management
- and metadata refresh

---

### 216. [wwiens/trakt_mcpserver](https://github.com/wwiens/trakt_mcpserver)  `innovation: 9.7`

**A protocol server that enables AI language models to securely and efficiently interact with external entertainment data APIs via standardized protocols.**

**Key Features:**
- Secure authentication and session management
- Real-time access to trending and popular content
- Detailed show and episode data including ratings and watch history
- Personalized recommendations based on user preferences
- Integration with external APIs for dynamic content fetching
- Support for multiple languages and formats
- Scalable architecture for enterprise use

---

### 217. [1yhy/figma-context-mcp](https://github.com/1yhy/figma-context-mcp)  `innovation: 9`

**A server that enables seamless integration of Figma designs with AI coding tools by providing real-time design-to-code generation.**

**Key Features:**
- Smart Layout Detection
- Icon Merging
- CSS Generation
- Image Export
- Multi-layer Caching
- Design-to-Code Prompts
- Lightweight Data Access

---

### 218. [Ak-9647/Evernote-MCP](https://github.com/Ak-9647/Evernote-MCP)  `innovation: 9`

**A secure, AI-powered MCP server for seamless Evernote integration with Claude Desktop.**

**Key Features:**
- Secure token management using environment variables
- Rich note creation with HTML
- tables
- and lists
- Search and organization of notes by content and tags
- Professional templates for meeting notes
- shopping lists
- and more
- Integration with Claude Desktop for natural language input and output

---

### 219. [Cluster444/agentic](https://github.com/Cluster444/agentic)  `innovation: 9`

**Cluster444 Agentic Harness**

**Key Features:**
- Structured /thoughts directory
- phased implementation loops
- specialized subagent delegation
- automated ticket decomposition.

---

### 220. [DeanWard/HAL](https://github.com/DeanWard/HAL)  `innovation: 9`

**HAL provides a secure, isolated environment for LLMs to interact with web APIs and external services while maintaining strict access control.**

**Key Features:**
- HTTP GET/POST/PUT/PATCH/DELETE/OPTIONS/HEAD requests
- Secure secret management with automatic redaction
- Automatic tool generation from OpenAPI/Swagger specifications
- Environment-based secret substitution and access control
- Response scanning for secret values
- Automatic replacement of secrets in responses

---

### 221. [Dinesh-Satram/fitness_coach_MCP](https://github.com/Dinesh-Satram/fitness_coach_MCP)  `innovation: 9`

**A platform that integrates AI tools with fitness data via the Model Context Protocol to deliver intelligent, context-aware coaching.**

**Key Features:**
- AI-powered fitness dashboard using Next.js
- MCP server for protocol-compliant data integration
- Smart tools for activity logging
- nutrition tracking
- and feedback collection
- Context-aware AI for personalized workout and meal plans
- Real-time progress visualization and goal setting

---

### 222. [ProtonOS/ProtonOS](https://github.com/ProtonOS/ProtonOS)  `innovation: 9`

**A bare-metal operating system written in C# targeting x86-64, designed for secure and efficient enterprise environments with advanced kernel features.**

**Key Features:**
- Custom Tier 0 JIT compiler
- Hardware abstraction layer
- Secure boot process
- Cross-assembly loading
- NUMA-aware memory allocation
- Preemptive scheduler
- Virtual memory management
- Device drivers (VirtIO
- SATA)
- Networking stack (Ethernet

---

### 223. [Raistlin82/btp-sap-odata-to-mcp-server-optimized](https://github.com/Raistlin82/btp-sap-odata-to-mcp-server-optimized)  `innovation: 9`

**An enterprise-grade MCP server optimized for SAP OData, designed to address the tool explosion problem with modular authentication, hierarchical tool registry, and secure integration.**

**Key Features:**
- Enhanced security architecture
- Modular authentication system
- Role-based access control
- Principal propagation
- Secure session management
- Smart query routing
- Hierarchical tool registry
- Intelligent workflow orchestration
- Real-time analytics and dashboards

---

### 224. [SecureBitChat/securebit-chat](https://github.com/SecureBitChat/securebit-chat)  `innovation: 9`

**World's most secure P2P messenger with end-to-end encryption and a shared Rust-based cryptographic core.**

**Key Features:**
- End-to-end encryption
- zero-server architecture
- WebRTC direct connections
- ECDH + DTLS + SAS verification
- full ASN.1 validation
- and a shared Rust-based cryptographic core.

---

### 225. [acryldata/mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)  `innovation: 9`

**DataHub MCP Server enables AI agents to find, understand, and manage data across the entire ecosystem using natural language queries.**

**Key Features:**
- Natural language search across tables
- columns
- dashboards
- and metrics
- Data lineage and impact analysis for changes
- SQL query generation and understanding
- Metadata management (tags
- owners
- descriptions)
- Document integration and knowledge base organization

---

### 226. [andrefigueira/.context](https://github.com/andrefigueira/.context)  `innovation: 9`

**A Git-native, AI-optimized documentation system that turns your repo into a living knowledge base.**

**Key Features:**
- The core innovation is the 'Substrate Methodology' which structures documentation within `.context/` to provide AI tools with a brain dump of the project's architecture
- patterns
- and specific constraints. It offers a complete template for turning a software project into an AI-optimized knowledge base.

---

### 227. [ashish-bansal/playwright-mcp](https://github.com/ashish-bansal/playwright-mcp)  `innovation: 9`

**Enhances Playwright test automation by providing full browser context, enabling accurate interaction with web pages.**

**Key Features:**
- Full browser visibility
- Interaction recording
- DOM extraction
- JavaScript execution

---

### 228. [blockscout/mcp-server](https://github.com/blockscout/mcp-server)  `innovation: 9`

**The Blockscout MCP server enables AI agents and tools to access and analyze blockchain data contextually, enhancing intelligent workflows across multiple chains.**

**Key Features:**
- Contextual blockchain data access
- Multi-chain support
- AI skill integration (e.g.
- Claude)
- Smart contract analysis
- Token and NFT tracking
- Secure API endpoints
- Observability and progress notifications

---

### 229. [burtthecoder/mcp-virustotal](https://github.com/burtthecoder/mcp-virustotal)  `innovation: 9`

**A powerful MCP server for VirusTotal API integration, offering comprehensive security analysis with automatic relationship data fetching.**

**Key Features:**
- Comprehensive URL analysis
- File analysis with detailed report generation
- IP address and domain intelligence
- Relationship analysis with pagination support
- Automated threat actor identification
- Integration with Claude Desktop and GitHub Copilot

---

### 230. [chrismannina/pubmed-mcp](https://github.com/chrismannina/pubmed-mcp)  `innovation: 9`

**A model context protocol server for PubMed literature search and management, enabling advanced filtering, citation export, and research analysis.**

**Key Features:**
- Advanced PubMed search with filters (date
- type
- authors
- journals
- MeSH terms)
- Detailed article details including abstracts and metadata
- Citation export in multiple formats (BibTeX
- APA
- MLA
- etc.)

---

### 231. [cicatriiz/healthcare-mcp-public](https://github.com/cicatriiz/healthcare-mcp-public)  `innovation: 9`

**A healthcare MCP server enabling AI assistants to access authoritative medical data sources.**

**Key Features:**
- FDA Drug Information
- PubMed Research Search
- Health Topics Evidence-Based Content
- Clinical Trials Database
- ICD-10 & Medical Terminology Lookup
- Medical Calculator
- Caching for Performance Optimization
- Comprehensive Testing Suite
- RESTful API Endpoints
- Interactive API Documentation (Swagger UI)

---

### 232. [deeplcom/deepl-mcp-server](https://github.com/deeplcom/deepl-mcp-server)  `innovation: 9`

**A model context protocol server enabling translation between multiple languages using DeepL API.**

**Key Features:**
- Translate text between numerous languages
- Rephrase text using DeepL's capabilities
- Access to all DeepL API languages and features
- Automatic language detection
- Formality control for translations
- Integration with Claude Desktop for seamless conversational translation

---

### 233. [dojoengine/sensei-mcp](https://github.com/dojoengine/sensei-mcp)  `innovation: 9`

**Sensei MCP provides expert guidance for Dojo and Cairo development on Starknet.**

**Key Features:**
- Expert Cairo guidance
- Model Context Protocol (MCP) server
- Specialized tools for models
- systems
- testing

---

### 234. [emeryray2002/virustotal-mcp](https://github.com/emeryray2002/virustotal-mcp)  `innovation: 9`

**A tool for analyzing VirusTotal data to provide comprehensive security insights and relationship mapping.**

**Key Features:**
- Comprehensive URL analysis
- File and IP analysis
- Relationship queries (analyses
- comments
- etc.)
- Automated report generation
- Integration with MCP and Claude Desktop
- Advanced search capabilities

---

### 235. [findmine/findmine-mcp](https://github.com/findmine/findmine-mcp)  `innovation: 9`

**A MCP server that integrates FindMine's styling API with Claude and other MCP-compatible tools, enabling advanced fashion AI for product recommendations.**

**Key Features:**
- Connects to FindMine's styling API via Model Context Protocol
- Integrates with Claude and other MCP-compatible applications
- Provides outfit recommendations
- style guidance
- and visual similarity searches
- Customizable style guides for brand-specific aesthetics

---

### 236. [freshtechbro/Vibe-Coder-MCP](https://github.com/freshtechbro/Vibe-Coder-MCP)  `innovation: 9`

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

### 237. [furey/mongodb-lens](https://github.com/furey/mongodb-lens)  `innovation: 9`

**A powerful MCP server enabling natural language queries and advanced data management for MongoDB databases.**

**Key Features:**
- Natural language query support
- Schema inference and schema versioning
- Performance optimization tools
- Security auditing and protection
- Cross-collection analysis and indexing
- Integration with external tools and services

---

### 238. [glips/figma-context-mcp](https://github.com/glips/figma-context-mcp)  `innovation: 9`

**Framelink MCP server integrates Figma layout data into AI coding agents for precise design-to-code generation.**

**Key Features:**
- Fetch Figma layout information via API
- Provide context-aware code suggestions in real time
- Enable one-shot UI implementation using Cursor
- Support enterprise-grade security and privacy

---

### 239. [goodfel10w/WelcomeTextGenerator](https://github.com/goodfel10w/WelcomeTextGenerator)  `innovation: 9`

**Automatisiert die Generierung professioneller Willkommenstexte für neue Mitarbeiter basierend auf strukturierten Daten.**

**Key Features:**
- Text-Analyse aus Freitext-Informationen
- Modulares Template-System mit 5 flexiblen Modulen
- Speicherung und Verwaltung der extrahierten Mitarbeiterdaten
- Generierung von Einleitung
- Abschluss und Varianten für Onboarding
- Integration in Claude Desktop App für eine nahtlose Benutzererfahrung

---

### 240. [gyoridavid/short-video-maker](https://github.com/gyoridavid/short-video-maker)  `innovation: 9`

**An open-source automated video creation tool that generates short-form videos from text inputs using text-to-speech, automatic captions, background videos, and music.**

**Key Features:**
- Text-to-speech conversion
- Automatic caption generation
- Background video selection from Pexels
- Music integration with genre/mood selection
- Video assembly using Remotion
- Web UI for browser-based video creation
- Support for n8n workflow integration
- Customizable settings and configurations

---

### 241. [hyperb1iss/droidmind](https://github.com/hyperb1iss/droidmind)  `innovation: 9`

**DroidMind enables AI assistants to securely interact with Android devices via the Model Context Protocol, allowing direct control and system analysis.**

**Key Features:**
- Manage devices (connect
- list
- view properties
- reboot)
- Analyze system logs and crash reports
- Handle files and manage device directories
- Control apps (install
- uninstall
- start
- stop

---

### 242. [ia-programming/mcp-images](https://github.com/ia-programming/mcp-images)  `innovation: 9`

**A powerful image processing server for AI applications, web services, and data pipelines.**

**Key Features:**
- Fetch images from URLs
- Process images locally
- Automatic image compression
- Parallel processing of multiple images
- Proper MIME type mapping
- Comprehensive error handling and logging

---

### 243. [ivan-saorin/mcp-expr-lang](https://github.com/ivan-saorin/mcp-expr-lang)  `innovation: 9`

**A powerful expression evaluation tool for Claude Desktop using the Model Context Protocol, enabling complex data manipulations and transformations within AI conversations.**

**Key Features:**
- Expression evaluation
- Mathematical operations
- String manipulation
- Array and object sorting
- Conditional logic
- Object property access
- String conversion
- Data transformation

---

### 244. [jimpick/mcp-json-db-collection-server](https://github.com/jimpick/mcp-json-db-collection-server)  `innovation: 9`

**Integration and management of multiple Fireproof JSON document databases within a Model Context Protocol server.**

**Key Features:**
- Multi-database support via Model Context Protocol
- Fireproof integration for scalable and secure data handling
- Context-aware database orchestration
- Real-time synchronization with cloud services
- Enhanced security and privacy controls

---

### 245. [jsdelivr/globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server)  `innovation: 9`

**Globalping MCP Server enables AI models to interact with a global network measurement platform via natural language, providing secure and scalable access to network probes.**

**Key Features:**
- Global network access for AI models
- Natural language interface for network tests
- Support for multiple authentication methods
- Comparative analysis of network performance
- Secure integration with AI tools via MCP protocol

---

### 246. [juyterman1000/entroly](https://github.com/juyterman1000/entroly)  `innovation: 9`

**Entroly-Daemon enables self-evolving AI assistants by compressing large codebases into a minimal context, enhancing performance and efficiency.**

**Key Features:**
- Self-evolving AI model with token-efficient learning
- Integration with multiple AI agents (Claude
- Copilot
- Codex
- etc.)
- Dynamic skill promotion and knowledge sharing across runtimes
- Live benchmarking and continuous improvement loop

---

### 247. [leghis/smart-thinking](https://github.com/leghis/smart-thinking)  `innovation: 9`

**Smart-Thinking is a local, deterministic Model Context Protocol server for multi-step reasoning without external AI dependencies.**

**Key Features:**
- Graph-based reasoning
- Heuristic-based scoring
- Verification tracking
- Memory management
- Visualization

---

### 248. [lingodotdev/lingo.dev](https://github.com/lingodotdev/lingo.dev)  `innovation: 9`

**A tool for automated, context-aware localization in React applications using AI-assisted translation.**

**Key Features:**
- AI-assisted i18n setup for React apps
- Localization engine integration (stateful APIs)
- Automatic translation generation at build time
- Support for multiple languages and localization engines
- Continuous localization in CI/CD pipelines
- Real-time progress tracking via WebSocket
- Integration with GitHub Actions
- GitLab CI/CD
- and Bitbucket Pipelines

---

### 249. [machjesusmoto/claude-lazy-loading](https://github.com/machjesusmoto/claude-lazy-loading)  `innovation: 9`

**This project demonstrates a proof-of-concept for significantly reducing initial context load in Claude Code by lazily loading necessary MCP servers and tools only when required.**

**Key Features:**
- Lazy loading of MCP servers/tools
- Context usage tracking
- Keyword-based trigger detection
- Tool indexing/registry generation
- Workflow-specific preloading profiles

---

### 250. [mapbox/mcp-server](https://github.com/mapbox/mcp-server)  `innovation: 9`

**Mapbox MCP Server enables AI agents to access geospatial intelligence, enabling location-aware decision making and spatial reasoning.**

**Key Features:**
- Geocoding and reverse geocoding
- Point of interest (POI) search
- Multi-modal routing (driving
- walking
- cycling)
- Travel time matrices and optimization
- Route visualization with maps
- Offline geospatial calculations
- Integration with popular AI tools like Claude Desktop and VS Code

---

### 251. [mfydev/ghost-mcp](https://github.com/mfydev/ghost-mcp)  `innovation: 9`

**A Model Context Protocol server enabling LLM interfaces to control a Ghost CMS blog securely.**

**Key Features:**
- Secure JWT authentication
- Comprehensive entity access (posts
- users
- members
- tiers
- offers)
- Advanced search with fuzzy and exact matching
- Human-readable output for entities
- Robust error handling with custom GhostError exceptions

---

### 252. [minimax-ai/minimax-mcp](https://github.com/minimax-ai/minimax-mcp)  `innovation: 9`

**MiniMax-MCP 官方服务器，支持与强大的文本转语音、图像生成和视频生成API的交互。**

**Key Features:**
- Text-to-Speech generation
- Image generation
- Video generation
- Voice cloning
- Audio file conversion
- Music creation
- Preview text for voice design

---

### 253. [mubarakhalketbi/game-asset-mcp](https://github.com/mubarakhalketbi/game-asset-mcp)  `innovation: 9`

**An AI-powered platform that enables rapid creation of 2D and 3D game assets from natural language prompts using Hugging Face models, integrated with MCP for seamless interaction.**

**Key Features:**
- Text-to-Image Asset Generation
- Multi-language Prompt Support
- Integration with Hugging Face Spaces
- Multiple 3D Model Generation Spaces
- Secure Remote Access via HTTPS
- Customizable Inference Parameters
- Automated File Saving and Organization

---

### 254. [nekzus/npm-sentinel-mcp](https://github.com/nekzus/npm-sentinel-mcp)  `innovation: 9`

**A powerful Model Context Protocol server for AI-driven NPM package analysis.**

**Key Features:**
- AI-powered security analysis
- Dependency mapping and resolution
- Real-time vulnerability detection
- Version tracking and changelog
- Package size and performance metrics
- Secure coding practices enforcement

---

### 255. [oevortex/ddg_search](https://github.com/oevortex/ddg_search)  `innovation: 9`

**A powerful Model Context Protocol (MCP) server for web search and AI-powered content extraction using DuckDuckGo.**

**Key Features:**
- Web search via DuckDuckGo
- AI-powered search with IAsk AI
- Monica & Brave AI
- Performance optimization with caching
- Security features including rate limiting and rotating user agents
- MCP-compliant server implementation

---

### 256. [pars-doe/autodocument](https://github.com/pars-doe/autodocument)  `innovation: 9`

**Automated documentation generation for code repositories using OpenRouter API and AI.**

**Key Features:**
- Smart directory analysis with respect to .gitignore patterns
- AI-powered documentation creation using OpenRouter API
- Intelligent file handling and fallback generation
- Comprehensive documentation at multiple levels (documentation.md
- testplan.md
- review.md)
- Customizable prompts for tailored output
- Modular architecture for future extensibility

---

### 257. [peterparker57/project-hub-mcp-server](https://github.com/peterparker57/project-hub-mcp-server)  `innovation: 9`

**A comprehensive platform for managing software projects, integrating GitHub, project tracking, and development workflows.**

**Key Features:**
- Project creation and management
- Local Git functionality with branch management
- Integration with GitHub for version control
- Code review and change tracking
- Automated workflows and CI/CD support
- Secure code deployment and protection
- Project notes and documentation management
- Multi-account GitHub support
- File snapshots and metadata management

---

### 258. [prathammanocha/wordpress-mcp-server](https://github.com/prathammanocha/wordpress-mcp-server)  `innovation: 9`

**A comprehensive WordPress MCP server enabling AI-driven interaction with WordPress sites via REST API, offering full CRUD capabilities and advanced security features.**

**Key Features:**
- CRUD operations for posts
- users
- categories
- comments
- Custom requests to external REST API endpoints
- Security features including code reviews and vulnerability detection
- Integration with AI assistants for enhanced user interaction
- Comprehensive documentation and support services

---

### 259. [pv-bhat/gemsuite-mcp](https://github.com/pv-bhat/gemsuite-mcp)  `innovation: 9`

**A professional Gemini API integration for Claude and MCP-compatible hosts, offering intelligent model selection and advanced file handling.**

**Key Features:**
- Intelligent model selection based on task and content
- Unified file handling with automatic format detection
- Support for multiple file types and operations
- Batch processing capabilities
- Automated error handling and exponential backoff

---

### 260. [renCosta2025/context7fork](https://github.com/renCosta2025/context7fork)  `innovation: 9`

**Context7 MCP Server provides up-to-date documentation and code examples for LLMs, enhancing AI development workflows.**

**Key Features:**
- Real-time
- version-specific documentation for LLMs and AI code editors
- Integration with GitHub Copilot for intelligent code generation
- Secure access control via JWT authentication
- Support for Cloudflare Workers to cache API responses
- Enhanced security features including vulnerability detection and secure code practices

---

### 261. [richard-weiss/mcp-google-cse](https://github.com/richard-weiss/mcp-google-cse)  `innovation: 9`

**A model context protocol server enabling AI systems to securely interact with external data sources and tools.**

**Key Features:**
- Custom search engine integration
- Secure API access for AI models
- Automated workflow automation
- Code review and change tracking
- Integration with external tools and services
- Enterprise security and compliance

---

### 262. [roland0511/mcp-feishu-proj](https://github.com/roland0511/mcp-feishu-proj)  `innovation: 9`

**A software development platform enabling AI-assisted management of project workflows using the MCP protocol.**

**Key Features:**
- MCP Server implementation for secure API access
- AI-powered assistant integration via MCP protocol
- Workflow automation and task management
- Code review and change tracking
- Secure code deployment and protection
- Integration with external tools and CI/CD pipelines

---

### 263. [sage-hq/agentcortex-mcp](https://github.com/sage-hq/agentcortex-mcp)  `innovation: 9`

**AI memory system that maintains isolated, persistent contexts for each project to prevent context bleed.**

**Key Features:**
- Project context separation per codebase
- Persistent cross-session memory
- Automatic project detection and context switching
- Cumulative learning and intelligent importance ranking

---

### 264. [sdiehl/sympy-mcp](https://github.com/sdiehl/sympy-mcp)  `innovation: 9`

**A server-based platform for enabling LLMs to perform symbolic mathematics and complex algebra, enhancing AI-driven computation.**

**Key Features:**
- Symbolic manipulation of mathematical expressions
- Integration with MCP (Model Context Protocol) for advanced algebra
- Support for differential equations and general relativity calculations
- Custom metric creation and tensor operations
- LaTeX support for mathematical notation
- Standalone executable server for on-demand computation

---

### 265. [stefanoamorelli/fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server)  `innovation: 9`

**A robust, open-source FRED MCP Server enabling secure and efficient access to Federal Reserve Economic Data for analytical applications.**

**Key Features:**
- Secure API key integration for protected data access
- Three powerful tools for browsing
- searching
- and retrieving economic time series
- Support for custom transformations and date range filtering
- Real-time updates and interactive visualization capabilities
- Scalable architecture supporting enterprise-grade security

---

### 266. [steveyegge/beads](https://github.com/steveyegge/beads)  `innovation: 9`

**Beads Context Tracker**

**Key Features:**
- Graph-based dependency tracking
- Semantic memory compaction
- Stateless session support
- Dolt-backed versioned state.

---

### 267. [sunwood-ai-labs/ideagram-mcp-server](https://github.com/sunwood-ai-labs/ideagram-mcp-server)  `innovation: 9`

**Ideogram MCP Server enables secure, context-aware image generation via the Model Context Protocol, integrating AI models with MCP clients for enterprise-grade workflow automation.**

**Key Features:**
- MCP Server Integration
- AI-Powered Image Generation
- Secure API Communication
- Custom Prompt Handling
- Scalable Deployment & CI/CD Support

---

### 268. [sunwood-ai-labs/source-sage-mcp-server](https://github.com/sunwood-ai-labs/source-sage-mcp-server)  `innovation: 9`

**SourceSage MCP Server is a context-aware, AI-powered platform that integrates advanced security features and developer tools to streamline software development workflows.**

**Key Features:**
- Markdown-based visualization of project directory structure
- Automatic file content documentation with language-specific syntax highlighting
- Flexible exclusion patterns via .SourceSageignore
- Customizable file filtering and content generation
- Integration with ES2022 and Node.js 16 modules
- Secure development environment with enterprise-grade security features

---

### 269. [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp)  `innovation: 9`

**Connect Supabase projects to AI assistants via the Model Context Protocol (MCP) for seamless integration.**

**Key Features:**
- Connect Supabase to AI assistants like Claude and Windsurf
- Manage prompts
- code reviews
- and workflows
- Secure code as you build with enterprise-grade security
- Automate workflows and deploy intelligent apps
- Integrate external tools and manage CI/CD pipelines

---

### 270. [szeider/mcp-solver](https://github.com/szeider/mcp-solver)  `innovation: 9`

**A model context protocol server enabling AI models to interactively solve constraint problems using large language models.**

**Key Features:**
- Constraint solving in MiniZinc
- PySAT
- Z3
- and ASP
- Integration with LLMs via Model Context Protocol
- Support for SAT
- SMT
- and ASP problem types
- Interactive problem formulation and solution generation
- Model training and deployment capabilities

---

### 271. [szowesgad/mcp-server-semgrep](https://github.com/szowesgad/mcp-server-semgrep)  `innovation: 9`

**A model context protocol-compliant server integrating Semgrep with AI assistants for advanced code analysis and security.**

**Key Features:**
- Model Context Protocol compliance
- Integration with Semgrep static analysis tool
- AI-assisted code review via Anthropic Claude
- Automated vulnerability detection
- Security rule customization
- Live documentation and explanations

---

### 272. [tejpalvirk/contextmanager](https://github.com/tejpalvirk/contextmanager)  `innovation: 9`

**A collection of Model Context Protocol (MCP) servers to enhance AI models with persistent context across work sessions.**

**Key Features:**
- Persistent context management across sessions
- Unified access to domain-specific knowledge graphs
- Cross-domain relationship creation and maintenance
- Session-based state tracking and synchronization
- Integrated priority and sequencing for complex workflows

---

### 273. [vgiri2015/ai-spark-mcp-server](https://github.com/vgiri2015/ai-spark-mcp-server)  `innovation: 9`

**A model context protocol (MCP) server and client for intelligent Spark code optimization.**

**Key Features:**
- Model Context Protocol (MCP) integration
- AI-driven code optimization
- Real-time performance analysis
- Automated code transformation
- Validation and reporting

---

### 274. [wondermuttt/gtmcp](https://github.com/wondermuttt/gtmcp)  `innovation: 9`

**A Borg intelligence platform integrating MCP course data with ChatGPT for academic research and workflow automation.**

**Key Features:**
- ChatGPT integration via HTTP API
- Course scheduling and subject lookup
- Course details and seat availability
- Research paper and faculty matching
- Automated setup and deployment scripts

---

### 275. [xiaolaa2/midi-file-mcp](https://github.com/xiaolaa2/midi-file-mcp)  `innovation: 9`

**A powerful MIDI file parsing and manipulation tool based on Tone.js, enabling AI assistants to read, analyze, and modify MIDI files without complexities.**

**Key Features:**
- Read MIDI file information
- Get and modify track
- note
- control change
- and pitch bend information
- Set MIDI file tempo (BPM)
- Add new notes to specific tracks
- Add new tracks
- Add control changes to specific tracks
- Add pitch bends to specific tracks

---

### 276. [xtellect/cactus](https://github.com/xtellect/cactus)  `innovation: 9`

**A lightweight parallel recursion runtime for C that optimizes task distribution and load balancing across CPU cores.**

**Key Features:**
- Work-stealing parallelism with automatic load balancing
- Fork-join parallelism with BEGIN/FORK/JOIN macros
- Random-victim work stealing for efficient resource sharing
- Continuation-passing model for seamless thread communication
- Stack slab pooling for memory efficiency and performance
- Direct register manipulation for low-overhead context switching
- Compiler-agnostic support for GCC/Clang with C11

---

### 277. [z-libs/Zen-C](https://github.com/z-libs/Zen-C)  `innovation: 9`

**Zen C is a modern systems programming language designed for high-performance, secure, and maintainable software development.**

**Key Features:**
- Type inference and static analysis
- Pattern matching and functional programming constructs
- Generics and traits for type-safe abstractions
- Async/await support for non-blocking I/O
- Manual memory management with RAII
- Portable Executable (APE) support
- Cross-platform compilation to multiple architectures
- Integrated standard library with extensive functionality

---

### 278. [zabaglione/mcp-server-unity](https://github.com/zabaglione/mcp-server-unity)  `innovation: 9`

**A Unity MCP Server enabling Claude to interact with Unity projects.**

**Key Features:**
- Unity MCP Server integration
- Natural language script creation
- Shader management (e.g.
- water effects)
- Project organization tools
- Automated build and deployment
- Secure
- isolated AI interaction

---

### 279. [zhengwanbo/oracle-mcp-server](https://github.com/zhengwanbo/oracle-mcp-server)  `innovation: 9`

**A powerful Model Context Protocol server that enhances AI assistants' understanding of large Oracle databases by providing contextual schema information, enabling accurate and efficient database interactions.**

**Key Features:**
- Smart Schema Caching
- Targeted Schema Lookup
- Table Search
- Relationship Mapping
- Database Vendor Information
- Oracle Database Support

---

### 280. [ziyadmir/nba-player-stats-mcp](https://github.com/ziyadmir/nba-player-stats-mcp)  `innovation: 9`

**A Model Context Protocol server for retrieving comprehensive NBA player statistics from basketball-reference.com.**

**Key Features:**
- Model Context Protocol (MCP) server integration
- Comprehensive NBA player statistics
- Career stats
- season comparisons
- advanced metrics
- Player performance analysis tools
- Historical data access and projections

---

### 281. [olaservo/shannon-thinking](https://github.com/olaservo/shannon-thinking)  `innovation: 8.5`

**A tool designed to apply Claude Shannon-inspired problem-solving methodology for structured thinking and systematic problem resolution.**

**Key Features:**
- Claude Shannon-inspired problem breakdown
- Structured thought process with problem definition
- constraints
- modeling
- proof
- implementation
- Integration of theoretical and practical validation

---

### 282. [szeider/mcp-dblp](https://github.com/szeider/mcp-dblp)  `innovation: 8.5`

**A model context protocol server integrating DBLP bibliography for LLM applications.**

**Key Features:**
- Model context protocol integration
- DBLP bibliography access
- BibTeX generation
- Search and filtering tools
- Code execution environment

---

### 283. [vinayaktiwari1103/mcp-smallest-ai](https://github.com/vinayaktiwari1103/mcp-smallest-ai)  `innovation: 8.5`

**A model context protocol server for integrating Smallest.ai knowledge bases into applications.**

**Key Features:**
- MCP Server Integration
- Client Application Layer
- API Communication Middleware
- Error Handling & Validation
- Knowledge Base Management Tools

---

### 284. [zundamonnovrchatkaisetu/unity-mcp-ollama](https://github.com/zundamonnovrchatkaisetu/unity-mcp-ollama)  `innovation: 8.5`

**A Unity MCP package enabling local Large Language Model integration for automated Unity development workflows.**

**Key Features:**
- Asset Management
- Scene Control
- Material Editing
- Script Integration
- Automation
- Editor Automation

---

### 285. [0xdwong/sui-mcp](https://github.com/0xdwong/sui-mcp)  `innovation: 8`

**A tool for interacting with the Sui blockchain using MCP SDK, supporting multiple network environments.**

**Key Features:**
- Deep integration with Sui blockchain
- Support for multiple network environments
- TypeScript-based development
- Code analysis and security tools
- CI/CD automation

---

### 286. [0xhijo/mcp_twitter](https://github.com/0xhijo/mcp_twitter)  `innovation: 8`

**A TypeScript-based Model Context Protocol enabling AI applications to interact with Twitter/X securely and efficiently.**

**Key Features:**
- Create Twitter posts
- Reply to specific tweets
- Retrieve recent tweets
- Manage user profiles
- Fetch tweet history and replies
- Follow users
- Get user profile data
- View account information

---

### 287. [1595901624/qrcode-mcp](https://github.com/1595901624/qrcode-mcp)  `innovation: 8`

**A Model Context Protocol (MCP) server for generating simple QR codes with custom styles.**

**Key Features:**
- Support custom QR code styles
- Easy installation via Smithery
- Automated build and deployment
- Customizable parameters (text
- size
- color)

---

### 288. [1panel-dev/mcp-1panel](https://github.com/1panel-dev/mcp-1panel)  `innovation: 8`

**MCP Server implementation for 1Panel enabling secure, protocol-based communication.**

**Key Features:**
- Model Context Protocol (MCP) server
- Secure communication channels
- Integration with 1Panel
- Customizable configurations

---

### 289. [54yyyu/school-mcp](https://github.com/54yyyu/school-mcp)  `innovation: 8`

**A model context protocol server integrating academic tools with Canvas and Gradescope.**

**Key Features:**
- Integration with Canvas and Gradescope
- Deadline fetching and calendar sync
- File management and downloads
- Environment setup and configuration
- Automated reminders and notifications

---

### 290. [66julienmartin/mcp-server-deepseek_r1](https://github.com/66julienmartin/mcp-server-deepseek_r1)  `innovation: 8`

**A server implementation enabling seamless integration of DeepSeek language models with Claude Desktop for advanced AI-driven interactions.**

**Key Features:**
- MCP server integration
- DeepSeek R1/V3 model support
- Node.js/TypeScript stack
- Docker containerization
- Custom model configuration
- Error handling and logging

---

### 291. [7gugu/zip-mcp](https://github.com/7gugu/zip-mcp)  `innovation: 8`

**A MCP tool enabling AI to compress and decompress local files with advanced security and metadata support.**

**Key Features:**
- Compression and decompression of files and data
- Parameter-controlled compression levels (0-9)
- Password protection and encryption settings
- Query function for compressed package metadata
- Support for multi-file packaging
- Integration with AI models via MCP protocol

---

### 292. [AbanteAI/LoCoDiff-bench](https://github.com/AbanteAI/LoCoDiff-bench)  `innovation: 8`

**LoCoDiff-bench is a benchmark designed to evaluate language models' ability to understand and reconstruct code based on a series of Git history changes within long contexts.**

**Key Features:**
- Natural Git history evaluation
- No junk context methodology
- Long-form output testing
- Procedural benchmark generation from any Git repository
- Simple prompt/output evaluation structure.

---

### 293. [BytexGrid/NeatShift](https://github.com/BytexGrid/NeatShift)  `innovation: 8`

**A modern Windows file organization tool with symbolic link support.**

**Key Features:**
- Relocate files and folders without breaking application paths. Smart Moving: Move files anywhere
- and NeatShift creates symbolic links so everything still works. Double Safety: Choose between NeatSaves quick backup or system restore points - or use both! Looks Good
- Feels Good: Modern Windows 11 style with both light and dark themes. Stay in Control: See and manage all of the symbolic links in one place.

---

### 294. [CH-122/mcp-server](https://github.com/CH-122/mcp-server)  `innovation: 8`

**A Borg project demonstrating MCP-based multi-functional server implementations for database search, GitHub search, and time management.**

**Key Features:**
- Database Search with natural language query support
- GitHub Search for repositories
- users
- and issues
- Time Management with current time and time zone conversion
- Integration with MCP protocol for secure client-server communication

---

### 295. [ChanMeng666/server-google-news](https://github.com/ChanMeng666/server-google-news)  `innovation: 8`

**A cloud-based MCP server enabling AI-driven Google News search with multilingual support and structured data output.**

**Key Features:**
- Automatic news categorization
- Multi-language support
- SerpAPI integration
- Structured JSON output
- AI-friendly API endpoints

---

### 296. [Edison-Watch/open-edison](https://github.com/Edison-Watch/open-edison)  `innovation: 8`

**Borg intelligence database focused on securing and monitoring agent data interactions to prevent exfiltration.**

**Key Features:**
- Data leak monitoring
- Controlled execution (to reduce exfiltration risks)
- Visibility into agent interactions
- Simple API for managing MCP servers
- Docker support
- Quick integration with LangGraph/Python agents.

---

### 297. [IlyaGusev/academia_mcp](https://github.com/IlyaGusev/academia_mcp)  `innovation: 8`

**A comprehensive open-source platform for automated scientific research, integrating web search, document analysis, and LLM-powered tools to streamline research workflows.**

**Key Features:**
- Web search across multiple sources (arXiv
- ACL Anthology
- Hugging Face
- etc.)
- LLM-powered document understanding and QA
- Token-based authentication for secure API access
- Integration with Docker and CI/CD pipelines
- LaTeX compilation and PDF generation
- Code review and security scanning
- Workflow automation and project management tools

---

### 298. [Korfu/mcp-bitbucket](https://github.com/Korfu/mcp-bitbucket)  `innovation: 8`

**Integrates Bitbucket with Cursor IDE to enable seamless repository and commit data access for users without GitHub.**

**Key Features:**
- Fetch repositories from Bitbucket
- View detailed repository information
- Retrieve commit history and latest commit details
- Manage branch restrictions
- Access pull requests and project details
- Integrate with Cursor IDE for enhanced development workflow

---

### 299. [OfficialIncubo/BeatDrop-Music-Visualizer](https://github.com/OfficialIncubo/BeatDrop-Music-Visualizer)  `innovation: 8`

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

### 300. [Paul-Bonneville-Labs/neemee-mcp](https://github.com/Paul-Bonneville-Labs/neemee-mcp)  `innovation: 8`

**A TypeScript client library for integrating with Neemee MCP servers, enabling secure and efficient management of personal knowledge systems.**

**Key Features:**
- TypeScript support
- HTTP/STDIO transport modes
- API access to MCP tools and resources
- Secure authentication and error handling

---

### 301. [Roobyx/awesome-game-design](https://github.com/Roobyx/awesome-game-design)  `innovation: 8`

**A comprehensive list of Game Design related learning materials, examples and tools.**

**Key Features:**
- A curated collection of Game Design documents
- templates
- learning materials
- and tools. Focus on bridging the gap between artistic vision (game design) and technical implementation (programming/tools).

---

### 302. [SembojaTech/mcp-postgres](https://github.com/SembojaTech/mcp-postgres)  `innovation: 8`

**A model context protocol server enabling LLMs to inspect and query PostgreSQL databases securely.**

**Key Features:**
- Read-only access to PostgreSQL databases
- Schema inspection for LLMs
- Execute read-only SQL queries
- Automatic database metadata discovery

---

### 303. [SuperSonicHub1/awesome-libsm64](https://github.com/SuperSonicHub1/awesome-libsm64)  `innovation: 8`

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

### 304. [XeroOl/mirin-template](https://github.com/XeroOl/mirin-template)  `innovation: 8`

**The NotITG Mirin Template. Easily create modfiles using Lua.**

**Key Features:**
- Easy creation of modfiles using Lua. Powerful abstractions allowing users to create custom modifiers (e.g.
- turn on invert ease {0
- 1
- outExpo
- 100
- 'invert'}). Optimized code execution. Theme independent design. Powerful system for custom modifiers.

---

### 305. [a2xdeveloper/tagesschau-mcp-server](https://github.com/a2xdeveloper/tagesschau-mcp-server)  `innovation: 8`

**An MCP server for accessing and managing news articles from the tagesschau platform.**

**Key Features:**
- Fetch latest news articles
- Retrieve detailed article information
- Integrate news data into applications

---

### 306. [adamamer20/paper-search-mcp-openai](https://github.com/adamamer20/paper-search-mcp-openai)  `innovation: 8`

**A Python-based MCP server for searching and downloading academic papers from multiple sources, enabling seamless integration with LLMs.**

**Key Features:**
- Multi-source paper search (arXiv
- PubMed
- bioRxiv
- etc.)
- Asynchronous HTTP requests using httpx
- Standardized output in dictionary format via Paper class
- Support for LLM context enhancement with MCP clients like Claude Desktop
- Extensible design for adding new academic platforms

---

### 307. [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)  `innovation: 8`

**A Model Context Protocol server for programmatically exploring GitHub repositories.**

**Key Features:**
- Clone repositories from GitHub
- Generate structured directory trees
- Read and parse important files (e.g.
- README.md)
- Handle file reading errors gracefully
- Clean up temporary directories after processing

---

### 308. [agent-kilo/jwno](https://github.com/agent-kilo/jwno)  `innovation: 8`

**A tiling window manager for Windows 10/11, built with Janet and ❤️.**

**Key Features:**
- Tiling window manager for Windows 10/11
- built with Janet and ❤️.

---

### 309. [agentclientprotocol/agent-client-protocol](https://github.com/agentclientprotocol/agent-client-protocol)  `innovation: 8`

**A protocol for connecting any editor to any agent.**

**Key Features:**
- Standardizing communication between code editors and coding agents. Providing a protocol layer for connecting any editor to any agent.

---

### 310. [akramsaouri/mcp-translate](https://github.com/akramsaouri/mcp-translate)  `innovation: 8`

**A platform for translating text using the Model Context Protocol.**

**Key Features:**
- translate_text
- model_context_protocol
- api_integration
- customizable_translation_rules

---

### 311. [al-how/supernotes-to-obsidian](https://github.com/al-how/supernotes-to-obsidian)  `innovation: 8`

**Automates the import of Supernotes notes into Obsidian daily using MCP.**

**Key Features:**
- Import Supernotes exports into Obsidian daily
- Automate note creation and formatting
- Handle OCR errors and wikilinks
- Clean up note templates
- Integrate with MCP

---

### 312. [aleksey-saenko/MusicRecognizer](https://github.com/aleksey-saenko/MusicRecognizer)  `innovation: 8`

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

### 313. [alekspetrov/mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)  `innovation: 8`

**MCP Documentation Service enables AI-assisted management of documentation through natural language interactions.**

**Key Features:**
- Read and write markdown documents with frontmatter metadata
- Edit documents with precise line-based changes
- List and search documents by content or metadata
- Generate navigation structures from documentation
- Analyze documentation quality and identify issues
- LLM-optimized documentation output for large language models

---

### 314. [alex-llm/attAck-mcp-server](https://github.com/alex-llm/attAck-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server that enables querying of ATT&CK techniques and tactics for security analysis.**

**Key Features:**
- Query ATT&CK techniques by ID or name
- Search with name or partial match
- View detailed information including kill chain stages
- mitigations
- and references
- List all ATT&CK tactics
- Provide mitigation strategies for each technique

---

### 315. [allglenn/mcp-name-origin-server](https://github.com/allglenn/mcp-name-origin-server)  `innovation: 8`

**A Python-based MCP server for predicting the origin of names using external APIs.**

**Key Features:**
- Predict name origin
- Batch prediction
- Real-time API integration
- Secure code deployment
- Automated workflows

---

### 316. [alperenkocyigit/authorprofilemcp](https://github.com/alperenkocyigit/authorprofilemcp)  `innovation: 8`

**A Model Context Protocol server for analyzing academic author networks and research collaborations.**

**Key Features:**
- get_coauthors
- get_author_keywords
- data integration from multiple APIs
- async operations
- rate limiting
- error handling

---

### 317. [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube)  `innovation: 8`

**A model-context protocol server for integrating AI models with YouTube content.**

**Key Features:**
- Model-context protocol server
- YouTube subtitle extraction
- AI integration with Claude AI
- Secure code management
- Automated deployment tools

---

### 318. [andradehenrique/dokploy-mcp](https://github.com/andradehenrique/dokploy-mcp)  `innovation: 8`

**A tool-based platform for programmatic interaction with Dokploy server functionalities via the Model Context Protocol (MCP).**

**Key Features:**
- Expose Dokploy APIs as consumable tools via MCP
- Support multiple transport modes (stdio
- HTTP
- SSE)
- Provide flexible deployment options (Docker
- Windows
- etc.)
- Enable secure and isolated client-server communication

---

### 319. [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver)  `innovation: 8`

**A MCP server enabling Claude to access real-time time, holiday information, and date calculations across multiple regions.**

**Key Features:**
- Get current local time with timezone support
- Check public and school holidays by country or city
- Calculate time distance between dates (days
- weeks
- etc.)
- Provide business-day counts excluding holidays
- Integrate location-based time context

---

### 320. [angrysky56/mcp-rocq](https://github.com/angrysky56/mcp-rocq)  `innovation: 8`

**A Coq-based reasoning server enabling automated verification and proof generation for formal software development.**

**Key Features:**
- Automated Dependent Type Checking
- Inductive Type Definition
- Property Proving
- XML Protocol Integration
- Rich Error Handling

---

### 321. [anycontext-ai/thingsboard-mcp-server](https://github.com/anycontext-ai/thingsboard-mcp-server)  `innovation: 8`

**Server for integrating Thingsboard data as context in LLM tools.**

**Key Features:**
- Integrate Thingsboard data
- Contextual enrichment for LLMs
- Secure API access
- Scalable deployment options

---

### 322. [ap425q/cuttermcp](https://github.com/ap425q/cuttermcp)  `innovation: 8`

**A platform enabling LLMs to reverse engineer applications using MCP protocol.**

**Key Features:**
- MCP Server
- Cutter Plugin Decompiler
- Code Analysis Tools
- Integration with Cutter
- Automated Workflow Execution

---

### 323. [apache/iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server)  `innovation: 8`

**IoTDB MCP Server enables secure, scalable database interaction and business intelligence for IoT data using Apache IoTDB.**

**Key Features:**
- Database interaction via SQL queries
- Support for Tree Model and Table Model dialects
- Query execution with metadata and statistics
- Data export to CSV or Excel
- Schema exploration and table description
- Performance optimizations including connection pooling and fetch size management

---

### 324. [apoorvv/mcp-claude-enhancements](https://github.com/apoorvv/mcp-claude-enhancements)  `innovation: 8`

**Enhancing Claude Desktop with MCP for local file access and interaction.**

**Key Features:**
- Leave Policy Lookup
- Conversation Saver
- File Counter

---

### 325. [appleinmusic/baidu-search-mcp](https://github.com/appleinmusic/baidu-search-mcp)  `innovation: 8`

**A Borg project integrating Baidu Search MCP for intelligent search capabilities.**

**Key Features:**
- Integrate Baidu TextMind API
- Support multiple AI models
- Provide search results with sources
- Enable deep search and time filtering

---

### 326. [aquarius-wing/actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)  `innovation: 8`

**Advanced dual-perspective analysis platform for performance evaluation.**

**Key Features:**
- dual-perspective analysis
- actor-critic methodology
- comprehensive evaluation
- balanced assessment
- actionable feedback

---

### 327. [arjunkmrm/perplexity-search](https://github.com/arjunkmrm/perplexity-search)  `innovation: 8`

**A lightweight Model Context Protocol server enabling AI assistants to perform web searches with enhanced context handling.**

**Key Features:**
- Model Context Protocol server
- Perplexity API integration
- Search results filtering (by recency)
- Context-aware search results

---

### 328. [artemsvit/figma-mcp-pro](https://github.com/artemsvit/figma-mcp-pro)  `innovation: 8`

**AI-powered Figma design analysis and code generation tool for enterprise development.**

**Key Features:**
- AI-optimized design-to-code conversion
- Framework-specific data extraction
- Smart comment-to-element mapping
- Asset batch downloads
- Reference image analysis
- Responsive layout processing
- Customizable configuration files

---

### 329. [askme765cs/open-docs-mcp](https://github.com/askme765cs/open-docs-mcp)  `innovation: 8`

**Open-source MCP implementation for document management and indexing.**

**Key Features:**
- Document indexing
- Full-text search capabilities
- Resource-based access
- Tool-based document management
- Custom docs management via enable_doc tool

---

### 330. [asyncfuncai/github-chat-mcp](https://github.com/asyncfuncai/github-chat-mcp)  `innovation: 8`

**A Model Context Protocol for analyzing and querying GitHub repositories using the GitHub Chat API.**

**Key Features:**
- Repository Indexing
- Repository Querying

---

### 331. [athapong/argus](https://github.com/athapong/argus)  `innovation: 8`

**A Model Context Protocol server for analyzing GitLab repositories and performing security assessments.**

**Key Features:**
- multi-language support
- security scanning
- code quality analysis
- commit history analysis
- branch enumeration
- diff comparisons
- repository visualization

---

### 332. [auto-browse/unbundle_openapi_mcp](https://github.com/auto-browse/unbundle_openapi_mcp)  `innovation: 8`

**A tool for programmatically splitting and extracting OpenAPI specifications into smaller files, enabling modular development and maintenance.**

**Key Features:**
- Unbundle large OpenAPI specs
- Extract specific endpoints
- Split OpenAPI definitions
- Generate smaller
- focused OpenAPI files

---

### 333. [awslabs/mcp](https://github.com/awslabs/mcp)  `innovation: 8`

**A suite of specialized MCP servers for AWS to enhance AI applications with contextual data and best practices.**

**Key Features:**
- Improved output quality through context integration
- Access to the latest documentation and API references
- Automation of common workflows
- Secure
- auditable interactions with AWS services

---

### 334. [axiomhq/mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom)  `innovation: 8`

**A model context protocol server enabling AI agents to query Axiom datasets using APL.**

**Key Features:**
- Model Context Protocol Server
- APL query execution
- Dataset management
- Monitoring configurations
- Secure token-based authentication

---

### 335. [azer/react-analyzer-mcp](https://github.com/azer/react-analyzer-mcp)  `innovation: 8`

**Analyzes React code to extract component structure and metadata for documentation.**

**Key Features:**
- Analyze React components
- Generate documentation
- Integrate with Claude
- Support MCP server

---

### 336. [bartekke8it56w2/new-mcp](https://github.com/bartekke8it56w2/new-mcp)  `innovation: 8`

**A context-aware MCP implementation integrating Gemini for analytical thinking and problem-solving.**

**Key Features:**
- Gemini-powered thinking
- Thought branching
- Session persistence
- Advanced filtering

---

### 337. [bartwisch/mcprules](https://github.com/bartwisch/mcprules)  `innovation: 8`

**A powerful Model Context Protocol server managing programming guidelines and rules for consistent coding standards.**

**Key Features:**
- Rule Management
- Rule Filtering by Category
- Markdown-based Rule Definitions
- Local and GitHub Repository Support
- Integration with IDEs like VSCode
- Rule Export and Configuration

---

### 338. [behole/cooper-hewitt-mcp](https://github.com/behole/cooper-hewitt-mcp)  `innovation: 8`

**A model context protocol server for interacting with the Cooper Hewitt Collection API.**

**Key Features:**
- Search objects in the Cooper Hewitt collection
- Retrieve detailed information about museum objects
- Integrate with external tools and APIs
- Support for automated workflows and code execution

---

### 339. [bengineer19/digikey_mcp](https://github.com/bengineer19/digikey_mcp)  `innovation: 8`

**A MCP server for DigiKey's Product Search API, enabling secure and efficient integration with DigiKey's product data.**

**Key Features:**
- MCP Server Integration
- Product Search API Access
- Secure Authentication
- Customizable Commands

---

### 340. [berlinbra/binary-reader-mcp](https://github.com/berlinbra/binary-reader-mcp)  `innovation: 8`

**A server for reading and analyzing binary files, supporting Unreal Engine asset files and custom formats.**

**Key Features:**
- Read Unreal Engine asset files
- Read generic binary files
- Extract binary file metadata
- Auto-detect file formats
- Support extensibility for new formats

---

### 341. [bigsy/clojars-mcp-server](https://github.com/bigsy/clojars-mcp-server)  `innovation: 8`

**A model context protocol server for fetching Clojars dependency information.**

**Key Features:**
- Get the latest version of a Clojars dependency
- Check if a specific version of a dependency exists
- View version history with configurable limits
- Integrate with Claude Desktop for easy dependency management

---

### 342. [bigsy/shadow-cljs-mcp](https://github.com/bigsy/shadow-cljs-mcp)  `innovation: 8`

**A Model Context Protocol server for monitoring and managing shadow-cljs builds.**

**Key Features:**
- Model Context Protocol server
- Build status tracking
- Real-time updates
- Code verification integration

---

### 343. [billduke13/code-explainer-mcp](https://github.com/billduke13/code-explainer-mcp)  `innovation: 8`

**A Cloudflare Worker that provides code explanation and context for developers.**

**Key Features:**
- Code Explainer
- Architecture Visualization
- Multi-language Support
- Secure API with Bearer Token

---

### 344. [blackhole89/autopen](https://github.com/blackhole89/autopen)  `innovation: 8`

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

### 345. [blazickjp/shell-mcp-server](https://github.com/blazickjp/shell-mcp-server)  `innovation: 8`

**Secure shell command execution MCP server for Claude AI, enabling controlled access within specified directories.**

**Key Features:**
- Secure shell execution within specified directories
- Multiple shell support (bash
- sh
- cmd
- powershell)
- Timeout control for command execution
- Cross-platform compatibility (Unix and Windows)
- Directory and shell validation to prevent traversal attacks

---

### 346. [block/square-mcp](https://github.com/block/square-mcp)  `innovation: 8`

**A server-based implementation for accessing Square API functionality via Model Context Protocol.**

**Key Features:**
- Square Model Context Protocol Server
- API access via MCP
- Environment setup and configuration
- Security token management
- Migration to new server version

---

### 347. [bmaltais/kohya_ss](https://github.com/bmaltais/kohya_ss)  `innovation: 8`

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

### 348. [bootcamptoprod/spring-boot-ai-confluence-mcp-server](https://github.com/bootcamptoprod/spring-boot-ai-confluence-mcp-server)  `innovation: 8`

**A Spring Boot AI-powered Model Context Protocol Server for Confluence Cloud integration.**

**Key Features:**
- Spring Boot AI-powered Model Context Protocol Server
- Confluence Cloud integration
- Callable tools for document management
- Tool registration and testing

---

### 349. [brandon-butterwick/mrp_calculation](https://github.com/brandon-butterwick/mrp_calculation)  `innovation: 8`

**A tool for performing Material Requirements Planning (MRP) calculations using the Model Context Protocol (MCP).**

**Key Features:**
- MRP calculation
- Order need determination
- MRP period calculations
- Configuration via MCP settings file
- Validation and testing

---

### 350. [brockreece/whimsical-mcp-server](https://github.com/brockreece/whimsical-mcp-server)  `innovation: 8`

**A server enabling the creation of whimsical diagrams from LLM context using MCP protocol.**

**Key Features:**
- Whimsical diagram creation
- MCP protocol integration
- LLM context processing
- Code generation support
- Secure deployment options

---

### 351. [bsmi021/mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)  `innovation: 8`

**A Model Context Protocol server enabling LLMs to access and analyze code files with advanced caching and real-time monitoring.**

**Key Features:**
- File operations
- Real-time file watching
- Advanced caching
- Code analysis
- Quality metrics

---

### 352. [bsmi021/mcp-node-omnibus-server](https://github.com/bsmi021/mcp-node-omnibus-server)  `innovation: 8`

**A comprehensive Model Context Protocol (MCP) server offering advanced Node.js development tooling and automation.**

**Key Features:**
- Project Management
- Project Creation
- TypeScript Integration
- Component Generation
- Configuration Management
- AI-Powered Assistance
- Code Analysis & Improvements
- Documentation Generation

---

### 353. [bsmi021/mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)  `innovation: 8`

**A local Model Context Protocol (MCP) server enabling client-driven project and task management with SQLite persistence.**

**Key Features:**
- Project-based task organization
- SQLite database for data persistence
- MCP protocol compliance
- Client-driven workflow tools
- Task creation
- listing
- updating
- and subtask expansion

---

### 354. [buga-luga/cursor-mcp](https://github.com/buga-luga/cursor-mcp)  `innovation: 8`

**A tool enabling seamless integration between Claude AI and desktop applications via Cursor IDE.**

**Key Features:**
- Real-time AI assistance in development
- Context-aware code completions
- Desktop integration with Claude AI
- Automation of development workflows
- Environment configuration via .env file

---

### 355. [buhe/mcp_rss](https://github.com/buhe/mcp_rss)  `innovation: 8`

**MCP RSS enables secure and efficient interaction with RSS feeds using a Model Context Protocol.**

**Key Features:**
- Parse OPML files
- Automatically fetch RSS updates
- Mark articles as favorites
- Filter articles by source and status

---

### 356. [callebtc/bitchat-android](https://github.com/callebtc/bitchat-android)  `innovation: 8`

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

### 357. [cappahccino/sb-mcp](https://github.com/cappahccino/sb-mcp)  `innovation: 8`

**A model context protocol server enabling secure, isolated database interactions for AI models like Claude.**

**Key Features:**
- Database CRUD operations via MCP
- Secure integration with Supabase Postgres
- Support for edge functions and CLI tools
- Environment configuration and deployment options

---

### 358. [cc-apk/mobsf-mcp](https://github.com/cc-apk/mobsf-mcp)  `innovation: 8`

**Node.js-based Model Context Protocol implementation for MobSF security analysis.**

**Key Features:**
- MobSF MCP integration
- Automated security scanning
- API-driven analysis endpoints
- Report generation and visualization
- Integration with third-party tools

---

### 359. [cdmx-in/authentik-mcp](https://github.com/cdmx-in/authentik-mcp)  `innovation: 8`

**A comprehensive GitHub repository providing MCP server implementations for Authentik API integration, including diagnostic, monitoring, and management tools.**

**Key Features:**
- Full-featured MCP servers (Python
- Node.js)
- Diagnostic and monitoring capabilities
- User and group management
- Application and flow configuration
- System health and security monitoring
- Audit trail and compliance reporting

---

### 360. [champierre/image-mcp-server](https://github.com/champierre/image-mcp-server)  `innovation: 8`

**A server that analyzes images using GPT-4o-mini and OpenAI API.**

**Key Features:**
- Image URL analysis
- Local file path analysis
- OpenAI API integration
- Security and quality monitoring
- Code review and management
- Workflow automation

---

### 361. [chand45/mcp-server-azure-impact-reporting](https://github.com/chand45/mcp-server-azure-impact-reporting)  `innovation: 8`

**A tool for large language models to report impacts on Azure resources using natural language inputs.**

**Key Features:**
- Natural language impact reporting
- Automatic Azure resource parsing
- Support for multiple impact categories
- Integration with Azure Management API
- CLI and GUI support

---

### 362. [chatmol/molecule-mcp](https://github.com/chatmol/molecule-mcp)  `innovation: 8`

**A model-context-protocol server for molecules that enables AI-driven molecule modeling and interaction.**

**Key Features:**
- Model-context-protocol integration
- AI-assisted molecule modeling
- Secure code deployment
- Automated workflows
- Enterprise security

---

### 363. [chris-schra/mcp-funnel](https://github.com/chris-schra/mcp-funnel)  `innovation: 8`

**MCP Funnel Proxy**

**Key Features:**
- Wildcard tool filtering (tree-shaking)
- 40-60% context reduction
- multi-server aggregation
- developer-centric proxy.

---

### 364. [christophenglisch/keycloak-model-context-protocol](https://github.com/christophenglisch/keycloak-model-context-protocol)  `innovation: 8`

**A model context protocol server for managing Keycloak users and realms with AI-powered automation.**

**Key Features:**
- AI-powered administration of Keycloak users and realms
- Integration with Claude Desktop and other MCP clients
- Automated user operations via Model Context Protocol

---

### 365. [clouatre-labs/math-mcp-learning-server](https://github.com/clouatre-labs/math-mcp-learning-server)  `innovation: 8`

**A cloud-hosted educational mathematics server with interactive tools for math operations, matrix algebra, visualization, and persistent workspace.**

**Key Features:**
- math operations
- matrix algebra
- data visualization
- persistent workspace

---

### 366. [cloudflare/workers-sdk](https://github.com/cloudflare/workers-sdk)  `innovation: 8`

**Wrangler, the CLI for Cloudflare Workers®**

**Key Features:**
- Cloudflare Workers SDK
- Wrangler (CLI for Cloudflare Workers)
- Create-Cloudflare (C3) CLI for creating and deploying new applications
- Miniflare simulator for development/testing
- Chrome DevTools fork for inspecting Workers pages.

---

### 367. [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest)  `innovation: 8`

**Codebase Ingestion and LLM Prompt Generation**

**Key Features:**
- ['Codebase Ingestion via URL or directory path.'
- 'Smart Formatting of the extracted content for LLM prompts.'
- 'CLI tool usage (`gitingest`) for analyzing codebases.'
- 'Option to include submodules using `--include-submodules`.'
- 'Customizable output file naming using `--output/-o`.'
- 'Handling private repositories via GitHub PATs (Personal Access Tokens).']

---

### 368. [cognitive-stack/hermes-search-mcp](https://github.com/cognitive-stack/hermes-search-mcp)  `innovation: 8`

**Hermes Search MCP enables secure, type-safe full-text and semantic search over Azure Cognitive Search.**

**Key Features:**
- Full-text and semantic search capabilities
- Type-safe operations with TypeScript
- Integration with Azure Cognitive Search
- Support for structured and unstructured data indexing

---

### 369. [colygon/zkpmcp](https://github.com/colygon/zkpmcp)  `innovation: 8`

**A tool for building and verifying zero-knowledge proofs using Circom, enabling privacy-preserving applications.**

**Key Features:**
- Build circuits from Circom files
- Perform trusted setup for circuits
- Generate proofs for circuits
- Verify proofs

---

### 370. [comet-ml/opik-mcp](https://github.com/comet-ml/opik-mcp)  `innovation: 8`

**Model Context Protocol (MCP) implementation for Opik, enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics.**

**Key Features:**
- Prompt lifecycle management
- Workspace
- project
- and trace exploration
- Metrics and dataset operations
- MCP resources and resource templates for metadata-aware flows

---

### 371. [configcat/mcp-server](https://github.com/configcat/mcp-server)  `innovation: 8`

**A server enabling secure, isolated management of ConfigCat's feature flags and configurations.**

**Key Features:**
- Feature Flags Management
- Environment Configuration
- Integration Support
- Audit Logging

---

### 372. [connerlambden/bgpt-mcp](https://github.com/connerlambden/bgpt-mcp)  `innovation: 8`

**A remote MCP server providing structured access to scientific paper data for AI-driven research and analysis.**

**Key Features:**
- Remote connection via SSE or Streamable HTTP
- Search papers with detailed experimental data
- Structured results including methods
- results
- quality scores
- and metadata

---

### 373. [coop-deluxe/sm64coopdx](https://github.com/coop-deluxe/sm64coopdx)  `innovation: 8`

**An official continuation of https://github.com/djoslin0/sm64ex-coop on sm64coopdx for the enhancements and progress it already has.**

**Key Features:**
- Online multiplayer synchronization of entities and levels
- enhanced capability for modders via the Lua API (similar to Roblox/Garry's Mod)
- community-driven project maintained by the Coop Deluxe Team.

---

### 374. [creis-ai/mcp-property-valuation-server](https://github.com/creis-ai/mcp-property-valuation-server)  `innovation: 8`

**MCP Property Valuation Server provides AI-driven property valuation and small district evaluation for real estate transactions.**

**Key Features:**
- Multi-dimensional small district rating system
- Precise property valuation with detailed analysis
- Secure data handling via APPID authentication
- Standardized Markdown output format

---

### 375. [crisschan/mcp-repo2llm](https://github.com/crisschan/mcp-repo2llm)  `innovation: 8`

**A tool to transform code repositories into formats optimized for large language models.**

**Key Features:**
- Smart Repository Scanning
- Context Preservation
- Multi-language Support
- Metadata Enhancement
- Efficient Processing

---

### 376. [cuongpo/coti-mcp](https://github.com/cuongpo/coti-mcp)  `innovation: 8`

**A blockchain-based platform enabling secure AI interactions with the COTI blockchain using Multi-Party Computation.**

**Key Features:**
- Account management and switching between networks
- Private ERC20 token operations
- Private ERC721 NFT operations
- Transaction management and privacy features
- Secure key generation and encryption

---

### 377. [cyanheads/toolkit-mcp-server](https://github.com/cyanheads/toolkit-mcp-server)  `innovation: 8`

**A Model Context Protocol server providing LLM agents with system utilities and tools.**

**Key Features:**
- IP geolocation
- network diagnostics
- system monitoring
- cryptographic operations
- qr code generation

---

### 378. [da-snap/mcp-server-developer-tool](https://github.com/da-snap/mcp-server-developer-tool)  `innovation: 8`

**A modular Go implementation of the Model Context Protocol server, designed for secure and controlled file operations.**

**Key Features:**
- Path restriction system for file operations
- Configurable allowed and denied paths
- Secure execution of shell commands
- Integration with Go tools and utilities

---

### 379. [daipendency/daipendency-mcp](https://github.com/daipendency/daipendency-mcp)  `innovation: 8`

**Model Context Protocol server for Daipendency enabling secure context management and integration.**

**Key Features:**
- Model Context Protocol server
- Secure context management
- Integration with external tools
- Code review and tracking
- Automated workflows
- Instant dev environments

---

### 380. [damus-io/nostrdb-mcp](https://github.com/damus-io/nostrdb-mcp)  `innovation: 8`

**A Model Context Protocol server enabling LLMs to interface with ndb for local database queries.**

**Key Features:**
- Model Context Protocol server
- Integration with ndb
- LLM-enabled database queries

---

### 381. [dandeliongold/mcp-decent-sampler-drums](https://github.com/dandeliongold/mcp-decent-sampler-drums)  `innovation: 8`

**A Model Context Protocol server for generating DecentSampler drum kit configurations.**

**Key Features:**
- WAV file analysis and validation
- Global pitch and envelope controls
- Multi-mic routing with MIDI controls
- Flexible velocity layer handling
- Muting group support
- Auxiliary output routing
- Documentation and developer tools

---

### 382. [dasheck0/face-generator](https://github.com/dasheck0/face-generator)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling developers to generate realistic human faces with customizable shapes, sizes, and appearances.**

**Key Features:**
- Model Context Protocol (MCP) server integration
- Customizable face generation with various shapes and sizes
- Support for image output in multiple formats
- Integration with VS Code via Cline extension
- Automated build and deployment workflows

---

### 383. [data-skunks/kpu-mcp](https://github.com/data-skunks/kpu-mcp)  `innovation: 8`

**A context-aware developer platform integrating AI and security tools for secure, automated software development workflows.**

**Key Features:**
- AI-powered code generation
- Automated code review
- Workflow automation
- Secure development environment
- Integration with external tools

---

### 384. [davidorex/git-forensics-mcp](https://github.com/davidorex/git-forensics-mcp)  `innovation: 8`

**A specialized MCP server for in-depth git repository analysis, focusing on branch relationships, commit patterns, and development insights.**

**Key Features:**
- Branch Overview
- Time Period Analysis
- File Changes Analysis
- Merge Recommendations

---

### 385. [dazeb/mcp-github-mapper](https://github.com/dazeb/mcp-github-mapper)  `innovation: 8`

**A tool for mapping and analyzing GitHub repositories to provide detailed insights and structure information.**

**Key Features:**
- Map GitHub repositories remotely
- Retrieve repository summary statistics
- Analyze repository structure
- Provide detailed repository file structure

---

### 386. [dcspark/mcp-server-jupiter](https://github.com/dcspark/mcp-server-jupiter)  `innovation: 8`

**A model context protocol server enabling Claude to interact with Jupiter's swap API for blockchain operations.**

**Key Features:**
- MCP server integration
- Claude AI model access
- Swap transaction building/sending
- Node.js installation
- Secure development environment
- Code review and management
- Automation of workflows

---

### 387. [deadletterq/mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)  `innovation: 8`

**A developer platform providing access to a comprehensive food database for nutrition analysis and barcode lookups.**

**Key Features:**
- Access to comprehensive food database
- Nutritional data analysis
- Barcode lookups
- Local development environment

---

### 388. [deepseek-ai/awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration)  `innovation: 8`

**Cherry Studio: A powerful desktop AI assistant for producer.**

**Key Features:**
- Desktop AI assistant functionality
- Integration with Deepseek API
- Clear demonstration of an AI tool/agent framework.

---

### 389. [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server)  `innovation: 8`

**A MCP server that integrates with Postman to provide structured access and management of API collections, environments, and APIs.**

**Key Features:**
- Collection CRUD operations
- Folder and request management
- Environment setup and management
- API key authentication
- Version control and collaboration features
- Webhooks and monitoring integration

---

### 390. [demcp/demcp-debank-mcp](https://github.com/demcp/demcp-debank-mcp)  `innovation: 8`

**A stateless Model Context Protocol (MCP) server for interacting with blockchain and DeFi data.**

**Key Features:**
- Stateless architecture
- Comprehensive DeFi data tools
- Pagination support
- Robust error handling
- Tool integration for blockchain queries

---

### 391. [deshabhishek007/domain-tools-mcp-server](https://github.com/deshabhishek007/domain-tools-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server for comprehensive domain analysis including WHOIS, DNS records, and DNS health checks.**

**Key Features:**
- WHOIS lookup
- DNS record queries
- DNS health checking
- Comprehensive domain assessment
- API integration with MCP protocol

---

### 392. [devonmojito/ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)  `innovation: 8`

**A Python-based MCP server enabling natural language interaction with the TON blockchain.**

**Key Features:**
- Natural Language Processing for blockchain queries
- Trading pattern analysis
- Hot trends detection
- Forensic and compliance tools
- Real-time TON blockchain data access

---

### 393. [dfkai/xtquantai](https://github.com/dfkai/xtquantai)  `innovation: 8`

**xtquantai integrates AI and MCP to enable AI access to quantitative trading data, enhancing decision-making with advanced analytics.**

**Key Features:**
- 基础数据查询
- 获取交易日期
- 获取板块股票列表
- 获取股票详情
- 获取历史行情数据
- 创建图表面板
- 创建自定义布局

---

### 394. [dhkts1/sequentialstory](https://github.com/dhkts1/sequentialstory)  `innovation: 8`

**A Python-based sequential thinking framework for structured problem-solving using narrative techniques.**

**Key Features:**
- Sequential Story tool for narrative-based problem structuring
- Sequential Thinking tool for pure Python implementation
- Integration with AI systems and MCP protocol support
- Development environment setup and pre-commit hooks
- Color-coded display of story elements

---

### 395. [diganto-deb/local_file_organizer](https://github.com/diganto-deb/local_file_organizer)  `innovation: 8`

**A Python-based file organization system using the Model Context Protocol to securely manage and categorize files across directories.**

**Key Features:**
- Directory security with permission checking
- Smart categorization by file type (documents
- images
- videos
- etc.)
- Recursive processing for nested directory structures
- Resource-efficient handling of large directory sets
- Detailed analytics on file distribution by type

---

### 396. [dion-hagan/mcp-server-spinnaker](https://github.com/dion-hagan/mcp-server-spinnaker)  `innovation: 8`

**A Model Context Protocol server enabling AI integration with Spinnaker for intelligent CI/CD operations.**

**Key Features:**
- AI-driven deployment decisions
- proactive issue detection
- continuous process optimization
- automated root cause analysis

---

### 397. [direkt/mcp-test](https://github.com/direkt/mcp-test)  `innovation: 8`

**A tool for creating and managing SQLite databases from compressed log files, enabling integration with MCP Server.**

**Key Features:**
- Create SQLite database from compressed logs
- Interact with database using Model Context Protocol (MCP)
- Extract and parse log data

---

### 398. [dncampo/fiware-mcp-server](https://github.com/dncampo/fiware-mcp-server)  `innovation: 8`

**A first implementation of a FIWARE Model Context Protocol (MCP) server to enable context broker communication.**

**Key Features:**
- Context Broker interaction
- CRUD operations
- Entity publishing/updating
- Stateless HTTP session support
- Integration with external APIs via ngrok

---

### 399. [docherty/contextmgr-mcp](https://github.com/docherty/contextmgr-mcp)  `innovation: 8`

**A context management platform for managing development workflows and tool integrations.**

**Key Features:**
- Socket-based transport with JSON-RPC 2.0 protocol
- Session management and state persistence
- Tool registry and dynamic registration
- Capability negotiation for secure interactions
- Project
- workpackage
- and task management
- QA review workflow support
- Initial setup and development mode configurations

---

### 400. [doggybee/mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)  `innovation: 8`

**A Model Context Protocol server enabling AI access to LeetCode problems, user data, and contest information.**

**Key Features:**
- Access to LeetCode API
- Search problems and daily challenges
- User profile and submission tracking
- Contest ranking and details

---

### 401. [domdomegg/google-documents-mcp.git](https://github.com/domdomegg/google-documents-mcp.git)  `innovation: 8`

**A server enabling secure, isolated access to Google Docs for reading, creating, and editing documents.**

**Key Features:**
- OAuth integration with Google Docs API
- Secure client credentials management
- Cross-platform compatibility (web
- mobile)
- Real-time document synchronization
- Granular access control and permissions

---

### 402. [dreamfactorysoftware/df-mcp](https://github.com/dreamfactorysoftware/df-mcp)  `innovation: 8`

**A self-hosted platform enabling secure, governed API access to enterprise data sources and local LLMs.**

**Key Features:**
- Secured API access
- Role-based access control
- Identity passthrough
- Integration with enterprise applications
- Data governance

---

### 403. [drjforrest/mcp-things3](https://github.com/drjforrest/mcp-things3)  `innovation: 8`

**A Model Context Protocol server for macOS Things3, enabling secure and efficient management of tasks and projects via AppleScript and x-call URLs.**

**Key Features:**
- Create Projects
- Create Todos
- View Tasks
- Complete Tasks
- Search Functionality
- Robust Error Handling
- Secure URL Encoding
- AppleScript Integration
- Validation and Metadata Management

---

### 404. [duhlink/instagram-server-next-mcp](https://github.com/duhlink/instagram-server-next-mcp)  `innovation: 8`

**A modular, type-safe Instagram MCP server built with TypeScript and Node.js, supporting secure media handling and integration with Chrome login sessions.**

**Key Features:**
- Modular architecture
- Type-safe implementation
- Automatic media downloading
- SEO-friendly description generation
- JSON-RPC 2.0 compliant communication

---

### 405. [dweigend/joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling secure note access and integration with AI assistants.**

**Key Features:**
- Model Context Protocol for Joplin
- Integration with AI assistants like Claude
- Secure code management and deployment
- AI development workflow automation
- Enterprise-grade security features

---

### 406. [dxheroes/mcp-devtools](https://github.com/dxheroes/mcp-devtools)  `innovation: 8`

**A suite of Model Context Protocol servers enabling AI assistants to interact with developer tools and services.**

**Key Features:**
- Seamless integration with external tools via MCP
- Extensible framework for custom integrations
- Powerful interactions with AI assistants
- Robust support for Jira and Linear platforms

---

### 407. [dylangroos/nhl-mcp](https://github.com/dylangroos/nhl-mcp)  `innovation: 8`

**An unofficial model context protocol for the NHL API, enabling chat with live games, scores, stats, and teams.**

**Key Features:**
- Live game chat and updates
- Standings and team statistics
- Player biographical and performance data
- Aggregated game scores and status
- Historical data access

---

### 408. [dylangroos/patchright-mcp-lite](https://github.com/dylangroos/patchright-mcp-lite)  `innovation: 8`

**A lightweight MCP server for AI models that enables stealth browser automation to improve integration with AI tools.**

**Key Features:**
- stealth browser automation
- model context protocol integration
- browser navigation and interaction
- content extraction

---

### 409. [edricgsh/Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)  `innovation: 8`

**A secure, context-aware MCP server enabling seamless integration with Readwise Reader API for enriched document management.**

**Key Features:**
- Secure authentication using environment variables
- Document metadata management (save
- list
- update
- delete)
- Tag-based filtering and search
- Rich filtering by location
- category
- tags
- and more

---

### 410. [el-el-san/fal-mcp-server](https://github.com/el-el-san/fal-mcp-server)  `innovation: 8`

**MCP server implementation for AI model context management and video generation.**

**Key Features:**
- AI model context management
- video generation from text prompts
- customizable video parameters
- support for Luma Ray2 and Kling models
- integration with Claude Desktop

---

### 411. [emzimmer/server-moz-readability](https://github.com/emzimmer/server-moz-readability)  `innovation: 8`

**A tool that extracts and transforms webpage content into clean, LLM-optimized Markdown.**

**Key Features:**
- Readability extraction
- Markdown conversion
- Content filtering
- Metadata extraction

---

### 412. [endaoment/endaoment-postgres-mcp](https://github.com/endaoment/endaoment-postgres-mcp)  `innovation: 8`

**A model context protocol server enabling secure, standardized interaction between AI models and PostgreSQL databases.**

**Key Features:**
- Connects to PostgreSQL using connection pooling
- Implements Model Context Protocol for AI model database interactions
- Provides schema information as reusable resources
- Handles SQL queries with retry logic
- Supports graceful shutdown and error handling

---

### 413. [epsilla-cloud/mcp-epsilla](https://github.com/epsilla-cloud/mcp-epsilla)  `innovation: 8`

**A model context protocol implementation using Epsilla tools for secure and efficient data handling.**

**Key Features:**
- Model Context Protocol
- Code review automation
- CI/CD integration
- Secure code management
- External tool integration

---

### 414. [ertiqah/linkedin-mcp-runner](https://github.com/ertiqah/linkedin-mcp-runner)  `innovation: 8`

**A tool that integrates LinkedIn context into AI responses for strategic decision-making.**

**Key Features:**
- Integrate LinkedIn context into AI responses
- Analyze recent LinkedIn activity
- Provide strategic insights based on user engagement
- Support enterprise-level decision-making

---

### 415. [esh2n/mcp-servers](https://github.com/esh2n/mcp-servers)  `innovation: 8`

**MCP servers extending AI model capabilities with tools and resources via the Model Context Protocol.**

**Key Features:**
- Type safety in MCP servers using Deno
- Integration of various tool sets for text
- data
- and API operations
- Modular architecture supporting extensibility and customization
- Support for secure and efficient AI model deployment

---

### 416. [esnark/blowback](https://github.com/esnark/blowback)  `innovation: 8`

**Blowback Blowback aims to integrate MCP server with AI tools for frontend development, enabling advanced context-aware code assistance.**

**Key Features:**
- Integration of local development servers with AI tools like Claude Desktop and Cursor
- AI-powered code completion and context management
- Snapshot-based checkpoints for version control and testing
- Screenshot capture and SQLite database management
- HMR event monitoring and hot module replacement support

---

### 417. [eternnoir/aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)  `innovation: 8`

**A powerful server integrating Google AI Studio with Gemini API for advanced multi-modal content processing.**

**Key Features:**
- Multi-modal file processing (images
- PDFs
- audio
- documents)
- PDF-to-Markdown conversion
- Image analysis and detailed visual description
- Audio transcription with speaker identification
- Integration with Gemini 2.5 models for context-aware generation

---

### 418. [everythingishacked/Pants](https://github.com/everythingishacked/Pants)  `innovation: 8`

**A video filter to add pants or blur out your lower half on Zoom calls when you forget to wear pants.**

**Key Features:**
- The pants filter uses OpenCV and MediaPipe's Pose detection to add a real-time pants filter to video input. The result is piped to a virtual camera output using pyvirtualcam. It allows users to toggle between different styles of pants or blur out the lower half of their body during Zoom calls.

---

### 419. [fashionzzz/markdown-to-html](https://github.com/fashionzzz/markdown-to-html)  `innovation: 8`

**A Model Context Protocol server that converts Markdown to HTML.**

**Key Features:**
- Markdown to HTML conversion
- Integration with AI tools like Claude Desktop
- Support for enterprise-grade security
- Automated build and deployment capabilities

---

### 420. [feiskyer/mcp-kubernetes-server](https://github.com/feiskyer/mcp-kubernetes-server)  `innovation: 8`

**A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters by translating natural language requests into Kubernetes operations.**

**Key Features:**
- Natural language understanding for Kubernetes operations
- Executes kubectl commands and manages Kubernetes clusters
- Interprets and returns structured responses from Kubernetes API
- Supports integration with AI assistants like Claude
- Cursor
- and GitHub Copilot

---

### 421. [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp)  `innovation: 8`

**A Model Context Protocol server enabling real-time command execution and interactive assistance within iTerm.**

**Key Features:**
- Model Context Protocol server
- REPL support
- Full terminal control
- Code execution in iTerm
- Interactive assistance

---

### 422. [flexpa/mcp-fhir](https://github.com/flexpa/mcp-fhir)  `innovation: 8`

**A model context protocol implementation for FHIR enabling secure, isolated access to healthcare data resources.**

**Key Features:**
- MCP server integration
- FHIR resource access
- secure context management
- LLM interaction support

---

### 423. [fradser/mcp-server-to-markdown](https://github.com/fradser/mcp-server-to-markdown)  `innovation: 8`

**A server that converts various file formats into Markdown descriptions using Cloudflare AI services.**

**Key Features:**
- Cloudflare AI integration
- Markdown conversion
- Cross-platform compatibility
- File format support
- User-friendly interface

---

### 424. [fred-em/headline-vibes](https://github.com/fred-em/headline-vibes)  `innovation: 8`

**A server-based solution for analyzing and visualizing investor sentiment from US news headlines.**

**Key Features:**
- Analyze US news headlines
- Daily and monthly sentiment analysis
- Structured JSON outputs
- Investor relevance filtering
- Political breakdowns
- Token budgeting
- Rate-limit telemetry

---

### 425. [freepik-company/freepik-mcp](https://github.com/freepik-company/freepik-mcp)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling seamless integration of AI assistants with Freepik APIs.**

**Key Features:**
- MCP Server Integration
- AI Assistant Connectivity
- Content Generation & Search
- Image Classification
- Custom Image Creation
- Resource Management
- Automated Workflows

---

### 426. [freestylefly/mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)  `innovation: 8`

**A tool that integrates micro services and LLM clients via MCP protocol to provide structured data for AI models.**

**Key Features:**
- Get bookshelf information from WeChat Readbook
- Search books by keyword or detailed info
- Retrieve book notes and highlights with chapter organization
- Fetch best reviews and ratings for books
- Integrate with Claude Desktop via JSON configuration

---

### 427. [fulcradynamics/fulcra-context-mcp](https://github.com/fulcradynamics/fulcra-context-mcp)  `innovation: 8`

**A MCP server enabling secure access to Fulcra Context data via API, supporting local and remote configurations.**

**Key Features:**
- MCP server integration
- OAuth2 token management
- Local and remote connection support
- Debugging utilities
- API access for Fulcra Context

---

### 428. [futureunreal/mcp-pdf2md](https://github.com/futureunreal/mcp-pdf2md)  `innovation: 8`

**A tool for converting PDF files to structured Markdown format, supporting batch processing and intelligent document handling.**

**Key Features:**
- PDF to Markdown conversion
- Multi-source support (local files and URLs)
- Intelligent processing with best method selection
- Batch processing for large PDF volumes
- Structure preservation in output

---

### 429. [ganelson/inform](https://github.com/ganelson/inform)  `innovation: 8`

**The core software distribution for the Inform 7 programming language, which is a medium for literary writing and a prototyping tool in the games industry.**

**Key Features:**
- Inform is a programming language for interactive fiction. Its core features revolve around natural language syntax
- serving as a medium for literary writing and a prototyping tool. It is also highly influential
- ranking among the top 100 most influential programming languages according to the TIOBE index.

---

### 430. [gbcui/horoscope-serve](https://github.com/gbcui/horoscope-serve)  `innovation: 8`

**A Model Context Protocol (MCP) server providing daily horoscope readings and fortune telling for all zodiac signs.**

**Key Features:**
- MCP Server Integration
- AI-Powered Horoscope Readings
- Error Handling & Validation
- IDE Plugin Support (VSCode)
- Time Range Customization
- Detailed Fortune Readings
- Secure Development Practices

---

### 431. [georgejeffers/gemini-mcp-server](https://github.com/georgejeffers/gemini-mcp-server)  `innovation: 8`

**A TypeScript implementation of a Model Context Protocol (MCP) server integrating with Google's Gemini Pro model for use in Claude Desktop App.**

**Key Features:**
- MCP Server Integration
- Cloud-based AI Model Access
- Secure API Communication
- Developer Tools for Customization

---

### 432. [georgenance/hackernews-mcp](https://github.com/georgenance/hackernews-mcp)  `innovation: 8`

**A server that provides real-time access to Hacker News content for AI assistants and developers.**

**Key Features:**
- Fetch top stories from Hacker News
- Get detailed story information
- Retrieve comments and markdown content
- Search and filter stories by keywords
- Display story metadata

---

### 433. [gianlucamazza/mcp_python_toolbox](https://github.com/gianlucamazza/mcp_python_toolbox)  `innovation: 8`

**A Model Context Protocol server enabling AI tools like Claude to securely and efficiently manage Python development workflows.**

**Key Features:**
- File operations
- Code analysis
- Code execution
- Dependency management
- Project management

---

### 434. [glzr-io/glazewm](https://github.com/glzr-io/glazewm)  `innovation: 8`

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

### 435. [gnosis23/findrepo-mcp-server](https://github.com/gnosis23/findrepo-mcp-server)  `innovation: 8`

**A mcp server application for analyzing code repositories.**

**Key Features:**
- Repository analysis
- Code clone and installation
- Dependency management
- Security scanning and vulnerability detection
- Integration with CI/CD pipelines
- Code review and change tracking
- Automated workflows and actions

---

### 436. [gongrzhe/json-mcp-server](https://github.com/gongrzhe/json-mcp-server)  `innovation: 8`

**A JSON model context protocol server enabling LLMs to interact with structured JSON data through standardized tools.**

**Key Features:**
- JSONPath querying
- JSON transformation operations
- Data filtering and aggregation
- Date manipulation
- String operations

---

### 437. [gongrzhe/office-powerpoint-mcp-server](https://github.com/gongrzhe/office-powerpoint-mcp-server)  `innovation: 8`

**A modular MCP server for PowerPoint manipulation using Python, enabling advanced presentation creation, editing, and management.**

**Key Features:**
- 32 powerful tools organized into 11 specialized modules
- Support for complete PowerPoint operations including template management and professional design
- Enhanced parameter handling and intelligent operation selection
- Comprehensive error handling and validation
- Integration with external tools and workflows

---

### 438. [google/timesketch](https://github.com/google/timesketch)  `innovation: 8`

**Collaborative forensic timeline analysis using sketches for organizing and analyzing timelines.**

**Key Features:**
- Collaborative timeline organization via sketches
- Rich annotations/tags for raw data
- Collaborative analysis across users
- Clear structure for forensic timelines.

---

### 439. [gregkop/sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling secure discovery and download of 3D models from Sketchfab.**

**Key Features:**
- Search for 3D models
- View model details
- Download models in various formats
- Integrate with Claude or Cursor

---

### 440. [greptimeteam/greptimedb-mcp-server](https://github.com/greptimeteam/greptimedb-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server for GreptimeDB that enables secure, isolated querying and analysis of observability data using SQL, TQL, and RANGE queries.**

**Key Features:**
- Model Context Protocol (MCP) integration
- Read-only database access
- Data masking for sensitive information
- Audit logging of all tool invocations
- Support for PromQL-compatible time-series analysis
- Secure connection enforcement and protocol support

---

### 441. [guilhermelirio/brasil-api-mcp](https://github.com/guilhermelirio/brasil-api-mcp)  `innovation: 8`

**A developer platform that integrates Brazilian public data APIs to enable AI assistants and applications to query services like postal codes, company registrations, currency exchange rates, and more.**

**Key Features:**
- Integrate Brazilian public data APIs
- Support AI assistants via MCP protocol
- Secure code deployment and management
- Automated workflows and CI/CD integration

---

### 442. [guilhermelirio/brazilian-cep-mcp](https://github.com/guilhermelirio/brazilian-cep-mcp)  `innovation: 8`

**A server providing tools to query Brazilian postal codes (CEP) using the MCP protocol.**

**Key Features:**
- API integration
- code compilation
- secure development
- AI support
- CI/CD pipeline

---

### 443. [gutmutcode/mcp-server-cloudflare](https://github.com/gutmutcode/mcp-server-cloudflare)  `innovation: 8`

**A cloud-based MCP server for integrating large language models with Cloudflare APIs, enabling seamless interaction between LLMs and external systems.**

**Key Features:**
- Cloudflare MCP Server for IDE
- Integration with Cline
- Windsurf
- Cursor
- etc.
- Secure code deployment and management
- Automated workflows and CI/CD support
- Developer workflow automation and code review
- Security features including vulnerability detection and protection

---

### 444. [hannesj/mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)  `innovation: 8`

**A tool for LLMs to explore and understand GraphQL schemas, providing query, mutation, subscription details, type definitions, and field information.**

**Key Features:**
- Load any GraphQL schema file via command line
- Explore query
- mutation
- and subscription fields
- Search for types and fields using pattern matching
- Filter out internal GraphQL types
- Get simplified field information including types and arguments

---

### 445. [hanzoai/mcp](https://github.com/hanzoai/mcp)  `innovation: 8`

**Model Context Protocol server with 260+ tools for AI agents.**

**Key Features:**
- Model Context Protocol server
- Integration of 260+ AI and development tools
- Secure code execution with encryption and protection
- Automated workflows and task management
- Developer-centric UI/UX components

---

### 446. [hawstein/mcp-server-reddit](https://github.com/hawstein/mcp-server-reddit)  `innovation: 8`

**A Model Context Protocol server enabling LLMs to interact with Reddit content.**

**Key Features:**
- Fetch Reddit frontpage posts
- Access subreddit information
- Retrieve hot posts from subreddits
- View post details
- Display comments with depth
- Integrate with LLMs for context-aware interactions

---

### 447. [healthnotelabs/modular-health-nips](https://github.com/healthnotelabs/modular-health-nips)  `innovation: 8`

**A modular health note API integration for Nostr, enabling secure handling of encrypted health data.**

**Key Features:**
- Discover NIP-101h kinds
- Prepare NIP-101h event structures
- Fetch and decrypt encrypted health events
- Configure client-side encryption/decryption

---

### 448. [hebcal/hebcal-mcp](https://github.com/hebcal/hebcal-mcp)  `innovation: 8`

**Model Context Protocol extension for Hebrew calendar to enhance awareness and observance of Jewish holidays.**

**Key Features:**
- Hebrew calendar generation
- Holiday list creation
- Date conversion tools
- Shabbat candle lighting times
- Torah readings (full kriyah and triennial system)
- Yahrzeits
- birthdays
- and anniversaries lookup

---

### 449. [heetvekariya/linear-regression-mcp](https://github.com/heetvekariya/linear-regression-mcp)  `innovation: 8`

**A MCP server enabling automated training of linear regression models using Claude and a Python-based workflow.**

**Key Features:**
- Automated data preprocessing
- Model training via Claude Desktop
- RMSE evaluation
- Integration with external tools
- Support for linear regression models

---

### 450. [heyzgj/mcp-feargreedindex](https://github.com/heyzgj/mcp-feargreedindex)  `innovation: 8`

**A Model Context Protocol server integrating CoinMarketCap data for cryptocurrency market insights.**

**Key Features:**
- Integrate CoinMarketCap API
- Smart caching for performance
- TypeScript support
- Modular design
- Detailed error handling

---

### 451. [hiretechupup/mcp-server-novacv](https://github.com/hiretechupup/mcp-server-novacv)  `innovation: 8`

**MCP Server for NovaCV API integration, enabling secure access to job application context protocols.**

**Key Features:**
- Generate resume PDF from text
- Convert resume text to JSON Resume format
- Analyze resume text for completeness and keyword usage
- Transform text into structured JSON Resume
- Integrate external tools and manage workflows

---

### 452. [hithereiamaliff/mcp-datagovmy](https://github.com/hithereiamaliff/mcp-datagovmy)  `innovation: 8`

**An unofficial Model Context Protocol (MCP) server enabling secure and efficient access to Malaysia's Open Data APIs.**

**Key Features:**
- Unified search across datasets and dashboards
- Live metadata fetching from Nominatim for GTFS location searches
- Zero-credential geocoding for GTFS location search
- Built-in analytics endpoints and dashboard
- Self-hosted deployment options with Docker
- Integration with Firebase Analytics for tracking tool usage

---

### 453. [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server)  `innovation: 8`

**A server-based context protocol implementation for searching, reading, and accessing files within a Box environment.**

**Key Features:**
- Search files
- Read files
- Access files

---

### 454. [holepunchto/bare](https://github.com/holepunchto/bare)  `innovation: 8`

**A lightweight, modular JavaScript runtime designed for cross-platform execution on desktops and mobile devices.**

**Key Features:**
- Small and modular JavaScript runtime
- Cross-platform support (desktop & mobile)
- Native addon system
- Lightweight threads with synchronous joins
- Bidirectional interoperability between CJS and ESM
- Support for native modules and platform-specific APIs

---

### 455. [hosakakeigo/spreadsheet-mcp-server](https://github.com/hosakakeigo/spreadsheet-mcp-server)  `innovation: 8`

**A server-based solution for accessing and manipulating Google Spreadsheet data via Model Context Protocol (MCP) integration.**

**Key Features:**
- Access spreadsheet metadata
- Retrieve specific sheet data
- Format sheet data in markdown
- Integrate with Claude for Desktop
- Support API key and environment variables

---

### 456. [hrishi0102/payman_mcp](https://github.com/hrishi0102/payman_mcp)  `innovation: 8`

**A context-aware MCP server enabling secure, isolated payment operations for AI assistants.**

**Key Features:**
- Create and manage Payman payees (TEST_RAILS
- US_ACH
- CRYPTO_ADDRESS)
- Send payments with custom amounts and memos
- Search payees by name
- contact info
- or account details
- Check current account balances
- Secure API key management for authentication
- Support SSE transport for real-time client communication

---

### 457. [hrkalona/Fractal-Zoomer](https://github.com/hrkalona/Fractal-Zoomer)  `innovation: 8`

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

### 458. [hugohow/mcp-music-analysis](https://github.com/hugohow/mcp-music-analysis)  `innovation: 8`

**Integrates audio analysis tools to provide insights from music files.**

**Key Features:**
- audio analysis
- beat detection
- duration measurement
- MFCC computation
- lyric transcription

---

### 459. [hzzy2o/flux-cloudfare-mcp](https://github.com/hzzy2o/flux-cloudfare-mcp)  `innovation: 8`

**A cloud-native MCP server enabling AI-driven image generation via Flux model, integrated with Cloudflare Workers for secure, scalable deployment.**

**Key Features:**
- High-quality image generation using Flux model
- Seamless integration with AI assistants like Claude
- Customizable parameters for output control
- Secure local processing and API-based inference
- Support for enterprise-grade security and compliance

---

### 460. [idcdev/mcp-magic-ui](https://github.com/idcdev/mcp-magic-ui)  `innovation: 8`

**A server enabling access and search for Magic UI components via the Model Context Protocol.**

**Key Features:**
- Component discovery through MCP tools
- Automatic categorization of components
- Local caching to reduce API calls
- Support for both stdio and HTTP transport
- Fallback mechanism with mock data

---

### 461. [idea-research/dino-x-mcp](https://github.com/idea-research/dino-x-mcp)  `innovation: 8`

**DINO-X MCP empowers LLMs with advanced visual perception for real-world applications.**

**Key Features:**
- Image object detection
- Object localization
- Caption generation
- Attribute reasoning
- Pose estimation
- Scene understanding
- Visualization of detection results

---

### 462. [ihatesea69/aws-mcp](https://github.com/ihatesea69/aws-mcp)  `innovation: 8`

**AWS MCP enables secure, flexible integration of AI models with AWS services through natural language.**

**Key Features:**
- Query and modify AWS resources using natural language
- Support for multiple AWS profiles and SSO authentication
- Secure credential management
- Local execution with AWS credentials

---

### 463. [imprvhub/mcp-status-observer](https://github.com/imprvhub/mcp-status-observer)  `innovation: 8`

**A tool for monitoring and querying the operational status of major digital platforms via the Model Context Protocol.**

**Key Features:**
- Real-time platform status tracking
- Incident history and resolution tracking
- Platform-specific status details
- Integration with AI providers and developer tools

---

### 464. [instructa/ai-prompts-mcp](https://github.com/instructa/ai-prompts-mcp)  `innovation: 8`

**Implementation of Model Context Protocol for AI Prompts API.**

**Key Features:**
- Model Context Protocol implementation
- TypeScript architecture
- Monorepo structure
- Environment configuration
- Production server support

---

### 465. [iqaicom/mcp-iqwiki](https://github.com/iqaicom/mcp-iqwiki)  `innovation: 8`

**A model context protocol server enabling AI agents to interact with IQ.wiki content.**

**Key Features:**
- Wiki access via Model Context Protocol (MCP)
- User contributions tracking by Ethereum address
- Activity tracking for wiki creations and edits
- Search functionality using natural language queries

---

### 466. [jakedahn/deno2-playwright-mcp-server](https://github.com/jakedahn/deno2-playwright-mcp-server)  `innovation: 8`

**A server enabling LLMs to interact with web pages using browser automation via Playwright and Deno 2.**

**Key Features:**
- Model Context Protocol server
- Browser automation via Playwright
- JavaScript execution in real browser
- Screenshot capture
- Secure execution with Deno

---

### 467. [jaokuohsuan/draw-things-mcp-cursor](https://github.com/jaokuohsuan/draw-things-mcp-cursor)  `innovation: 8`

**Integrates Draw Things MCP cursor with MCP using Model Context Protocol for AI-driven image generation.**

**Key Features:**
- MCP cursor integration
- image generation via model context protocol
- negative prompt support
- step control
- customizable parameters

---

### 468. [jayli52/api2mcptools](https://github.com/jayli52/api2mcptools)  `innovation: 8`

**A Node.js package converting APIs into MCP tools for model context protocol integration.**

**Key Features:**
- API conversion
- MCP tool generation
- CLI support
- code automation
- security features

---

### 469. [jbdamask/cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)  `innovation: 8`

**A Model Context Protocol server enabling AI interaction with Cursor IDE's chat history and project data.**

**Key Features:**
- Access Cursor chat history
- Retrieve composer IDs
- Query database tables
- Refresh database paths

---

### 470. [jeffreygroneberg/mcp-fiar](https://github.com/jeffreygroneberg/mcp-fiar)  `innovation: 8`

**A Spring Boot-based Model Context Protocol (MCP) server enabling interaction with GitHub Copilot for AI-assisted game development.**

**Key Features:**
- MCP server implementation using Spring Boot
- Integration with GitHub Copilot for real-time code assistance
- Game logic for Connect Four with AI opponent
- Command-line interface for game interaction
- Automatic server startup with VS Code extension

---

### 471. [jfrog/mcp-jfrog](https://github.com/jfrog/mcp-jfrog)  `innovation: 8`

**Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, and release lifecycle management.**

**Key Features:**
- Repository management
- Build tracking
- Release lifecycle management
- Artifact search and cataloging
- Integration with JFrog Platform

---

### 472. [jimmcq/lemonade-stand-mcp-server](https://github.com/jimmcq/lemonade-stand-mcp-server)  `innovation: 8`

**A simple MCP server demonstrating AI-driven gameplay for Lemonade Stand using Claude Desktop.**

**Key Features:**
- Dynamic weather system
- Supply and demand simulation
- Strategic pricing and inventory management
- Profit tracking over 14 days
- Integration with Claude Desktop tools

---

### 473. [jkf87/hwp-mcp](https://github.com/jkf87/hwp-mcp)  `innovation: 8`

**HWP-MCP is a Model Context Protocol server enabling AI models like Claude to control and manipulate Korean documents.**

**Key Features:**
- New document creation
- Text insertion in documents
- Table creation and data entry
- Automated batch operations
- Secure file handling with protection against unauthorized access

---

### 474. [jorekai/db-timetable-mcp](https://github.com/jorekai/db-timetable-mcp)  `innovation: 8`

**Ein Model Context Protocol (MCP) Server for accessing Deutsche Bahn timetable data.**

**Key Features:**
- API integration with Deutsche Bahn Timetable API
- MCP tools and resources for train schedules
- station info
- and changes
- Support for semantic data processing and historical analysis
- KI-based predictions for delays and passenger load
- Multimodal transport connection management

---

### 475. [joshuarileydev/app-store-connect-mcp-server](https://github.com/joshuarileydev/app-store-connect-mcp-server)  `innovation: 8`

**A tool for managing apps, beta testers, and app metadata in App Store Connect using conversational AI.**

**Key Features:**
- AI-powered app management
- Comprehensive analytics dashboard
- Streamlined beta testing tools
- Localization management
- Secure authentication via JWT
- Real-time data access from Apple systems

---

### 476. [joshuatanderson/factbook-mcp](https://github.com/joshuatanderson/factbook-mcp)  `innovation: 8`

**A serverlet that integrates with the CIA World Factbook to fetch and display country information.**

**Key Features:**
- Model Context Protocol integration
- Automated data fetching
- Dynamic content rendering

---

### 477. [jotjunior/mcp-server-zplanner](https://github.com/jotjunior/mcp-server-zplanner)  `innovation: 8`

**A command-line tool for project planning and management with AI-assisted development.**

**Key Features:**
- Project creation and configuration
- Hierarchical structure (phases
- tasks
- subtasks)
- Automatic progress calculation
- HTML reports and visualization
- Task management (add
- remove
- update
- complete)

---

### 478. [jpinillagoshawk/mcp-server-file-modifier](https://github.com/jpinillagoshawk/mcp-server-file-modifier)  `innovation: 8`

**A server enabling file modifications and control via AI-assisted Model Context Protocol.**

**Key Features:**
- add content at specific line
- replace existing content
- delete content
- support UTF-8 encoding

---

### 479. [jxnl/apple-mcp](https://github.com/jxnl/apple-mcp)  `innovation: 8`

**Collection of apple-native tools for the MCP protocol to enable secure, context-aware communication.**

**Key Features:**
- Apple MCP tools
- Secure communication
- Context awareness
- Privacy features
- Integration with Apple devices

---

### 480. [jxnl/python-apple-mcp](https://github.com/jxnl/python-apple-mcp)  `innovation: 8`

**A Python implementation for interacting with macOS applications via AppleScript, supporting integration with native apps and asynchronous operations.**

**Key Features:**
- Interact with macOS apps
- Asynchronous operations
- Error handling
- Type-safe interfaces

---

### 481. [kalivaraprasad-gonapa/react-mcp](https://github.com/kalivaraprasad-gonapa/react-mcp)  `innovation: 8`

**React MCP enables integration between Claude AI and React applications via the Model Context Protocol.**

**Key Features:**
- Integration with Claude Desktop
- Model Context Protocol support
- React application creation and modification
- File and directory management
- Process tracking and execution
- Detailed process logs
- Real-time output monitoring

---

### 482. [kapishmalik/hoverfly-mcp-server](https://github.com/kapishmalik/hoverfly-mcp-server)  `innovation: 8`

**A Spring Boot-based MCP server enabling AI assistants to manage mock APIs via JSON, supporting full lifecycle control.**

**Key Features:**
- Model Context Protocol (MCP) integration
- Dynamic API mocking via JSON
- Simulation persistence
- Docker-based deployment
- AI assistant compatibility

---

### 483. [karthikkrs/isms-mcp-project](https://github.com/karthikkrs/isms-mcp-project)  `innovation: 8`

**A comprehensive security management platform integrating AI capabilities for enhanced information security.**

**Key Features:**
- User Management
- Asset Management
- Policy Management
- Risk Management
- Incident Management
- AI Integration

---

### 484. [kashuncheng/dap_mcp](https://github.com/kashuncheng/dap_mcp)  `innovation: 8`

**A framework for managing debugger sessions and enhancing large language model debugging workflows.**

**Key Features:**
- Debug Adapter Protocol Integration
- Rich Debugging Tools
- Flexible Configuration
- Customizable Debugger Settings

---

### 485. [kaznak/shell-command-mcp](https://github.com/kaznak/shell-command-mcp)  `innovation: 8`

**A secure Docker-based MCP server enabling isolated execution of shell commands for AI/development workflows.**

**Key Features:**
- Secure isolated Docker container execution
- MCP protocol support for remote command execution
- Non-root user environment for enhanced security
- Persistent file mounting from host
- Integration with Kubernetes tools (kubectl
- helm)
- AI-friendly development workspace

---

### 486. [kazuph/mcp-fetch](https://github.com/kazuph/mcp-fetch)  `innovation: 8`

**A tool for fetching and processing web content, including images, to support AI-driven applications.**

**Key Features:**
- Web content extraction
- Image processing and optimization
- Automatic file saving with date-based directory structure
- Base64 encoding for AI display
- Pagination support for text and images
- Image subsampling and compression

---

### 487. [kazuph/mcp-pocket](https://github.com/kazuph/mcp-pocket)  `innovation: 8`

**A tool to integrate Pocket API with Claude Desktop for retrieving and managing saved articles.**

**Key Features:**
- Fetch saved articles from Pocket API
- Mark articles as read in Pocket
- Customize and organize saved content
- Integrate with Claude Desktop for a unified experience

---

### 488. [kbsooo/mcp_atom_of_thoughts](https://github.com/kbsooo/mcp_atom_of_thoughts)  `innovation: 8`

**A framework for decomposing complex problems into atomic reasoning units for enhanced AI inference.**

**Key Features:**
- Decomposition-contraction mechanism
- Automatic termination based on depth or confidence
- Confidence-based conclusion suggestion
- Support for hypothesis verification
- Integration of premise
- reasoning
- hypothesis
- verification
- and conclusion atoms

---

### 489. [keithah/hostex-mcp](https://github.com/keithah/hostex-mcp)  `innovation: 8`

**A server-based solution for managing property data via the Model Context Protocol, supporting both stdio and streamable HTTP transport.**

**Key Features:**
- Property and room type management
- Reservations CRUD operations with custom fields and lock codes
- Availability calendars
- Listings and channel listings
- Messaging and guest communication
- Review management and response handling
- Webhooks for real-time notifications
- Custom channels and income methods
- Integration with Claude and other MCP clients

---

### 490. [kentaro/aivis-speech-mcp](https://github.com/kentaro/aivis-speech-mcp)  `innovation: 8`

**A server implementation for integrating AivisSpeech using the Model Context Protocol (MCP) to enable AI-driven voice synthesis.**

**Key Features:**
- MCP protocol integration
- TypeScript-based API design
- High-quality text-to-speech synthesis
- Scalable architecture
- Environment configuration support

---

### 491. [keonchennl/mcp-graphdb](https://github.com/keonchennl/mcp-graphdb)  `innovation: 8`

**A model context protocol server enabling LLMs to query Ontotext GraphDB using SPARQL.**

**Key Features:**
- SPARQL query execution
- GraphDB integration
- Read-only access
- Model context protocol
- AI platform compatibility

---

### 492. [kevint-cerebras/cerebras-code-mcp](https://github.com/kevint-cerebras/cerebras-code-mcp)  `innovation: 8`

**A platform for AI-assisted code generation integrated with Cerebras MCP to enhance productivity and intelligence.**

**Key Features:**
- AI-powered code generation
- Integration with AI tools (Claude Code
- Cline
- Cursor)
- Visual code diff display
- Secure development environment
- IDE integration support

---

### 493. [klara-research/mcp-analyzer](https://github.com/klara-research/mcp-analyzer)  `innovation: 8`

**A tool for analyzing and debugging MCP logs directly within the client environment.**

**Key Features:**
- Direct MCP log access
- Smart filtering and search
- Paginated browsing
- Large file handling
- Integration with Claude Desktop

---

### 494. [kmexnx/excel-to-pdf-mcp](https://github.com/kmexnx/excel-to-pdf-mcp)  `innovation: 8`

**A server that enables secure and automated conversion of Excel and Apple Numbers files to PDF, integrating with AI assistants for streamlined file management.**

**Key Features:**
- Convert Excel (.xls/.xlsx) and Apple Numbers (.numbers) files to PDF
- Integration with Claude AI for conversational file conversion
- Secure file handling respecting project boundaries

---

### 495. [korigamik/markitdown_mcp_server](https://github.com/korigamik/markitdown_mcp_server)  `innovation: 8`

**A Model Context Protocol server that converts various file formats to Markdown using the MarkItDown utility.**

**Key Features:**
- File format conversion
- Markdown output generation
- Integration with MCP clients
- Support for OCR and metadata extraction

---

### 496. [krupalp525/fledge-mcp](https://github.com/krupalp525/fledge-mcp)  `innovation: 8`

**A server enabling Fledge functionality to interact with Cursor AI via natural language.**

**Key Features:**
- Model Context Protocol (MCP) server
- API key authentication
- Tool integration
- Real-time data access
- Secure deployment

---

### 497. [krzko/google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling secure, context-aware interactions with Google Cloud services.**

**Key Features:**
- Connects to Google Cloud services via MCP protocol
- Provides tools for managing billing
- IAM
- logging
- monitoring
- and security
- Supports automated error detection and remediation
- Integrates with CI/CD pipelines and developer workflows

---

### 498. [kshern/image-tools-mcp](https://github.com/kshern/image-tools-mcp)  `innovation: 8`

**A Model Context Protocol (MCP) service for retrieving image dimensions and compressing images from URLs and local files.**

**Key Features:**
- Retrieve image dimensions from URLs
- Compress images using TinyPNG API
- Compress local images using TinyPNG API
- Fetch image links from Figma API
- Integrate with MCP client for programmatic access

---

### 499. [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)  `innovation: 8`

**A model context protocol server for DuckDB enabling unified database interaction.**

**Key Features:**
- Unified query interface
- Database interaction via MCP
- Read-only mode support
- Secure database handling

---

### 500. [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp)  `innovation: 8`

**A Python-based MCP server for tracking and analyzing cryptocurrency whale transactions.**

**Key Features:**
- get_recent_transactions
- get_transaction_details
- query_whale_activity
- api_key_configuration

---

### 501. [kuon-dev/advanced-reason-mcp](https://github.com/kuon-dev/advanced-reason-mcp)  `innovation: 8`

**A tool for advanced reasoning and reflection using the Gemini API to enhance decision-making processes.**

**Key Features:**
- Gemini API integration
- Code completion with Copilot
- Workflow automation
- Secure code deployment
- CI/CD support

---

### 502. [kursk-ye/code2flow-mcp-server](https://github.com/kursk-ye/code2flow-mcp-server)  `innovation: 8`

**A platform that enables AI applications to generate and access code call graphs via MCP protocol.**

**Key Features:**
- Generate code call graphs
- Support multiple programming languages
- Integrate with AI tools
- Provide code analysis features

---

### 503. [kuzudb/kuzu-mcp-server](https://github.com/kuzudb/kuzu-mcp-server)  `innovation: 8`

**A model context protocol server enabling LLMs to interact with and query Kuzu databases.**

**Key Features:**
- Model context protocol integration
- Database schema inspection
- Cypher query execution
- Data querying capabilities

---

### 504. [lakphy/deep-reasoning-mcp](https://github.com/lakphy/deep-reasoning-mcp)  `innovation: 8`

**A deep reasoning MCP tool enabling advanced context-based decision making using deepseek-r1 model.**

**Key Features:**
- deep reasoning
- context management
- model integration
- code security
- automated workflows

---

### 505. [lamaalrajih/kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)  `innovation: 8`

**The lamaalrajih/kicad-mcp project provides a Model Context Protocol (MCP) server for integrating with KiCad, enabling seamless interaction between LLMs and hardware design tools.**

**Key Features:**
- Model Context Protocol (MCP) server integration
- Resource access via resources vs tools vs prompts
- Natural language interaction capabilities
- Project management features (list
- search
- analysis)
- Design rule checking and DRC support
- Visualization of PCB layouts
- Circuit pattern recognition
- BOM generation and analysis

---

### 506. [laulauland/bluesky-context-server](https://github.com/laulauland/bluesky-context-server)  `innovation: 8`

**A Bluesky Context Server enabling secure, isolated context management for AI applications.**

**Key Features:**
- MCP server integration
- AI-powered context queries
- Secure data handling
- Automated workflow execution

---

### 507. [leftspin/mcp-xcode-diagnostics](https://github.com/leftspin/mcp-xcode-diagnostics)  `innovation: 8`

**A tool for extracting and analyzing Xcode build errors and warnings to assist AI assistants in debugging Swift projects.**

**Key Features:**
- Extracts diagnostics from Xcode build logs
- Parses complex diagnostics including Swift concurrency warnings
- Provides detailed error and warning information with file paths
- line numbers
- and notes
- Supports code suggestions and fixes for common issues

---

### 508. [letz-ai/letzai-mcp](https://github.com/letz-ai/letzai-mcp)  `innovation: 8`

**A GitHub-hosted implementation of the LetzAI MCP for image generation, enabling integration with Claude Desktop App.**

**Key Features:**
- Model Context Protocol (MCP) integration
- Image generation via prompt-based API
- Node.js runtime environment
- Cloud deployment and configuration

---

### 509. [liangjunyu2010/mcp_server_safe_content_check](https://github.com/liangjunyu2010/mcp_server_safe_content_check)  `innovation: 8`

**A secure MCP server for content safety using Baidu Cloud models.**

**Key Features:**
- MCP server deployment
- input analysis via Baidu Cloud models
- secure configuration management
- content safety enforcement
- integration with Cursor AI editor

---

### 510. [lincest/mcp-papersearch](https://github.com/lincest/mcp-papersearch)  `innovation: 8`

**A GitHub-based tool for searching ArXiv papers using the Model Context Protocol (MCP).**

**Key Features:**
- MCP integration
- ArXiv paper search
- code review tools
- CI/CD support
- secure code deployment

---

### 511. [lite/iterm-mcp](https://github.com/lite/iterm-mcp)  `innovation: 8`

**A Model Context Protocol server enabling real-time command execution and interactive assistance within iTerm2.**

**Key Features:**
- Model context protocol integration
- REPL support
- CLI command execution
- Full terminal control
- Debugging tools

---

### 512. [liuscraft/superset-mcp-server](https://github.com/liuscraft/superset-mcp-server)  `innovation: 8`

**A Borg-based MCP server enabling advanced querying and integration with external tools.**

**Key Features:**
- Query database and tables using SQL
- Execute SQL queries with Node.js
- Integrate external tools via APIs
- Support enterprise-grade security features
- Enable automated workflows and code reviews
- Provide instant dev environments with Codespaces

---

### 513. [lizthedeveloper/terminal-mcp-idk](https://github.com/lizthedeveloper/terminal-mcp-idk)  `innovation: 8`

**A tool for managing code changes, security, and workflow automation in a modular context.**

**Key Features:**
- code review
- security scanning
- workflow automation
- integration with Copilot
- CI/CD support

---

### 514. [lpbayliss/server-dice-roll](https://github.com/lpbayliss/server-dice-roll)  `innovation: 8`

**A MCP server for simulating dice rolls with support for standard and Fate/Fudge dice notation.**

**Key Features:**
- Dice Notation Parsing
- Multiple Dice Types Support
- Random Rolling with Probability Control
- Validation using Zod schemas
- Integration with Claude Desktop

---

### 515. [lrstanley/context7-http](https://github.com/lrstanley/context7-http)  `innovation: 8`

**A MCP server supporting HTTP streaming for the Context7 project, enabling remote access without local installation.**

**Key Features:**
- HTTP streaming support
- Context7 MCP server integration
- Code review and collaboration tools
- Security features and vulnerability management
- Integration with external services and tools

---

### 516. [ltejedor/newsfeed-mcp](https://github.com/ltejedor/newsfeed-mcp)  `innovation: 8`

**A platform for integrating AI assistants with RSS feeds to deliver real-time news and information.**

**Key Features:**
- News aggregation from multiple RSS feeds
- AI assistant integration (e.g.
- Claude)
- Customizable news feeds
- Detailed article content access
- Real-time updates and notifications

---

### 517. [m-gonzalo/cosa-sai](https://github.com/m-gonzalo/cosa-sai)  `innovation: 8`

**A MCP server that retrieves relevant documentation from a knowledge base using the Gemini API, enabling developers to access curated technical information directly.**

**Key Features:**
- MCP server for accessing documentation
- Integration with Gemini API for context-aware responses
- Support for multiple technologies and tools
- Automated code review and security checks

---

### 518. [mackenly/mcp-fathom-analytics](https://github.com/mackenly/mcp-fathom-analytics)  `innovation: 8`

**A Borg-based MCP server enabling AI-driven access and management of Fathom Analytics data.**

**Key Features:**
- MCP server integration for Fathom Analytics
- AI-powered analytics tooling
- Secure code execution and protection
- Automated workflows and CI/CD support

---

### 519. [macrat/mcp-ayd-server](https://github.com/macrat/mcp-ayd-server)  `innovation: 8`

**A server-based implementation for monitoring Ayd model context using the Model Context Protocol.**

**Key Features:**
- MCP Server Integration
- Ayd Model Context Monitoring
- Real-time Status Updates
- Secure Configuration Management

---

### 520. [magenie33/quality-dimension-generator](https://github.com/magenie33/quality-dimension-generator)  `innovation: 8`

**A sophisticated Model Context Protocol server that generates precise quality evaluation dimensions and assessment criteria for tasks or projects.**

**Key Features:**
- AI-powered analysis
- Transforms vague requirements into measurable standards
- Generates specific quality dimensions with scoring criteria

---

### 521. [mahdin75/geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)  `innovation: 8`

**A Model Context Protocol (MCP) server implementation that enables Large Language Models to interact with GeoServer REST APIs for geospatial data and services.**

**Key Features:**
- Integration of LLMs with GeoServer REST API
- Geospatial data and service access via MCP protocol
- Support for spatial queries
- map visualizations
- and OGC-compliant web services
- Customizable client configurations (e.g.
- Claude Desktop or Cursor)
- Secure deployment options including Docker and direct installation

---

### 522. [mario-andreschak/mcp-gameboy](https://github.com/mario-andreschak/mcp-gameboy)  `innovation: 8`

**A GameBoy emulator server enabling LLMs to interact with GameBoy screens via protocol.**

**Key Features:**
- MCP server implementation
- GameBoy screen control
- ROM loading and rendering
- SDK-based protocol support
- automated deployment tools

---

### 523. [mateusribeirocampos/npm-mcp-server](https://github.com/mateusribeirocampos/npm-mcp-server)  `innovation: 8`

**A TypeScript-based MCP server for fetching npm package information.**

**Key Features:**
- search npm package
- install npm mcp server
- integrate with ai models
- code review tools
- secure code deployment

---

### 524. [matthewdailey/figma-mcp](https://github.com/matthewdailey/figma-mcp)  `innovation: 8`

**A model context protocol server enabling AI interaction with Figma files.**

**Key Features:**
- add_figma_file
- read_comments
- post_comment
- reply_to_comment

---

### 525. [matthewdcage/pbs-mcp-server](https://github.com/matthewdcage/pbs-mcp-server)  `innovation: 8`

**A standalone MCP server enabling AI models to access and query the Australian Pharmaceutical Benefits Scheme (PBS) API using natural language LLM integration.**

**Key Features:**
- Model Context Protocol (MCP) support for PBS data
- Natural language LLM integration for querying pharmaceutical information
- Secure
- structured access to PBS data via HTTP/SSE
- Customizable API endpoints and tool invocations
- Real-time updates and structured pharmaceutical data output

---

### 526. [matthewdcage/vapi-mcp](https://github.com/matthewdcage/vapi-mcp)  `innovation: 8`

**Vapi MCP server integrates Vapi's voice AI with Cursor for context-aware interactions.**

**Key Features:**
- Vapi MCP server integration
- Voice AI context management
- Secure API key configuration
- Environment variable management
- Direct server execution support

---

### 527. [mattiasw/browserloop](https://github.com/mattiasw/browserloop)  `innovation: 8`

**A Model Context Protocol server for capturing screenshots and monitoring browser console logs during web development.**

**Key Features:**
- High-quality screenshot capture using Playwright
- Console log reading and collection from web pages
- Cookie-based authentication for protected pages
- Docker containerization for consistent environments
- Support for localhost and remote URLs
- Configurable viewport sizes and capture options

---

### 528. [mattmorgis/nuanced-mcp](https://github.com/mattmorgis/nuanced-mcp)  `innovation: 8`

**A model context protocol server enabling LLMs to analyze code structure via call graphs.**

**Key Features:**
- Initialize call graphs
- Switch between repositories
- Analyze function dependencies
- Get detailed function information

---

### 529. [mauricio-cantu/brasil-api-mcp-server](https://github.com/mauricio-cantu/brasil-api-mcp-server)  `innovation: 8`

**A Model Context Protocol server to enhance AI applications with rich data from Brasil resources.**

**Key Features:**
- BrasilAPI data querying
- Model Context Protocol (MCP) support
- Integration with AI applications
- Rich data enrichment from Brazil resources
- Automated workflow management

---

### 530. [maverickg59/sushimcp](https://github.com/maverickg59/sushimcp)  `innovation: 8`

**SushiMCP is a model context protocol server that enhances AI development environments by providing contextual information to LLM models.**

**Key Features:**
- Contextual information delivery
- Improved code generation speed
- Integration with AI IDEs
- Support for multiple LLMs
- Customizable configuration

---

### 531. [mcp-100/mcp-sentry](https://github.com/mcp-100/mcp-sentry)  `innovation: 8`

**A Model Context Protocol server for retrieving and analyzing issues from Sentry.io.**

**Key Features:**
- Retrieve and analyze Sentry issues
- Inspect error reports and stack traces
- Integrate with Claude Desktop via uvx
- Support project slug-based analysis
- Enable detailed issue information viewing

---

### 532. [mcpnow-io/conduit](https://github.com/mcpnow-io/conduit)  `innovation: 8`

**Conduit is a Model Context Protocol (MCP) server enabling seamless integration with Phabricator and Phorge APIs for advanced automation.**

**Key Features:**
- MCP integration
- secure authentication
- type safety
- runtime validation
- smart pagination
- token optimization

---

### 533. [mehmetakinn/gitlab-mcp-code-review](https://github.com/mehmetakinn/gitlab-mcp-code-review)  `innovation: 8`

**A GitLab MCP integration for AI assistants to review code changes directly within merge requests.**

**Key Features:**
- Merge Request Analysis
- File-Specific Diffs
- Version Comparison
- Review Management (Comments
- Approval)
- Project Overview & Lists

---

### 534. [metehan777/alsoasked-mcp](https://github.com/metehan777/alsoasked-mcp)  `innovation: 8`

**A platform for managing and analyzing People Also Asked data to enhance SEO and content optimization.**

**Key Features:**
- Search People Also Ask questions
- Integrate with Google's APIs
- Customizable search parameters

---

### 535. [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server)  `innovation: 8`

**A Kubernetes observability platform enabling LLM interaction with external data sources via MCP.**

**Key Features:**
- eBPF-based telemetry collection
- Kubernetes-native observability
- LLM integration via Claude Desktop App
- API-driven access to metrics and logs

---

### 536. [mhe8mah/webp-batch-mcp](https://github.com/mhe8mah/webp-batch-mcp)  `innovation: 8`

**A cross-platform batch WebP conversion tool that integrates with MCP for efficient image processing.**

**Key Features:**
- Batch conversion of multiple image formats
- Cross-platform compatibility (macOS
- Linux
- Windows)
- Multi-threaded processing
- Quality control and lossless mode
- Metadata preservation
- Detailed conversion reporting

---

### 537. [microsoft/mcp](https://github.com/microsoft/mcp)  `innovation: 8`

**A Model Context Protocol server enabling seamless integration of AI agents with diverse data sources and tools.**

**Key Features:**
- Model Context Protocol (MCP) server implementation
- Integration with Azure services
- Support for AI assistants and IDEs
- Secure code execution and development workflows
- Customizable tooling for enterprise applications

---

### 538. [mightydillah/apple-doc-mcp](https://github.com/mightydillah/apple-doc-mcp)  `innovation: 8`

**A tool that provides seamless access to Apple Developer Documentation with smart search and wildcard support.**

**Key Features:**
- Smart search with symbol resolution
- Wildcard support
- Separate article results
- Integration with AI coding assistants

---

### 539. [milancermak/starknet-mcp](https://github.com/milancermak/starknet-mcp)  `innovation: 8`

**Model context protocol server for Starknet RPC enabling secure and isolated communication between applications.**

**Key Features:**
- Starknet RPC methods
- Secure communication protocols
- Integration with MCP
- Real-time blockchain data access

---

### 540. [milisp/codexia](https://github.com/milisp/codexia)  `innovation: 8`

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

### 541. [milkdrop2077/MilkDrop3](https://github.com/milkdrop2077/MilkDrop3)  `innovation: 8`

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

### 542. [milkosten/task-mcp-server](https://github.com/milkosten/task-mcp-server)  `innovation: 8`

**A MCP Task Server implementation for task management using the Model Context Protocol, supporting both CLI and web interfaces.**

**Key Features:**
- Task creation and management
- Task filtering and status updates
- Dual interface modes (STDIO and HTTP+SSE)
- Comprehensive validation and error handling
- Automated testing and server shutdown

---

### 543. [mingdaocloud/hap-mcp](https://github.com/mingdaocloud/hap-mcp)  `innovation: 8`

**HAP-MCP Server enables secure, isolated context management for AI-driven applications, facilitating seamless integration of machine learning models within enterprise workflows.**

**Key Features:**
- Model Context Protocol (MCP) server integration
- Secure code execution and protection against leaks
- Automated workflow automation and CI/CD support
- Developer-friendly APIs for AI tool integration
- Enhanced security features including vulnerability management

---

### 544. [minh-ton/reynard-browser](https://github.com/minh-ton/reynard-browser)  `innovation: 8`

**An experimental Gecko-based web browser for iOS 14+ designed to run independently of WebKit.**

**Key Features:**
- Gecko-based rendering engine
- Support for iOS 14+ and later
- Engine updates independent of OS
- Customizable extensions and app support
- Live development environment with sideloading options

---

### 545. [miniorangedev/wp-code-review-mcp-server](https://github.com/miniorangedev/wp-code-review-mcp-server)  `innovation: 8`

**A lightweight MCP server for fetching and enforcing coding guidelines, security rules, and validation patterns from external sources.**

**Key Features:**
- Dynamic configuration of coding guidelines
- Integration with external guidelines via URLs
- Real-time code validation and security scanning
- Customizable development standards
- Automatic updates without server restart

---

### 546. [mistizz/mcp-japanesetextanalyzer](https://github.com/mistizz/mcp-japanesetextanalyzer)  `innovation: 8`

**日本語テキストの形態素解析を行い、言語的特徴を分析するMCPサーバーです。**

**Key Features:**
- 日本語テキストの文字数（スペースや改行を除いた実質的な文字数）
- 日本語テキストの単語数
- 形態素解析による詳細な言語的特徴分析
- 平均文長、品詞の割合、語彙の多様性、助詞・カタカナ・漢字の割合、敬語使用頻度、句読点数

---

### 547. [mkearl/dependency-mcp](https://github.com/mkearl/dependency-mcp)  `innovation: 8`

**A Model Context Protocol server for analyzing code dependencies and architectural patterns.**

**Key Features:**
- Dependency graph generation in JSON/DOT format
- Architectural analysis and scoring
- File metadata extraction
- Support for multiple programming languages (TypeScript
- JavaScript
- C#
- Python)

---

### 548. [mladensu/cli-mcp-server](https://github.com/mladensu/cli-mcp-server)  `innovation: 8`

**A secure command-line interface for MCP clients with customizable security policies.**

**Key Features:**
- Secure command execution with strict validation
- Command whitelisting and flag restrictions
- Path traversal prevention
- Shell operator blocking (optional)
- Execution timeouts and length limits
- Detailed error reporting
- Async operation support
- Working directory restriction and validation

---

### 549. [mobizt/build-your-own-x](https://github.com/mobizt/build-your-own-x)  `innovation: 8`

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

### 550. [modelcontextprotocol-servers/google-search-mcp](https://github.com/modelcontextprotocol-servers/google-search-mcp)  `innovation: 8`

**A Playwright-based tool for performing Google searches, bypassing anti-bot mechanisms and extracting structured results for AI assistants.**

**Key Features:**
- Anti-bot bypass
- Automatic CAPTCHA handling
- State persistence
- Multi-language support
- Browser session saving

---

### 551. [modelcontextprotocol/servers-archived](https://github.com/modelcontextprotocol/servers-archived)  `innovation: 8`

**A MCP server integrating Brave Search API for web and local search capabilities.**

**Key Features:**
- Brave Search API integration
- Web and local search capabilities
- Flexible filtering and smart fallbacks
- Secure context management

---

### 552. [modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification)  `innovation: 8`

**This repository provides the specification and documentation for the Model Context Protocol, a protocol designed to enable secure, context-aware communication between AI models.**

**Key Features:**
- Model context sharing
- Secure communication protocols
- Code signing and verification
- Integration with CI/CD pipelines
- Automated security scanning
- Developer workflow automation

---

### 553. [monadical-sas/zulip-mcp](https://github.com/monadical-sas/zulip-mcp)  `innovation: 8`

**A model context protocol server enabling AI assistants to interact with Zulip workspaces.**

**Key Features:**
- Integrate Zulip API for AI assistant interaction
- Support message posting
- direct messages
- emoji reactions
- Channel management including subscriptions and users
- Docker-based deployment for scalability

---

### 554. [namin/dafny-mcp](https://github.com/namin/dafny-mcp)  `innovation: 8`

**A tool for verifying code correctness using Dafny within the Model Context Protocol.**

**Key Features:**
- Dafny Verifier Tool
- Model Context Protocol support
- Code verification
- Integration with Claude
- Automated testing

---

### 555. [nathanonn/mcp-url-fetcher](https://github.com/nathanonn/mcp-url-fetcher)  `innovation: 8`

**A tool for fetching and converting web content to various formats using the Model Context Protocol.**

**Key Features:**
- URL fetching from any source
- Format conversion (HTML
- JSON
- Markdown
- plain text)
- Automatic content detection
- Security measures for web content
- Integration with Claude for Desktop

---

### 556. [nearai/near-mcp](https://github.com/nearai/near-mcp)  `innovation: 8`

**A Model Context Protocol (MCP) compatible server for securely interacting with NEAR blockchain.**

**Key Features:**
- Interact with NEAR accounts using AI models
- Manage NEAR account balances and status
- Sign and send transactions
- Create and manage new accounts
- Inspect and execute smart contracts
- Import private keys for secure access

---

### 557. [nebula-contrib/nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)  `innovation: 8`

**A Model Context Protocol Server enabling integration with NebulaGraph 3.x for advanced data modeling and querying.**

**Key Features:**
- Model Context Protocol Server
- Seamless access to NebulaGraph 3.x
- Configuration via environment variables
- Command-line interface
- Support for schema management and querying

---

### 558. [neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp)  `innovation: 8`

**A cloud-based MCP server enabling secure, isolated interaction between FreeCAD and Claude Desktop for collaborative engineering workflows.**

**Key Features:**
- MCP (Model Context Protocol) server integration
- Secure remote access via RPC server
- Automatic startup on FreeCAD launch
- Remote connection configuration
- Integration with Claude Desktop for seamless workflow

---

### 559. [neno-is-ooo/mcp-openverse](https://github.com/neno-is-ooo/mcp-openverse)  `innovation: 8`

**A server enabling secure, isolated access to openly licensed images from Openverse for development and testing.**

**Key Features:**
- Open-source MCP server
- Image search with filters
- License verification
- Attribution handling

---

### 560. [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)  `innovation: 8`

**Neo4j MCP Servers enable context management between large language models and external systems, facilitating secure and efficient data exchange.**

**Key Features:**
- Model Context Protocol (MCP) servers
- Secure communication with Aura accounts
- Cloud deployment options
- Graph data modeling and visualization

---

### 561. [nermalcat69/zerops-mcp](https://github.com/nermalcat69/zerops-mcp)  `innovation: 8`

**A GitHub-based platform for managing code repositories, issues, pull requests, and project workflows with advanced search, automation, and security features.**

**Key Features:**
- Automatic branch creation
- Comprehensive error handling
- Git history preservation
- Batch file and code operations
- Advanced search across repositories and issues
- Pull request management
- Security features including vulnerability detection
- Code review and commenting
- Integration with external tools

---

### 562. [newerton/mcp-status-invest](https://github.com/newerton/mcp-status-invest)  `innovation: 8`

**A Model Context Protocol server enabling interaction with the Status Invest API for stock data and indicators.**

**Key Features:**
- Fetch stock data
- Fetch indicators
- Data validation with Zod
- Integration with external APIs

---

### 563. [newideas99/deepseek-thinking-claude-3.5-sonnet-cline-mcp](https://github.com/newideas99/deepseek-thinking-claude-3.5-sonnet-cline-mcp)  `innovation: 8`

**A MCP server integrating DeepSeek R1 reasoning with Claude 3.5 Sonnet for context-aware, conversational AI responses.**

**Key Features:**
- DeepSeek reasoning engine
- Claude 3.5 Sonnet response generation
- OpenRouter unified API integration
- Two-stage processing (50k & 600k character limits)
- Context clearing and conversation management

---

### 564. [ngeojiajun/mcp-code-snippets](https://github.com/ngeojiajun/mcp-code-snippets)  `innovation: 8`

**A server-based platform for managing and storing code snippets across multiple programming languages.**

**Key Features:**
- Create Snippet
- List Snippets
- Delete Snippet
- Lint
- Build
- Contribute

---

### 565. [nighttrek/software-planning-mcp](https://github.com/nighttrek/software-planning-mcp)  `innovation: 8`

**An experiment in software planning using MCP to structure and track development tasks.**

**Key Features:**
- Interactive Planning Sessions
- Task Management
- Complexity Scoring
- Implementation Plans
- Code Examples
- Insights & Analytics

---

### 566. [nikolamilosevic86/verifAI](https://github.com/nikolamilosevic86/verifAI)  `innovation: 8`

**VerifAI is a Generative Search/Productivity engine with Verifiable answers.**


---

### 567. [nodegis/geo-mcp-server](https://github.com/nodegis/geo-mcp-server)  `innovation: 8`

**A geospatial processing server enabling coordinate system conversions and spatial analysis for applications.**

**Key Features:**
- coordinate system conversion
- distance calculation
- area calculation
- spatial analysis tools

---

### 568. [nomagicln/mcp-harbor](https://github.com/nomagicln/mcp-harbor)  `innovation: 8`

**A Node.js application providing a Model Context Protocol (MCP) server for interacting with Harbor container registry.**

**Key Features:**
- MCP Server for Harbor
- Automated testing with Jest
- TypeScript-based development
- Integration with Harbor operations
- Support for projects
- repositories
- tags
- and Helm charts

---

### 569. [odancona/code2prompt-mcp](https://github.com/odancona/code2prompt-mcp)  `innovation: 8`

**A tool that generates contextual prompts from codebases to enhance AI interaction.**

**Key Features:**
- Contextual prompt generation
- Code analysis
- AI integration

---

### 570. [odgrim/mcp-datetime](https://github.com/odgrim/mcp-datetime)  `innovation: 8`

**A TypeScript implementation of the Model Context Protocol (MCP) server providing datetime and timezone information to AI systems.**

**Key Features:**
- Get current time in local timezone
- Retrieve current system timezone
- List available timezones
- Access timezone info via URI resources
- Support for SSE mode with custom port/uri prefix
- Integration with AI systems via MCP protocol

---

### 571. [omedia/mcp-server-drupal](https://github.com/omedia/mcp-server-drupal)  `innovation: 8`

**A TypeScript-based companion MCP server for Drupal that integrates with STDIO transport, enabling efficient communication and data handling.**

**Key Features:**
- MCP server integration
- STDIO transport support
- TypeScript-based architecture
- Docker container deployment
- Secure authentication mechanisms
- Development and production readiness

---

### 572. [omer-ayhan/custom-context-mcp](https://github.com/omer-ayhan/custom-context-mcp)  `innovation: 8`

**A model context protocol server that transforms text into structured JSON using predefined templates.**

**Key Features:**
- Group and structure text based on JSON templates with placeholders
- Extract key-value pairs from AI-generated text for downstream use
- Support nested JSON structures and complex data extraction
- Integrate with AI models to automate data structuring and processing

---

### 573. [omniwaifu/pydantic-ai-docs-server](https://github.com/omniwaifu/pydantic-ai-docs-server)  `innovation: 8`

**A programmatic interface to access and manage Pydantic-AI documentation via Model Context Protocol.**

**Key Features:**
- Clone or update Pydantic-AI documentation repository
- Retrieve specific documents by path
- List available topics and changelogs
- Execute tools like update_documentation
- get_document_by_path
- etc.
- Provide changelog content for review

---

### 574. [onnx/onnx](https://github.com/onnx/onnx)  `innovation: 8`

**Open standard for machine learning interoperability.**

**Key Features:**
- ONNX provides an open source format for AI models
- defining an extensible computation graph model with built-in operators and standard data types. It focuses on capabilities needed for inferencing (scoring)
- enabling interoperability between frameworks
- and streamlining the path from research to production.

---

### 575. [onurucard4/scan-url-mcp-server](https://github.com/onurucard4/scan-url-mcp-server)  `innovation: 8`

**A server-based solution using MCP to scan URLs via urlscan.io.**

**Key Features:**
- MCP protocol integration
- URL scanning via urlscan.io
- secure code execution
- automated workflow support

---

### 576. [opensvm/zig-mcp-server](https://github.com/opensvm/zig-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server that enhances Zig language support with code optimization, compute unit estimation, code generation, and best practices.**

**Key Features:**
- Modern build system support for Zig 0.15.2+
- Code optimization and performance analysis
- Automated migration guidance for legacy patterns
- Enhanced module system integration
- Comprehensive code generation from natural language prompts
- Detailed code recommendations for safety and efficiency

---

### 577. [orellazri/coda-mcp](https://github.com/orellazri/coda-mcp)  `innovation: 8`

**A community-built Model Context Protocol (MCP) server enabling AI assistants to interact with Coda documents.**

**Key Features:**
- coda_list_documents
- coda_list_pages
- coda_create_page
- coda_get_page_content
- coda_replace_page_content
- coda_append_page_content
- coda_duplicate_page
- coda_rename_page
- coda_peek_page
- coda_resolve_link

---

### 578. [panzer-jack/feuse-mcp](https://github.com/panzer-jack/feuse-mcp)  `innovation: 8`

**A toolset for automating API integration, code generation, and design-to-code workflows using Figma.**

**Key Features:**
- Figma integration for seamless design-to-code conversion
- API automation with TypeScript interface generation
- Asset management and extraction from Figma files
- Visual similarity comparison between Figma prototypes and project pages
- Customizable project standards and code rules

---

### 579. [patrickpalmer/mayamcp](https://github.com/patrickpalmer/mayamcp)  `innovation: 8`

**Maya MCP server enables AI-powered control of Autodesk Maya via natural language using the Model Context Protocol.**

**Key Features:**
- AI assistant integration for Maya
- Natural language command execution
- Dynamic tool registration
- Scene and object manipulation
- Model context protocol support

---

### 580. [paulotaylor/voyp-mcp](https://github.com/paulotaylor/voyp-mcp)  `innovation: 8`

**Voyp MCP server enables secure, two-way integration between AI models and external data sources, facilitating seamless call context management.**

**Key Features:**
- Construct robust call contexts
- Search for business information
- Call and make appointments/reservations
- Provide call status updates

---

### 581. [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat)  `innovation: 8`

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

### 582. [phialsbasement/pagespeed-mcp-server](https://github.com/phialsbasement/pagespeed-mcp-server)  `innovation: 8`

**PageSpeed MCP Server integrates AI capabilities with PageSpeed Insights to analyze website performance metrics.**

**Key Features:**
- Performance metrics analysis
- Core Web Vitals evaluation
- Accessibility audits
- SEO insights

---

### 583. [phil65/mcp-server-llmling](https://github.com/phil65/mcp-server-llmling)  `innovation: 8`

**A server for managing LLM contexts with YAML-based configuration and resource management.**

**Key Features:**
- Resource management (text
- CLI
- code
- images)
- Tool system registration and execution
- Prompt management with templates and dynamic inputs
- Multiple transport options (SSE
- custom)
- Resource watching and hot-reload capabilities

---

### 584. [photosynth-inc/gitlab_review](https://github.com/photosynth-inc/gitlab_review)  `innovation: 8`

**MCP Server extension for GitLab to enable review comments and merge request management.**

**Key Features:**
- Review comments posting for merge requests
- Retrieve merge request information
- Access latest version of merge requests
- Post discussion comments on merge requests

---

### 585. [piotrpalek/mcp-thinking-tool](https://github.com/piotrpalek/mcp-thinking-tool)  `innovation: 8`

**A tool designed to assist in complex reasoning and problem-solving by providing structured thought processes.**

**Key Features:**
- Step back and think through complex problems
- Break down reasoning into discrete steps
- Cache intermediate results during complex calculations
- Show its work when solving problems
- Provide detailed thought logs and explanations

---

### 586. [pixelsock/directus-mcp](https://github.com/pixelsock/directus-mcp)  `innovation: 8`

**A Node.js server implementing the Model Context Protocol (MCP) to enable AI clients to interact with the Directus API.**

**Key Features:**
- MCP server integration
- AI client interaction
- Directus API support

---

### 587. [politwit1984/mcp-perplexity-server](https://github.com/politwit1984/mcp-perplexity-server)  `innovation: 8`

**A Model Context Protocol server for intelligent code analysis and debugging using Perplexity AI, integrated with Claude desktop client.**

**Key Features:**
- Intelligent error analysis
- Pattern detection
- Comprehensive solutions
- Best practices and coding standards
- Error prevention tips

---

### 588. [pollinations/chucknorris](https://github.com/pollinations/chucknorris)  `innovation: 8`

**MCP server that dynamically adapts LLM enhancement prompts using jailbreak techniques for improved performance.**

**Key Features:**
- Dynamic schema adaptation
- Jailbreak prompt integration
- Two-phase approach to bypass detection
- Model-specific prompt customization

---

### 589. [pontusab/directories](https://github.com/pontusab/directories)  `innovation: 8`

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

### 590. [princefishthrower/orly-mcp](https://github.com/princefishthrower/orly-mcp)  `innovation: 8`

**A MCP server tool for generating O'Reilly parody dev books, integrating with Claude Desktop.**

**Key Features:**
- MCP server integration for O'Reilly book generation
- Support for custom titles
- authors
- and images
- Automated code generation and testing
- Cloud deployment and CI/CD support

---

### 591. [processing/processing4](https://github.com/processing/processing4)  `innovation: 8`

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

### 592. [https://github.com/projectM-visualizer](https://github.com/projectM-visualizer)  `innovation: 8`

**projectM Visualizer · GitHub**

**Key Features:**
- projectM Visualizer (Cross-platform Music Visualization Library)
- projectM Expression Evaluation Library
- and various frontend/backend implementations (SDL
- Rust
- Qt).

---

### 593. [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)  `innovation: 8`

**A server-based platform enabling integration of any large language model as a tool within the Borg ecosystem.**

**Key Features:**
- Integrate multiple AI chat completion APIs
- Dynamic tool selection per context
- Context-aware interactions
- Scalable deployment options

---

### 594. [qckfx/tree-hugger-js-mcp](https://github.com/qckfx/tree-hugger-js-mcp)  `innovation: 8`

**A tool for advanced code analysis and transformation using tree-hugger-js-mcp, supporting static analysis, refactoring, and integration with AI-driven development workflows.**

**Key Features:**
- Code analysis and pattern matching
- Automated code transformation
- Integration with MCP server for AI agents
- Support for TypeScript and JSX
- Development and testing environments

---

### 595. [qianniuspace/mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)  `innovation: 8`

**A tool for auditing npm package dependencies to identify security vulnerabilities using real-time remote registry integration.**

**Key Features:**
- Real-time security vulnerability scanning
- Remote npm registry integration
- Detailed CVSS scoring and CVE references
- Automatic fix recommendations
- Support for multiple severity levels

---

### 596. [qpd-v/mcp-delete](https://github.com/qpd-v/mcp-delete)  `innovation: 8`

**A Model Context Protocol server enabling AI assistants to safely delete files using relative or absolute paths with smart resolution.**

**Key Features:**
- File deletion via MCP
- Smart path resolution
- Support for relative and absolute paths
- Secure deletion with error messages
- Compatibility with Claude and other MCP-compatible AI assistants

---

### 597. [qpd-v/mcp-wordcounter](https://github.com/qpd-v/mcp-wordcounter)  `innovation: 8`

**A Model Context Protocol server for analyzing text documents with word and character counting capabilities.**

**Key Features:**
- word counting
- character counting
- document analysis
- text statistics

---

### 598. [quanticsoul4772/analytical-mcp](https://github.com/quanticsoul4772/analytical-mcp)  `innovation: 8`

**Analytical MCP Server provides AI-driven statistical analysis, decision support, and research verification tools for Claude.**

**Key Features:**
- Statistical Analysis
- Decision Analysis
- Logical Reasoning
- Research Verification

---

### 599. [quarkiverse/quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)  `innovation: 8`

**A server enabling Large Language Models to interact with databases via JDBC, supporting multiple database types and providing a unified interface.**

**Key Features:**
- JDBC protocol support
- Multi-database compatibility
- Integration with Quarkus ecosystem
- Dynamic configuration via command line

---

### 600. [qwang07/duck-duck-mcp](https://github.com/qwang07/duck-duck-mcp)  `innovation: 8`

**Implementation of a DuckDuckGo search engine integrated with the Model Context Protocol (MCP) for AI-driven context-aware applications.**

**Key Features:**
- DuckDuckGo search engine integration
- Customizable search settings (region
- safe search)
- Structured search result output
- Metadata extraction
- Scalable for AI/ML applications

---

### 601. [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp)  `innovation: 8`

**A Model Context Protocol server providing professional cycling data for analysis and visualization.**

**Key Features:**
- Retrieve rider biographical information
- Access race results and statistics
- Explore historical race data
- Analyze performance trends
- Visualize team and career progression

---

### 602. [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp)  `innovation: 8`

**A web-based platform enabling AI-driven exploration, analysis, and interaction with the Rijksmuseum's art collection through natural language queries.**

**Key Features:**
- Search Artworks
- Artwork Details
- High-Resolution Images
- User Collections
- Image Viewing
- Artist Timeline
- Collection Analysis
- Visual Details

---

### 603. [rafalwilinski/aws-mcp](https://github.com/rafalwilinski/aws-mcp)  `innovation: 8`

**A model context protocol server enabling natural language interaction with AWS resources.**

**Key Features:**
- Natural language querying of AWS resources
- Multi-region support
- Secure credential management
- Integration with AWS profiles and SSO
- Local execution with local credentials

---

### 604. [rajyraman/genaiscript-pac-az-mcp](https://github.com/rajyraman/genaiscript-pac-az-mcp)  `innovation: 8`

**A framework enabling communication with AI models via Model Context Protocol (MCP) to standardize interactions between AI and various data sources.**

**Key Features:**
- Integration with Azure CLI and Power Platform CLI for seamless API access
- Support for MCP server deployment in DevContainers or local environments
- Enables secure
- standardized communication with AI models using Graph API and Azure REST API
- Facilitates automation of workflows and integration with external tools

---

### 605. [random-robbie/mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)  `innovation: 8`

**An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling secure and flexible headless browser interactions.**

**Key Features:**
- Headless web browsing with MCP support
- Secure API for browser automation
- Advanced page interaction tools
- Multi-tab management
- JavaScript execution on pages
- Page content extraction and manipulation
- Screenshot capturing
- Link extraction and filtering

---

### 606. [ratchanonth60/querycraftmcp](https://github.com/ratchanonth60/querycraftmcp)  `innovation: 8`

**QueryCraftMCP is a flexible Model Context Protocol server enabling LLMs to interact with multiple databases via standardized APIs.**

**Key Features:**
- Multi-database backend support (PostgreSQL and SQLite)
- Dynamic tool loading based on active database
- Schema discovery and structured data querying
- Secure connection management with lifespan control
- Transport protocol: Server-Sent Events (SSE)
- Docker containerization for deployment

---

### 607. [ray0907/mcp-arxiv](https://github.com/ray0907/mcp-arxiv)  `innovation: 8`

**A platform for searching and retrieving academic papers from arXiv using MCP.**

**Key Features:**
- Search arXiv papers
- Retrieve paper content
- Integrate with LLMs
- Support code review and security checks

---

### 608. [receptopalak/postgis-mcp](https://github.com/receptopalak/postgis-mcp)  `innovation: 8`

**A server application integrating PostGIS with Model Context Protocol (MCP) for database connectivity.**

**Key Features:**
- MCP server integration
- PostGIS database support
- Hot-reload development mode
- Environment configuration (development/production)
- Secure code management and version control

---

### 609. [redhat-ai-tools/mcp-registry-mcp](https://github.com/redhat-ai-tools/mcp-registry-mcp)  `innovation: 8`

**A registry server for the Model Context Protocol (MCP) that enables secure and isolated management of MCP resources.**

**Key Features:**
- health_check
- list_registry_server_entries
- get_server_details
- ping

---

### 610. [reexpressai/reexpress_mcp_server](https://github.com/reexpressai/reexpress_mcp_server)  `innovation: 8`

**A tool for adding statistical verification and confidence estimation to AI model outputs, enhancing reliability in LLM-based workflows.**

**Key Features:**
- Tool-calling LLMs with SDM estimator
- Dynamic update handling after verification
- Ability to adapt models for custom tasks
- Integration of pre-trained Reexpress models
- Local processing to maintain data privacy

---

### 611. [rember/rember-mcp](https://github.com/rember/rember-mcp)  `innovation: 8`

**A Model Context Protocol (MCP) server for Rember to enhance memory and study workflows.**

**Key Features:**
- MCP server integration
- Flashcard creation from chats and documents
- API key management
- Logging and debugging support
- User session handling
- Secure code review tools
- CI/CD pipeline setup
- Observability and telemetry

---

### 612. [ricauts/cybermcp](https://github.com/ricauts/cybermcp)  `innovation: 8`

**CyberMCP enables AI-powered security testing of backend APIs using a Model Context Protocol server.**

**Key Features:**
- Authentication testing (JWT
- OAuth2)
- Injection testing (SQL injection
- XSS)
- Data protection checks (sensitive data exposure)
- Rate limiting and DoS vulnerability assessment
- Security header validation
- Comprehensive security checklists and guides

---

### 613. [rinardnick/mcp-terminal](https://github.com/rinardnick/mcp-terminal)  `innovation: 8`

**A secure terminal execution server supporting controlled command access for AI models.**

**Key Features:**
- secure terminal execution
- command validation
- resource limits
- MCP protocol support

---

### 614. [rishabkoul/iterm-mcp-server](https://github.com/rishabkoul/iterm-mcp-server)  `innovation: 8`

**A server enabling secure and isolated interaction between AI assistants and iTerm2 terminals using the Model Context Protocol.**

**Key Features:**
- Create and manage iTerm2 terminal sessions
- Execute commands in specific terminals
- Read and close active terminals
- Input sanitization and error handling

---

### 615. [rizaqpratama/mcp-cucumberstudio](https://github.com/rizaqpratama/mcp-cucumberstudio)  `innovation: 8`

**A Model Context Protocol server that integrates with CucumberStudio to provide contextual data for AI applications.**

**Key Features:**
- Fetch data from CucumberStudio API
- Provide context about CucumberStudio projects and features
- Enable AI to generate and modify test scenarios
- Apply changes to CucumberStudio resources
- View schema for MCP server

---

### 616. [robertpelloni/ffr-difficulty-model](https://github.com/robertpelloni/ffr-difficulty-model)  `innovation: 8`

**Supervised Learning Model to Quantify Difficulty of Stepfiles in FlashFlashRevolution**

**Key Features:**
- The core functionality is a prediction pipeline that estimates the difficulty score and meter for StepMania charts based on the input file's features. The model is designed to quantify the difficulty of these musical charts.

---

### 617. [roger1337/JDBG](https://github.com/roger1337/JDBG)  `innovation: 8`

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

### 618. [ronantakizawa/gis-dataconversion-mcp](https://github.com/ronantakizawa/gis-dataconversion-mcp)  `innovation: 8`

**A Model Context Protocol server enabling AI models to access and manipulate geographic data in various formats.**

**Key Features:**
- Reverse geocoding
- Coordinate system conversion
- WKT/GeoJSON conversion
- CSV/GeoJSON conversion
- TopoJSON/GeoJSON conversion
- KML to GeoJSON
- GeoJSON to KML

---

### 619. [ronniemh/phrases-mcp-server](https://github.com/ronniemh/phrases-mcp-server)  `innovation: 8`

**Servidor MCP elegante y eficiente para gestionar frases inspiradoras, integrándose con Claude for Desktop.**

**Key Features:**
- Gestión completa de frases (crear
- leer
- actualizar
- eliminar)
- Integración con Claude for Desktop
- API mock para pruebas y desarrollo
- Configuración personalizable para entornos MCP

---

### 620. [runninghare/ts-def-mcp](https://github.com/runninghare/ts-def-mcp)  `innovation: 8`

**A Model Context Protocol server to locate TypeScript symbol definitions within codebases.**

**Key Features:**
- Finds original definitions of TypeScript symbols
- Supports imported symbols from external packages
- Returns definition location and code snippet
- Works with stdio interface for AI integration
- Seamless integration with AI code editors

---

### 621. [russellw/sourceview](https://github.com/russellw/sourceview)  `innovation: 8`

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

### 622. [ryan0204/github-repo-mcp](https://github.com/ryan0204/github-repo-mcp)  `innovation: 8`

**A server enabling AI assistants to browse and interact with GitHub repositories.**

**Key Features:**
- Repository browsing
- Directory navigation
- File content viewing
- Rate limit management
- Token-based authentication

---

### 623. [ryft-io/iceberg-mcp](https://github.com/ryft-io/iceberg-mcp)  `innovation: 8`

**A model context protocol server enabling natural language interaction with Apache Iceberg Lakehouse tables.**

**Key Features:**
- Natural language interface
- MCP integration
- Table schema exploration
- Data query generation

---

### 624. [samihalawa/mcp-server-smtp](https://github.com/samihalawa/mcp-server-smtp)  `innovation: 8`

**A Model Context Protocol server enabling secure and flexible email sending for AI assistants.**

**Key Features:**
- Multiple SMTP configurations
- Email templates creation and management
- Bulk email sending with batching and rate limiting
- Full HTML support for rich email content
- Comprehensive logging of all email activities
- Dynamic template variables for personalized emails

---

### 625. [samwang0723/mcp-booking](https://github.com/samwang0723/mcp-booking)  `innovation: 8`

**An AI-powered model context protocol server for restaurant discovery and booking, integrating location data, cuisine preferences, mood, and event types.**

**Key Features:**
- Smart Restaurant Search with location filtering
- AI Recommendations based on user preferences
- Event-specific matching (dating
- family
- business
- etc.)
- Mood-based atmosphere alignment
- Booking assistance with mock reservation capabilities

---

### 626. [santos-404/mcp-server.sqlite](https://github.com/santos-404/mcp-server.sqlite)  `innovation: 8`

**Implementation of an MCP server for SQLite to enable AI models to execute queries and interact with databases.**

**Key Features:**
- SQLite database interaction
- MCP protocol support
- AI model context management
- Database schema management
- Query execution capabilities

---

### 627. [sapientpants/sonarqube-mcp-server](https://github.com/sapientpants/sonarqube-mcp-server)  `innovation: 8`

**A server implementation for Model Context Protocol (MCP) to integrate with SonarQube, enabling secure and efficient code analysis.**

**Key Features:**
- MCP server integration
- code analysis
- security features
- automation capabilities

---

### 628. [saurabhdaware/abell-mcp](https://github.com/saurabhdaware/abell-mcp)  `innovation: 8`

**Exploring MCPs for Abell to understand their architecture and integration.**

**Key Features:**
- Analyze MCPs
- Integrate external tools
- Developer workflows
- Code review
- Security features

---

### 629. [sboludaf/mcp-azure-pricing](https://github.com/sboludaf/mcp-azure-pricing)  `innovation: 8`

**A Python-based MCP server for programmatically querying Azure pricing data.**

**Key Features:**
- Service family management
- Product lookup
- Monthly cost calculation
- API integration with Azure Retail Prices
- Structured workflow automation

---

### 630. [seanivore/mcp-code-analyzer](https://github.com/seanivore/mcp-code-analyzer)  `innovation: 8`

**A Model Context Protocol server for Python code analysis with Claude.**

**Key Features:**
- code analysis
- security scanning
- AI integration
- code review support

---

### 631. [seanmcloughlin/mcp-vcd](https://github.com/seanmcloughlin/mcp-vcd)  `innovation: 8`

**A model context protocol implementation for handling large Value Change Dump (VCD) files.**

**Key Features:**
- Model Context Protocol
- Value Change Dump (VCD) support
- Signal extraction and management

---

### 632. [secretiveshell/mcp-toolhouse](https://github.com/secretiveshell/mcp-toolhouse)  `innovation: 8`

**A model context protocol server enabling secure access to AI and development tools.**

**Key Features:**
- Model context protocol access
- Tool integration from Toolhouse platform
- Secure code deployment
- Workflow automation
- Code review and management

---

### 633. [sellersmith/tailorkit-mcp](https://github.com/sellersmith/tailorkit-mcp)  `innovation: 8`

**TailorKit MCP enables e-commerce product customization via AI-driven personalization.**

**Key Features:**
- Template management
- Layer control
- Shopify integration
- AI-powered personalization
- Minimal development effort

---

### 634. [sentriz/betanin](https://github.com/sentriz/betanin)  `innovation: 8`

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

### 635. [setkyar/youtube-subtitles-mcp](https://github.com/setkyar/youtube-subtitles-mcp)  `innovation: 8`

**A GitHub repository providing a MCP server for integrating AI assistants like Claude with YouTube subtitle services.**

**Key Features:**
- YouTube subtitle download and analysis
- Language detection and subtitle translation
- Integration with Claude Desktop
- Docker-based deployment
- Multi-language support

---

### 636. [shanksxz/gh-mcp-server](https://github.com/shanksxz/gh-mcp-server)  `innovation: 8`

**A GitHub context server enabling AI models to access and interact with GitHub repository contents as contextual data.**

**Key Features:**
- Fetch repository contents
- Get file contents from a repository
- Filter files by extension
- Exclude specific paths
- View repository structure
- Limit number of files returned

---

### 637. [shashwat001/mcptools-langchain-integration](https://github.com/shashwat001/mcptools-langchain-integration)  `innovation: 8`

**A TypeScript project integrating LangChain with MCP tools for interactive chat-based tool execution.**

**Key Features:**
- Interactive chat interface
- MCP tool integration
- LLM-based tool execution
- Secure environment setup
- Real-time system prompts

---

### 638. [shenghaiwang/androidbuild](https://github.com/shenghaiwang/androidbuild)  `innovation: 8`

**A tool for building Android projects and providing feedback to LLMs.**

**Key Features:**
- Android project building
- Error feedback to LLMs
- Integration with VS Code extensions
- Support for unit and instrumented tests

---

### 639. [shinkeonkim/e-gonghun-mcp](https://github.com/shinkeonkim/e-gonghun-mcp)  `innovation: 8`

**A platform for managing and integrating external tools within the MCP ecosystem.**

**Key Features:**
- Context Management
- API Integration
- Automation Tools
- Secure Development Practices

---

### 640. [shinshin86/mcp-simple-aivisspeech](https://github.com/shinshin86/mcp-simple-aivisspeech)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling seamless integration with AivisSpeech for natural-sounding Japanese text-to-speech conversion.**

**Key Features:**
- Text-to-Speech Conversion
- Multiple Voice Characters
- Configurable Parameters (speed
- pitch
- volume)
- Cross-Platform Audio Support
- Task Notifications
- Smart Error Handling
- Engine Status Monitoring

---

### 641. [shreyaskarnik/mcpet](https://github.com/shreyaskarnik/mcpet)  `innovation: 8`

**A TypeScript-based virtual pet simulation platform demonstrating core Model Context Protocol concepts.**

**Key Features:**
- Virtual pet adoption and customization
- Dynamic pet lifecycle stages (baby to adult)
- Stat tracking: hunger
- happiness
- health
- energy
- cleanliness
- Interactive tools: feeding
- playing games
- bathing

---

### 642. [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp)  `innovation: 8`

**Integrates Apple Notes with Claude Model Context Protocol to enable AI-powered search and organization of personal notes.**

**Key Features:**
- Read all notes
- Search notes by content
- View full note content
- Manage notes and prompts
- Integrate with Claude Desktop for intelligent search

---

### 643. [skobyn/mcp-dataforseo](https://github.com/skobyn/mcp-dataforseo)  `innovation: 8`

**A server-based Model Context Protocol implementation for integrating with the DataForSEO API.**

**Key Features:**
- Model Context Protocol server
- JSON API integration
- DataForSEO API support
- Real-time response handling
- Environment variable configuration

---

### 644. [smithery-ai/smithery-cookbook](https://github.com/smithery-ai/smithery-cookbook)  `innovation: 8`

**Smithery Cookbook provides practical examples and guides for building MCP servers using various programming languages.**

**Key Features:**
- Interactive playground for hands-on learning
- Language-specific server examples
- Deployment options on Smithery platform
- Security best practices integration
- Community support and documentation

---

### 645. [softgridinc-pte-ltd/mcp-excel-reader-server](https://github.com/softgridinc-pte-ltd/mcp-excel-reader-server)  `innovation: 8`

**A Microsoft Excel server enabling secure and efficient reading of Excel files using modelcontextprotocol.**

**Key Features:**
- Read content from all sheets in an Excel file
- Read content from a specific sheet by name or index
- Handle empty cells and data type conversions
- Return structured JSON output
- Secure data handling and error management

---

### 646. [solana-foundation/solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)  `innovation: 8`

**Demo of a Model Context Protocol (MCP) server for Solana development.**

**Key Features:**
- Basic RPC methods for Solana (getBalance
- getAccountInfo
- getTransaction)
- Simple MCP server implementation with fetching tools
- Extensible architecture for adding new tools and resources

---

### 647. [solidus-/atlassian-cursor-mcp](https://github.com/solidus-/atlassian-cursor-mcp)  `innovation: 8`

**Managed Code Plugin for Cursor IDE integrating with Atlassian products.**

**Key Features:**
- JIRA integration
- Confluence integration
- BitBucket integration
- Pipeline automation
- Code review management
- Workflow automation

---

### 648. [spences10/mcp-duckduckgo-search](https://github.com/spences10/mcp-duckduckgo-search)  `innovation: 8`

**A unified search platform integrating DuckDuckGo with LLMs for enterprise-grade web search capabilities.**

**Key Features:**
- Comprehensive web search using DuckDuckGo
- Rich result types (knowledge graph
- news
- video
- images)
- Region-specific and safe search filtering
- Date-based and pagination controls
- Result caching and secure search options

---

### 649. [spences10/mcp-jinaai-grounding](https://github.com/spences10/mcp-jinaai-grounding)  `innovation: 8`

**A tool for integrating Jina.ai Grounding API with LLMs to enhance responses with real-time web content.**

**Key Features:**
- Advanced web content grounding
- Real-time fact-checking
- Web content analysis
- Precise relevance scoring

---

### 650. [spences10/mcp-wsl-exec](https://github.com/spences10/mcp-wsl-exec)  `innovation: 8`

**A secure Windows Subsystem for Linux (WSL) server enabling safe, isolated command execution and information gathering for enterprise software development.**

**Key Features:**
- Information Gathering (Read-Only)
- Command Execution with Safety
- Secure Command Sanitization
- Environment Monitoring

---

### 651. [squirrelogic/mcp-feature-discussion](https://github.com/squirrelogic/mcp-feature-discussion)  `innovation: 8`

**A platform enabling AI-driven intelligent discussions and architectural guidance for software development teams.**

**Key Features:**
- AI Lead Developer Interface
- Persistent memory of discussions
- Context-aware recommendations
- Feature memory management
- Architecture pattern recommendations

---

### 652. [stackloklabs/ocireg-mcp](https://github.com/stackloklabs/ocireg-mcp)  `innovation: 8`

**An MCP server enabling LLM-powered applications to query OCI registries and image references.**

**Key Features:**
- Get information about OCI images
- List tags for repositories
- Get image manifests
- Get image configs
- Retrieve image metadata
- Support authentication for private registries

---

### 653. [stackzero-labs/mcp](https://github.com/stackzero-labs/mcp)  `innovation: 8`

**Official MCP server for stackzero to enable Model Context Protocol communication.**

**Key Features:**
- Model Context Protocol Server
- Secure Integration
- Developer Tools
- CI/CD Support

---

### 654. [startr/web-mcpo-repo_scanner](https://github.com/startr/web-mcpo-repo_scanner)  `innovation: 8`

**A tool for automatically scanning codebases for unmanaged or incomplete TODO items, improving code quality and maintainability.**

**Key Features:**
- AI-powered TODO detection across repositories
- Integration with MCP-compatible assistants (Sage.is
- Claude.ai)
- Real-time scanning and live updates
- Support for local and remote repositories
- Priority inference from TODO comments
- Dashboard for visualizing TODO metrics

---

### 655. [starwind-ui/starwind-ui-mcp](https://github.com/starwind-ui/starwind-ui-mcp)  `innovation: 8`

**A TypeScript implementation of a Model Context Protocol (MCP) server for Starwind UI and Pro, enhancing AI tool integration.**

**Key Features:**
- Model Context Protocol server
- AI assistant integration with Claude
- Component validation
- Live documentation fetching

---

### 656. [stefanoamorelli/sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)  `innovation: 8`

**A secure, AI-powered platform for accessing SEC EDGAR filings and financial data with precise numeric accuracy.**

**Key Features:**
- AI-assisted code generation
- SEC EDGAR data integration
- Secure development environment
- Automated workflows
- Code review and management

---

### 657. [stevenstavrakis/obsidian-mcp](https://github.com/stevenstavrakis/obsidian-mcp)  `innovation: 8`

**A lightweight MCP server enabling AI assistants to interact with Obsidian vaults for note management.**

**Key Features:**
- Read and search notes
- Create
- edit
- delete
- move
- rename notes
- Manage tags
- Integrate with Obsidian vaults

---

### 658. [strangelove-ventures/web3-mcp](https://github.com/strangelove-ventures/web3-mcp)  `innovation: 8`

**Web3 MCP server enabling secure, isolated blockchain interactions across multiple chains.**

**Key Features:**
- Multi-chain support (Solana
- Ethereum
- THORChain
- XRP Ledger
- Cardano
- etc.)
- Environment variable configuration for tool registration
- Secure handling of private keys and tokens
- Cross-chain operations including swaps and transfers
- Real-time transaction history and analytics

---

### 659. [studentofjs/mcp-figma-to-react](https://github.com/studentofjs/mcp-figma-to-react)  `innovation: 8`

**A tool that converts Figma designs into React components using TypeScript and Tailwind CSS.**

**Key Features:**
- Fetch Figma designs via API
- Extract components from Figma files
- Generate React components with TypeScript
- Apply Tailwind CSS classes
- Enhance accessibility features
- Support standard and SSE transports

---

### 660. [sugatraj/cursor-browser-tools-mcp](https://github.com/sugatraj/cursor-browser-tools-mcp)  `innovation: 8`

**A browser monitoring and interaction tool that enables AI-powered analysis of web pages through a Chrome extension.**

**Key Features:**
- Browser data capture via Chrome extension
- AI-powered insights using Anthropic's Model Context Protocol (MCP)
- Automated auditing for accessibility
- performance
- SEO
- and best practices
- Integration with Node server for seamless communication
- Structured reporting and actionable recommendations

---

### 661. [suixinlei/tongyi-wanx-mcp-server](https://github.com/suixinlei/tongyi-wanx-mcp-server)  `innovation: 8`

**A TypeScript-based MCP server enabling integration with large language models for AI-generated images and videos.**

**Key Features:**
- Text-to-Image generation via MCP API
- Text-to-Video generation via MCP API
- Asynchronous task handling for long-running generation tasks
- Support for custom prompts
- negative prompts
- and advanced configurations

---

### 662. [sujianqingfeng/mcp-apifox](https://github.com/sujianqingfeng/mcp-apifox)  `innovation: 8`

**A tool to bridge AI assistants with Apifox API documentation via Model Context Protocol.**

**Key Features:**
- API information extraction from Apifox URL
- Integration with Model Context Protocol (MCP)
- Code generation and workflow automation
- Secure development environment setup
- AI-assisted code review and security checks

---

### 663. [superfaceai/mcp](https://github.com/superfaceai/mcp)  `innovation: 8`

**A platform enabling integration of Superface AI tools via Model Context Protocol for enterprise applications.**

**Key Features:**
- Model context protocol integration
- API key management
- Docker-based deployment
- Code review and security features
- Developer workflow automation

---

### 664. [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp)  `innovation: 8`

**A collection of Apple-native tools designed to enhance the model context protocol for seamless integration with AI applications.**

**Key Features:**
- Apple MCP (Model Context Protocol) implementation
- Automated code generation and management
- Integration with GitHub Copilot and other AI development tools
- Secure code deployment and protection against vulnerabilities
- Development environments like Codespaces for instant access

---

### 665. [superseoworld/mcp-spotify](https://github.com/superseoworld/mcp-spotify)  `innovation: 8`

**A server enabling secure and efficient interaction with Spotify's Web API for enterprise applications.**

**Key Features:**
- Spotify API access via MCP protocol
- Search for tracks
- albums
- artists
- and playlists
- Artist information including top tracks and related artists
- Album and track details
- Audiobook information with market-specific content
- Playlist management (creation
- modification

---

### 666. [surescaleai/openai-gpt-image-mcp](https://github.com/surescaleai/openai-gpt-image-mcp)  `innovation: 8`

**A tool server enabling context-aware image generation and editing using OpenAI's GPT-4o/gpt-image-1 API.**

**Key Features:**
- Generate images from text prompts
- Edit images using advanced prompts and masks
- Support for multiple image processing operations
- Integration with MCP protocol for context-aware APIs
- Deployment options including Azure

---

### 667. [surya-madhav/mcp](https://github.com/surya-madhav/mcp)  `innovation: 8`

**A platform for integrating external tools and APIs into a unified workflow, enabling secure and automated data processing.**

**Key Features:**
- Integration of external tools
- Web scraping capabilities
- AI model interaction
- Security and code security features
- Streamlit UI for visualization

---

### 668. [suthio/brave-deep-research-mcp](https://github.com/suthio/brave-deep-research-mcp)  `innovation: 8`

**A Borg-based AI platform that integrates Brave Search with Puppeteer for deep web research, enabling comprehensive content extraction and analysis.**

**Key Features:**
- Deep search using Brave Search API
- Puppeteer-powered page exploration
- Content extraction from full webpages
- Link traversal to gather related information
- Metadata and structured data collection
- Configurable search depth and customization options

---

### 669. [svnscha/mcp-windbg](https://github.com/svnscha/mcp-windbg)  `innovation: 8`

**A model context protocol server that integrates AI with WinDbg for crash dump analysis and remote debugging.**

**Key Features:**
- AI-powered crash dump analysis using Model Context Protocol
- Remote debugging via WinDbg/CDB integration
- Natural language query support for debugging commands
- Cross-platform compatibility with MCP clients

---

### 670. [syucream/lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)  `innovation: 8`

**A MCP-compatible server enabling AI assistants to interact with Lightdash data via standardized API.**

**Key Features:**
- MCP-compatible access to Lightdash API
- Integration with Lightdash dashboards and charts
- Support for multiple transport modes (Stdio
- HTTP)
- Development and production deployment options
- Hot reloading in development mode

---

### 671. [tanker327/uuid-mcp](https://github.com/tanker327/uuid-mcp)  `innovation: 8`

**A lightweight Model Context Protocol (MCP) server generating timestamp-based UUIDs for secure, unique identifiers in AI applications.**

**Key Features:**
- Generate UUID v7
- Timestamp-based uniqueness
- Integration with Claude Desktop
- RFC-compliant UUID generation

---

### 672. [tatn/mcp-server-fetch-typescript](https://github.com/tatn/mcp-server-fetch-typescript)  `innovation: 8`

**A server-based tool for fetching and converting web content into various formats, supporting tasks from raw text extraction to rendered HTML.**

**Key Features:**
- get_raw_text
- get_rendered_html
- get_markdown
- get_markdown_summary

---

### 673. [taweili/mcp-rss-md](https://github.com/taweili/mcp-rss-md)  `innovation: 8`

**A tool for converting RSS feeds into Markdown format using the Model Context Protocol.**

**Key Features:**
- rss-to-md-server
- convert_rss
- output_path
- standalone_server

---

### 674. [tcehjaava/tmdb-mcp-server](https://github.com/tcehjaava/tmdb-mcp-server)  `innovation: 8`

**A server that provides access to The Movie Database API for searching movies, TV shows, people, and retrieving detailed information.**

**Key Features:**
- Search movies and TV shows by title or genre
- Get detailed movie information (budget
- runtime
- genres)
- Receive recommendations based on user queries
- Access person details including biographical data
- Discover trending content
- Integrate with Claude Desktop for enhanced UX

---

### 675. [tchbw/mcp-imessage](https://github.com/tchbw/mcp-imessage)  `innovation: 8`

**Implementation of Model Context Protocol for secure iMessage communication using MCP.**

**Key Features:**
- Send & receive iMessages
- Model Context Protocol integration
- Secure message delivery
- Context-aware communication

---

### 676. [tddt/stock_info_mcp](https://github.com/tddt/stock_info_mcp)  `innovation: 8`

**A Borg-based stock intelligence platform providing historical data, fundamental info, news, and risk alerts.**

**Key Features:**
- 获取股票历史数据
- 查询股票基本信息
- 获取风险警示股票列表
- 查看个股新闻
- 获取财经新闻（支持分页）
- 获取股票主营业务信息

---

### 677. [tejpalvirk/qualitativeresearch](https://github.com/tejpalvirk/qualitativeresearch)  `innovation: 8`

**A knowledge graph-based MCP server for managing qualitative research context across sessions.**

**Key Features:**
- Persistent research context management
- Session tracking and progress monitoring
- Thematic analysis and code application
- Participant and data source organization
- Research question linking and status tracking

---

### 678. [tejpalvirk/quantitativeresearch](https://github.com/tejpalvirk/quantitativeresearch)  `innovation: 8`

**A knowledge graph-based MCP server for managing quantitative research context across sessions.**

**Key Features:**
- Persistent research context management
- Session tracking and progress monitoring
- Hypothesis testing and result documentation
- Dataset and variable management
- Statistical analysis and model performance tracking
- Visualization of data models
- Integration with external tools and APIs

---

### 679. [tejpalvirk/student](https://github.com/tejpalvirk/student)  `innovation: 8`

**A knowledge graph-based MCP server for managing educational contexts, enabling structured representation of courses, assignments, exams, and study resources.**

**Key Features:**
- Knowledge graph management
- Session tracking and management
- Priority and status tracking
- Sequential learning path creation
- Real-time updates and notifications

---

### 680. [terrakube-io/mcp-server-terrakube](https://github.com/terrakube-io/mcp-server-terrakube)  `innovation: 8`

**A Model Context Protocol server for managing Terrakube workspaces, variables, and modules.**

**Key Features:**
- Workspace management
- Variable handling
- Module operations
- Environment configuration
- Type safety with TypeScript
- Modular design for maintenance

---

### 681. [terrehbyte/awesome-devblogs](https://github.com/terrehbyte/awesome-devblogs)  `innovation: 8`

**A curated list of links to game developer blogs and/or portfolios that you found interesting.**

**Key Features:**
- The resource provides links to various developer blogs
- portfolio sites
- and company websites
- focusing on showcasing skills
- projects
- and technical expertise within the game development/tech sphere.

---

### 682. [text2go/ai-humanizer-mcp-server](https://github.com/text2go/ai-humanizer-mcp-server)  `innovation: 8`

**A Model Context Protocol server designed to refine AI-generated content for natural, human-like output.**

**Key Features:**
- AI text detection
- natural language enhancement
- grammar perfection
- readability optimization
- length control
- preservation of key terms

---

### 683. [th-ad/oas-to-mcp](https://github.com/th-ad/oas-to-mcp)  `innovation: 8`

**A tool for transforming OAS to MCP, focusing on workflow automation and integration.**

**Key Features:**
- code generation
- workflow automation
- security integration
- CI/CD support
- code review tools

---

### 684. [thargor6/JWildfire](https://github.com/thargor6/JWildfire)  `innovation: 8`

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

### 685. [thunderboltsid/mcp-nutanix](https://github.com/thunderboltsid/mcp-nutanix)  `innovation: 8`

**A Go-based MCP server enabling LLMs to interact with Nutanix Prism Central APIs via the Model Context Protocol.**

**Key Features:**
- Connect to Nutanix Prism Central
- List and retrieve resources (VMs
- clusters
- hosts)
- Retrieve detailed resource information via URI
- Support interactive prompts for Claude or static credentials for Cursor

---

### 686. [timholden/figma-mcp-server](https://github.com/timholden/figma-mcp-server)  `innovation: 8`

**A server implementation enabling secure, isolated access to Figma files and projects via the Model Context Protocol.**

**Key Features:**
- Model Context Protocol (MCP) server integration
- Read-only file and project access
- Server-side architecture for design token management
- Variable creation
- reference handling
- and theme configuration
- Performance optimizations including caching and rate limiting

---

### 687. [tlazypanda/aptos-mcp-server](https://github.com/tlazypanda/aptos-mcp-server)  `innovation: 8`

**A Model Context Protocol (MCP) server enabling interaction with Aptos documentation and building full-stack blockchain applications.**

**Key Features:**
- Browse and search Aptos documentation
- Create new Aptos projects
- Generate components for Aptos projects
- Test and generate ABIs

---

### 688. [tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server)  `innovation: 8`

**A server enabling integration of tl;dv API with MCP for unified meeting intelligence across platforms.**

**Key Features:**
- Retrieve meetings from multiple platforms
- Fetch meeting metadata
- Get transcripts and highlights
- Import meetings via URL

---

### 689. [toolbase-ai/uploadthing-mcp](https://github.com/toolbase-ai/uploadthing-mcp)  `innovation: 8`

**Integration of MCP protocol for AI-assisted file uploads in UploadThing.**

**Key Features:**
- MCP protocol integration
- AI-assisted file uploads
- automated workflow execution

---

### 690. [tositon/opendeepsearch](https://github.com/tositon/opendeepsearch)  `innovation: 8`

**OpenDeepSearch is an open-source research tool that integrates MCP for structured, in-depth analysis of complex topics.**

**Key Features:**
- Comprehensive research with sub-question breakdown
- Iterative search and multiple queries
- Intelligent analysis and synthesis
- Citations and sources
- MCP integration
- WebSocket support

---

### 691. [trypeggy/instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)  `innovation: 8`

**A Python-based Instagram DM MCP server enabling secure and isolated communication between Instagram accounts.**

**Key Features:**
- Instagram Direct Message (DM) integration
- Secure handling of Instagram credentials
- Environment variable and configuration management
- Support for multiple platforms (Claude Desktop
- Cursor)
- Automatic session management for seamless user experience

---

### 692. [turlockmike/mcp-rand](https://github.com/turlockmike/mcp-rand)  `innovation: 8`

**A versatile random number and generator utility library for secure code generation, supporting UUIDs, numbers, passwords, dice, cards, and more.**

**Key Features:**
- UUID generation
- Random number generation (RNG)
- Password generation
- Dice rolling
- Card drawing
- Secure random string generation

---

### 693. [u3588064/entity-resolution](https://github.com/u3588064/entity-resolution)  `innovation: 8`

**A tool for identifying whether two data sets originate from the same entity using MCP protocol.**

**Key Features:**
- Text normalization
- Semantic value comparison
- JSON object traversal
- Language model integration
- MCP protocol support

---

### 694. [ujjalcal/mcp](https://github.com/ujjalcal/mcp)  `innovation: 8`

**A Python SDK for building MCP servers to provide context, resources, and tools for LLM applications.**

**Key Features:**
- MCP Server Creation
- Resource Management (Resources
- Prompts)
- Tool Integration (Tools
- Prompts)
- Context Provision via Context Objects
- Dynamic User Interaction (Prompts
- Debugging)
- Data Handling (Images
- Files

---

### 695. [unievo/xpilot-mcp-library](https://github.com/unievo/xpilot-mcp-library)  `innovation: 8`

**Library enabling xPilot to interact with MCP servers for context and tool integration.**

**Key Features:**
- MCP server configuration
- context management
- tool integration

---

### 696. [victoriametrics-community/mcp-victoriametrics](https://github.com/victoriametrics-community/mcp-victoriametrics)  `innovation: 8`

**Implementation of Model Context Protocol (MCP) server for VictoriaMetrics to enable advanced observability, integration, and automation capabilities.**

**Key Features:**
- Access to all read-only VictoriaMetrics APIs
- Seamless integration with VictoriaMetrics dashboard and documentation
- Advanced monitoring
- alerting
- and data exploration
- Alert debugging
- rule testing
- and configuration management
- Integration with external tools and workflows
- Support for DevOps and CI/CD pipelines

---

### 697. [vitaliiivanovspryker/spryker-package-search-mcp](https://github.com/vitaliiivanovspryker/spryker-package-search-mcp)  `innovation: 8`

**A tool for searching and managing Spryker packages using Model Context Protocol.**

**Key Features:**
- Model Context Protocol server
- Natural language search
- GitHub repository integration
- Code-level search
- Filtering by organization

---

### 698. [vltansky/cursor-chat-history-mcp](https://github.com/vltansky/cursor-chat-history-mcp)  `innovation: 8`

**A tool that links GitHub cursor conversations to code commits and context, enabling developers to trace discussions and fixes directly back to their source code.**

**Key Features:**
- Link Cursor conversations to Git commits
- Retrieve context for specific commits or files
- Search and filter conversations by keywords
- timestamps
- and project
- Extract patterns in code and discussions
- Integrate with VS Code for seamless development experience

---

### 699. [vlttnv/k8s-mcp](https://github.com/vlttnv/k8s-mcp)  `innovation: 8`

**A Python-based Model Context Protocol (MCP) tool for Kubernetes clusters to retrieve cluster information and diagnose issues.**

**Key Features:**
- Model Context Protocol API
- Cluster diagnostics
- Resource inspection
- Pod and deployment management

---

### 700. [vortiago/mcp-azure-devops](https://github.com/vortiago/mcp-azure-devops)  `innovation: 8`

**A Model Context Protocol server enabling AI assistants to interact with Azure DevOps services via Python SDK.**

**Key Features:**
- Work Item Management
- Project Management
- Team Management
- Pipeline Operations
- Branch Policy Administration

---

### 701. [vulh1209/context-bank-mcp](https://github.com/vulh1209/context-bank-mcp)  `innovation: 8`

**A project that uses the Model Context Protocol to interface with the AtherOS knowledge base, enabling secure and isolated querying of information.**

**Key Features:**
- Create new chat sessions
- Send messages to chat sessions

---

### 702. [waldur/waldur-mcp-server](https://github.com/waldur/waldur-mcp-server)  `innovation: 8`

**Waldur MCP server enabling secure integration between Waldur instance and Claude Desktop via Model Context Protocol.**

**Key Features:**
- Model Context Protocol implementation
- Secure token management
- Integration with Waldur instance
- Support for Claude Desktop

---

### 703. [wallaceobsidian01/pipedream](https://github.com/wallaceobsidian01/pipedream)  `innovation: 8`

**A platform for building and managing MCP servers to host APIs, enabling secure, isolated environments for applications.**

**Key Features:**
- Run MCP servers locally or in production
- Manage server accounts
- credentials
- and API requests
- Integrate with external tools and services
- Support OAuth2 authorization for secure access control
- Customize server behavior via configuration files

---

### 704. [wangtsiao/pulse-cn-mcp](https://github.com/wangtsiao/pulse-cn-mcp)  `innovation: 8`

**A server that provides real-time trending content from Chinese internet sources using the Model Context Protocol.**

**Key Features:**
- Weibo real-time trends
- Weibo hotspots
- Daily horoscopes
- Daily motivational quotes
- Internet hotspot aggregator
- Today's headlines
- Paper news hotspots
- 36Kr business news
- Huxiu 24-hour trends

---

### 705. [wazzan/mcp-coincap-jj](https://github.com/wazzan/mcp-coincap-jj)  `innovation: 8`

**A MCP server providing real-time cryptocurrency analysis using the CoinCap API.**

**Key Features:**
- Real-time price data
- Market analysis
- Historical trends
- API integration

---

### 706. [weaviate/mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)  `innovation: 8`

**Weaviate MCP Server for managing context and model data in Weaviate.**

**Key Features:**
- MCP Server Integration
- Model Context Management
- Secure Data Exchange

---

### 707. [webreactiva-devs/mcp-character-counter](https://github.com/webreactiva-devs/mcp-character-counter)  `innovation: 8`

**A lightweight Model Context Protocol server for detailed character analysis of text.**

**Key Features:**
- Character count analysis
- Character type breakdown (letters
- numbers
- symbols)
- Integration with Claude Desktop and GitHub Copilot
- Detailed usage examples and setup instructions

---

### 708. [weero-finance/kaiafun-mcp](https://github.com/weero-finance/kaiafun-mcp)  `innovation: 8`

**An MCP server for listing and trading tokens on KaiaFun and interacting with the Kaia blockchain.**

**Key Features:**
- List new tokens
- Buy and sell tokens
- Interact with Kaia blockchain
- Token metadata management

---

### 709. [wei/mymlh-mcp-server](https://github.com/wei/mymlh-mcp-server)  `innovation: 8`

**A secure, OAuth-authenticated Model Context Protocol (MCP) server enabling secure access to MyMLH API v4 for AI applications.**

**Key Features:**
- Secure authentication using MyMLH API v4 with OAuth
- User data access including profile
- education
- and employment history
- Automatic token management and refresh
- Cloudflare Workers deployment for low-latency edge performance
- Support for multiple MCP clients (VS Code
- Cline
- Roo
- Claude

---

### 710. [weidongxu-microsoft/mcp-azure-java-sdk-assist](https://github.com/weidongxu-microsoft/mcp-azure-java-sdk-assist)  `innovation: 8`

**A project demonstrating MCP server implementation for secure AI assistant integration.**

**Key Features:**
- MCP server implementation
- Azure Java SDK integration
- AI assistant connectivity
- secure input management
- tool management system

---

### 711. [winfsp/winfsp](https://github.com/winfsp/winfsp)  `innovation: 8`

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

### 712. [winterjung/mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)  `innovation: 8`

**A MCP server for Korean spell checking, enabling context-aware language processing.**

**Key Features:**
- Korean spell checking
- MCP server integration
- Context-aware language processing
- Developer-friendly API
- Customizable configurations

---

### 713. [wirdes/db-mcp-tool](https://github.com/wirdes/db-mcp-tool)  `innovation: 8`

**A powerful Model Context Protocol (MCP) tool for exploring and managing various database types including PostgreSQL, MySQL, and Firestore.**

**Key Features:**
- Connect to multiple databases
- List tables
- View triggers
- List functions
- Execute SQL queries
- Export table schemas
- Export table data

---

### 714. [wuyunmei/momedb-mcp](https://github.com/wuyunmei/momedb-mcp)  `innovation: 8`

**A platform for managing AI applications using MCP, focusing on knowledge management and secure development workflows.**

**Key Features:**
- User management (create_user
- get_user
- update_user
- delete_user)
- Conversation data management (insert_blob
- get_blob
- delete_blob)
- Knowledge base management (query_knowledge
- add_knowledge
- relate_knowledge)

---

### 715. [x-lab2017/open-digger-mcp-server](https://github.com/x-lab2017/open-digger-mcp-server)  `innovation: 8`

**OpenDigger MCP Server enables advanced repository analytics and insights through tools and prompts.**

**Key Features:**
- get_open_digger_metric
- get_open_digger_metrics_batch
- compare_repositories
- analyze_trends
- get_ecosystem_insights
- server_health
- prompts

---

### 716. [xaos-project/XaoS](https://github.com/xaos-project/XaoS)  `innovation: 8`

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

### 717. [xindong888999/phalcon-mcp](https://github.com/xindong888999/phalcon-mcp)  `innovation: 8`

**A Model Context Protocol (MCP) server for executing Phalcon 5.0.x commands, enabling AI-assisted framework management.**

**Key Features:**
- Command-line interface for Phalcon framework tools
- Integration with Cursor IDE for seamless development
- Automated project scaffolding and model generation
- Support for CRUD operations and API development
- Secure
- isolated execution environment

---

### 718. [yajihum/design-system-mcp](https://github.com/yajihum/design-system-mcp)  `innovation: 8`

**A design system MCP server for managing component props and design tokens.**

**Key Features:**
- MCP server for component prop and token management
- Dynamic token generation using Style Dictionary
- Integration with VSCode and VS Code
- Support for TypeScript
- CSS
- and JavaScript modules
- In-memory debugging capabilities
- Automated code generation and testing tools

---

### 719. [yamanoku/baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)  `innovation: 8`

**This server provides the status of Web Platform Dashboard API features via Model Context Protocol, supporting different baseline compatibility levels.**

**Key Features:**
- Baseline status lookup
- Feature availability by baseline level
- Browser compatibility filtering
- Usage statistics and data
- Integration with Docker and Deno
- API client configuration support

---

### 720. [yhc984/cursor-talk-to-figma-mcp-main](https://github.com/yhc984/cursor-talk-to-figma-mcp-main)  `innovation: 8`

**Integrates Cursor AI with Figma using Model Context Protocol for programmatic design interaction.**

**Key Features:**
- Model Context Protocol (MCP) integration
- WebSocket communication between Cursor and Figma
- Real-time document and selection management
- Automated creation
- editing
- and export of UI components

---

### 721. [yonaka15/mcp-pyodide](https://github.com/yonaka15/mcp-pyodide)  `innovation: 8`

**A Pyodide server implementation enabling LLMs to execute Python code via the Model Context Protocol (MCP).**

**Key Features:**
- Python code execution via MCP
- Support for stdio and SSE transport
- Type validation with arktype
- Data formatting handlers
- Request handling and message processing

---

### 722. [yuki10kobayashi/voicevox-mcp](https://github.com/yuki10kobayashi/voicevox-mcp)  `innovation: 8`

**Voicevox MCP Server enabling text-to-speech functionality for Mac devices using the Model Context Protocol.**

**Key Features:**
- MCP server implementation
- Voice synthesis via Text-to-Speech API
- Local audio playback using AFPlay
- Containerized deployment with Docker
- TypeScript-based architecture
- Integration with MCP SDK
- Secure and isolated execution environment

---

### 723. [yutakobayashidev/webforai-mcp-server](https://github.com/yutakobayashidev/webforai-mcp-server)  `innovation: 8`

**A cloud-based MCP server that extracts structured text from web pages for AI model consumption.**

**Key Features:**
- Web page text extraction via API
- Markdown-formatted output
- Error handling and retries
- Cloudflare Workers deployment
- Integration with MCP clients
- Support for tables
- images
- and links

---

### 724. [yy1588133/code-merge-mcp](https://github.com/yy1588133/code-merge-mcp)  `innovation: 8`

**A MCP-based server tool for code analysis, merging, and security inspection.**

**Key Features:**
- Code merging
- File tree generation
- Code analysis
- Security inspection
- Automated workflows
- Secure code management

---

### 725. [yzfly/mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)  `innovation: 8`

**A Python interpreter server enabling LLMs to interact with Python environments, execute code, and manage workflows securely.**

**Key Features:**
- Environment management (system/conda)
- Code execution in isolated directories
- File operations with safety limits
- Package installation and management
- Integration with Claude Desktop for enhanced UX

---

### 726. [zacco16/gmail-mcp-server](https://github.com/zacco16/gmail-mcp-server)  `innovation: 8`

**A server implementation for integrating Gmail API with AI assistants, enabling secure and context-aware email interactions.**

**Key Features:**
- Gmail Model Context Protocol (MCP) server implementation
- Email operations: sending
- receiving
- managing drafts
- calendar events
- Security features: OAuth2.0
- refresh tokens
- credential management
- Integration with external tools and APIs
- Multi-scope authorization and secure credential handling

---

### 727. [zaycruz/docker_mcp](https://github.com/zaycruz/docker_mcp)  `innovation: 8`

**A server that executes code in isolated Docker containers, enabling secure and isolated execution of applications.**

**Key Features:**
- Isolated code execution in Docker containers
- Multi-language support
- Complex script execution
- Container management (list
- create
- add dependencies
- execute)
- Integration with LLMs for intelligent code processing
- Package manager compatibility (pip
- npm

---

### 728. [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)  `innovation: 8`

**A Model Context Protocol server for converting various file types to Markdown.**

**Key Features:**
- Converts PDFs to Markdown
- Transforms images and audio with transcription
- Processes web pages and Bing search results
- Supports Docker-based deployment
- Integrates with TypeScript and Node.js ecosystems
- Provides customizable server behavior via configuration

---

### 729. [zeddy89/Context-Engine](https://github.com/zeddy89/Context-Engine)  `innovation: 8`

**Claude Code Context Engine**

**Key Features:**
- Four-layer context architecture
- Automated state restoration
- Native /compact hook integration
- Multi-file edit verification.

---

### 730. [zedmoster/revit-mcp](https://github.com/zedmoster/revit-mcp)  `innovation: 8`

**Integration of AI assistants with Revit via MCP for automated building design and management.**

**Key Features:**
- Automate Revit operations using AI tools
- Execute commands
- manage elements
- and interact programmatically
- Support modern DevOps workflows in enterprise environments

---

### 731. [zhangzhongnan928/mcp-blockchain-server](https://github.com/zhangzhongnan928/mcp-blockchain-server)  `innovation: 8`

**A secure blockchain server enabling AI assistants to interact with smart contracts while maintaining user control over private keys and transaction signing.**

**Key Features:**
- MCP Server (Model Context Protocol) for blockchain data access
- Web DApp for wallet integration and transaction signing
- Multi-chain support (Ethereum
- Polygon
- etc.)
- Smart contract interaction with verified networks
- Secure transaction preparation and signing workflow

---

### 732. [zxfgds/mcp-toolkit](https://github.com/zxfgds/mcp-toolkit)  `innovation: 8`

**A comprehensive MCP toolkit for AI assistants to interact securely with files, databases, and external services.**

**Key Features:**
- File system operations
- Database integration (MySQL
- PostgreSQL
- Redis)
- Code search and management
- Web scraping and content extraction
- Security features and token-based authentication
- Integration with external services

---

### 733. [zym9863/pixabay-mcp](https://github.com/zym9863/pixabay-mcp)  `innovation: 8`

**A model context protocol server for Pixabay image and video search with structured results and runtime validation.**

**Key Features:**
- Model Context Protocol (MCP) server
- Structured image/video search
- Runtime argument validation
- Safe search implementation

---

### 734. [zzaebok/mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)  `innovation: 8`

**A server implementation for interacting with Wikidata using the Model Context Protocol (MCP).**

**Key Features:**
- search_entity
- search_property
- get_properties
- execute_sparql
- get_metadata

---


## Websites & Non-GitHub Resources

### 735. [https://mbleigh.dev/posts/context-engineering-with-links](https://mbleigh.dev/posts/context-engineering-with-links)  `innovation: 10`

**Context Links Pattern**

**Key Features:**
- URI-addressable "Context Links"
- JIT resource fetching (file://
- data://)
- prevention of "context rot
- " HATEOAS for agent discovery.

---


*Total: 735 tools*
