# #1 · Estructura inicial del proyecto y solución de Visual Studio

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `chore` |
| **Alcance** | `repo` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `chore/1-estructura-inicial` |
| **Registrado** | 2026-11-10 (retroactivo) |
| **Trabajo realizado** | 2026-11-03 a 2026-11-10 |

## Descripción

Organizar el repositorio en tres carpetas con responsabilidades separadas (back, front y ejecución) y dejar el
proyecto abrible desde Visual Studio 2022.

## Criterios de aceptación

- [x] Existen `Back/` (motor), `Front/` (interfaz) y `Ejecucion/` (ejecución, despliegue y verificación).
- [x] `Ejecucion/ReconocedorBilletes.sln` y `ReconocedorBilletes.pyproj` abren el proyecto en Visual Studio 2022.
- [x] `.gitignore` excluye `.env` y archivos generados.
- [x] El repositorio incluye `LICENSE` (MIT) y un `README.md` con la estructura.

## Cómo verificar

1. Clonar el repositorio y comprobar que existen las tres carpetas.
2. Abrir `Ejecucion\ReconocedorBilletes.sln` en Visual Studio 2022.

## Historial en el repositorio

Fechas tomadas de los commits reales de `main` (`git log`). El ticket se registró después del trabajo.

| Fecha | Commit | Autor | Qué se hizo |
|---|---|---|---|
| 2026-11-03 | `3bb65ec, a451eba, 19f210b` | Chucho1303 | Se crean las carpetas Ejecucion, Back y Front |
| 2026-11-09 | `0fc6207` | Jesus Perez Estrada | chore(repo): crea estructura del proyecto y solución de Visual Studio (#1) |
| 2026-11-10 | `e8b3fea` | Jesus Perez Estrada | refactor(repo): reorganiza todo en Back, Front y Ejecucion (#1) |

## Relacionado

#6 (lanzadores y README) · #7 (Docker)
