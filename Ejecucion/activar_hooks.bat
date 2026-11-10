@echo off
cd /d "%~dp0.."
git config core.hooksPath Ejecucion/hooks
git config commit.template Ejecucion/.gitmessage
echo Validacion de commits activada (Conventional Commits + tarea). Consulta CONTRIBUTING.md.
pause
