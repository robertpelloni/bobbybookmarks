# GitHub Copilot Instructions

## Global Context
Please refer to `GLOBAL_RULES.md` for the overarching project architecture and rules.

## Copilot-Specific Directives
1. **Autocompletion Context**: When autocompleting within `bobbybookmarks-ui/client`, strictly adhere to the existing React/Vite/Tailwind patterns. Use Lucide-react for icons.
2. **Backend Context**: When completing Node.js Express code, use `sqlite3` and standard CommonJS imports unless modifying a specific module.
3. **Data Fetching**: When writing React hooks, mimic the existing `axios` patterns and state management styles found in `App.jsx`.
4. **Commenting**: Add concise, informative inline comments describing *why* a particular piece of logic exists, referencing `GLOBAL_RULES.md` when relevant.
