# #11 · Seguridad: configuración por variables de entorno y escaneo de secretos

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `feat` |
| **Alcance** | `security` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `feat/11-seguridad` |

## Descripción

Asegurar que ninguna credencial viva en el código y que la configuración se lea del entorno.

## Criterios de aceptación

- [x] `Back/billetes_config.py` centraliza la configuración y la lee de variables de entorno (`BILLETES_UMBRAL`, `BILLETES_PLANTILLAS`, `BILLETES_MAX_UPLOAD_MB`, `BILLETES_EQUIPO`, `BILLETES_GRUPO`).
- [x] Un valor inválido o fuera de rango cae al valor por defecto, sin romper la aplicación.
- [x] `Ejecucion/.env.example` documenta las variables; `Ejecucion/.env` está en `.gitignore`.
- [x] Límite de 50 millones de píxeles por imagen para evitar imágenes «bomba».
- [x] `Ejecucion/scripts/scan_secrets.py` detecta llaves y contraseñas escritas en el código.
- [x] `bandit` (`Ejecucion/bandit.yaml`) analiza `Back`, `Front` y `Ejecucion/scripts`.
- [x] `Ejecucion/docs/SEGURIDAD.md` y `.github/SECURITY.md` documentan controles y reporte de vulnerabilidades.

## Cómo verificar

```bash
python Ejecucion/scripts/scan_secrets.py
bandit -q -c Ejecucion/bandit.yaml -r Back Front Ejecucion/scripts Ejecucion/Iniciar_Visual_Studio.py
python -m pytest -c Ejecucion/pytest.ini Back/tests/test_config.py Ejecucion/tests/test_scan_secrets.py
```

## Relacionado

#7 (Docker) · #8 (job `security`)
