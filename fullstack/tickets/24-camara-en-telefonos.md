# #24 · Probar la cámara de la aplicación en teléfonos

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `test` |
| **Alcance** | `front` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `test/24-camara-moviles` |
| **Registrado** | 2026-11-16 |

## Descripción

El modo «Usar cámara» necesita permiso del navegador y conexión segura (https).

## Situación actual (revisión del repositorio)

- No hay constancia de pruebas de la cámara en teléfonos ni de qué navegadores funcionan.

## Criterios de aceptación

- [ ] Prueba en al menos un Android (Chrome) y un iPhone (Safari).
- [ ] Se anota si pide permiso, si toma la foto y si el resultado es correcto.
- [ ] Los fallos se documentan en la tabla de problemas del reporte.

## Cómo verificar

Abrir la aplicación desplegada en cada teléfono y usar «Usar cámara».

## Relacionado

#4 (interfaz) · #20 (documento)
