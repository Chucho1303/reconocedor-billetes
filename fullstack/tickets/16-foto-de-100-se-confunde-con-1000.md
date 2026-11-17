# #16 · Una foto de $100 se identifica como $1000

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `fix` |
| **Alcance** | `back` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `fix/16-100-confundido-con-1000` |
| **Registrado** | 2026-11-16 |

## Descripción

La foto `Front/ejemplos/100 pesos.jpeg`, que además es plantilla de $100, se identifica como $1000.

## Situación actual (revisión del repositorio)

- `python Back/billetes.py imagen "Front/ejemplos/100 pesos.jpeg"` responde `$1000 MXN (52%)`.
- Las otras dos fotos de $100 sí se reconocen (100 % y 94 %).
- `python Back/billetes.py evaluar Back/plantillas` da 14 de 15 aciertos: el único error es este.
- Las plantillas se cargan sin segmentar, mientras que la consulta pasa por `segmentar`; esa diferencia es una causa probable.

## Criterios de aceptación

- [ ] Se identifica la causa (segmentación, plantilla o pesos) y queda escrita en el ticket.
- [ ] `100 pesos.jpeg` se reconoce como $100 con confianza ≥ umbral de aceptación.
- [ ] Se agrega una prueba automática que cubre este caso.
- [ ] Las demás fotos de `Front/ejemplos/` siguen reconociéndose igual que antes.

## Cómo verificar

```bash
python Back/billetes.py imagen "Front/ejemplos/100 pesos.jpeg"
python -m pytest -c Ejecucion/pytest.ini
```

## Relacionado

#2 (motor) · #13 (plantillas) · #29 (calibración)
