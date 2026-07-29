@echo off
setlocal EnableExtensions

set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

if not defined SOURCE_DIR set "SOURCE_DIR=%USERPROFILE%\KnowledgeHub"
if not defined REMOTE_NAME set "REMOTE_NAME=mymac"
if not defined REMOTE_PATH set "REMOTE_PATH=Knowledge Hub"
if not defined LOG_DIR set "LOG_DIR=%SCRIPT_DIR%\rclone-logs"
if not defined EXCLUDE_FILE set "EXCLUDE_FILE=%SCRIPT_DIR%\rclone-vault-excludes.txt"

set "RUN_MODE=%~1"
if "%RUN_MODE%"=="" set "RUN_MODE=--dry-run"

if not "%RUN_MODE%"=="--dry-run" if not "%RUN_MODE%"=="--run" (
  echo Usage: %~nx0 [--dry-run^|--run]
  echo.
  echo Environment overrides:
  echo   SOURCE_DIR=C:\path\to\local\folder
  echo   REMOTE_NAME=mymac
  echo   REMOTE_PATH=Knowledge Hub
  echo   LOG_DIR=C:\path\to\logs
  echo   EXCLUDE_FILE=C:\path\to\rclone-vault-excludes.txt
  exit /b 2
)

where rclone >nul 2>nul
if errorlevel 1 (
  echo Error: rclone is not installed or not on PATH.
  exit /b 1
)

if not exist "%SOURCE_DIR%\" (
  echo Error: source folder does not exist: %SOURCE_DIR%
  exit /b 1
)

if not exist "%LOG_DIR%\" mkdir "%LOG_DIR%"

for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd-HHmmss"') do set "TIMESTAMP=%%I"
set "LOG_FILE=%LOG_DIR%\rclone-sync-%TIMESTAMP%.log"
set "DESTINATION=%REMOTE_NAME%:%REMOTE_PATH%"

echo Source:      %SOURCE_DIR%
echo Destination: %DESTINATION%
echo Log file:    %LOG_FILE%

set "DRY_RUN_ARG="
if "%RUN_MODE%"=="--dry-run" (
  echo Mode:        dry-run, no files will be changed
  set "DRY_RUN_ARG=--dry-run"
) else (
  echo Mode:        real sync
)

rclone sync "%SOURCE_DIR%" "%DESTINATION%" ^
  --progress ^
  --create-empty-src-dirs ^
  --exclude-from "%EXCLUDE_FILE%" ^
  --log-file "%LOG_FILE%" ^
  --log-level INFO ^
  %DRY_RUN_ARG%

exit /b %ERRORLEVEL%
