# #2 · Motor de reconocimiento: segmentación, histograma HSV y ORB + RANSAC

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `feat` |
| **Alcance** | `back` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `feat/2-motor-reconocimiento` |
| **Registrado** | 2026-11-10 (retroactivo) |
| **Trabajo realizado** | 2026-10-19 a 2026-11-09 |

## Descripción

Implementar en `Back/billetes.py` el algoritmo que, a partir de una fotografía, aísla el billete y estima su
denominación comparándolo contra plantillas reales.

## Criterios de aceptación

- [x] `segmentar(img)` aísla el billete de la fotografía y devuelve el recorte.
- [x] `extraer(recorte)` calcula las características usadas para comparar (histograma de color en HSV y puntos ORB).
- [x] `puntaje_color` y `puntaje_orb` (emparejamiento ORB con verificación geométrica RANSAC) producen puntajes entre 0 y 1.
- [x] `clasificar(recorte, plantillas)` devuelve `(denominación, confianza, detalle)`; el `detalle` incluye el puntaje de cada denominación.
- [x] Si la confianza queda por debajo de `UMBRAL_ACEPTACION` (0.35 por defecto) la denominación es `None` («No reconocido»).
- [x] Sin plantillas cargadas, `clasificar` lanza `RuntimeError`.
- [x] El resultado se muestra como estimación: **no certifica autenticidad** del billete.

## Archivos

`Back/billetes.py` · `Back/billetes_config.py`

## Cómo verificar

```bash
python -m pytest -c Ejecucion/pytest.ini Back/tests/test_billetes.py
```

## Historial en el repositorio

Fechas tomadas de los commits reales de `main` (`git log`). El ticket se registró después del trabajo.

| Fecha | Commit | Autor | Qué se hizo |
|---|---|---|---|
| 2026-10-19 | `0a4e57f, e3e2702` | Manuel1513, Chucho1303 | Primera versión de billetes.py (Add files via upload) |
| 2026-11-03 | `a451eba` | Chucho1303 | billetes.py movido a Back/ |
| 2026-11-09 | `905c405` | Jesus Perez Estrada | feat(back): agrega motor de reconocimiento y modos de línea de comandos (#2) |

## Relacionado

#3 (plantillas) · #12 (pruebas con datos reales)
