# Tickets del proyecto

Un archivo por tarea del [backlog](../../Ejecucion/docs/BACKLOG.md). El número del ticket es el `#N` que se usa en los commits
(`feat(back): agrega ... (#5)`), según `.github/CONTRIBUTING.md`.

> **Registro retroactivo:** estos tickets se redactaron el 2026-11-10 a partir del trabajo ya realizado. Las fechas de «Trabajo realizado» son las de los commits reales del repositorio (el historial empieza el 2026-10-19).
>
> Los tickets 15 a 30 se registraron el 2026-11-16 como trabajo pendiente o en curso, a partir de lo encontrado al revisar el repositorio; no tienen «Trabajo realizado» hasta que se hagan.

| # | Ticket | Tipo | Alcance | Estado | Trabajo realizado |
|---|---|---|---|---|---|
| 1 | [Estructura inicial y solución de Visual Studio](01-estructura-inicial.md) | `chore` | `repo` | Hecho | 2026-11-03 a 2026-11-10 |
| 2 | [Motor de reconocimiento](02-motor-reconocimiento.md) | `feat` | `back` | Hecho | 2026-10-19 a 2026-11-09 |
| 3 | [Plantillas de $20, $50 y $1,000](03-plantillas-20-50-1000.md) | `feat` | `back` | Hecho | 2026-10-19 a 2026-11-09 |
| 4 | [Interfaz web con Streamlit](04-interfaz-streamlit.md) | `feat` | `front` | Hecho | 2026-10-19 a 2026-11-09 |
| 5 | [Modos de línea de comandos](05-modos-linea-de-comandos.md) | `feat` | `back` | Hecho | 2026-11-09 |
| 6 | [Lanzadores de Windows y README](06-lanzadores-windows-y-readme.md) | `docs` | `repo` | Hecho | 2026-11-03 a 2026-11-10 |
| 7 | [Despliegue con Docker](07-despliegue-docker.md) | `build` | `docker` | Hecho | 2026-11-09 a 2026-11-10 |
| 8 | [Pipeline de CI/CD](08-pipeline-ci-cd.md) | `ci` | `ci` | Hecho | 2026-11-09 a 2026-11-10 |
| 9 | [Convenciones de commits y hooks](09-convenciones-commits-y-hooks.md) | `chore` | `repo` | Hecho | 2026-11-09 a 2026-11-10 |
| 10 | [Dependencias, auditoría y licencias](10-dependencias-y-licencias.md) | `build` | `deps` | Hecho | 2026-11-09 a 2026-11-10 |
| 11 | [Seguridad y escaneo de secretos](11-seguridad-y-secretos.md) | `feat` | `security` | Hecho | 2026-11-09 a 2026-11-10 |
| 12 | [Pruebas con datos reales](12-pruebas-con-datos-reales.md) | `test` | `back` | Hecho | 2026-11-09 |
| 13 | [Plantillas de $100, $200 y $500](13-plantillas-100-200-500.md) | `feat` | `back` | Pendiente | 2026-11-03 a 2026-11-09 |
| 14 | [Lectura en voz alta del resultado](14-lectura-en-voz-alta.md) | `feat` | `front` | Hecho | 2026-11-10 |
| 15 | [Corregir el aviso de bandit (B110) que deja el CI en rojo](15-corregir-aviso-bandit.md) | `fix` | `front` | Pendiente | — |
| 16 | [Una foto de $100 se identifica como $1000](16-foto-de-100-se-confunde-con-1000.md) | `fix` | `back` | Pendiente | — |
| 17 | [Foto vertical de $50 aparece como «No reconocido»](17-foto-vertical-de-50-no-reconocida.md) | `fix` | `back` | Pendiente | — |
| 18 | [Conjunto de fotografías de evaluación independiente de las plantillas](18-conjunto-de-evaluacion-independiente.md) | `test` | `back` | Pendiente | — |
| 19 | [Reporte de exactitud con matriz de confusión](19-reporte-de-exactitud.md) | `docs` | `repo` | Pendiente | — |
| 20 | [Actualizar el documento Word del proyecto con el código actual](20-actualizar-documento-word.md) | `docs` | `repo` | En curso | 2026-11-16 (en curso) |
| 21 | [Capturas actuales de la aplicación para el reporte](21-capturas-actuales-de-la-app.md) | `docs` | `front` | Pendiente | — |
| 22 | [Verificar nombres de equipo y grupo en la aplicación desplegada](22-equipo-y-grupo-en-la-app-desplegada.md) | `chore` | `front` | Pendiente | — |
| 23 | [Probar la lectura en voz alta con un lector de pantalla real](23-prueba-con-lector-de-pantalla.md) | `test` | `front` | Pendiente | — |
| 24 | [Probar la cámara de la aplicación en teléfonos](24-camara-en-telefonos.md) | `test` | `front` | Pendiente | — |
| 25 | [Confirmar plantillas de las versiones anterior y nueva de $20 y $50](25-versiones-anterior-y-nueva-de-20-y-50.md) | `feat` | `back` | Pendiente | — |
| 26 | [Proteger la rama main y exigir revisión del CI](26-proteger-rama-main.md) | `chore` | `repo` | Pendiente | — |
| 27 | [Pruebas automáticas de la interfaz con Streamlit AppTest](27-pruebas-automaticas-del-front.md) | `test` | `front` | Pendiente | — |
| 28 | [Publicar la primera versión (v1.0.0) y la imagen de Docker](28-primera-version-v1.md) | `build` | `ci` | Pendiente | — |
| 29 | [Calibrar el umbral de aceptación y los pesos color / ORB](29-calibrar-umbral-y-pesos.md) | `feat` | `back` | Pendiente | — |
| 30 | [Medir el tiempo de respuesta del reconocimiento](30-medir-tiempo-de-respuesta.md) | `test` | `back` | Pendiente | — |

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
