@echo off
setlocal

echo.
echo  #######################################################
echo  #                                                     #
echo  #     BOBBYINTEL // KINETIC HUD [LOCAL RUNNER]        #
echo  #                                                     #
echo  #######################################################
echo.

:: Check for Go
where go >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Go is not installed. Please install Go to run the backend.
    pause
    exit /b
)

:: Check for Node
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Node.js is not installed. Please install Node to run the frontend.
    pause
    exit /b
)

:: Ensure backend binary is built or run directly
echo [*] Initializing BobbyIntel Unified Core...
echo [*] Target: http://localhost:5000
echo.

:: Start the unified service
:: CGO is NO LONGER REQUIRED due to modernc.org/sqlite migration
set CGO_ENABLED=0

echo [*] Starting Backend Service...
start /b cmd /c "cd backend && set PORT=5000 && go run cmd/api/main.go"

echo [*] Starting Frontend Development Server...
:: We use 'npm run dev' for local hot-reloading
npm run dev

echo.
echo [!] Servers are shutting down...
pause
