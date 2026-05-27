@echo off
REM Usage: run_with_input.bat "path\to\script.py" "path\to\input.txt"
IF "%~1"=="" (
  echo Usage: %~nx0 "path\to\script.py" "path\to\input.txt"
  exit /b 1
)
set "SCRIPT=%~1"
set "INPUT=%~2"
if "%INPUT%"=="" (
  python "%SCRIPT%"
) else (
  type "%INPUT%" | python "%SCRIPT%"
)
