@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "GENERATOR=%~dp0src\license_generator.py"
set "BUNDLED_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

where python >nul 2>nul
if %errorlevel% equ 0 (
    python "%GENERATOR%" %*
    exit /b !errorlevel!
)

where py >nul 2>nul
if %errorlevel% equ 0 (
    py -3 "%GENERATOR%" %*
    exit /b !errorlevel!
)

if exist "%BUNDLED_PYTHON%" (
    "%BUNDLED_PYTHON%" "%GENERATOR%" %*
    exit /b !errorlevel!
)

echo Python 3.11 or later was not found. Install Python or provide it on PATH. 1>&2
exit /b 2
