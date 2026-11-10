# #6 · Lanzadores de Windows y README

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `docs` |
| **Alcance** | `repo` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `docs/6-lanzadores-readme` |

## Descripción

Permitir que cualquier integrante ejecute, pruebe y registre plantillas en Windows con un doble clic, y documentar el
proyecto en el README.

## Criterios de aceptación

- [x] `Ejecucion/iniciar.bat` arranca la aplicación Streamlit.
- [x] `Ejecucion/registrar_plantilla.bat <den> <imagen>` agrega una plantilla a su carpeta.
- [x] `Ejecucion/verificar.bat` ejecuta pruebas, escaneo de secretos, bandit y licencias.
- [x] `Ejecucion/activar_hooks.bat` activa los hooks de commits.
- [x] `Ejecucion/Iniciar_Visual_Studio.py` sirve como archivo de inicio (F5) en Visual Studio 2022.
- [x] El README documenta estructura, ejecución local, Visual Studio, Docker, pruebas, convención de commits, plantillas, dependencias y autores.

## Cómo verificar

Ejecutar `Ejecucion\iniciar.bat` en Windows y abrir `http://localhost:8501`.

## Relacionado

#1 (estructura) · #4 (interfaz) · #9 (hooks)
