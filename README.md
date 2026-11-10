# Reconocedor de billetes mexicanos

## Abrir y ejecutar desde Visual Studio 2022

1. Instala Visual Studio 2022 con la carga de trabajo **Desarrollo de Python**.
2. Instala Python 3.12 o superior y marca la opción para agregar Python al PATH.
3. Descomprime esta carpeta completa.
4. Abre `ReconocedorBilletes.sln` desde Visual Studio.
5. Si Visual Studio solicita seleccionar un intérprete, elige tu instalación de Python 3.12+.
6. Abre **Ver > Terminal** y ejecuta una sola vez:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. En el Explorador de soluciones, clic derecho sobre `Iniciar_Visual_Studio.py` y elige **Establecer como archivo de inicio** si no aparece ya seleccionado.
8. Presiona **F5** o **Ctrl+F5**. Streamlit iniciará el servidor y mostrará una dirección local; normalmente `http://localhost:8501`. Ábrela en tu navegador.
9. Para detener la aplicación, vuelve a Visual Studio y presiona **Mayús+F5** o cierra la terminal que ejecuta Streamlit.

> Si no aparece la plantilla de proyecto Python o Visual Studio no reconoce `.pyproj`, modifica la instalación de Visual Studio e instala la carga de trabajo **Desarrollo de Python**.

## Ejecutar con Docker (despliegue repetible)

```bash
cp .env.example .env          # opcional: ajusta la configuración
docker compose up --build     # abre http://localhost:8501
```

O sin compose:

```bash
docker build -t reconocedor-billetes .
docker run --rm -p 8501:8501 reconocedor-billetes
```

La imagen usa `python:3.12-slim`, dependencias con versión fija, usuario sin privilegios y un
`HEALTHCHECK` (`/_stcore/health`). El pipeline `.github/workflows/ci.yml` construye la imagen y
comprueba que arranca en cada Pull Request; al crear un tag `vX.Y.Z` la publica en GitHub Container Registry.

## Configuración y secretos

Todo valor configurable se lee de variables de entorno (ver `.env.example` y `docs/SEGURIDAD.md`).
**Nunca** se escriben contraseñas, llaves de API ni credenciales en el código; `.env` está en `.gitignore`.

## Pruebas y verificaciones

```bash
pip install -r requirements-dev.txt
python -m pytest                      # pruebas con las fotos reales de Front/ejemplos
python scripts/scan_secrets.py        # busca credenciales escritas en el código
bandit -q -c bandit.yaml -r Back Front Iniciar_Visual_Studio.py scripts
python scripts/check_licenses.py      # política de licencias
pip-audit -r requirements.lock.txt    # vulnerabilidades conocidas
```

En Windows basta con ejecutar `Ejecucion\verificar.bat`.

## Convención de commits

Conventional Commits con referencia a la tarea, por ejemplo `feat(back): agrega votación por fotogramas (#5)`.
Para activar la validación en Windows ejecuta `Ejecucion\activar_hooks.bat` (o `git config core.hooksPath .githooks`). Detalles en `CONTRIBUTING.md`; historial de tareas en `docs/BACKLOG.md`.

## Dependencias y licencias

Versiones fijadas en `requirements.txt` / `requirements.lock.txt`; inventario y política de licencias en
`docs/DEPENDENCIAS_Y_LICENCIAS.md`. Licencia del proyecto: MIT (`LICENSE`).

## Estructura solicitada
- `Ejecucion/`: lanzadores auxiliares de Windows.
- `Back/`: motor OpenCV y plantillas.
- `Front/`: interfaz Streamlit y fotografías de ejemplo.
- `ReconocedorBilletes.sln` y `ReconocedorBilletes.pyproj`: solución y proyecto para Visual Studio.
- `Iniciar_Visual_Studio.py`: punto de entrada de F5.
- `requirements.txt`, `requirements.lock.txt`, `requirements-dev.txt`: dependencias fijadas.
- `Dockerfile`, `docker-compose.yml`, `.github/workflows/ci.yml`: despliegue y CI/CD.
- `tests/`, `scripts/`, `docs/`: pruebas, herramientas de verificación y documentación.

## Plantillas disponibles
El ZIP original incluye plantillas reales para $20, $50 y $1,000. Las carpetas de $100, $200 y $500 están preparadas, pero necesitan fotografías reales para entrenar esas denominaciones.

## Importante
El sistema estima la **denominación**; no certifica que un billete sea auténtico. El porcentaje mostrado es un puntaje de similitud del algoritmo, no una probabilidad estadística ni una validación bancaria.
