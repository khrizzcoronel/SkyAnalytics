# Especificación de Caso de Uso: CU-T01

## 1. Nombre de la Funcionalidad
**Gestionar Campañas de Growth Hacking**

## 2. Objetivo
Diseñar, ejecutar y monitorear campañas automatizadas de marketing orientadas a la captación acelerada de Beta Testers (Growth Hacking) para la plataforma SkyAnalytics, segmentando por industria (aerolínea, logística, agencia).

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** HubSpot (CRM & Marketing Automation), Google Analytics.

## 4. Contexto del Problema
Para alcanzar el objetivo estratégico de penetración digital (50 Beta Testers activos en Q4), el equipo de marketing debe ejecutar campañas experimentales de rápida iteración. Se requiere integrarse con herramientas de terceros (HubSpot) y rastrear las tasas de conversión desde el clic hasta la creación de la cuenta (Tenant) en la plataforma SaaS.

## 5. Requisitos Funcionales
*   **RF-T01-001:** El sistema debe integrarse bidireccionalmente con la API de HubSpot para sincronizar los leads capturados en la Landing Page con el CRM en tiempo real.
*   **RF-T01-002:** El sistema debe registrar un evento de conversión (`ACCOUNT_CREATED`) y enviarlo al webhook de HubSpot cada vez que un lead finaliza el registro de Tenant (CU-O01).
*   **RF-T01-003:** El panel interno debe mostrar métricas de A/B Testing, cruzando el origen del lead (UTM tags) con el LTV proyectado de ese lead.
*   **RF-T01-004:** El sistema debe calcular y mostrar el Costo de Adquisición de Clientes (CAC) por campaña en base a la inversión publicitaria ingresada.

## 6. Requisitos No Funcionales
*   **RNF-T01-001:** La sincronización de leads hacia HubSpot no debe bloquear el flujo de registro del usuario (procesamiento asíncrono vía colas o workers).
*   **RNF-T01-002:** El rastreo de eventos (Tracking) debe cumplir estrictamente con las políticas de privacidad y consentimiento de cookies (GDPR/CCPA).

## 7. Reglas de Negocio
*   **RN-T01-001 (Lead Scoring):** Cualquier registro proveniente de una cuenta de correo corporativa que contenga las palabras "airlines", "cargo" o "logistics" recibe automáticamente un multiplicador x2 en su lead score.
*   **RN-T01-002 (Cálculo de CAC de Campaña):** `Presupuesto gastado en la campaña / Total de Tenants activados atribuibles a los UTM de la campaña`.

## 8. Entradas
*   Variables de UTM (Query params capturados en frontend: `utm_source`, `utm_medium`, `utm_campaign`).
*   Payload de webhook de HubSpot (cuando el lead entra a una automatización).

## 9. Salidas
*   **Payload JSON:** Evento asíncrono de conversión enviado al CRM.
*   **UI:** Dashboard analítico de rendimiento de campaña (Tasas de apertura, CTR, CVR).

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Atribución exitosa de conversión
**Dado** que un usuario ingresa a la landing page a través de un enlace con `utm_campaign=beta_launch_europe`
**Y** completa el formulario de registro de Tenant
**Cuando** el sistema crea la cuenta en la base de datos
**Entonces** dispara un evento asíncrono a HubSpot
**Y** marca el origen del contacto como `beta_launch_europe`
**Y** actualiza la tasa de conversión de la campaña en el panel del Desarrollador (Tú).

## 11. Criterios de Aceptación
*   **CA-T01-001:** Un registro masivo de 500 leads simultáneos no degrada el rendimiento de la API principal, encolando correctamente las peticiones a HubSpot.
*   **CA-T01-002:** Si la API de HubSpot cae, el sistema debe reintentar el envío del evento de conversión (Retry pattern con Exponential Backoff).

## 12. Restricciones
*   SkyAnalytics no envía correos de marketing directamente; toda la automatización de correos se delega estrictamente en HubSpot.

## 13. Fuera de Alcance
*   Creación visual de landing pages (Se hacen directamente en CMS / Webflow / HubSpot).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Rate Limiting:** Se aplicará un **Soft Limit** temporal (bloqueo por 1 hora) al exceder las cuotas, permitiendo a los testers seguir probando tras el enfriamiento, en lugar de un bloqueo permanente mensual.
