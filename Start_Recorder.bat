@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>&1
if %errorlevel%==0 (
  python "%~dp0launch_recorder.py"
  if %errorlevel% neq 0 pause
  goto :end
)

where py >nul 2>&1
if %errorlevel%==0 (
  py -3 "%~dp0launch_recorder.py"
  if %errorlevel% neq 0 pause
  goto :end
)

echo Python 3 was not found in PATH. Please install Python 3 or open index.html directly in Chrome/Edge.
pause

:end
