@echo off
setlocal
title BobbyIntel v1.2.0 - Unified Runner
cd /d "%~dp0"

echo.
echo  =======================================================
echo    BOBBYINTEL // BORG INTELLIGENCE HARVESTER [v1.2.0]
echo  =======================================================
echo.

set CGO_ENABLED=0
if "%PORT%"=="" set PORT=5000

if /I "%~1"=="--dev" (
    echo [*] Launching Go API Backend on http://localhost:%PORT% ...
    start "BobbyIntel-API" cmd /c "cd /d "%~dp0" && set CGO_ENABLED=0&& set PORT=%PORT%&& go -C backend run -buildvcs=false ./cmd/api"
    echo [*] Launching Vite Frontend Dev Server on http://localhost:3000 ...
    npm run dev
    goto :end
)

if not exist "backend\bobby-api.exe" (
    where go >nul 2>nul
    if errorlevel 1 (
        echo [!] backend\bobby-api.exe not found and Go is not installed.
        pause
        exit /b 1
    )
    echo [*] Building backend\bobby-api.exe ...
    go -C backend build -buildvcs=false -o bobby-api.exe ./cmd/api
    if errorlevel 1 (
        echo [!] Go backend build failed.
        pause
        exit /b 1
    )
)

echo [*] Starting Unified BobbyIntel Server on http://localhost:%PORT%
echo [*] Capability Atlas available at http://localhost:%PORT%/atlas.html
"backend\bobby-api.exe"

:end
endlocal
