# #8 · Pipeline de CI/CD con GitHub Actions

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `ci` |
| **Alcance** | `ci` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `ci/8-pipeline` |
| **Registrado** | 2026-11-10 (retroactivo) |
| **Trabajo realizado** | 2026-11-09 a 2026-11-10 |

## Descripción

Automatizar la verificación de cada cambio y la publicación de la imagen en `.github/workflows/ci.yml`.

## Criterios de aceptación

- [x] Se ejecuta en `push` a `main`, en Pull Requests hacia `main` y en tags `v*`.
- [x] Job **commits**: valida los mensajes del PR (Conventional Commits + tarea); se omite para Dependabot.
- [x] Job **test**: ejecuta `pytest` con Python 3.12.
- [x] Job **security**: escaneo de secretos, `bandit`, `pip-audit` y política de licencias.
- [x] Job **docker**: depende de `test` y `security`; hace lint con hadolint, construye la imagen y espera a que responda el healthcheck.
- [x] Job **publish**: solo en tags `vX.Y.Z`; publica la imagen en GitHub Container Registry con permisos mínimos.
- [x] Permisos por defecto restringidos a `contents: read`.

## Cómo verificar

Abrir un Pull Request y comprobar en la pestaña **Actions** que los jobs pasan.

## Historial en el repositorio

Fechas tomadas de los commits reales de `main` (`git log`). El ticket se registró después del trabajo.

| Fecha | Commit | Autor | Qué se hizo |
|---|---|---|---|
| 2026-11-09 | `e97dbc6` | Jesus Perez Estrada | ci: agrega pipeline de GitHub Actions y Dependabot (#8) |
| 2026-11-10 | `40730f8` | Jesus Perez Estrada | build(docker): endurece Dockerfile y agrega hadolint al CI (#7) |

## Relacionado

#7 (Docker) · #9 (commits) · #10 (dependencias) · #11 (seguridad) · #12 (pruebas)
