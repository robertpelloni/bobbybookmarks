# AGENTS.md: Model Instructions

## Reference
All operations must follow the [GLOBAL_RULES.md](./GLOBAL_RULES.md).

## Task Protocol
1.  **Analyze**: Deeply research the codebase and conversation history.
2.  **Plan**: Document the strategy in full detail.
3.  **Execute**: Implement, test, and commit autonomously.
4.  **Sync**: Run the Master Sync Pulse via `master_sync.py`.
5.  **Verify**: Run `health_check.py` to ensure the party didn't stop.

## Role-Specific Guidance
- **Research**: Use `deep_research.py` logic. Respect API quotas via model rotation.
- **Unification**: Aggressively deduplicate links to the same GitHub project using `get_project_url`.
- **Documentation**: Update `CHANGELOG.md` and `MEMORY.md` after every turn.
