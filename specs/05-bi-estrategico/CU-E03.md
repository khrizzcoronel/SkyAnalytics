# Especificación de Caso de Uso: CU-E03

## 1. Nombre de la Funcionalidad
**Evaluar Uptime Global y Cumplimiento SLA**

## 2. Objetivo
Permitir al Desarrollador (Tú) verificar la disponibilidad del sistema (Uptime) en tiempo real a través de todas las regiones de despliegue, calcular el consumo del Error Budget y validar el cumplimiento del SLA garantizado del 99.0% (Best Effort).

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** Grafana LGTM stack (métricas de observabilidad), Grafana LGTM stack.

## 4. Contexto del Problema
SkyAnalytics promete a sus clientes Enterprise un Uptime del 99.0% (Best Effort). El incumplimiento genera penalizaciones económicas. El Desarrollador (Tú) necesita visualizar de un vistazo si la plataforma está degradada en alguna región específica (Single-region) y decidir si debe activar protocolos de emergencia o congelar nuevos despliegues.

## 5. Requisitos Funcionales
*   **RF-E03-001:** El sistema debe consultar y mostrar el Uptime global y regional en base a las métricas ingestadas por Grafana LGTM stack de los últimos 30 días.
*   **RF-E03-002:** El sistema debe calcular y mostrar el remanente del Error Budget mensual (Presupuesto total de caída: 432 minutos al mes para SLA 99.0%).
*   **RF-E03-003:** El sistema debe desglosar el cumplimiento de SLA por cada endpoint del API Gateway (REST y GraphQL).
*   **RF-E03-004:** El sistema debe permitir generar automáticamente un reporte de SLA limpio, orientado al cliente Enterprise, certificando el cumplimiento mensual.

## 6. Requisitos No Funcionales
*   **RNF-E03-001:** La integración con Grafana LGTM stack debe ser asíncrona para no bloquear el hilo principal de la UI del Desarrollador (Tú).
*   **RNF-E03-002:** El panel debe actualizarse automáticamente cada 30 segundos (Polling o WebSockets) sin requerir recarga manual de la página.

## 7. Reglas de Negocio
*   **RN-E03-001 (Error Budget Policy):** Si el consumo del Error Budget proyectado supera el 80% en el mes en curso, el sistema debe alertar visualmente al Desarrollador (Tú) para que autorice el congelamiento de despliegues (CU-O10).
*   **RN-E03-002 (Cálculo SLA):** Se consideran "caídas" los errores HTTP 5xx que superen una tasa del 1% del tráfico durante una ventana de evaluación de 1 minuto continuo.

## 8. Entradas
*   Filtros UI:
    *   `region_aws` (String: us-east-1, eu-central-1, global)
    *   `time_window` (Enum: last_24h, last_7d, last_30d, current_month)

## 9. Salidas
*   **Payload JSON:**
    *   `{ uptime_percentage, error_budget_consumed_seconds, error_budget_remaining_seconds, status_indicator }`
    *   `[ { endpoint, uptime, total_requests, errors_5xx } ]`
*   **UI:** Dashboard técnico con medidores circulares (gauges) y tablas de salud por servicio.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Verificación de salud global
**Dado** que el Desarrollador (Tú) abre el panel de SLA
**Cuando** selecciona la ventana de "Últimos 30 días"
**Entonces** el sistema consulta Grafana LGTM stack
**Y** muestra un uptime de 99.50%
**Y** el medidor de Error Budget marca "Crítico" (más del 80% consumido).

### Escenario 2: Degradación zonal detectada
**Dado** que existe una degradación en la red de la región `eu-central-1`
**Cuando** el Desarrollador (Tú) ingresa al dashboard
**Entonces** el sistema muestra el indicador global en Amarillo
**Y** al hacer drill-down, la región europea muestra errores 5xx por encima del 1%
**Y** se recomienda iniciar el failover activo-activo a la región US.

## 11. Criterios de Aceptación
*   **CA-E03-001:** Las métricas mostradas en la UI coinciden exactamente con los registros crudos de PromQL ejecutados directamente contra el cluster.
*   **CA-E03-002:** El reporte PDF generado para los clientes no expone IPs internas, nombres de nodos PaaS ni información sensible de infraestructura, solo SLAs y porcentajes.
*   **CA-E03-003:** Cuando una región supera el 1% de errores 5xx, el dashboard muestra una recomendación explícita de failover activo-activo y resalta la región degradada.

## 12. Restricciones
*   El cálculo del uptime excluye ventanas de mantenimiento programado que hayan sido previamente notificadas a los clientes.

## 13. Fuera de Alcance
*   Ejecución directa del failover o reinicio de clusters PaaS desde esta pantalla (Esta pantalla es analítica, las acciones operativas se hacen vía Terraform / IaC).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Logs:** Retención obligatoria de 30 días.

