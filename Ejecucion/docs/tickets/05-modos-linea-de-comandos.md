# #5 · Modos de línea de comandos: registrar, imagen, cámara y evaluar

| Campo | Valor |
|---|---|
| **Estado** | Hecho |
| **Tipo** | `feat` |
| **Alcance** | `back` |
| **Responsable** | _por asignar_ |
| **Rama sugerida** | `feat/5-modos-cli` |

## Descripción

Exponer el motor mediante una CLI (`Back/billetes.py`) con cuatro subcomandos.

## Criterios de aceptación

- [x] `registrar --den {20|50|100|200|500|1000} [--imagen …] [--camara N]` guarda plantillas desde fotos o cámara.
- [x] `imagen RUTA [--salida ARCHIVO]` clasifica una foto y opcionalmente guarda la imagen anotada.
- [x] `camara [--camara N]` reconoce en vivo con la cámara.
- [x] `evaluar CARPETA [--csv ARCHIVO]` calcula la exactitud sobre fotos etiquetadas en subcarpetas `20`, `50`, `100`, … y opcionalmente guarda el detalle por imagen.
- [x] Una denominación inválida en `--den` es rechazada por el argumento.

## Cómo verificar

```bash
python Back/billetes.py imagen "Front/ejemplos/50 pesos.jpeg"
python Back/billetes.py evaluar Back/plantillas --csv resultado.csv
```

## Relacionado

#2 (motor) · #6 (`registrar_plantilla.bat`)
