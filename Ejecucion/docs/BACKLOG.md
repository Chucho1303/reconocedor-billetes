# Backlog e historial de tareas

Cada commit del repositorio referencia una de estas tareas (`#N`) para mantener la trazabilidad.
Para crearlas en GitHub con la misma numeración, ejecuta `Ejecucion/scripts/crear_issues.sh` en un repositorio
nuevo y vacío (GitHub numera los issues en orden: #1, #2, …).

| # | Tarea | Estado |
|---|---|---|
| 1 | Estructura inicial del proyecto y solución de Visual Studio | Hecho |
| 2 | Motor de reconocimiento: segmentación, histograma HSV y ORB + RANSAC | Hecho |
| 3 | Plantillas reales de $20, $50 y $1,000 | Hecho |
| 4 | Interfaz web con Streamlit | Hecho |
| 5 | Modos de línea de comandos: registrar, imagen, cámara y evaluar | Hecho |
| 6 | Lanzadores de Windows y README | Hecho |
| 7 | Despliegue repetible con Docker | Hecho |
| 8 | Pipeline de CI/CD con GitHub Actions | Hecho |
| 9 | Convenciones de commits y hooks de Git | Hecho |
| 10 | Dependencias fijadas, auditoría de vulnerabilidades y licencias | Hecho |
| 11 | Seguridad: configuración por variables de entorno y escaneo de secretos | Hecho |
| 12 | Pruebas automáticas con datos reales | Hecho |
| 13 | Plantillas de $100, $200 y $500 (faltan fotografías reales) | Pendiente |
| 14 | Lectura en voz alta del resultado (accesibilidad) | Hecho |
| 15 | Corregir el aviso de bandit (B110) que deja el CI en rojo | Pendiente |
| 16 | Una foto de $100 se identifica como $1000 | Pendiente |
| 17 | Foto vertical de $50 aparece como «No reconocido» | Pendiente |
| 18 | Conjunto de fotografías de evaluación independiente de las plantillas | Pendiente |
| 19 | Reporte de exactitud con matriz de confusión | Pendiente |
| 20 | Actualizar el documento Word del proyecto con el código actual | En curso |
| 21 | Capturas actuales de la aplicación para el reporte | Pendiente |
| 22 | Verificar nombres de equipo y grupo en la aplicación desplegada | Pendiente |
| 23 | Probar la lectura en voz alta con un lector de pantalla real | Pendiente |
| 24 | Probar la cámara de la aplicación en teléfonos | Pendiente |
| 25 | Confirmar plantillas de las versiones anterior y nueva de $20 y $50 | Pendiente |
| 26 | Proteger la rama main y exigir revisión del CI | Pendiente |
| 27 | Pruebas automáticas de la interfaz con Streamlit AppTest | Pendiente |
| 28 | Publicar la primera versión (v1.0.0) y la imagen de Docker | Pendiente |
| 29 | Calibrar el umbral de aceptación y los pesos color / ORB | Pendiente |
| 30 | Medir el tiempo de respuesta del reconocimiento | Pendiente |

El detalle de cada tarea (descripción, criterios de aceptación y cómo verificarla) está en `fullstack/tickets/`.
