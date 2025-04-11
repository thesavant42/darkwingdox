@echo off
setlocal EnableDelayedExpansion

:: --- Darkwing Dox Build Script ---
:: Creates single .exe using PyInstaller and logs to build_logs

set SPEC_FILE=darkwing_dox.spec
set LOGDIR=build_logs
set LOGFILE=%LOGDIR%\build_%%DATE:~10,4%%-%%DATE:~4,2%%-%%DATE:~7,2%%_%%TIME:~0,2%%-%%TIME:~3,2%%.log

:: Clean up dist/build folders
echo [+] Cleaning old builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if not exist %LOGDIR% mkdir %LOGDIR%

echo [+] Building executable from %SPEC_FILE%
echo Logging to %LOGFILE%
pyinstaller --clean %SPEC_FILE% > "%LOGFILE%" 2>&1

if %ERRORLEVEL% EQU 0 (
    echo [✓] Build complete! Executable in /dist
) else (
    echo [!] Build failed. Check log: %LOGFILE%
)

pause
