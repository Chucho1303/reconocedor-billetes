# #4 · Interfaz web con Streamlit

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `feat` |
| **Alcance** | `front` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `feat/4-interfaz-streamlit` |

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

## Relacionado

#2 (motor) · #6 (lanzadores) · #14 (lectura en voz alta)
