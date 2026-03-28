# SUBMODULES.md: Intelligence Sources & Skills

This document serves as the master dashboard for all external registries and knowledge bases integrated into the BobbyBookmarks ecosystem.

## 🗂️ MCP Registries (Data Sources)
These submodules are programmatically scanned by `sync_submodules.py` to populate the research queue.

| Name | Location | Purpose |
| :--- | :--- | :--- |
| **Awesome MCP Servers (Punkpeye)** | `submodules/awesome-mcp-servers-punkpeye` | Massive community-curated list of MCP implementations. |
| **Awesome MCP Servers (Appcypher)** | `submodules/awesome-mcp-servers-appcypher` | Focuses on categorized MCP tools and frameworks. |
| **Awesome MCP Servers (Wong2)** | `submodules/awesome-mcp-servers-wong2` | Early-stage and specialized MCP server collection. |
| **ToolSDK MCP Registry** | `submodules/toolsdk-mcp-registry` | Enterprise-grade registry with structured JSON definitions. |
| **Awesome AI Apps** | `submodules/awesome-ai-apps` | General AI agent and application registry. |

## 🛠️ Skill & Agent Repositories
These submodules provide the specialized logic and prompt protocols used by the system.

| Name | Location | Contribution |
| :--- | :--- | :--- |
| **Anthropics Skills** | `submodules/anthropics-skills` | Foundation skills for webapp testing, PDF processing, and more. |
| **OpenAI Skills** | `submodules/openai-skills` | Curated skills for Notion integration, Figma, and security. |
| **Stared Gemini Skills** | `submodules/stared-gemini-claude-skills` | Native Gemini-optimized consultant and research patterns. |
| **Bkircher Skills** | `submodules/bkircher-skills` | Engineering workflow skills (GH Review, Commit Messages, Jira). |
| **YKDojo Tips** | `submodules/ykdojo-claude-code-tips` | Advanced CLI hacks, prompt patches, and research scripts. |
| **A2A Project** | `submodules/a2aproject-A2A` | The core Agent-to-Agent communication protocol definitions. |
| **TaskSync** | `submodules/4regab-TaskSync` | Cross-agent task synchronization and state protocols. |

## 🧠 Experimental & Research
| Name | Location | Purpose |
| :--- | :--- | :--- |
| **MetaMCP** | `submodules/robertpelloni-metamcp` | Research into MCP proxying and meta-layer discovery. |
| **Dotfiles** | `submodules/dotfiles` | Local configuration and environment tuning for AI agents. |

---
*Last Updated: 2026-03-26*
*Note: All submodules are automatically updated by the `auto_pulse.py` daemon.*
