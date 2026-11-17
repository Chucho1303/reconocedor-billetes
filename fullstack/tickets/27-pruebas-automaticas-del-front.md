# #27 · Pruebas automáticas de la interfaz con Streamlit AppTest

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `test` |
| **Alcance** | `front` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `test/27-pruebas-front` |
| **Registrado** | 2026-11-16 |

## Descripción

Las pruebas actuales cubren `Back/` y `Ejecucion/`; la interfaz no tiene ninguna.

## Situación actual (revisión del repositorio)

- No existe una carpeta `Front/tests/`.
- Cambios en `Front/app.py` (como la voz o el límite de 10 MB) no se validan en el CI.

## Criterios de aceptación

- [ ] `Front/tests/test_app.py` carga la app con `streamlit.testing.v1.AppTest`.
- [ ] Cubre: carga sin errores, selector de origen, ejemplo conocido y mensaje de «No reconocido».
- [ ] Se ejecuta con `pytest` y dentro del job `test` del CI.

## Cómo verificar

```bash
python -m pytest -c Ejecucion/pytest.ini Front/tests
```

## Relacionado

#4 (interfaz) · #8 (CI) · #12 (pruebas)
