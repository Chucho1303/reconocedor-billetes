# #14 · Lectura en voz alta del resultado (accesibilidad)

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `feat` |
| **Alcance** | `front` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `feat/14-lectura-voz` |

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

## Relacionado

#4 (interfaz)
