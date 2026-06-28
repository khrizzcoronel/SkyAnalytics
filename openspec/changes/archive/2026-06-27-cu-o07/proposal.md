## Why
El sistema genera miles de eventos por segundo. Necesitamos observabilidad (Logs, Métricas, Trazas) con OpenTelemetry para poder diagnosticar caídas y latencias rápidamente sin perdernos en logs desconectados.

## What Changes
- Simulación de inyección de telemetría (OpenTelemetry Stub).
- Creación de un logger centralizado en `backend/src/telemetry/`.

## Capabilities
- `telemetry-tracer`: Generación de TraceID y SpanID.
- `centralized-logger`: Escritura de logs estructurados simulando scrubbing de PII.
