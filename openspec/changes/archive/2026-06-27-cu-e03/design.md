## Context

El SLA de SkyAnalytics garantiza un Uptime de 99.0% mensual. Esto otorga un "Error Budget" (presupuesto de error) de aproximadamente 7.3 horas al mes o 438 minutos. El Monolito Modular necesita leer métricas pre-agregadas sobre la latencia y la tasa de errores HTTP 5xx que Sentry y Promtail recolectan en background.

## Goals / Non-Goals

**Goals:**
- Mostrar un panel que indique el Uptime Global y Regional.
- Calcular y renderizar el porcentaje consumido del Error Budget (Presupuesto de Caída).
- Proveer una tabla de salud con el desglose del tráfico y errores por endpoint.
- Incorporar Refresco Automático (Polling) en el cliente.
- Permitir la exportación del SLA en PDF ocultando detalles de infraestructura (IPs, instancias) en el renderizado final.

**Non-Goals:**
- Configurar Sentry o los exporters de Prometheus.
- Proveer botones de reinicio o failover de base de datos desde la UI (fuera de alcance de la vista analítica).

## Decisions

- **Patrón de Refresco (Polling):** Utilizar `setInterval` en el Client Component (SWR o React genérico) para hacer polling a `/api/v1/estrategico/engineering/health` cada 30 segundos.
  - *Rationale:* Evita la complejidad operacional y los costos de infra de mantener conexiones persistentes (WebSockets) en arquitecturas Serverless y cumple RNF-E03-002.
- **BFF para Uptime:** La API Next.js consultará MonetDB (que a su vez está siendo rellenado con logs estructurados en el Módulo Operativo).
  - *Rationale:* Mantiene la consistencia del patrón, todas las lecturas masivas van hacia la base analítica, asegurando que la carga nunca afecta la base de datos operativa (PocketBase).
- **Sanitización del Reporte SLA:** Se aplicará una clase CSS específica `.internal-infra` con `display: none` dentro del `@media print` para ocultar columnas como "Internal Node" o "Pod IP" al exportar a PDF para el cliente final.

## Risks / Trade-offs

- **Frecuencia de Ingesta vs Polling:** Si MonetDB se actualiza cada 5 minutos, un polling de 30s mostrará datos repetidos.
  - *Mitigación:* Se asume para el MVP que los datos en `vw_uptime_telemetry` están suficientemente frescos, o se reflejará el `last_updated_at` en el UI.
