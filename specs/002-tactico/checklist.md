# Checklist de Validación: Módulo Táctico (QA / UAT)

Este documento contiene los criterios de aceptación y casos de prueba para validar la correcta implementación de los casos de uso **CU-T01 al CU-T10** (Capa Command Center / DevOps).

## 1. Requisitos Funcionales y Flujos Exitosos (Happy Paths)

### Observabilidad y CI/CD (CU-T02, CU-T03, CU-T04)
- `[ ]` **CA-F01:** Verificar que el tablero `LogViewerTable` extrae y renderiza exitosamente los logs recientes desde la API de Sentry sin necesidad de paginación manual (Infinite Scroll).
- `[ ]` **CA-F02:** Verificar que el tablero de CI/CD muestra correctamente el estado (Success/Failed) de los últimos 5 despliegues de GitHub Actions consultando la API de GitHub.
- `[ ]` **CA-F03:** Verificar que al actualizar un secreto desde la interfaz de la aplicación, este se inyecta correctamente en GitHub Secrets vía API, manteniendo la configuración como código.

### Finanzas Cloud (FinOps) y Alertas (CU-T06, CU-T08)
- `[ ]` **CA-F04:** Verificar que un administrador puede establecer un límite de presupuesto mensual (ej. $50) en PocketBase (CU-T08).
- `[ ]` **CA-F05:** Verificar que el Command Center puede leer exitosamente la API del PaaS/AWS y calcular el gasto actual vs. el límite.
- `[ ]` **CA-F06:** Verificar que al exceder un umbral de alerta (CU-T06), el sistema envía correctamente un Webhook hacia el canal de Slack configurado.

## 2. Reglas de Negocio

- `[ ]` **CA-B01 (Umbral FinOps):** Verificar que la `FinOpsProgressBar` cambia de color a **Rojo** cuando el gasto actual consumido supera el **90%** del límite establecido en PocketBase.
- `[ ]` **CA-B02 (Retención de Logs):** Verificar que existe una tarea programada (cron) que vuelca los logs de Sentry (con antigüedad > 13 días) hacia un Bucket S3, cumpliendo la retención de 30 días de la Constitución.

## 3. Escenarios de Error y Flujos Alternativos

- `[ ]` **CA-E01 (Caída de API Externa):** Simular una caída de la API de GitHub (cortando conexión o usando mock). Verificar que el `ThirdPartyStatusBadge` cambia a estado "Degradado" y no rompe la UI principal.
- `[ ]` **CA-E02 (Rate Limit de Terceros):** Forzar 100 recargas de la página del Command Center. Verificar que gracias a `Next.js Data Cache (revalidate: 60)`, la API de Next.js NO envía 100 peticiones a Sentry/GitHub, evitando un banneo 429.

## 4. Aspectos de Seguridad (Constitución)

- `[ ]` **CA-S01 (Control de Acceso):** Verificar que **solo** los usuarios con rol `SUPER_ADMIN` pueden acceder a las rutas `/api/v1/tactico/*`. Cualquier otro rol (incluso Ejecutivos) debe recibir un HTTP 403.
- `[ ]` **CA-S02 (Cifrado de Volumen):** Verificar que la VPS que aloja a PocketBase tiene habilitado cifrado a nivel de disco (LUKS o EBS Encryption AES-256) auditando la consola de la nube.
- `[ ]` **CA-S03 (Manejo de Secretos):** Verificar que bajo ninguna circunstancia la UI devuelve en texto plano el valor de los Secretos de GitHub. La API solo debe permitir escritura (`POST/PUT`), no lectura.

## 5. Aspectos de Rendimiento y SLA

- `[ ]` **CA-P01 (Tiempo de Proxy):** Medir la latencia de las rutas del Backend-For-Frontend que actúan de proxy. Estas no deben añadir más de **50ms** de latencia extra sobre el tiempo de respuesta natural de la API externa (GitHub/Sentry).
