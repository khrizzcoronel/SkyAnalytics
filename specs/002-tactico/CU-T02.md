# Especificación de Caso de Uso: CU-T02

## 1. Nombre de la Funcionalidad
**Configurar y Publicar API en RapidAPI**

## 2. Objetivo
Gestionar el ciclo de vida de publicación, versionado y empaquetado (pricing plans) de la API predictiva de SkyAnalytics en el marketplace RapidAPI, facilitando la monetización y descubrimiento por desarrolladores externos.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** RapidAPI Platform, Gateway simplificado API Gateway.

## 4. Contexto del Problema
Para escalar mediante ecosistemas de APIs, SkyAnalytics requiere exponer sus modelos de Machine Learning (retrasos, clima) como endpoints públicos monetizables. Publicar en RapidAPI permite derivar la gestión de facturación a la plataforma, pero requiere configuración de rate limits y validación de tokens de acceso (`X-RapidAPI-Key`).

## 5. Requisitos Funcionales
*   **RF-T02-001:** El sistema debe proveer un endpoint de validación (`/auth/rapidapi`) que verifique la autenticidad de las peticiones ruteadas por los proxies de RapidAPI usando el secreto compartido.
*   **RF-T02-002:** El API Gateway interno (Gateway simplificado) debe sincronizar los contadores de Rate Limit locales con las cuotas asignadas en el plan de RapidAPI (Freemium, Pro, Ultra).
*   **RF-T02-003:** El sistema debe exportar automáticamente las especificaciones OpenAPI 3.1 en un formato 100% compatible para su importación en el portal de RapidAPI ante cada nueva versión.
*   **RF-T02-004:** El panel interno debe consolidar y mostrar las analíticas de uso delegadas por RapidAPI (llamadas, latencia percibida por el proxy, facturación estimada).

## 6. Requisitos No Funcionales
*   **RNF-T02-001:** La validación de la autenticidad del proxy (RapidAPI Proxy Secret Validation) debe resolverse en menos de 10 milisegundos para no añadir latencia significativa a la llamada real de la API.
*   **RNF-T02-002:** Alta disponibilidad requerida en el endpoint de autenticación delegada, ya que si falla, ninguna petición del marketplace será procesada.

## 7. Reglas de Negocio
*   **RN-T02-001 (Planes de Monetización Típicos):**
    *   *Freemium:* 1,000 peticiones / mes.
    *   *Pro:* 10,000 peticiones / mes. Hard Limit.
*   **RN-T02-002 (Caché):** Para llamadas idénticas de datos históricos (ej. clima del mes pasado), el Gateway debe cachear la respuesta por 1 hora, independientemente de quién llame desde RapidAPI, para ahorrar cómputo interno.

## 8. Entradas
*   Peticiones HTTP entrantes con cabeceras `X-RapidAPI-Proxy-Secret` y `X-RapidAPI-User`.
*   Archivo `openapi.json` validado (Artifact del CI/CD).

## 9. Salidas
*   **Respuestas API:** Códigos de estado estándar (200 OK, 429 Too Many Requests, 401 Unauthorized).
*   **Archivos:** `rapidapi-spec-v1.json` para subida.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Validación exitosa de llamada a través de RapidAPI
**Dado** que un desarrollador tercero llama al endpoint `/v1/flight/delay-prediction` a través de RapidAPI
**Cuando** la petición llega al API Gateway de SkyAnalytics con las cabeceras secretas correctas
**Entonces** el Gateway valida el secreto en $\leq$ 10 ms
**Y** registra el consumo contra el usuario de RapidAPI
**Y** enruta la petición al microservicio interno de Machine Learning.

### Escenario 2: Intento de bypass del Proxy
**Dado** que un atacante descubre la IP pública del API Gateway
**Cuando** intenta consumir un endpoint mandando cabeceras falsas o omitiendo `X-RapidAPI-Proxy-Secret`
**Entonces** el Gateway rechaza inmediatamente la petición con un `401 Unauthorized`
**Y** no procesa ninguna lógica de negocio para proteger la infraestructura.

## 11. Criterios de Aceptación
*   **CA-T02-001:** El linter Spectral del CI/CD debe fallar si la especificación OpenAPI contiene parámetros incompatibles con el importador de RapidAPI.
*   **CA-T02-002:** El rate limiting implementado localmente debe concordar con el rate limiting del plan configurado en RapidAPI para prevenir facturación excesiva o fugas de cómputo.

## 12. Restricciones
*   La facturación directa de estos usuarios es gestionada 100% por RapidAPI, SkyAnalytics no almacena tarjetas de crédito de estos clientes.

## 13. Fuera de Alcance
*   Soporte técnico de nivel 1 a clientes que no pueden pagar en RapidAPI.

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Retención de Logs:** Los registros de acceso y errores se retendrán durante **30 días** en el almacenamiento de logs, priorizando la capacidad de diagnóstico histórico sobre el ahorro extremo de costos.
