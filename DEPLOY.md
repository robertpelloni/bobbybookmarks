# DEPLOY.md: Deployment Guide

## Local Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+ & npm
- Git

### 1. Repository Initialization
```bash
git clone https://github.com/robertpelloni/bobbybookmarks.git
cd bobbybookmarks
git submodule update --init --recursive
```

### 2. Backend Setup (Python)
```bash
pip install -r requirements.txt
# No database initialization needed (uses bookmarks.db in root)
```

### 3. UI Stack Setup (Node.js)
```bash
# API Layer
cd bobbybookmarks-ui/server
npm install

# Frontend Layer
cd ../client
npm install
```

### 4. Configuration
Create a `.env` file in the root (optional, defaults are in `config.py`):
```env
GEMINI_API_KEY=your_key_here
LLM_BACKEND=gemini
```

### 5. Running the Stack
The system is designed to run multiple background components:
- **Research Worker**: `python deep_research.py`
- **Flask API**: `python app.py`
- **Express API**: `cd bobbybookmarks-ui/server && node server.js`
- **React Frontend**: `cd bobbybookmarks-ui/client && npm run dev`
- **Automation**: `python auto_pulse.py`

## Production Deployment (Recommended)

### Docker (Coming Soon)
We are moving towards a unified `docker-compose.yml` to orchestrate all five services.

### Manual Cloud Hosting
1.  **Database**: Host `bookmarks.db` on persistent storage or migrate to a managed SQLite provider (e.g., Turso).
2.  **Workers**: Run `deep_research.py` and `auto_pulse.py` as managed background services (e.g., using `pm2` or systemd).
3.  **UI**: Deploy the Vite frontend to a static host (Vercel, Netlify) and the Node/Python APIs to a container runner (Render, Railway, Fly.io).
