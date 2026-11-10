@echo off
setlocal
cd /d "%~dp0.."
if not exist ".venv\Scripts\python.exe" (
    echo Primero ejecuta iniciar.bat para crear el entorno.
    pause
    exit /b 1
)
call ".venv\Scripts\activate.bat"
pip install -r Ejecucion\requirements-dev.txt || goto :error
python -m pytest -c Ejecucion\pytest.ini || goto :error
python Ejecucion\scripts\scan_secrets.py || goto :error
bandit -q -c Ejecucion\bandit.yaml -r Back Front Ejecucion\scripts Ejecucion\Iniciar_Visual_Studio.py || goto :error
python Ejecucion\scripts\check_licenses.py || goto :error
pip-audit -r Ejecucion\requirements.lock.txt || goto :error
echo.
echo TODAS LAS VERIFICACIONES PASARON.
pause
exit /b 0
:error
echo.
echo FALLO una verificacion. Revisa el mensaje de arriba.
pause
exit /b 1
