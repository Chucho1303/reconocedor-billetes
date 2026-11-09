@echo off
setlocal
cd /d "%~dp0.."
if not exist ".venv\Scripts\python.exe" (
    echo Primero ejecuta iniciar.bat para crear el entorno.
    pause
    exit /b 1
)
call ".venv\Scripts\activate.bat"
pip install -r requirements-dev.txt || goto :error
python -m pytest || goto :error
python scripts\scan_secrets.py || goto :error
bandit -q -c bandit.yaml -r Back Front Iniciar_Visual_Studio.py scripts || goto :error
python scripts\check_licenses.py || goto :error
pip-audit -r requirements.lock.txt || goto :error
echo.
echo TODAS LAS VERIFICACIONES PASARON.
pause
exit /b 0
:error
echo.
echo FALLO una verificacion. Revisa el mensaje de arriba.
pause
exit /b 1
