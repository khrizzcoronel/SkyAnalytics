# Especificación de Caso de Uso: CU-O13

## 1. Nombre de la Funcionalidad
**Realizar Post-Mortem de Incidente**

## 2. Objetivo
Fomentar una cultura de mejora continua y transparencia ("Blameless Culture") mediante la documentación estructurada de incidentes graves (Sev1/Sev2), analizando la causa raíz (Root Cause) y definiendo acciones correctivas para prevenir su repetición.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Líder del Incidente
*   **Sistemas Externos / Actores Secundarios:** Notion / Confluence (Base de conocimiento), Notificaciones de Slack, GitHub Issues (Tickets de seguimiento).

## 4. Contexto del Problema
Cuando ocurre una caída masiva, restaurar el servicio es solo la primera mitad del trabajo. Si no se investiga el porqué (Causa Raíz), el mismo error ocurrirá nuevamente la semana siguiente. Para cumplir con las métricas de madurez de ingeniería (DORA) y políticas SOC 2, todo incidente que viole el SLA debe ser auditado.

## 5. Requisitos Funcionales
*   **RF-O13-001:** El sistema (Notificaciones de Slack) debe generar automáticamente una plantilla de documento Post-Mortem en Notion/Confluence tan pronto como un incidente Sev1 o Sev2 se marca como `Resolved`.
*   **RF-O13-002:** La plantilla debe incluir pre-poblada la cronología del incidente (Timeline) extraída de los chats de Slack y alertas del sistema.
*   **RF-O13-003:** El equipo involucrado debe completar la sección de "Causa Raíz" utilizando la metodología de los "5 Porqués" (5 Whys).
*   **RF-O13-004:** El sistema debe obligar a que se creen tickets de acción correctiva (Action Items) vinculados al documento, asignados en el gestor de tareas (GitHub Issues/GitHub Issues) antes de poder cerrar el Post-Mortem.

## 6. Requisitos No Funcionales
*   **RNF-O13-001 (Tiempos):** Un documento Post-Mortem debe completarse y ser aprobado formalmente en un plazo máximo de 72 horas hábiles luego de cerrado el incidente.

## 7. Reglas de Negocio
*   **RN-O13-001 (Blameless Culture):** Está estrictamente prohibido utilizar nombres propios o culpar a individuos específicos en el documento (ej. "El error fue porque Juan borró la tabla"). Se debe usar lenguaje sistémico (ej. "El sistema permitió que un comando destructivo se ejecutara sin confirmación secundaria").
*   **RN-O13-002 (Aprobación):** El cierre oficial de un Post-Mortem de grado Sev1 requiere la firma/revisión del Desarrollador (Tú).

## 8. Entradas
*   Transcripciones del canal de Slack de respuesta a incidentes (`#incident-xyz`).
*   Métricas de Dashboard Básico / Sentry y Logs de Archivos de Log al momento de la falla.

## 9. Salidas
*   **Documento Oficial:** Post-Mortem finalizado en Notion.
*   **Tickets generados:** Action Items en GitHub Issues/GitHub Issues para el próximo Sprint.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Generación y completitud de un Post-Mortem
**Dado** que se acaba de resolver una caída de base de datos de 20 minutos (Sev1)
**Cuando** el Incident Commander marca el incidente como resuelto en Notificaciones de Slack
**Entonces** se crea automáticamente la página de Post-Mortem en Notion con el Timeline de eventos
**Y** el equipo se reúne, documenta que la causa raíz fue un script de migración sin timeout
**Y** crea un Action Item en GitHub Issues para añadir "Timeouts por defecto en todas las migraciones"
**Y** el Desarrollador (Tú) aprueba el documento, cerrando el ciclo.

## 11. Criterios de Aceptación
*   **CA-O13-001:** Los Action Items generados a raíz del Post-Mortem deben heredar automáticamente un nivel de prioridad P1 (Bloqueador) y entrar al inicio del backlog del siguiente sprint (CU-O15).

## 12. Restricciones
*   Los documentos de Post-Mortem son confidenciales (uso interno). Si el incidente afectó a clientes externos, se generará a partir del Post-Mortem un *Public RCA (Root Cause Analysis)* con lenguaje filtrado para publicar en la página de Status.

## 13. Fuera de Alcance
*   Atención y respuesta en vivo al incidente. (El Post-Mortem inicia *después* de que el fuego se ha apagado).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Comunicación de Incidentes:** Ante caídas o mantenimientos, el sistema actualizará una **Status Page estática** y enviará un **Correo electrónico automático** a todos los usuarios registrados para mantener transparencia proactiva.
