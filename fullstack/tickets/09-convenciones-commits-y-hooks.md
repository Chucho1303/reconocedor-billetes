# #9 · Convenciones de commits y hooks de Git

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `chore` |
| **Alcance** | `repo` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `chore/9-convenciones-commits` |
| **Registrado** | 2026-11-10 (retroactivo) |
| **Trabajo realizado** | 2026-11-09 a 2026-11-10 |

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

## Historial en el repositorio

Fechas tomadas de los commits reales de `main` (`git log`). El ticket se registró después del trabajo.

| Fecha | Commit | Autor | Qué se hizo |
|---|---|---|---|
| 2026-11-09 | `61cbeb7` | Jesus Perez Estrada | chore(repo): agrega validador de commits y hook de Git (#9) |
| 2026-11-10 | `3cf636c` | Jesus Perez Estrada | chore(repo): agrega .gitattributes, hook portable y plantilla de PR (#9) |

## Relacionado

#8 (CI)
