# #20 · Actualizar el documento Word del proyecto con el código actual

| Campo | Valor |
|---|---|
| **Estado** | En curso |
| **Tipo** | `docs` |
| **Alcance** | `repo` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `docs/20-documento-word` |
| **Registrado** | 2026-11-16 |
| **Trabajo realizado** | 2026-11-16 (en curso) |

## Descripción

Poner `Doc_M9_ampliado.docx` al día con el proyecto sin cambiar su estructura.

## Situación actual (revisión del repositorio)

- El documento habla de una barra lateral que la interfaz actual ya no tiene.
- Dice que $100, $200 y $500 son trabajo posterior, pero ya tienen plantillas.
- No menciona la lectura en voz alta, el límite de 10 MB ni Docker.
- La ruta del repositorio y las carpetas (`Ejecucion`, `fullstack`) no coinciden con las actuales.

## Criterios de aceptación

- [ ] Mismo índice, secciones, tablas y estilos que el original.
- [ ] Texto, tablas y capturas coinciden con la aplicación actual.
- [ ] Las cifras citadas se pueden reproducir con comandos del repositorio.
- [ ] Se entrega el .docx y la lista de cambios.

## Cómo verificar

Comparar cada sección del documento con `Front/app.py` y `Back/billetes.py`.

## Relacionado

#21 (capturas) · #19 (reporte)
