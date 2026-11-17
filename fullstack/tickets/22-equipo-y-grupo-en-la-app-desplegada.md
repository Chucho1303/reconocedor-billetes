# #22 · Verificar nombres de equipo y grupo en la aplicación desplegada

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `chore` |
| **Alcance** | `front` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `chore/22-equipo-grupo` |
| **Registrado** | 2026-11-16 |

## Descripción

La pestaña «Acerca del proyecto» lee el equipo y el grupo de las variables `BILLETES_EQUIPO` y `BILLETES_GRUPO`.

## Situación actual (revisión del repositorio)

- Los valores no están en el código ni en el repositorio (solo en `Ejecucion/.env.example`).
- En Streamlit Community Cloud hay que definirlos en la configuración de secretos o variables.

## Criterios de aceptación

- [ ] Se abre la aplicación desplegada y se revisa la pestaña «Acerca del proyecto».
- [ ] Aparecen los nombres reales del equipo y el grupo.
- [ ] Si no aparecen, se configuran las variables en el despliegue y se vuelve a comprobar.
- [ ] Queda anotado dónde se configuran, sin escribir datos personales en el repositorio.

## Cómo verificar

Abrir la aplicación desplegada y mirar «Acerca del proyecto».

## Relacionado

#4 (interfaz) · #11 (variables de entorno)
