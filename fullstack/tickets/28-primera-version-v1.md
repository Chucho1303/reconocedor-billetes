# #28 · Publicar la primera versión (v1.0.0) y la imagen de Docker

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `build` |
| **Alcance** | `ci` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `build/28-version-1` |
| **Registrado** | 2026-11-16 |

## Descripción

El job `publish` del CI solo corre con tags `vX.Y.Z`, y el repositorio todavía no tiene ninguno.

## Situación actual (revisión del repositorio)

- GitHub muestra 0 tags y 0 releases.
- Mientras el job de seguridad esté en rojo, `docker` se omite y `publish` no puede ejecutarse.

## Criterios de aceptación

- [ ] Se corrige el aviso de bandit (#15) y el CI queda en verde.
- [ ] Se crea el tag `v1.0.0` desde `main`.
- [ ] El job `publish` sube la imagen a GitHub Container Registry.
- [ ] Se crea el release con notas de cambios.

## Cómo verificar

Ver la pestaña **Actions** y la sección **Packages** del repositorio.

## Relacionado

#7 (Docker) · #8 (CI) · #15 (bandit)
