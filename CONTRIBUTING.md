# Guía de contribución

## Flujo de trabajo

1. Toda tarea nace como **issue** (GitHub Issues / Jira / Trello) y tiene un número o clave.
2. Crea una rama: `feat/12-descripcion-corta`, `fix/15-umbral`, `docs/20-readme`.
3. Haz commits pequeños con **Conventional Commits** y la referencia a la tarea.
4. Abre un Pull Request hacia `main`; el CI debe pasar (pruebas, seguridad, licencias, Docker).

## Formato del mensaje de commit

```
tipo(alcance): descripción en imperativo, máx. 72 caracteres (#N)

Cuerpo opcional: qué cambia y por qué.

Closes #N
```

| Tipo | Úsalo para |
|---|---|
| `feat` | funcionalidad nueva |
| `fix` | corrección de errores |
| `docs` | documentación |
| `refactor` / `perf` | cambios internos / rendimiento |
| `test` | pruebas |
| `build` / `ci` | dependencias, Docker, pipelines |
| `chore` / `style` / `revert` | mantenimiento, formato, reversiones |

Alcances sugeridos: `back`, `front`, `docker`, `ci`, `deps`, `security`, `repo`.

Ejemplos válidos:

```
feat(back): agrega votación por fotogramas en modo cámara (#5)
fix(front): muestra error si la imagen subida está dañada (#11)
build(deps): fija versiones exactas de dependencias (#10)
```

## Activar las validaciones locales (una vez por clon)

```bash
git config core.hooksPath .githooks     # rechaza commits que incumplan el formato
git config commit.template .gitmessage  # plantilla de mensaje
```

El mismo validador corre en el CI sobre todos los commits de cada Pull Request:
`python scripts/check_commit_msg.py --range origin/main..HEAD`.

## Antes de abrir un PR

```bash
pip install -r requirements-dev.txt
python -m pytest
python scripts/scan_secrets.py
bandit -q -c bandit.yaml -r Back Front Iniciar_Visual_Studio.py scripts
python scripts/check_licenses.py
```
(En Windows: `Ejecucion\verificar.bat` ejecuta todo.)

## Reglas de oro

- Nunca subas `.env`, llaves ni contraseñas (ver `docs/SEGURIDAD.md`).
- Una funcionalidad que no está en el backlog no entra al repositorio (evitar *scope creep*).
