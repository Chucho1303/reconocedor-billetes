#!/usr/bin/env python3
"""Audita las licencias de las dependencias INSTALADAS contra la politica del proyecto.

Politica (docs/DEPENDENCIAS_Y_LICENCIAS.md):
  - Permitidas: MIT, BSD, Apache-2.0, PSF, ISC, Zlib, 0BSD, CC0, MIT-CMU.
  - Permitidas con aviso: MPL-2.0 (copyleft debil por archivo; solo uso sin modificar).
  - Prohibidas: GPL, AGPL, LGPL, SSPL, "Proprietary" / "Commercial" (incompatibles con una
    distribucion comercial sin revision legal).
Uso:  python scripts/check_licenses.py [--markdown salida.md]
"""
import json
import re
import subprocess
import sys

PROHIBIDAS = re.compile(r"(?i)\b(A?GPL|LGPL|GNU (Affero|Lesser|General)|SSPL|proprietary|commercial)\b")
AVISO = re.compile(r"(?i)(MPL|Mozilla Public)")


def main(argv):
    crudo = subprocess.run([sys.executable, "-m", "piplicenses", "--format=json", "--with-urls"],
                           capture_output=True, text=True, check=True).stdout
    paquetes = json.loads(crudo)
    errores, avisos = [], []
    filas = []
    for p in sorted(paquetes, key=lambda x: x["Name"].lower()):
        lic = p["License"]
        if PROHIBIDAS.search(lic) or lic.strip().upper() in ("UNKNOWN", ""):
            errores.append("%s %s: %s" % (p["Name"], p["Version"], lic))
        elif AVISO.search(lic):
            avisos.append("%s %s: %s" % (p["Name"], p["Version"], lic))
        filas.append((p["Name"], p["Version"], lic, p["URL"]))

    if "--markdown" in argv:
        destino = argv[argv.index("--markdown") + 1]
        with open(destino, "w", encoding="utf-8") as fh:
            fh.write("| Paquete | Version | Licencia | Sitio |\n|---|---|---|---|\n")
            for n, v, l, u in filas:
                fh.write("| %s | %s | %s | %s |\n" % (n, v, l.replace("|", "/"), u))

    print("%d paquetes revisados." % len(filas))
    for a in avisos:
        print("AVISO (copyleft debil, uso sin modificar): " + a)
    for e in errores:
        print("ERROR licencia no permitida: " + e)
    if errores:
        return 1
    print("OK: todas las licencias son compatibles con la politica comercial.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
