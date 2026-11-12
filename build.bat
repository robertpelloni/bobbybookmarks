@echo off
setlocal
title BobbyIntel v1.2.0 - Full System Build
cd /d "%~dp0"

echo.
echo  =======================================================
echo    BOBBYINTEL // FULL SYSTEM BUILD [v1.2.0]
echo  =======================================================
echo.

where node >nul 2>nul
if errorlevel 1 (
    echo [!] Node.js not found on PATH.
    exit /b 1
)
if not exist "node_modules\vite\package.json" (
    echo [*] Installing npm dependencies...
    call npm install
    if errorlevel 1 exit /b 1
)
echo [*] Building Vite frontend bundle into dist/...
node build-render.js
if errorlevel 1 (
    echo [!] Frontend Vite build failed.
    exit /b 1
)

where go >nul 2>nul
if errorlevel 1 (
    echo [!] Go toolchain not found on PATH.
    exit /b 1
)
set CGO_ENABLED=0
echo [*] Building Go backend binaries (backend\bobby-api.exe ^& backend\api.exe)...
go -C backend build -buildvcs=false -o bobby-api.exe ./cmd/api
if errorlevel 1 exit /b 1
go -C backend build -buildvcs=false -o api.exe ./cmd/api
if errorlevel 1 exit /b 1

echo [*] Running Go backend verification suite...
go -C backend test -buildvcs=false ./internal/...
if errorlevel 1 exit /b 1

echo success> "backend\.build_success"
echo [OK] Build v1.2.0 completed successfully.
endlocal
