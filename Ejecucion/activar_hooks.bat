@echo off
cd /d "%~dp0.."
git config core.hooksPath .githooks
git config commit.template .gitmessage
echo Validacion de commits activada (Conventional Commits + tarea). Consulta CONTRIBUTING.md.
pause
