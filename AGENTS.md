# AGENTS.md: Universal Model & Agent Instructions

## Reference
All operations must follow the [GLOBAL_RULES.md](./GLOBAL_RULES.md).

## Specific Model Instructions
To maximize the strengths of different LLMs working on this codebase, refer to the specific instruction files appended below:
- **[CLAUDE.md](./CLAUDE.md)**: Directives for Claude models (Architecture, Refactoring, Documentation).
- **[GEMINI.md](./GEMINI.md)**: Directives for Gemini models (Velocity, Sandbox Navigation, Vectors).
- **[GPT.md](./GPT.md)**: Directives for GPT models (Code Synthesis, Database Mastery, Robustness).
- **[copilot-instructions.md](./copilot-instructions.md)**: Context for IDE autocomplete integrations.

## Task Protocol
1.  **Analyze**: Deeply research the codebase and conversation history.
2.  **Plan**: Document the strategy in full detail.
3.  **Execute**: Implement, test, and commit autonomously.
4.  **Sync**: Run the Master Sync Pulse via `master_sync.py`.
5.  **Verify**: Run `health_check.py` to ensure the party didn't stop.

## Role-Specific Guidance
- **Research**: Use `deep_research.py` logic. Respect API quotas via model rotation.
- **Unification**: Aggressively deduplicate links to the same GitHub project using `get_project_url`.
- **Documentation**: Update `CHANGELOG.md`, `ROADMAP.md`, `TODO.md` and `MEMORY.md` after every turn.
