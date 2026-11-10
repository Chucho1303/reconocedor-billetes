# #10 · Dependencias fijadas, auditoría de vulnerabilidades y licencias

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `build` |
| **Alcance** | `deps` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `build/10-dependencias` |

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

## Relacionado

#8 (job `security`)
