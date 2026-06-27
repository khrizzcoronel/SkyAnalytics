# Especificación de Caso de Uso: CU-O07

## 1. Nombre de la Funcionalidad
**Monitorear Telemetría de Contenedores**

## 2. Objetivo
Centralizar y visualizar métricas, logs distribuidos y trazas de rendimiento de todos los servicios en PaaS/Serverless, posibilitando la detección temprana de anomalías antes de que afecten el Uptime del sistema.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** Stack LGTM (Archivos de Log, Dashboard Básico / Sentry, Logs, Sentry / Logs), OpenTelemetry.

## 4. Contexto del Problema
Una arquitectura monolítica o serverless simple genera miles de eventos por segundo. Si un servicio de "Facturación" falla al comunicarse con el de "Inferencia ML", investigar logs sueltos en cada contenedor demora horas. El SRE necesita una vista de panel unificada con trazabilidad distribuida para aplicar resolución rápida de incidentes.

## 5. Requisitos Funcionales
*   **RF-O07-001:** Los servicios deben inyectar cabeceras de trazabilidad (TraceID, SpanID) a cada petición utilizando OpenTelemetry.
*   **RF-O07-002:** Sentry / Logs debe realizar "scrape" periódico a los endpoints `/metrics` de cada pod de PaaS/Serverless.
*   **RF-O07-003:** Archivos de Log debe centralizar los `stdout` y `stderr` de todos los contenedores con etiquetas automáticas (`namespace`, `pod`, `app`).
*   **RF-O07-004:** El dashboard (Dashboard Básico / Sentry) debe correlacionar mágicamente una petición lenta (métrica) con sus trazas correspondientes en Logs y sus logs en Archivos de Log usando un único TraceID.

## 6. Requisitos No Funcionales
*   **RNF-O07-001:** El sistema de observabilidad (Stack LGTM) debe estar desacoplado de la infraestructura principal de forma que si el cluster productivo se cae por completo, el panel de observabilidad siga accesible en otro cluster para diagnóstico.

## 7. Reglas de Negocio
*   **RN-O07-001 (Privacidad de Logs):** Los logs de la aplicación NO deben contener bajo ninguna circunstancia información de tarjetas de crédito o contraseñas en texto plano (Scrubbing).
*   **RN-O07-002 (Retención):** Logs detallados (Debug/Info) se retienen 14 días. Métricas agregadas se retienen 1 año. Trazas se retienen 7 días.

## 8. Entradas
*   Flujo constante de telemetría (gRPC/HTTP) enviada desde los Agentes OpenTelemetry instalados en los Nodos hacia los colectores.

## 9. Salidas
*   **UI:** Paneles de control de Dashboard Básico / Sentry operativos.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Diagnóstico de latencia inter-servicio
**Dado** que el Desarrollador (Tú) recibe una alerta de latencia (CU-E03) en el endpoint `/predict`
**Cuando** el SRE ingresa a Logs en Dashboard Básico / Sentry
**Entonces** busca el TraceID de la petición anómala
**Y** la cascada de trazas revela que el microservicio de "Clima" consumió 4.8 segundos esperando respuesta de una base de datos externa.

## 11. Criterios de Aceptación
*   **CA-O07-001:** Toda aplicación en el cluster que no exponga un endpoint de métricas estándar hace fallar los pipelines de despliegue de CI/CD.

## 12. Restricciones
*   Las librerías de instrumentación deben sumar menos de un 2% de latencia y uso de CPU extra a la aplicación base.

## 13. Fuera de Alcance
*   Remediación de código fuente directamente (La observabilidad solo diagnostica el error; la corrección es un desarrollo de ingeniería).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Retención de Logs:** Los registros de acceso y errores se retendrán durante **30 días** en el almacenamiento de logs, priorizando la capacidad de diagnóstico histórico sobre el ahorro extremo de costos.
