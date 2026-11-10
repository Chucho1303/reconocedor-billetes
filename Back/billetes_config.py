"""Configuracion centralizada del proyecto.

Regla de seguridad: NINGUN valor sensible (contrasenas, llaves de API, tokens,
credenciales de produccion) se escribe en el codigo. Todo se lee desde variables
de entorno o, en desarrollo local, desde un archivo ``Ejecucion/.env`` que NO se sube a Git
(ver ``Ejecucion/.env.example`` y ``.gitignore``).

Este modulo debe importarse ANTES que ``cv2`` para que el limite de pixeles de
OpenCV se aplique.
"""
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent


def _cargar_dotenv(ruta):
    """Lector minimo de .env (KEY=VALUE). Nunca pisa variables ya definidas."""
    try:
        lineas = Path(ruta).read_text(encoding="utf-8").splitlines()
    except OSError:
        return
    for linea in lineas:
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, _, valor = linea.partition("=")
        clave, valor = clave.strip(), valor.strip().strip('"').strip("'")
        if clave:
            os.environ.setdefault(clave, valor)


_cargar_dotenv(ROOT_DIR / "Ejecucion" / ".env")

# Proteccion contra imagenes "bomba" (dimensiones gigantes que agotan la memoria).
MAX_PIXELES = 50_000_000
os.environ.setdefault("OPENCV_IO_MAX_IMAGE_PIXELS", str(MAX_PIXELES))


def _numero(nombre, defecto, minimo, maximo, tipo=float):
    """Lee un numero del entorno; si es invalido o esta fuera de rango usa el defecto."""
    crudo = os.environ.get(nombre)
    if crudo is None or crudo.strip() == "":
        return defecto
    try:
        valor = tipo(crudo)
    except ValueError:
        return defecto
    return valor if minimo <= valor <= maximo else defecto


# --- Ajustes del algoritmo -------------------------------------------------
UMBRAL_ACEPTACION = _numero("BILLETES_UMBRAL", 0.35, 0.0, 1.0)

# --- Rutas -----------------------------------------------------------------
CARPETA_PLANTILLAS = os.environ.get("BILLETES_PLANTILLAS") or str(ROOT_DIR / "Back" / "plantillas")

# --- Limites de la interfaz ------------------------------------------------
MAX_UPLOAD_MB = _numero("BILLETES_MAX_UPLOAD_MB", 10, 1, 200, tipo=int)

# --- Datos del equipo (no son secretos, pero se configuran sin tocar el codigo)
EQUIPO = [n.strip() for n in os.environ.get("BILLETES_EQUIPO", "").split(";") if n.strip()] \
    or ["Integrante 1", "Integrante 2", "Integrante 3"]
GRUPO = os.environ.get("BILLETES_GRUPO", "").strip()
