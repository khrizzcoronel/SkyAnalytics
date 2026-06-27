# Tareas de Implementación: Módulo Táctico

Este documento define la secuencia lógica de desarrollo para construir el Command Center (FinOps y DevOps - CU-T01 a CU-T10). Las tareas están ordenadas por dependencia para evitar bloqueos de integración.

---

## FASE 1: Configuración de Metadatos (PocketBase)

### TASK-T01: Configurar Tablas de Políticas en PocketBase
*   **Descripción:** Crear las colecciones `rbac_policies` (Reglas de acceso), `alert_policies` (Reglas de notificación) y `budget_limits` (Límites de costo FinOps). Configurar la seguridad para que solo el rol `SUPER_ADMIN` tenga acceso de lectura/escritura a estas tablas.
*   **Requisitos:** RF-T01-001, RF-T06-001, RF-T08-001
*   **Dependencias:** PocketBase instalado (del Módulo Estratégico).
*   **Criterio de Completado:** Las tres tablas existen y aceptan operaciones CRUD mediante cURL o Postman usando un JWT de administrador.

---

## FASE 2: Integración Backend y Proxy (Next.js)

### TASK-T02: Implementar Proxy para APIs de Sentry y GitHub
*   **Descripción:** Crear el servicio `TacticalIntegrationsService` en Node.js. Este servicio hará fetch a la API de Sentry (para leer logs - CU-T02) y a la API de GitHub (para ver estado del CI/CD - CU-T04). **Obligatorio:** Envolver estas llamadas en la caché de Next.js (`revalidate: 60`) para evitar bloqueos por *Rate Limit*.
*   **Requisitos:** RF-T02-001, RF-T04-001, CA-E02
*   **Dependencias:** TASK-T01
*   **Criterio de Completado:** Una llamada a `/api/v1/tactico/observability/logs` devuelve un JSON unificado con los últimos errores sin consumir la cuota de Sentry en recargas repetidas.

### TASK-T03: Desarrollar Lógica FinOps y Webhooks de Alerta
*   **Descripción:** Crear el endpoint `/api/v1/tactico/finops/billing` que extrae el límite de PocketBase y el gasto actual desde la API del PaaS. Además, crear la utilidad `WebhookDispatcher` para enviar un mensaje a Slack si el gasto supera el 90%.
*   **Requisitos:** RF-T08-001, CA-B01
*   **Dependencias:** TASK-T02
*   **Criterio de Completado:** El endpoint de FinOps cruza exitosamente ambos datos, y si se simula un exceso de presupuesto, llega un mensaje a Slack.

### TASK-T04: Desarrollar Inyector de Secretos a GitHub
*   **Descripción:** Construir el endpoint `POST /api/v1/tactico/cicd/secrets` que utiliza la API REST de GitHub para encriptar (LibSodium) y actualizar un Secreto de Entorno en el repositorio, manteniendo el concepto de configuración como código (CU-T03).
*   **Requisitos:** RF-T03-002, CA-S03
*   **Dependencias:** Ninguna (Se puede aislar).
*   **Criterio de Completado:** Enviar un POST exitoso actualiza el timestamp del secreto en la interfaz web de GitHub Actions.

---

## FASE 3: Interfaz de Usuario Táctica (Command Center)

### TASK-T05: Construir Tabla Virtualizada de Logs
*   **Descripción:** Implementar el componente `LogViewerTable` en React. Dado que los logs pueden ser miles, usar una librería de virtualización (ej. `react-window` o `TanStack Virtual`) para permitir el *Infinite Scroll* sin congelar el navegador.
*   **Requisitos:** RF-T02-002, CA-F01
*   **Dependencias:** TASK-T02
*   **Criterio de Completado:** La tabla renderiza 1,000 logs simulados a 60 FPS sin lag al hacer scroll.

### TASK-T06: Integrar Dashboard de Monitoreo FinOps y CI/CD
*   **Descripción:** Consumir los endpoints creados en la Fase 2 para ensamblar el Command Center. Renderizar la barra `FinOpsProgressBar` (que se pondrá roja al > 90%) y los badges `ThirdPartyStatusBadge` para vigilar las integraciones.
*   **Requisitos:** CA-F02, CA-B01
*   **Dependencias:** TASK-T03, TASK-T05
*   **Criterio de Completado:** El Command Center muestra datos en vivo de GitHub, Sentry y AWS/PaaS en una sola vista cohesiva y protegida bajo el rol `SUPER_ADMIN`.
