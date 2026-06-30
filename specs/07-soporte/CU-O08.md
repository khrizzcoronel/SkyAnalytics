# Especificación de Caso de Uso: CU-O08

## 1. Nombre de la Funcionalidad
**Atender Ticket de Bug**

## 2. Objetivo
Gestionar, clasificar, diagnosticar y resolver reportes de errores (bugs) provenientes de usuarios finales o sistemas automáticos, asegurando el cumplimiento estricto del tiempo medio de resolución (MTTR) acordado en los SLAs.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Desarrollador L3
*   **Sistemas Externos / Actores Secundarios:** Sistema de Gestión de Tickets (GitHub Issues / GitHub Issues), Slack, GitHub.

## 4. Contexto del Problema
Cuando una agencia de viajes reporta que un endpoint le retorna `500 Internal Server Error`, cada minuto que pasa daña la reputación corporativa de SkyAnalytics. Un Desarrollador (Tú) debe triar el problema, reproducirlo e involucrar al equipo de desarrollo adecuado sin causar cuellos de botella.

## 5. Requisitos Funcionales
*   **RF-O08-001:** El sistema de soporte debe crear un Ticket asignándole un Nivel de Severidad (S1 a S4) basado en palabras clave y tipo de cliente (Freemium vs Enterprise).
*   **RF-O08-002:** El sistema debe sincronizar el Ticket con el tablero de ingeniería (GitHub Issues) bidireccionalmente.
*   **RF-O08-003:** El sistema debe requerir que el desarrollador asocie un `Pull Request` al Ticket antes de permitirle cambiar su estado a `Done/Resolved`.
*   **RF-O08-004:** El sistema debe notificar al cliente vía portal de desarrolladores o correo electrónico cuando su bug pase a estado "En Despliegue" y "Resuelto".

## 6. Requisitos No Funcionales
*   **RNF-O08-001:** El sistema de tickets debe contar con una disponibilidad garantizada del 99.9%, alojado externamente (SaaS) para evitar que una caída interna bloquee la recepción de quejas.

## 7. Reglas de Negocio
*   **RN-O08-001 (Tiempos de Respuesta - SLAs):** 
    *   *Enterprise:* Primera respuesta $\leq$ 30 mins; Resolución Bug Crítico $\leq$ 4 horas.
    *   *Pro:* Primera respuesta $\leq$ 4 horas.
    *   *Freemium:* Respuesta *Best-effort*.
*   **RN-O08-002 (Escalamiento):** Si un Ticket marcado como "Bloqueador" supera el tiempo límite del SLA, el sistema escala automáticamente notificando al Desarrollador (Tú) en Slack.

## 8. Entradas
*   Reportes de usuarios (Formulario de soporte) que contienen: `TenantID`, `Endpoint`, `Payload utilizado`, y `Comportamiento esperado`.

## 9. Salidas
*   **Status Update:** Notificaciones en la plataforma de tickets.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Triage y resolución de bug de cliente Enterprise
**Dado** que un cliente Enterprise abre un ticket reportando que el endpoint predictivo le da error de deserialización
**Cuando** el ticket se registra
**Entonces** el sistema etiqueta el ticket como S1 (Critical) y dispara una alerta al canal `#support-escalations`
**Y** el Desarrollador asignado genera un parche en GitHub en 2 horas
**Y** al fusionar (Merge) el PR referenciando "Fixes #1043", el ticket se cierra automáticamente notificando al cliente el arreglo.

## 11. Criterios de Aceptación
*   **CA-O08-001:** Todo ticket debe incluir forzosamente los pasos de reproducción antes de ser transicionado al equipo de Ingeniería. Si faltan datos, el Desarrollador (Tú) lo devuelve al cliente.

## 12. Restricciones
*   El personal de soporte no tiene acceso directo (SSH/RDP) a las bases de datos transaccionales para resolver bugs (Zero Trust). Toda corrección se hace vía código.

## 13. Fuera de Alcance
*   Desarrollo de nuevas funcionalidades solicitadas por el cliente (Feature Requests). Estas son redirigidas al Product Manager (CU-E05/Tácticos).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Rate Limiting:** Se aplicará un **Soft Limit** temporal (bloqueo por 1 hora) al exceder las cuotas, permitiendo a los testers seguir probando tras el enfriamiento, en lugar de un bloqueo permanente mensual.
