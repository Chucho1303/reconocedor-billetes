# #1 · Estructura inicial del proyecto y solución de Visual Studio

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `chore` |
| **Alcance** | `repo` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `chore/1-estructura-inicial` |

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

## Relacionado

#6 (lanzadores y README) · #7 (Docker)
