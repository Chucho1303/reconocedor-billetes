# Política de seguridad

## Reportar una vulnerabilidad
Abre un *issue* privado o escribe a los integrantes del equipo (ver pestaña "Acerca del proyecto" de la app).
No publiques detalles de la falla ni credenciales en issues o Pull Requests públicos.

## Reglas del proyecto
- Ninguna contraseña, llave de API o credencial se escribe en el código: se usan variables de entorno (`Ejecucion/.env.example`).
- Los controles automáticos (escáner de secretos, bandit, pip-audit) corren en cada cambio; detalle en `Ejecucion/docs/SEGURIDAD.md`.
