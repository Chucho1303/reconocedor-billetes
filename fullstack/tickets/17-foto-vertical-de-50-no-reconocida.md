# #17 · Foto vertical de $50 aparece como «No reconocido»

| Campo | Valor |
|---|---|
| **Estado** | Pendiente |
| **Tipo** | `fix` |
| **Alcance** | `back` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `fix/17-foto-vertical-50` |
| **Registrado** | 2026-11-16 |

## Descripción

El billete en posición vertical no se reconoce aunque `segmentar` intenta girarlo.

## Situación actual (revisión del repositorio)

- `Front/ejemplos/billete_50_vertical.jpg` termina como «No reconocido».
- La prueba actual acepta `None` o 50 para esta foto, así que el defecto no se detecta.

## Criterios de aceptación

- [ ] Se identifica por qué falla (orientación del recorte, giro de 90°/270° o segmentación).
- [ ] La foto se reconoce como $50 con confianza ≥ umbral de aceptación.
- [ ] La prueba exige exactamente 50 (no `None`).
- [ ] Una foto horizontal del mismo billete mantiene su resultado.

## Cómo verificar

```bash
python Back/billetes.py imagen Front/ejemplos/billete_50_vertical.jpg
```

## Relacionado

#2 (motor) · #12 (pruebas)
