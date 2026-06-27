# Especificación de Caso de Uso: CU-O15

## 1. Nombre de la Funcionalidad
**Gestionar Sprint en GitHub Issues**

## 2. Objetivo
Planificar, asignar y dar seguimiento al ciclo de desarrollo iterativo (Sprint/Ciclo) del equipo de ingeniería utilizando la herramienta de gestión ágil (GitHub Issues), asegurando que el trabajo táctico esté alineado a las metas estratégicas (OKRs).

## 3. Actores Involucrados
*   **Actor Principal:** Product Manager / Líder Técnico
*   **Sistemas Externos / Actores Secundarios:** GitHub Issues, GitHub (Sincronización de PRs).

## 4. Contexto del Problema
un desarrollador solitario necesita transparencia total sobre qué se está construyendo, por qué se está construyendo y cuándo estará listo. Sin un marco de trabajo ágil estructurado (Scrum/Kanban) y vinculado directamente al código, los proyectos se retrasan y las dependencias causan bloqueos.

## 5. Requisitos Funcionales
*   **RF-O15-001:** El sistema (GitHub Issues) debe agrupar los tickets técnicos (Issues) en ciclos o Sprints de 2 semanas de duración.
*   **RF-O15-002:** El sistema debe sincronizarse bidireccionalmente con GitHub, moviendo un ticket al estado `In Progress` cuando se crea una rama (`branch`), al estado `In Review` cuando se abre un PR, y al estado `Done` cuando el PR se fusiona.
*   **RF-O15-003:** El Product Manager debe poder estimar la complejidad técnica de los tickets utilizando puntos de historia (Story Points o T-shirt sizing).
*   **RF-O15-004:** El sistema debe generar un gráfico de "Burndown" para visualizar la velocidad de entrega del equipo a lo largo del Sprint.

## 6. Requisitos No Funcionales
*   **RNF-O15-001:** La integración GitHub Issues-GitHub debe ser en tiempo real (vía Webhooks) con un retraso máximo de sincronización de estado de 5 segundos.

## 7. Reglas de Negocio
*   **RN-O15-001 (Prioridad de Action Items):** Cualquier ticket derivado de un Post-Mortem (CU-O13) o una falla de seguridad (Security Vulnerability) entra forzosamente al tope del Sprint actual como prioridad `Urgent`, desplazando tickets de nuevas características (Features) si es necesario.
*   **RN-O15-002 (Definition of Done):** Un ticket no puede considerarse "Completado" a menos que tenga el código fusionado a main, los tests pasando, y el Changelog/Doc actualizado.

## 8. Entradas
*   Creación manual de Issues (Tareas).
*   Eventos de Webhooks desde GitHub (Apertura de PRs, Reviews, Merges).

## 9. Salidas
*   Tablero visual Kanban (Todo, In Progress, In Review, Done).
*   Métricas de velocidad del equipo (Velocity Tracking).

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Sincronización transparente del flujo de trabajo
**Dado** que el Product Manager planificó el ticket "SKY-101: Añadir endpoint GraphQL de Clima" en el Sprint actual
**Cuando** un desarrollador crea una rama en Git llamada `feature/SKY-101-graphql-weather`
**Entonces** el webhook avisa a GitHub Issues
**Y** GitHub Issues mueve automáticamente el ticket SKY-101 a la columna "En Progreso"
**Cuando** el desarrollador abre un PR
**Entonces** el ticket se mueve a "En Revisión".

## 11. Criterios de Aceptación
*   **CA-O15-001:** Todos los tickets de tipo "Feature" (nueva característica) deben estar obligatoriamente vinculados (Enlace de Proyecto/Iniciativa) a un OKR trimestral definido en el CU-E05. Tickets sueltos sin justificación estratégica son rechazados en la planeación.

## 12. Restricciones
*   Los miembros del equipo (Devs, SREs) tienen prohibido cerrar tickets de nuevas funcionalidades manualmente. El cierre siempre debe ser el resultado automatizado de un Merge en GitHub para garantizar que el código real respalda el estado del ticket.

## 13. Fuera de Alcance
*   Despliegue de código a Producción. (GitHub Issues solo rastrea el estado del trabajo; GitHub Actions o ArgoCD se encargan del despliegue físico CU-T03/CU-O10).
