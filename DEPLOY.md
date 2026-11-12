# Deployment & Build Instructions (`v1.2.0`)

## Full System Build (Windows)
Run `build.bat` from the repository root to compile both the React 19 / TypeScript Dual-HUD frontend (`dist/`) and the pure-Go unified backend (`backend/bobby-api.exe` & `backend/api.exe`), then run Go backend tests:
```bat
build.bat
```

## Starting the Unified Server
Run `start.bat` from the repository root to launch `backend\bobby-api.exe` on `http://localhost:5000` (serves `/api/*`, the compiled Dual-HUD SPA from `dist/`, and `/atlas.html`):
```bat
start.bat
```
For hot-reloading frontend development (`http://localhost:3000` proxying `/api` to `:5000`):
```bat
start.bat --dev
```

## Manual Component Commands
### Frontend (React 19 + Vite + Tailwind v4)
```bash
npm install
npm run build   # executes node build-render.js -> dist/
```

### Go Unified Backend (`CGO_ENABLED=0`)
```bash
cd backend
CGO_ENABLED=0 go build -buildvcs=false -o bobby-api.exe ./cmd/api
CGO_ENABLED=0 go test -buildvcs=false ./internal/...
```

### Python Borg Ingestion & Exports
```bash
python deep_research.py                      # LLM enrichment worker
python _gen_atlas_v8.py                      # Regenerate atlas.html, atlas.json, and layer .md docs
python scripts/generate_public_registry.py   # Export exports/public_registry.html from bookmarks.db
python scripts/rebuild_prompts.py            # Rebuild data/prompt_library.db
```

### Static Landing Pages
Commits under `landing/**` on `main` trigger Cloudflare Pages deployment (`tormentnexus.site` and `hypernexus.site`) via `.github/workflows/deploy-landing.yml`.
