# #14 · Lectura en voz alta del resultado (accesibilidad)

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `feat` |
| **Alcance** | `front` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `feat/14-lectura-voz` |
| **Registrado** | 2026-11-10 (retroactivo) |
| **Trabajo realizado** | 2026-11-10 |

## Descripción

Leer el resultado en voz alta para que personas ciegas o con baja visión puedan usar la aplicación. Este ticket se
agrega porque la funcionalidad ya está en `main` y la regla de `CONTRIBUTING.md` pide que toda funcionalidad
tenga tarea en el backlog.

## Criterios de aceptación

- [x] El resultado se lee con la voz del navegador (`speechSynthesis`), sin instalar nada.
- [x] Hay un botón **🔊 Escuchar resultado** con `aria-label`, porque algunos navegadores bloquean la voz automática hasta que la persona toca la pantalla.
- [x] La interfaz informa del servicio en la descripción y en la pestaña «Acerca del proyecto».
- [x] Se indica compatibilidad con lectores de pantalla (TalkBack, VoiceOver).

## Pendiente (no bloquea el cierre)

- [ ] Probar con un lector de pantalla real y registrar el resultado.

## Cómo verificar

```bash
streamlit run Front/app.py
```

Subir una foto, esperar el resultado y pulsar **Escuchar resultado**.

## Historial en el repositorio

Fechas tomadas de los commits reales de `main` (`git log`). El ticket se registró después del trabajo.

| Fecha | Commit | Autor | Qué se hizo |
|---|---|---|---|
| 2026-11-10 | `a8930b8, bdf907e, 82b76cb` | Chucho1303 | Update app.py (x2); Implement voice reading for recognition results |

## Relacionado

#4 (interfaz)
