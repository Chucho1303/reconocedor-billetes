# Reconocedor de billetes mexicanos

## Abrir y ejecutar desde Visual Studio 2022

1. Instala Visual Studio 2022 con la carga de trabajo **Desarrollo de Python**.
2. Instala Python 3.10 o superior y marca la opción para agregar Python al PATH.
3. Descomprime esta carpeta completa.
4. Abre `ReconocedorBilletes.sln` desde Visual Studio.
5. Si Visual Studio solicita seleccionar un intérprete, elige tu instalación de Python 3.10+.
6. Abre **Ver > Terminal** y ejecuta una sola vez:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. En el Explorador de soluciones, clic derecho sobre `Iniciar_Visual_Studio.py` y elige **Establecer como archivo de inicio** si no aparece ya seleccionado.
8. Presiona **F5** o **Ctrl+F5**. Streamlit iniciará el servidor y mostrará una dirección local; normalmente `http://localhost:8501`. Ábrela en tu navegador.
9. Para detener la aplicación, vuelve a Visual Studio y presiona **Mayús+F5** o cierra la terminal que ejecuta Streamlit.

> Si no aparece la plantilla de proyecto Python o Visual Studio no reconoce `.pyproj`, modifica la instalación de Visual Studio e instala la carga de trabajo **Desarrollo de Python**.

## Estructura solicitada
- `Ejecucion/`: lanzadores auxiliares de Windows.
- `Back/`: motor OpenCV y plantillas.
- `Front/`: interfaz Streamlit y fotografías de ejemplo.
- `ReconocedorBilletes.sln` y `ReconocedorBilletes.pyproj`: solución y proyecto para Visual Studio.
- `Iniciar_Visual_Studio.py`: punto de entrada de F5.
- `requirements.txt`: dependencias.

## Plantillas disponibles
El ZIP original incluye plantillas reales para $20, $50 y $1,000. Las carpetas de $100, $200 y $500 están preparadas, pero necesitan fotografías reales para entrenar esas denominaciones.

## Importante
El sistema estima la **denominación**; no certifica que un billete sea auténtico. El porcentaje mostrado es un puntaje de similitud del algoritmo, no una probabilidad estadística ni una validación bancaria.
