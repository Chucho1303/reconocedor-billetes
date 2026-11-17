# #30 · Medir el tiempo de respuesta del reconocimiento

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `test` |
| **Alcance** | `back` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `test/30-tiempo-respuesta` |
| **Registrado** | 2026-11-16 |

## Descripción

La aplicación compara cada foto contra todas las plantillas; falta saber cuánto tarda y cómo crece al agregar más.

## Situación actual (revisión del repositorio)

- Hay 15 plantillas y cada consulta las recorre todas.
- No hay mediciones registradas.

## Criterios de aceptación

- [ ] Un script mide el tiempo de `segmentar` + `clasificar` en una foto real, con varias repeticiones.
- [ ] Se anota la mediana y el máximo, y el equipo donde se midió.
- [ ] Se estima el efecto de duplicar las plantillas.
- [ ] Los resultados quedan en la documentación.

## Cómo verificar

Ejecutar el script y comparar con los números del documento.

## Relacionado

#2 (motor) · #18 (conjunto)
