# #12 · Pruebas automáticas con datos reales

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `test` |
| **Alcance** | `back` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `test/12-pruebas-datos-reales` |

## Descripción

Probar el motor con las fotografías reales del repositorio, no con datos sintéticos únicamente.

## Criterios de aceptación

- [x] `Back/tests/test_billetes.py` usa fotos reales de `Front/ejemplos/` y las plantillas de `Back/plantillas/`.
- [x] Una foto real de $1,000 se reconoce con confianza ≥ 0.9.
- [x] Una foto real de $50 se reconoce con confianza ≥ el umbral de aceptación.
- [x] Una foto vertical no falla y devuelve puntajes válidos entre 0 y 1.
- [x] Cada plantilla se reconoce a sí misma.
- [x] Una imagen de ruido aleatorio **no** se reconoce como billete.
- [x] Sin plantillas se lanza `RuntimeError`.
- [x] `Back/tests/test_config.py` cubre la lectura y validación de variables de entorno.
- [x] `Ejecucion/pytest.ini` permite correr todo desde la raíz y el CI lo ejecuta.

## Cómo verificar

```bash
pip install -r Ejecucion/requirements-dev.txt
python -m pytest -v -c Ejecucion/pytest.ini
```

## Relacionado

#2 (motor) · #8 (job `test`) · #13 (ampliar pruebas a $100, $200 y $500)
