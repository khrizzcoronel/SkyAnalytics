# Tareas de Implementación: Módulo Estratégico

Este documento define la secuencia lógica de desarrollo para construir la Capa Directiva (CU-E01 a CU-E06). Las tareas están ordenadas por dependencia estricta para evitar bloqueos.

---

## FASE 1: Infraestructura y Base de Datos (Backend Profundo)

### TASK-001: Configurar Esquema en PocketBase (Operativa)
*   **Descripción:** Crear la colección `strategic_targets` en PocketBase (SQLite). Debe incluir los campos: `kpi_name` (Texto), `target_value` (Número Decimal) y `quarter` (Texto, ej. '2025-Q1'). Configurar permisos para que solo el rol `SUPER_ADMIN` pueda escribir.
*   **Requisitos:** RF-E05-001, RF-E05-002
*   **Dependencias:** Ninguna.
*   **Criterio de Completado:** El esquema existe en la interfaz de administración de PocketBase y expone su API REST nativa.

### TASK-002: Desplegar Instancia Always-On de MonetDB (Analítica)
*   **Descripción:** Provisionar una VPS económica en la nube e instalar MonetDB. Configurar la conexión para aceptar tráfico externo estrictamente mediante **TLS 1.3** (`sslmode=require`). Crear el usuario y esquema de base de datos inicial para SkyAnalytics.
*   **Requisitos:** RNF-E01-002 (TLS 1.3)
*   **Dependencias:** Ninguna.
*   **Criterio de Completado:** Se puede conectar a MonetDB desde un cliente DBeaver externo mediante conexión encriptada.

### TASK-003: Crear Vistas Materializadas Analíticas en MonetDB
*   **Descripción:** Ejecutar scripts SQL para crear las vistas `vw_bsc_monthly`, `vw_financial_metrics`, y `vw_uptime_telemetry`. Por ahora, inyectar 10-20 filas de datos de prueba manuales (Mock Data) para que el frontend tenga qué leer.
*   **Requisitos:** RF-E01-001, RF-E02-001
*   **Dependencias:** TASK-002
*   **Criterio de Completado:** Un `SELECT * FROM vw_bsc_monthly` devuelve datos simulados del último año.

---

## FASE 2: Backend-For-Frontend (APIs en Next.js)

### TASK-004: Implementar Capa de Acceso a Datos (Repository Pattern)
*   **Descripción:** En el proyecto de Next.js, crear la clase Singleton `StrategicRepository`. Implementar el SDK de PocketBase en Node.js y un driver ODBC/JDBC ligero para conectarse a MonetDB.
*   **Requisitos:** Arquitectónico
*   **Dependencias:** TASK-001, TASK-002
*   **Criterio de Completado:** El código fuente contiene las funciones abstractas `fetchTargets()` y `fetchAnalytics()`.

### TASK-005: Desarrollar API de Tablero BSC y Finanzas
*   **Descripción:** Crear las Serverless Functions `/api/v1/estrategico/bsc/summary` y `/api/v1/estrategico/finance/metrics`. La API debe hacer un `fetchTargets` a PocketBase y cruzarlos en memoria con `fetchAnalytics` de MonetDB.
*   **Requisitos:** RF-E01-001, RF-E02-001
*   **Dependencias:** TASK-003, TASK-004
*   **Criterio de Completado:** Una llamada cURL al endpoint devuelve el JSON unificado consolidando el valor actual (MonetDB) y la meta (PocketBase).

### TASK-006: Implementar Seguridad de Rutas (Auth & Rate Limit)
*   **Descripción:** Añadir un middleware a las rutas `/api/v1/estrategico/*` que extraiga el JWT de PocketBase, verifique el rol `SUPER_ADMIN` y aplique caché `revalidate` para evitar caídas de Timeout.
*   **Requisitos:** CA-S01, CA-S02 (MFA), CA-S04
*   **Dependencias:** TASK-005
*   **Criterio de Completado:** Un request sin JWT devuelve HTTP 401; un request con JWT válido devuelve HTTP 200.

---

## FASE 3: Interfaz de Usuario (Frontend React)

### TASK-007: Construir Componentes Base (Tailwind CSS)
*   **Descripción:** Desarrollar los componentes puros (aislados): `KpiTrafficLightWidget` (Semáforos responsivos), `EmptyState` y la estructura de navegación tipo Sidebar.
*   **Requisitos:** RNF-E01-004 (Responsive)
*   **Dependencias:** Ninguna (Se puede hacer en paralelo).
*   **Criterio de Completado:** Componentes testeables en Storybook o renderizados en una página estática.

### TASK-008: Construir Modal de Gráfico Histórico (Recharts)
*   **Descripción:** Implementar `HistoricalChartModal` usando la librería `recharts`. Debe soportar la inyección de series temporales. Configurar el filtro por defecto a **LTM (Últimos 12 Meses)**.
*   **Requisitos:** RF-E01-003, CA-B02
*   **Dependencias:** TASK-007
*   **Criterio de Completado:** El gráfico se dibuja correctamente y es responsivo en pantallas móviles.

### TASK-009: Integración de Vistas Principales (Dashboard & CRUD)
*   **Descripción:** Conectar los componentes de React con las APIs de Next.js usando SWR o React Query. Renderizar el Dashboard principal (CU-E01), el de Finanzas (CU-E02) y crear el formulario para ingresar/editar metas trimestrales (CU-E05).
*   **Requisitos:** RF-E01-001, RF-E02-001, RF-E05-001
*   **Dependencias:** TASK-005, TASK-008
*   **Criterio de Completado:** El dashboard carga datos reales desde las APIs y el formulario permite guardar nuevas metas en PocketBase con validación exitosa.

### TASK-010: Implementar Exportación a PDF Nativa
*   **Descripción:** Crear el componente `PrintToPdfButton`. Configurar CSS media queries (`@media print`) para ocultar el Sidebar, botones de acciones y reformatear el grid para ajustarse a una hoja A4 antes de invocar `window.print()`.
*   **Requisitos:** RF-E01-005, CA-F04
*   **Dependencias:** TASK-009
*   **Criterio de Completado:** Al presionar el botón, el navegador abre el diálogo de impresión con un formato de reporte ejecutivo limpio.
