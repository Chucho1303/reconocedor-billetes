# Fullstack · Reconocedor de billetes mexicanos

Vista general de todo el proyecto (interfaz, motor, ejecución y seguimiento de tareas) en un solo lugar.
El código vive en `Back/`, `Front/` y `Ejecucion/`; esta carpeta reúne la documentación y los tickets.

🔗 Aplicación en línea: [reconocedor-billetes-uaem.streamlit.app](https://reconocedor-billetes-uaem.streamlit.app/)

> ⚠️ El sistema **estima** la denominación de un billete a partir de una fotografía. No certifica que sea auténtico.

## Capas del proyecto

| Capa | Carpeta | Qué contiene | Tecnología |
|---|---|---|---|
| **Front** | [`Front/`](../Front) | Interfaz web `app.py` con pestañas Probar, Cómo funciona y Acerca del proyecto; fotos de ejemplo; lectura del resultado en voz alta | Streamlit 1.67.0 |
| **Back** | [`Back/`](../Back) | Motor de reconocimiento `billetes.py`, configuración `billetes_config.py`, plantillas por denominación y pruebas | Python 3.12, OpenCV 5.0.0.93 (headless), NumPy 2.5.4 |
| **Ejecución** | [`Ejecucion/`](../Ejecucion) | Lanzadores de Windows, Docker, dependencias fijadas, scripts de seguridad y licencias, hooks de Git y documentación técnica | Docker, GitHub Actions |
| **Seguimiento** | [`fullstack/tickets/`](tickets) | Un ticket por tarea con criterios de aceptación e historial real de commits | Markdown |

## Flujo de una predicción

1. El usuario sube una fotografía, usa la cámara o elige un ejemplo en `Front/app.py`.
2. El front llama al motor del back: `segmentar` aísla el billete, `extraer` calcula histograma HSV y puntos ORB.
3. `clasificar` compara contra las plantillas de `Back/plantillas/<denominación>/` (color + ORB con RANSAC).
4. Si el puntaje supera `BILLETES_UMBRAL` (0.35 por defecto) se devuelve la denominación; si no, «No reconocido».
5. El front muestra el resultado con su nivel de confianza y lo lee en voz alta.

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
streamlit run Front/app.py                 # http://localhost:8501
```

Con Docker: `docker compose -f Ejecucion/docker-compose.yml up --build`. En Windows: `Ejecucion\iniciar.bat`.

## Verificaciones antes de abrir un PR

```bash
python -m pytest -c Ejecucion/pytest.ini
python Ejecucion/scripts/scan_secrets.py
python Ejecucion/scripts/check_licenses.py
```

## Tickets

Los tickets están en [`tickets/`](tickets), con su [índice y estados](tickets/README.md). El backlog original
con la numeración que usan los commits (`#N`) está en [`Ejecucion/docs/BACKLOG.md`](../Ejecucion/docs/BACKLOG.md).

## Más documentación

- [README del repositorio](../README.md)
- [Guía de contribución y formato de commits](../.github/CONTRIBUTING.md)
- [Seguridad y manejo de datos sensibles](../Ejecucion/docs/SEGURIDAD.md)
- [Dependencias y licencias](../Ejecucion/docs/DEPENDENCIAS_Y_LICENCIAS.md)

## Autores

- [Chucho1303](https://github.com/Chucho1303)
- [Manuel1513](https://github.com/Manuel1513)
