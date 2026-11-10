# #7 · Despliegue repetible con Docker

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `build` |
| **Alcance** | `docker` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `build/7-docker` |

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

## Relacionado

#8 (el CI construye y prueba la imagen) · #11 (variables de entorno)
