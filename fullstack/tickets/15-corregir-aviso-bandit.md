# #15 · Corregir el aviso de bandit (B110) que deja el CI en rojo

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `fix` |
| **Alcance** | `front` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `fix/15-aviso-bandit` |
| **Registrado** | 2026-11-16 |

## Descripción

El job **Seguridad, dependencias y licencias** falla en `main` por `bandit`, y por eso los jobs de Docker y de publicación se omiten.

## Situación actual (revisión del repositorio)

- `bandit` reporta B110 (`try/except/pass`) en `Front/app.py`, en el bloque que evita que el navegador traduzca «$20» a «20 dólares».
- El fallo ya existía antes de los tickets: se reproduce sobre `main` sin cambios.

## Criterios de aceptación

- [ ] El bloque registra o acota el error (`except Exception` con aviso, o `# nosec B110` con justificación escrita).
- [ ] `bandit -q -c Ejecucion/bandit.yaml -r Back Front Ejecucion/scripts Ejecucion/Iniciar_Visual_Studio.py` termina sin hallazgos.
- [ ] El job `security` del CI queda en verde y el job `docker` deja de omitirse.
- [ ] La traducción automática del navegador sigue sin convertir «$20» en dólares.

## Cómo verificar

```bash
bandit -q -c Ejecucion/bandit.yaml -r Back Front Ejecucion/scripts Ejecucion/Iniciar_Visual_Studio.py
```

## Relacionado

#8 (CI) · #11 (seguridad)
