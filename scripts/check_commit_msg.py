#!/usr/bin/env python3
"""Valida mensajes de commit: Conventional Commits + referencia a una tarea.

Formato:   tipo(alcance opcional): descripcion en imperativo   ...  (#12)

Tipos: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert
Trazabilidad: el mensaje debe incluir un identificador de tarea (#N de GitHub
Issues, o CLAVE-N de Jira/Trello), p. ej. "(#12)", "Refs #12" o "Closes #12".

Uso:
  check_commit_msg.py ARCHIVO         # hook commit-msg de Git
  check_commit_msg.py --range A..B    # valida todos los commits de un rango (CI)
"""
import re
import subprocess
import sys

TIPOS = "feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert"
ENCABEZADO = re.compile(r"^(%s)(\([a-z0-9._-]+\))?!?: \S.{0,70}$" % TIPOS)
TAREA = re.compile(r"(#\d+|\b[A-Z][A-Z0-9]+-\d+\b)")
EXENTOS = re.compile(r"^(Merge |Revert \"|fixup! |squash! )")


def validar(mensaje):
    """Devuelve una lista de errores (vacia si el mensaje es correcto)."""
    lineas = [l for l in mensaje.splitlines() if not l.startswith("#") or TAREA.match(l)]
    texto = "\n".join(lineas).strip()
    if not texto:
        return ["El mensaje esta vacio."]
    if EXENTOS.match(texto):
        return []
    errores = []
    primera = texto.splitlines()[0]
    if not ENCABEZADO.match(primera):
        errores.append("Encabezado invalido: %r. Usa 'tipo(alcance): descripcion' (max. 72 caracteres). "
                       "Tipos: %s" % (primera, TIPOS.replace("|", ", ")))
    if not TAREA.search(texto):
        errores.append("Falta la referencia a la tarea (ej. '(#12)', 'Refs #12' o 'Closes #12').")
    segunda = texto.splitlines()[1:2]
    if segunda and segunda[0].strip():
        errores.append("Deja una linea en blanco entre el encabezado y el cuerpo.")
    return errores


def main(argv):
    if len(argv) == 3 and argv[1] == "--range":
        hashes = subprocess.run(["git", "log", "--format=%H", "--no-merges", argv[2]],
                                capture_output=True, text=True, check=True).stdout.split()
        mensajes = [(h[:8], subprocess.run(["git", "log", "-1", "--format=%B", h],
                                           capture_output=True, text=True, check=True).stdout) for h in hashes]
    elif len(argv) == 2:
        with open(argv[1], encoding="utf-8") as fh:
            mensajes = [("commit", fh.read())]
    else:
        print(__doc__)
        return 2

    malos = 0
    for ident, msg in mensajes:
        for e in validar(msg):
            malos += 1
            print("[%s] %s" % (ident, e))
    if malos:
        print("\nCommit rechazado. Consulta CONTRIBUTING.md.")
        return 1
    print("OK: %d mensaje(s) de commit validos." % len(mensajes))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
