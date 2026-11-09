#!/bin/sh
# Crea en GitHub los issues de docs/BACKLOG.md en orden (#1..#13). Requiere "gh auth login".
# Ejecutar UNA vez en un repositorio nuevo (sin issues) para que la numeracion coincida.
set -e
grep -E '^\| [0-9]+ \|' "$(dirname "$0")/../docs/BACKLOG.md" | while IFS='|' read -r _ n titulo estado _; do
  titulo=$(echo "$titulo" | sed 's/^ *//;s/ *$//')
  gh issue create --title "$titulo" --body "Tarea #$(echo $n | tr -d ' ') del backlog (docs/BACKLOG.md)."
done
