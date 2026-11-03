@echo off
setlocal
cd /d "%~dp0.."
set "ROOT=%CD%"
if not exist ".venv\Scripts\python.exe" (
    echo Creando entorno virtual...
    py -3 -m venv .venv
    if errorlevel 1 python -m venv .venv
)
call ".venv\Scripts\activate.bat"
echo.
echo Instalando o verificando dependencias...
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: No se pudieron instalar las dependencias.
    pause
    exit /b 1
)
echo.
echo Abriendo el reconocedor en el navegador...
python -m streamlit run "Front\app.py"
pause
