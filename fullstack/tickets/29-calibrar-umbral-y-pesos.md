# #29 · Calibrar el umbral de aceptación y los pesos color / ORB

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `feat` |
| **Alcance** | `back` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `feat/29-calibracion` |
| **Registrado** | 2026-11-16 |

## Descripción

El motor usa `UMBRAL_ACEPTACION = 0.35` y pesos 35 % color / 65 % ORB sin una justificación medida.

## Situación actual (revisión del repositorio)

- Los valores están fijos en `Back/billetes.py` (`PESO_COLOR`, `PESO_ORB`, `INLIERS_REF`).
- No hay una comparación de alternativas.

## Criterios de aceptación

- [ ] Se prueban varias combinaciones con el conjunto del ticket #18.
- [ ] Se elige la que da mejor exactitud sin aceptar billetes falsos (ruido sigue como «No reconocido»).
- [ ] Los valores y la tabla de comparación quedan documentados.
- [ ] Las pruebas existentes siguen pasando.

## Cómo verificar

```bash
python Back/billetes.py evaluar <carpeta-de-evaluacion>
python -m pytest -c Ejecucion/pytest.ini
```

## Relacionado

#2 (motor) · #16 (error de $100) · #18 (conjunto)
