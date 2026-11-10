# #7 · Despliegue repetible con Docker

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `build` |
| **Alcance** | `docker` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `build/7-docker` |
| **Registrado** | 2026-11-10 (retroactivo) |
| **Trabajo realizado** | 2026-11-09 a 2026-11-10 |

## Descripción

Empaquetar la aplicación en una imagen para que se ejecute igual en cualquier máquina o servidor.

## Criterios de aceptación

- [x] `Ejecucion/Dockerfile` usa `python:3.12-slim` y se construye desde la raíz del repo.
- [x] Las dependencias se instalan antes que el código para aprovechar la caché de capas.
- [x] La aplicación corre con un usuario sin privilegios (UID 10001), no como root.
- [x] La imagen expone el puerto 8501 y define un `HEALTHCHECK` sobre `/_stcore/health`.
- [x] `Ejecucion/docker-compose.yml` levanta el servicio con un solo comando, lee `Ejecucion/.env` (opcional) y usa `no-new-privileges`.
- [x] Existe `Dockerfile.dockerignore` para no copiar archivos innecesarios.

## Cómo verificar

```bash
docker compose -f Ejecucion/docker-compose.yml up --build    # http://localhost:8501
```

## Historial en el repositorio

Fechas tomadas de los commits reales de `main` (`git log`). El ticket se registró después del trabajo.

| Fecha | Commit | Autor | Qué se hizo |
|---|---|---|---|
| 2026-11-09 | `f63e74f` | Jesus Perez Estrada | build(docker): agrega Dockerfile y docker-compose para despliegue repetible (#7) |
| 2026-11-10 | `40730f8` | Jesus Perez Estrada | build(docker): endurece Dockerfile y agrega hadolint al CI (#7) |

## Relacionado

#8 (el CI construye y prueba la imagen) · #11 (variables de entorno)
