# Tickets del proyecto

Un archivo por tarea del [backlog](../BACKLOG.md). El número del ticket es el `#N` que se usa en los commits
(`feat(back): agrega ... (#5)`), según `.github/CONTRIBUTING.md`.

| # | Ticket | Tipo | Alcance | Estado |
|---|---|---|---|---|
| 1 | [Estructura inicial y solución de Visual Studio](01-estructura-inicial.md) | `chore` | `repo` | Hecho |
| 2 | [Motor de reconocimiento](02-motor-reconocimiento.md) | `feat` | `back` | Hecho |
| 3 | [Plantillas de $20, $50 y $1,000](03-plantillas-20-50-1000.md) | `feat` | `back` | Hecho |
| 4 | [Interfaz web con Streamlit](04-interfaz-streamlit.md) | `feat` | `front` | Hecho |
| 5 | [Modos de línea de comandos](05-modos-linea-de-comandos.md) | `feat` | `back` | Hecho |
| 6 | [Lanzadores de Windows y README](06-lanzadores-windows-y-readme.md) | `docs` | `repo` | Hecho |
| 7 | [Despliegue con Docker](07-despliegue-docker.md) | `build` | `docker` | Hecho |
| 8 | [Pipeline de CI/CD](08-pipeline-ci-cd.md) | `ci` | `ci` | Hecho |
| 9 | [Convenciones de commits y hooks](09-convenciones-commits-y-hooks.md) | `chore` | `repo` | Hecho |
| 10 | [Dependencias, auditoría y licencias](10-dependencias-y-licencias.md) | `build` | `deps` | Hecho |
| 11 | [Seguridad y escaneo de secretos](11-seguridad-y-secretos.md) | `feat` | `security` | Hecho |
| 12 | [Pruebas con datos reales](12-pruebas-con-datos-reales.md) | `test` | `back` | Hecho |
| 13 | [Plantillas de $100, $200 y $500](13-plantillas-100-200-500.md) | `feat` | `back` | Pendiente |
| 14 | [Lectura en voz alta del resultado](14-lectura-en-voz-alta.md) | `feat` | `front` | Hecho |

## Plantilla para tickets nuevos

```markdown
# #N · Título corto

| Campo | Valor |
|---|---|
| **Estado** | Pendiente / En curso / Hecho |
| **Tipo** | feat / fix / docs / test / build / ci / chore |
| **Alcance** | back / front / docker / ci / deps / security / repo |
| **Responsable** | nombre |
| **Rama sugerida** | tipo/N-descripcion |

## Descripción
## Criterios de aceptación
- [ ] ...
## Cómo verificar
## Relacionado
```

Al crear un ticket nuevo, agrégalo también a la tabla de `Ejecucion/docs/BACKLOG.md`.
