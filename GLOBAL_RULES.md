# GLOBAL_RULES.md: Universal Instructions

## Core Directives
1.  **Don't Stop the Party**: Never terminate active background processes (workers, servers, daemons) unless absolutely necessary for an essential update. Autonomous operation is the priority.
2.  **Data Integrity First**: Use centralized deduplication (`deduplicator.py`) and unification logic for all data operations. Avoid redundant links; aim for project-level consolidation.
3.  **Borg Taxonomy**: Categorize all technical intelligence using the established Borg taxonomy (Orchestration, Context, Memory, Interface, Interoperability, Infrastructure).
4.  **Full Transparency**: Every major change must be documented in `CHANGELOG.md`. Keep `ROADMAP.md` and `TODO.md` updated after every significant feature implementation.
5.  **Version Synchronicity**: The version number in `VERSION.md` is the source of truth. Bumping the version requires a commit with the new version referenced in the message.

## LLM Interaction Standards
- **Exhaustive Detail**: Document all input information, findings, and architectural decisions in full extreme detail.
- **Autonomous Execution**: Proceed with implementation, testing, and pushing changes without waiting for confirmation once a clear path is identified.
- **Deep Research**: Utilize all available tools (subagents, web search, codebase investigator) for deep technical grounding before proposing changes.
- **Universal Reference**: All specialized instruction files (`AGENTS.md`, `GEMINI.md`, etc.) must reference these global rules.

## Maintenance Protocols
- **Build Pulse**: Run `master_sync.py` or ensure the `auto_pulse.py` daemon is active to keep submodules and databases synced.
- **Health Verification**: Use `health_check.py` to monitor the system state and auto-restart services if needed.
- **Memory Management**: Update `MEMORY.md` with new observations about codebase patterns or user preferences.
