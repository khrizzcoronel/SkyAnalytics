## Context
Necesitamos simular la generación de logs con TraceID para correlacionar eventos.

## Decisions
- Utilizaremos el módulo nativo `logging` de Python configurado para emitir JSON.
- Implementaremos una función `get_trace_id()` para simular el paso de contexto (OpenTelemetry).
- **Regla RN-O07-001 (Privacidad):** Enmascararemos campos sensibles (como contraseñas o tarjetas) antes de loggear.
