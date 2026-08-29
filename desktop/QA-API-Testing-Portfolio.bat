@echo off
setlocal
set "ROOT=%~dp0"
if exist "%ROOT%app\index.html" (
  start "QA API Testing Portfolio" "%ROOT%app\index.html"
) else if exist "%ROOT%..\index.html" (
  start "QA API Testing Portfolio" "%ROOT%..\index.html"
) else (
  echo Arquivo index.html nao encontrado.
  pause
  exit /b 1
)
endlocal
