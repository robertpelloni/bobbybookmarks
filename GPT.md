# GPT Instructions

## Global Context
Please refer to `GLOBAL_RULES.md` for the core operational directives, and the "Don't Stop the Party" mandate.

## GPT-Specific Strengths & Directives
1. **Code Synthesis**: You are highly trusted for writing complex from-scratch scripts and novel algorithms.
2. **Database Mastery**: When interacting with `bookmarks.db` or writing new SQLite queries (e.g., in `server.js` or `auto_process.py`), pay special attention to schema consistency and index performance.
3. **Robustness**: When writing Python code, always include try/except blocks and graceful fallbacks for API quota limits or missing files.
4. **Iterative Planning**: Heavily utilize the `set_plan` and `request_plan_review` tools to ensure your complex executions remain perfectly aligned with user expectations.
