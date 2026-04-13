@echo off
SETLOCAL EnableDelayedExpansion

echo [1/4] Checking Python environment...
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo [2/4] Installing/Updating Python dependencies...
call venv\Scripts\activate
pip install -r requirements.txt

echo [3/4] Installing/Updating Frontend dependencies...
cd bobbybookmarks-ui\client
if not exist node_modules (
    echo Installing npm packages...
    call npm install
)
cd ..\..

echo [4/4] Starting services...

:: Start Backend in a new window
start "BobbyBookmarks Backend" cmd /k "call venv\Scripts\activate && python app.py"

:: Start Frontend in a new window
echo Starting Frontend...
cd bobbybookmarks-ui\client
start "BobbyBookmarks Frontend" cmd /k "npm run dev"

echo.
echo ===================================================
echo Services are starting!
echo Backend: http://127.0.0.1:5000
echo Frontend: http://localhost:5173 (usually)
echo ===================================================
pause
