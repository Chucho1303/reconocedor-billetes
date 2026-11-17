# #26 · Proteger la rama main y exigir revisión del CI

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `chore` |
| **Alcance** | `repo` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `chore/26-proteger-main` |
| **Registrado** | 2026-11-16 |

## Descripción

GitHub avisa que `main` no está protegida: se puede subir o borrar sin revisión.

## Situación actual (revisión del repositorio)

- `main` no tiene reglas de protección.
- El CI existe (commits, pruebas, seguridad, Docker) pero no es obligatorio.

## Criterios de aceptación

- [ ] Regla de rama para `main`: exigir Pull Request antes de fusionar.
- [ ] Exigir que pasen los checks de commits y pruebas.
- [ ] Bloquear el borrado y el push forzado.
- [ ] Se documenta en `.github/CONTRIBUTING.md`.

## Cómo verificar

Intentar un push directo a `main` y comprobar que se rechaza.

## Relacionado

#8 (CI) · #9 (commits) · #15 (bandit)
