# Seguridad y manejo de datos sensibles

Documento del punto **9. Seguridad y Manejo de Datos Sensibles**.

## Regla crítica: cero credenciales en el código

Ninguna contraseña, llave de API o credencial de producción está escrita en el código (*hardcoded*).
Toda configuración variable entra por **variables de entorno** (`Back/billetes_config.py`):

| Variable | Uso | Valor por defecto |
|---|---|---|
| `BILLETES_UMBRAL` | Umbral de aceptación (0–1) | `0.35` |
| `BILLETES_PLANTILLAS` | Carpeta de plantillas | `Back/plantillas` |
| `BILLETES_MAX_UPLOAD_MB` | Tamaño máximo de imagen | `10` |
| `BILLETES_EQUIPO` / `BILLETES_GRUPO` | Datos mostrados en la interfaz | marcadores |

- Desarrollo local: copia `Ejecucion/.env.example` a `Ejecucion/.env` (ignorado por Git).
- Docker: `docker compose` lee `Ejecucion/.env` o las variables del servidor.
- CI/CD: el único token usado (`GITHUB_TOKEN`, para publicar la imagen) viene de `secrets.*` de GitHub.

Hoy la aplicación **no necesita** ninguna llave externa. Si en el futuro se agrega una (base de datos,
API de terceros), se declara en `Ejecucion/.env.example` sin valor real y se lee con `os.environ`.

## Controles automáticos

| Control | Herramienta | Dónde corre |
|---|---|---|
| Secretos escritos en código (llaves AWS/Google/GitHub/Slack, claves privadas, `password = "..."`, URLs con usuario:clave) | `Ejecucion/scripts/scan_secrets.py` | CI + `Ejecucion/verificar.bat` |
| Vulnerabilidades del código (filtros básicos) | `bandit` (`Ejecucion/bandit.yaml`) | CI |
| Vulnerabilidades conocidas en dependencias | `pip-audit` | CI + Dependabot |
| Archivos secretos fuera del repositorio | `.gitignore` (`.env`, `*.pem`, `*.key`, `secrets/`) | Git |

## Endurecimiento de la aplicación

- Imágenes subidas: límite de tamaño (`BILLETES_MAX_UPLOAD_MB` y `maxUploadSize`), validación de que
  realmente se decodifican, y tope de 50 millones de píxeles contra imágenes “bomba”.
- Protección XSRF de Streamlit activada; telemetría de uso desactivada (`gatherUsageStats = false`).
- Las imágenes se procesan en memoria: **no se guardan ni se envían a terceros**. No se recolectan
  datos personales.
- El HTML personalizado de la interfaz (`unsafe_allow_html`) solo incluye texto fijo o números
  calculados por la aplicación; nunca texto escrito por el usuario.
- Contenedor Docker: se ejecuta con usuario sin privilegios (`uid 10001`), `no-new-privileges`, sin
  `.env` dentro de la imagen (`Ejecucion/Dockerfile.dockerignore`).
- Línea de comandos: la denominación solo acepta valores de una lista cerrada, así que no hay
  recorrido de rutas al registrar plantillas.

## Cumplimiento legal

La aplicación no procesa datos personales (RGPD / LFPDPPP): las fotografías son de billetes y se
descartan al terminar la sesión. Si se añadieran cuentas de usuario o almacenamiento de imágenes,
habría que agregar aviso de privacidad, base legal y política de retención.

## Si se filtra una credencial

1. Revocarla de inmediato en el proveedor. 2. Generar una nueva y guardarla solo en variables de
entorno. 3. Eliminarla del historial de Git (`git filter-repo`) — borrar el archivo no basta.
