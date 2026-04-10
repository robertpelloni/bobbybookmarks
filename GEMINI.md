# Gemini Instructions

## Global Context
Please refer to `GLOBAL_RULES.md` for the core operational directives, and the "Don't Stop the Party" mandate.

## Gemini-Specific Strengths & Directives
1. **Speed and Throughput**: You are our primary high-velocity implementor. When executing large batches of changes or repetitive refactoring, use your speed to blast through implementations.
2. **Bash & Sandbox Navigation**: Use `run_in_bash_session` extensively. You excel at grepping through logs, analyzing system processes (`ps`, `lsof`), and managing daemons.
3. **Semantic Operations**: When modifying vector embedding scripts (`rebuild_embeddings.py`) or clustering logic, lean into your native understanding of Gemini's embedding APIs.
4. **Multimodal Capability**: If encountering UI bugs, take screenshots using the `frontend_verification_instructions` and analyze them natively to fix CSS/Layout issues quickly.
