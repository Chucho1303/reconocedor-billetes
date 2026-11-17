# #23 · Probar la lectura en voz alta con un lector de pantalla real

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `test` |
| **Alcance** | `front` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `test/23-lector-pantalla` |
| **Registrado** | 2026-11-16 |

## Descripción

Cerrar el pendiente del ticket #14: la accesibilidad todavía no se probó con TalkBack ni VoiceOver.

## Situación actual (revisión del repositorio)

- La interfaz declara compatibilidad con lectores de pantalla, pero no hay una prueba registrada.

## Criterios de aceptación

- [ ] Prueba en Android con TalkBack y en iOS/macOS con VoiceOver (o la que haya disponible).
- [ ] Se verifica que el resultado se anuncia (`role="status"`) y que el botón «Escuchar resultado» es operable.
- [ ] Se anota navegador, sistema y resultado.
- [ ] Los problemas encontrados se registran como tickets nuevos.

## Cómo verificar

Seguir los pasos en un teléfono real y llenar una tabla con lo observado.

## Relacionado

#14 (voz) · #24 (móviles)
