@echo off
setlocal
cd /d "%~dp0.."
if "%~1"=="" (
  echo Uso: registrar_plantilla.bat DENOMINACION ruta_de_foto
  echo Ejemplo: registrar_plantilla.bat 100 "C:\Fotos\billete100.jpg"
  pause
  exit /b 1
)
if "%~2"=="" (
  echo Debes indicar la ruta de una fotografia.
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  echo Primero ejecuta iniciar.bat para instalar el proyecto.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" "Back\billetes.py" registrar --den %1 --imagen "%~2"
pause
