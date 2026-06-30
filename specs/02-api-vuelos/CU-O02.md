# Especificación de Caso de Uso: CU-O02

## 1. Nombre de la Funcionalidad
**Consultar Datos de Vuelo vía API**

## 2. Objetivo
Proveer un endpoint de alto rendimiento para que clientes corporativos consulten información consolidada y predicciones de vuelos mediante APIs REST y GraphQL, asegurando cuotas de consumo, caché y seguridad perimetral.

## 3. Actores Involucrados
*   **Actor Principal:** Cliente B2B (Sistema Máquina-a-Máquina / Desarrollador)
*   **Sistemas Externos / Actores Secundarios:** API Gateway (Gateway simplificado), Redis (Caché), Microservicio Predictivo.

## 4. Contexto del Problema
Las aerolíneas y agencias necesitan consultar el estado de vuelos y las predicciones de retrasos en tiempo real para alimentar sus propias pantallas (FIDS) o sistemas de reservas. Esta API recibe tráfico masivo. Si no hay control de cuotas (Rate Limiting) o la latencia es alta, la plataforma colapsará.

## 5. Requisitos Funcionales
*   **RF-O02-001:** El API Gateway debe interceptar todas las peticiones y validar la existencia y validez de la cabecera `Authorization: Bearer <API_KEY>` o `x-api-key`.
*   **RF-O02-002:** El sistema debe identificar el `Tenant` asociado a la llave y aplicar la política de Rate Limiting correspondiente a su plan de suscripción.
*   **RF-O02-003:** El sistema debe responder peticiones idénticas frecuentes utilizando una capa de caché en memoria (Redis) sin tocar el backend transaccional.
*   **RF-O02-004:** El sistema debe inyectar las cabeceras estándar de rate limit en la respuesta HTTP (`X-RateLimit-Limit`, `X-RateLimit-Remaining`).
*   **RF-O02-005:** El backend (microservicio) debe procesar la consulta, invocar al modelo ML si se pide predicción, y retornar los datos en formato JSON según el contrato OpenAPI.

## 6. Requisitos No Funcionales
*   **RNF-O02-001 (Latencia):** El tiempo de respuesta total (p95) para consultas almacenadas en caché debe ser $\leq$ 50ms; para consultas de inferencia ML en vivo debe ser $\leq$ 300ms.
*   **RNF-O02-002 (Concurrencia):** La arquitectura monolítica o serverless simple (PaaS HPA) debe escalar automáticamente para soportar picos de 5,000 requests per second (RPS).

## 7. Reglas de Negocio
*   **RN-O02-001 (Comportamiento de Cuota Excedida):** Si un Tenant sobrepasa su límite de plan, el Gateway debe rechazar inmediatamente con `HTTP 429 Too Many Requests`.
*   **RN-O02-002 (Caché Predictiva):** Las predicciones de vuelos que despegan en más de 24 horas se cachean por 1 hora. Vuelos que despegan en menos de 2 horas se cachean por solo 5 minutos.

## 8. Entradas
*   Request HTTP GET `/v1/flights/{flight_id}`.
*   Query Params: `include_prediction=true`, `lang=es`.
*   Cabeceras: `x-api-key`.

## 9. Salidas
*   **Payload JSON:**
    *   Datos del vuelo: origen, destino, aerolínea, horario programado, horario estimado.
    *   Predicción (si se solicita): probabilidad de retraso (%), minutos de retraso estimados.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Consulta de API exitosa con Caché (Hit)
**Dado** que un sistema cliente consulta el vuelo `AA123` con un API Key válida
**Cuando** la petición llega al Gateway
**Entonces** el Gateway valida el rate limit restante
**Y** encuentra la respuesta en Redis (Caché Hit)
**Y** retorna la respuesta `HTTP 200 OK` en 15 milisegundos junto con las cabeceras de `X-RateLimit-Remaining`.

### Escenario 2: Bloqueo por cuota de plan excedida (Hard Limit)
**Dado** que un Tenant con plan Freemium ha consumido 1,000 peticiones en el mes
**Cuando** intenta realizar la petición número 1,001
**Entonces** el API Gateway corta la petición en el perímetro (Edge)
**Y** retorna el código `429 Too Many Requests`
**Y** el payload indica "Monthly quota exceeded. Upgrade to Pro plan."

## 11. Criterios de Aceptación
*   **CA-O02-001:** Las peticiones rechazadas por Rate Limit (429) no deben generar consumo de CPU en los servicios internos ni ser contabilizadas como "Errores 5xx" para el Error Budget del SRE.
*   **CA-O02-002:** Un token revocado en el panel de control debe perder acceso de inmediato (TTL de propagación al Edge $\leq$ 5 segundos).

## 12. Restricciones
*   El endpoint no permite escaneo masivo (Scraping). La paginación en endpoints de lista (`/v1/flights`) está limitada forzosamente a un máximo de 100 resultados por página.

## 13. Fuera de Alcance
*   Webhooks push para cambios de estado de vuelo (Este caso de uso es puramente Pull/REST. El modelo asíncrono se manejará en otro endpoint).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Rate Limiting:** Se aplicará un **Soft Limit** temporal (bloqueo por 1 hora) al exceder las cuotas, permitiendo a los testers seguir probando tras el enfriamiento, en lugar de un bloqueo permanente mensual.
