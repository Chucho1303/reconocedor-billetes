# #9 · Convenciones de commits y hooks de Git

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `chore` |
| **Alcance** | `repo` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `chore/9-convenciones-commits` |

## Descripción

Garantizar trazabilidad: cada commit sigue Conventional Commits y referencia una tarea (`#N`).

## Criterios de aceptación

- [x] `Ejecucion/scripts/check_commit_msg.py` valida encabezado `tipo(alcance): descripción` (máx. 72 caracteres) y la referencia a tarea.
- [x] Tipos permitidos: `feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert`.
- [x] El hook `Ejecucion/hooks/commit-msg` rechaza mensajes inválidos en local; se activa con `activar_hooks.bat` o `git config core.hooksPath Ejecucion/hooks`.
- [x] `Ejecucion/.gitmessage` ofrece plantilla de mensaje.
- [x] El mismo validador corre en el CI sobre todos los commits de un PR (`--range`).
- [x] `.github/CONTRIBUTING.md` y `.github/pull_request_template.md` documentan el flujo.
- [x] Existen pruebas en `Ejecucion/tests/test_commit_msg.py`.

## Cómo verificar

```bash
python Ejecucion/scripts/check_commit_msg.py --range origin/main..HEAD
python -m pytest -c Ejecucion/pytest.ini Ejecucion/tests/test_commit_msg.py
```

## Relacionado

#8 (CI)
