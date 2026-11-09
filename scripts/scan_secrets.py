#!/usr/bin/env python3
"""Busca credenciales escritas directamente en el codigo (hardcoded).

Revisa los archivos versionados por Git (o todos los de la carpeta si no hay Git)
y falla con codigo 1 si encuentra contrasenas, llaves de API, tokens o llaves
privadas. Uso:  python scripts/scan_secrets.py [carpeta]
"""
import re
import subprocess
import sys
from pathlib import Path

PATRONES = {
    "Llave privada": re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[0-9A-Za-z]{36,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b"),
    "Anthropic/OpenAI key": re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}\b"),
    "Credencial asignada en codigo": re.compile(
        r"""(?ix)[\w.-]*(?:password|passwd|pwd|contrasena|secret|api[_-]?key|apikey|token|access[_-]?key)\w*\s*[:=]\s*
        (?P<q>["'])(?P<v>[^"'\s]{6,})(?P=q)"""),
    "URL con usuario:clave": re.compile(r"[a-z][a-z0-9+.\-]*://[^/\s:@]+:[^/\s:@]+@[^/\s]+", re.I),
}
FALSOS_POSITIVOS = re.compile(r"(?i)(changeme|example|ejemplo|placeholder|your[_-]|tu[_-]|<.*>|\$\{|xxx|\*\*\*|os\.environ|getenv)")
BINARIOS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".gif", ".ico", ".zip", ".pyc", ".sln"}
IGNORAR = {"scan_secrets.py", "test_scan_secrets.py"}   # contienen los patrones de busqueda


def archivos(raiz):
    try:
        salida = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=raiz,
                                capture_output=True, text=True, check=True).stdout.split("\n")
        return [raiz / f for f in salida if f]
    except (OSError, subprocess.CalledProcessError):
        return [p for p in raiz.rglob("*") if p.is_file() and ".git" not in p.parts]


def escanear(raiz):
    hallazgos = []
    for ruta in archivos(raiz):
        if ruta.suffix.lower() in BINARIOS or ruta.name in IGNORAR or not ruta.is_file():
            continue
        try:
            texto = ruta.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for n, linea in enumerate(texto.splitlines(), 1):
            if FALSOS_POSITIVOS.search(linea):
                continue
            for nombre, patron in PATRONES.items():
                if patron.search(linea):
                    hallazgos.append((str(ruta.relative_to(raiz)), n, nombre))
    return hallazgos


def main():
    raiz = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    hallazgos = escanear(raiz)
    for archivo, n, nombre in hallazgos:
        print("%s:%d  posible secreto -> %s" % (archivo, n, nombre))
    if hallazgos:
        print("\n%d hallazgo(s). Mueve los secretos a variables de entorno (.env / secretos del servidor)." % len(hallazgos))
        return 1
    print("OK: no se encontraron secretos escritos en el codigo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
