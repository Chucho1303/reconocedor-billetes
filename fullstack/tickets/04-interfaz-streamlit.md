# #4 · Interfaz web con Streamlit

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `feat` |
| **Alcance** | `front` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `feat/4-interfaz-streamlit` |
| **Registrado** | 2026-11-10 (retroactivo) |
| **Trabajo realizado** | 2026-10-19 a 2026-11-09 |

## Descripción

Construir en `Front/app.py` una aplicación web para probar el reconocedor sin usar la línea de comandos.

## Criterios de aceptación

- [x] Tres pestañas: **Probar**, **Cómo funciona** y **Acerca del proyecto**.
- [x] Tres formas de entrada: subir fotografía, usar la cámara o elegir una imagen de ejemplo (`Front/ejemplos/`).
- [x] El resultado muestra la denominación, el nivel de confianza y el análisis por denominación.
- [x] Se rechazan imágenes que superen `BILLETES_MAX_UPLOAD_MB` (10 MB por defecto).
- [x] Se advierte que el sistema estima la denominación y no valida autenticidad.
- [x] La pestaña «Acerca del proyecto» muestra el equipo y grupo configurados por variables de entorno.
- [x] Tema y servidor configurados en `Front/.streamlit/config.toml`.
- [x] Desplegada en Streamlit Community Cloud (`Front/app.py`, Python 3.12).

## Cómo verificar

```bash
pip install -r requirements.txt
streamlit run Front/app.py     # http://localhost:8501
```

## Historial en el repositorio

Fechas tomadas de los commits reales de `main` (`git log`). El ticket se registró después del trabajo.

| Fecha | Commit | Autor | Qué se hizo |
|---|---|---|---|
| 2026-10-19 | `e3e2702` | Chucho1303 | Primera versión de app.py (Add files via upload) |
| 2026-11-03 | `19f210b, 93bb919` | Chucho1303, Manuel1513 | app.py y fotos de ejemplo movidos a Front/ |
| 2026-11-09 | `dba188c, a51a7c0` | Jesus Perez Estrada | feat(front): agrega interfaz web con Streamlit y fotos de ejemplo (#4); fix(repo): deja de ignorar la foto de ejemplo captura_01.jpg (#4) |

## Relacionado

#2 (motor) · #6 (lanzadores) · #14 (lectura en voz alta)
