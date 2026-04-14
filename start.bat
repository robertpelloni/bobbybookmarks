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

:: Check for GCC (Required for CGO/SQLite on Windows)
where gcc >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] GCC ^(C Compiler^) was not found. 
    echo [!] To run the backend locally, you need a C compiler for SQLite.
    echo [!] Download: https://github.com/skeeto/w64devkit/releases
    echo [!] Then add the 'bin' folder to your PATH.
    pause
    exit /b
)

:: Ensure backend binary is built or run directly
echo [*] Initializing BobbyIntel Unified Core...
echo [*] Target: http://localhost:10000
echo.

:: Start the unified service
:: Since we are running locally, we need CGO for SQLite
:: If you have GCC issues, you may need a clean TDM-GCC or w64devkit
set CGO_ENABLED=1

:: OPTIONAL: If the build fails with a 'cannot parse gcc output' error, 
:: it means your GCC version is incompatible with your Go architecture.
:: You can try: set GGO_ENABLED=0 (though SQLite might fail to open)

echo [*] Starting Backend Service...
start /b cmd /c "cd backend && go run -ldflags="-s -w" cmd/api/main.go"

echo [*] Starting Frontend Development Server...
:: We use 'npm run dev' for local hot-reloading
npm run dev

echo.
echo [!] Servers are shutting down...
pause
