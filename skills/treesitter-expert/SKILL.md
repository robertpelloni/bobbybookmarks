# TreeSitter Plugin Architecture Expert

Expert in building high-performance Neovim plugins using nvim-treesitter. Specializes in module systems, query-based parsing, virtual text manipulation, and performance optimization patterns.

## Instructions

When the user asks to "build a Neovim plugin", "implement TreeSitter integration", "create virtual text annotations", or "optimize Neovim plugin performance", follow these architectural patterns:

### 1. Module System Architecture
Use a three-tier structure:
- `plugin/`: Minimal entry point with VimL commands.
- `lua/your-plugin/`: Core logic (init, config, highlight, query).
- `queries/`: TreeSitter `.scm` definitions.

### 2. Configuration Management
- Use the **Deep Merge Pattern** for user options.
- Implement **Deferred Initialization** using `vim.api.nvim_get_vvar("vim_did_enter")` to ensure fast startup.

### 3. TreeSitter Query System
- Define queries in `queries/<lang>/<name>.scm`.
- Use `vim.treesitter.query.iter_captures` for efficient node traversal.
- Implement **Viewport-Limited Query Execution** to only process visible lines.

### 4. Virtual Text Display
- Use `vim.api.nvim_buf_set_extmark` for non-invasive annotations.
- Prefer `virt_text_pos = 'eol'` for summaries and `'overlay'` for code transformations.

### 5. Performance Optimization
- **Memoization**: Cache query results indexed by `vim.api.nvim_buf_get_changedtick`.
- **Throttling**: Use `vim.uv.new_timer()` to debounce updates on text changes.
- **Incremental State Tracking**: Only re-evaluate lines invalidated by `on_lines` buffer attachment events.

## Common Code Patterns

### Buffer Attachment with Auto-Cleanup
```lua
vim.api.nvim_buf_attach(bufnr, false, {
  on_lines = function(_, _, _, first, _, last_new)
    M.invalidate_range(bufnr, first, last_new)
  end,
  on_detach = function()
    M.state[bufnr] = nil
    return true
  end,
})
```

### Memoization by Buffer Tick
```lua
function M.memoize_by_buf_tick(fn)
  local cache = setmetatable({}, { __mode = "kv" })
  return function(bufnr)
    local tick = vim.api.nvim_buf_get_changedtick(bufnr)
    if cache[bufnr] and cache[bufnr].tick == tick then
      return cache[bufnr].result
    end
    local result = fn(bufnr)
    cache[bufnr] = { result = result, tick = tick }
    return result
  end
end
```
