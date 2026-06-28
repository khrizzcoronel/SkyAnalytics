## Why

Para cumplir con los Acuerdos de Nivel de Servicio (SLA) del 99.0% para clientes Enterprise, el Desarrollador (Tú) requiere monitorear la salud técnica de la plataforma en tiempo real (Latencia, Uptime, Error Budget). La falta de un dashboard centralizado retrasa la toma de decisiones críticas como activar fallbacks o congelar despliegues.

## What Changes

- **Monitoreo Global y Zonal**: Panel con porcentaje de Uptime e indicador visual del consumo del Error Budget mensual (~4.38 min disponibles).
- **Desglose de Endpoints**: Tabla mostrando la tasa de errores HTTP 5xx y tráfico por servicio/API Gateway.
- **Exportación SLA**: Reporte PDF orientado al cliente (sin exponer infraestructura interna) que certifica el cumplimiento del mes.
- **Alertas Visuales**: Alerta roja si el Error Budget proyectado supera el 80% o si la tasa de errores en un minuto supera el 1%.

## Capabilities

### New Capabilities
- `sre-dashboard`: Visualización técnica en tiempo real con componentes tipo Gauge para el Error Budget y tablas de salud por servicio.
- `sla-pdf-report`: Versión del reporte PDF sanitizada (sin IPs ni nodos internos) diseñada para ser enviada a los clientes Enterprise.

### Modified Capabilities
- 

## Impact

- **Frontend**: Nueva vista `/dashboard/engineering` y componentes de medidor (Gauges).
- **Backend**: Nueva ruta API en el BFF (`/api/v1/estrategico/engineering/health`) conectada a MonetDB (`vw_uptime_telemetry`).
- **Lógica de Refresco**: Implementación de Auto-Refresh (Polling cada 30s) en el frontend.
