# #18 · Conjunto de fotografías de evaluación independiente de las plantillas

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `test` |
| **Alcance** | `back` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `test/18-conjunto-evaluacion` |
| **Registrado** | 2026-11-16 |

## Descripción

Reunir fotos que no sean plantillas para medir el desempeño real, porque hoy las pruebas usan las mismas imágenes con que se registra cada denominación.

## Situación actual (revisión del repositorio)

- Doce archivos de `Front/ejemplos/` son idénticos (mismo hash) a plantillas de `Back/plantillas/`.
- La exactitud medida hoy (14 de 15) no es independiente.

## Criterios de aceptación

- [ ] Existe una carpeta de evaluación con subcarpetas `20`, `50`, `100`, `200`, `500`, `1000`.
- [ ] Al menos 5 fotos por denominación que **no** estén en `Back/plantillas/`.
- [ ] Variedad de luz, fondo, ángulo y desgaste, anotada en un archivo de descripción.
- [ ] Ninguna foto se repite entre evaluación y plantillas (se comprueba por hash).

## Cómo verificar

```bash
python Back/billetes.py evaluar <carpeta-de-evaluacion> --csv evaluacion.csv
```

## Relacionado

#12 (pruebas) · #19 (reporte) · #29 (calibración)
