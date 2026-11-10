# Reconocedor de billetes mexicanos

## Abrir y ejecutar desde Visual Studio 2022

1. Instala Visual Studio 2022 con la carga de trabajo **Desarrollo de Python**.
2. Instala Python 3.12 o superior y marca la opción para agregar Python al PATH.
3. Descomprime esta carpeta completa.
4. Abre `Ejecucion\ReconocedorBilletes.sln` desde Visual Studio.
5. Si Visual Studio solicita seleccionar un intérprete, elige tu instalación de Python 3.12+.
6. Abre **Ver > Terminal** y ejecuta una sola vez:

   ```powershell
   python -m pip install -r Ejecucion/requirements.txt
   ```

7. En el Explorador de soluciones, clic derecho sobre `Ejecucion\Iniciar_Visual_Studio.py` y elige **Establecer como archivo de inicio** si no aparece ya seleccionado.
8. Presiona **F5** o **Ctrl+F5**. Streamlit iniciará el servidor y mostrará una dirección local; normalmente `http://localhost:8501`. Ábrela en tu navegador.
9. Para detener la aplicación, vuelve a Visual Studio y presiona **Mayús+F5** o cierra la terminal que ejecuta Streamlit.

> Si no aparece la plantilla de proyecto Python o Visual Studio no reconoce `.pyproj`, modifica la instalación de Visual Studio e instala la carga de trabajo **Desarrollo de Python**.

## Ejecutar con Docker (despliegue repetible)

```bash
cp Ejecucion/.env.example Ejecucion/.env          # opcional: ajusta la configuración
docker compose -f Ejecucion/docker-compose.yml up --build     # abre http://localhost:8501
```

O sin compose:

```bash
docker build -f Ejecucion/Dockerfile -t reconocedor-billetes .
docker run --rm -p 8501:8501 reconocedor-billetes
```

La imagen usa `python:3.12-slim`, dependencias con versión fija, usuario sin privilegios y un
`HEALTHCHECK` (`/_stcore/health`). El pipeline `.github/workflows/ci.yml` construye la imagen y
comprueba que arranca en cada Pull Request; al crear un tag `vX.Y.Z` la publica en GitHub Container Registry.

## Configuración y secretos

Todo valor configurable se lee de variables de entorno (ver `Ejecucion/.env.example` y `Ejecucion/docs/SEGURIDAD.md`).
**Nunca** se escriben contraseñas, llaves de API ni credenciales en el código; `.env` está en `.gitignore`.

## Pruebas y verificaciones

```bash
pip install -r Ejecucion/requirements-dev.txt
python -m pytest -c Ejecucion/pytest.ini                      # pruebas con las fotos reales de Front/ejemplos
python Ejecucion/scripts/scan_secrets.py        # busca credenciales escritas en el código
bandit -q -c Ejecucion/bandit.yaml -r Back Front Ejecucion/scripts Ejecucion/Iniciar_Visual_Studio.py
python Ejecucion/scripts/check_licenses.py      # política de licencias
pip-audit -r Ejecucion/requirements.lock.txt    # vulnerabilidades conocidas
```

En Windows basta con ejecutar `Ejecucion\verificar.bat`.

## Convención de commits

Conventional Commits con referencia a la tarea, por ejemplo `feat(back): agrega votación por fotogramas (#5)`.
Para activar la validación en Windows ejecuta `Ejecucion\activar_hooks.bat` (o `git config core.hooksPath Ejecucion/hooks`). Detalles en `.github/CONTRIBUTING.md`; historial de tareas en `Ejecucion/docs/BACKLOG.md`.

## Dependencias y licencias

Versiones fijadas en `Ejecucion/requirements.txt` / `requirements.lock.txt`; inventario y política de licencias en
`Ejecucion/docs/DEPENDENCIAS_Y_LICENCIAS.md`. Licencia del proyecto: MIT (`LICENSE`).

## Estructura del repositorio
- `Back/`: motor OpenCV (`billetes.py`, `billetes_config.py`), plantillas por denominación y pruebas (`tests/`).
- `Front/`: interfaz Streamlit (`app.py`), fotografías de ejemplo y `.streamlit/config.toml`.
- `Ejecucion/`: todo lo necesario para ejecutar, desplegar y verificar:
  - lanzadores de Windows (`iniciar.bat`, `registrar_plantilla.bat`, `verificar.bat`, `activar_hooks.bat`);
  - `Iniciar_Visual_Studio.py`, `ReconocedorBilletes.sln` y `.pyproj` (Visual Studio);
  - `Dockerfile`, `docker-compose.yml`, `requirements*.txt`, `.env.example`;
  - `scripts/` (secretos, licencias, commits), `hooks/`, `tests/` y `docs/` (seguridad, licencias, backlog).
- `.github/`: CI/CD (`workflows/ci.yml`), Dependabot, plantilla de PR, `CONTRIBUTING.md` y `SECURITY.md`.

## Plantillas disponibles
`Back/plantillas/<denominación>/` contiene fotografías reales para $20, $50, $100, $200, $500 y $1,000. Para añadir más:
`Ejecucion\registrar_plantilla.bat 100 "C:\Fotos\billete100.jpg"`.

## Importante
El sistema estima la **denominación**; no certifica que un billete sea auténtico. El porcentaje mostrado es un puntaje de similitud del algoritmo, no una probabilidad estadística ni una validación bancaria.
