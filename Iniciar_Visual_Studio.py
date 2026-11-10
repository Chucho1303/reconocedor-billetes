"""Punto de entrada para ejecutar el proyecto desde Visual Studio."""
from pathlib import Path
import subprocess
import sys

if sys.version_info < (3, 12):
    raise SystemExit("Se requiere Python 3.12 o superior (tienes %d.%d). Instala una version nueva y "
                     "selecciona ese interprete en Visual Studio." % sys.version_info[:2])

ROOT = Path(__file__).resolve().parent
APP = ROOT / "Front" / "app.py"

if not APP.exists():
    raise FileNotFoundError(f"No se encontro la interfaz: {APP}")

print("Iniciando el reconocedor de billetes...")
print("Cuando Streamlit arranque, abre la direccion local que aparezca abajo.")
cmd = [sys.executable, "-m", "streamlit", "run", str(APP), "--server.address", "localhost"]
raise SystemExit(subprocess.call(cmd, cwd=str(ROOT)))
