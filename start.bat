@echo off
SETLOCAL EnableDelayedExpansion

echo ===================================================
echo   BOBBYBOOKMARKS REWRITE STARTUP (GO + TS)
echo ===================================================

echo [1/3] Checking Go Backend...
if not exist "backend\go.mod" (
    echo [ERROR] Go backend directory not found.
    pause
    exit /b
)
cd backend
echo Building Go API...
go build -o bobby-api.exe ./cmd/api/main.go
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Go build failed.
    pause
    exit /b
)
cd ..

echo [2/3] Checking TypeScript Frontend...
if not exist "bobbybookmarks-ui-ts\package.json" (
    echo [ERROR] TS frontend directory not found.
    pause
    exit /b
)
cd bobbybookmarks-ui-ts
if not exist node_modules (
    echo [INFO] Installing npm packages (using mirror for speed)...
    call npm config set registry https://registry.npmmirror.com
    call npm install
)
cd ..

echo [3/3] Launching Services...

:: Start Go Backend in a new window
echo Starting Go API on port 5000...
start "BobbyBookmarks (Go API)" cmd /k "cd backend && bobby-api.exe"

:: Start Vite Frontend in a new window
echo Starting Vite TS Frontend on port 3000...
cd bobbybookmarks-ui-ts
start "BobbyBookmarks (TS Frontend)" cmd /k "npm run dev"

echo.
echo ===================================================
echo   SERVICES ARE DEPLOYED LOCALLY!
echo ===================================================
echo   API Server:  http://localhost:5000/api
echo   UI Frontend: http://localhost:3000
echo ===================================================
pause
