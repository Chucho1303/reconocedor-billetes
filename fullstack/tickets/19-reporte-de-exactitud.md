# #19 · Reporte de exactitud con matriz de confusión

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `docs` |
| **Alcance** | `repo` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `docs/19-reporte-exactitud` |
| **Registrado** | 2026-11-16 |

## Descripción

Documentar los resultados de `evaluar` sobre el conjunto del ticket #18 para sustituir la frase «aún no se ha medido la exactitud».

## Situación actual (revisión del repositorio)

- El modo `evaluar` ya imprime matriz de confusión, exactitud global y por denominación, y puede guardar un CSV.
- Nada de eso está registrado en la documentación.

## Criterios de aceptación

- [ ] Un documento en `Ejecucion/docs/` con fecha, comando usado, matriz de confusión y exactitud global y por denominación.
- [ ] Aclara qué fotos se usaron y que son independientes de las plantillas.
- [ ] La sección de limitaciones del README y de la app se actualiza con la cifra real.

## Cómo verificar

Reproducir los números con el comando de `evaluar` y comparar con el documento.

## Relacionado

#18 (conjunto) · #12 (pruebas)
