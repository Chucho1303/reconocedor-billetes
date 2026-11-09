"""Punto de entrada para ejecutar el proyecto desde Visual Studio."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
APP = ROOT / "Front" / "app.py"

if not APP.exists():
    raise FileNotFoundError(f"No se encontro la interfaz: {APP}")

print("Iniciando el reconocedor de billetes...")
print("Cuando Streamlit arranque, abre la direccion local que aparezca abajo.")
cmd = [sys.executable, "-m", "streamlit", "run", str(APP), "--server.address", "localhost"]
raise SystemExit(subprocess.call(cmd, cwd=str(ROOT)))
