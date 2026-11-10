# #10 · Dependencias fijadas, auditoría de vulnerabilidades y licencias

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `build` |
| **Alcance** | `deps` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `build/10-dependencias` |
| **Registrado** | 2026-11-10 (retroactivo) |
| **Trabajo realizado** | 2026-11-09 a 2026-11-10 |

## Descripción

Hacer reproducible la instalación, vigilar vulnerabilidades y hacer cumplir una política de licencias.

## Criterios de aceptación

- [x] `Ejecucion/requirements.txt` fija las dependencias directas con versión exacta (`==`).
- [x] `Ejecucion/requirements.lock.txt` fija el árbol completo de ejecución.
- [x] `Ejecucion/requirements-dev.txt` separa pruebas y auditoría (no entran a la imagen Docker).
- [x] `requirements.txt` de la raíz es copia del de `Ejecucion/` (necesaria para Streamlit Cloud).
- [x] `pip-audit` revisa vulnerabilidades conocidas sobre el archivo lock.
- [x] `Ejecucion/scripts/check_licenses.py` falla (código 1) ante licencias prohibidas o desconocidas.
- [x] `.github/dependabot.yml` propone actualizaciones.
- [x] `Ejecucion/docs/DEPENDENCIAS_Y_LICENCIAS.md` documenta política, inventario y auditoría.

## Cómo verificar

```bash
pip-audit -r Ejecucion/requirements.lock.txt
python Ejecucion/scripts/check_licenses.py
```

## Historial en el repositorio

Fechas tomadas de los commits reales de `main` (`git log`). El ticket se registró después del trabajo.

| Fecha | Commit | Autor | Qué se hizo |
|---|---|---|---|
| 2026-11-09 | `afb5e78, 8c9698f` | Jesus Perez Estrada | build(deps): fija versiones exactas y agrega requirements-dev (#10); docs(deps): agrega auditor de licencias e inventario de dependencias (#10) |
| 2026-11-10 | `95770bc, 7b18a3d` | Jesus Perez Estrada, Chucho1303 | fix(deps): exige Python 3.12 al iniciar y corrige CRLF de .bat (#10); fix(deps): copia requirements.txt a la raiz para Streamlit Cloud |

## Relacionado

#8 (job `security`)
