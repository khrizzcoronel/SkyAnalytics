# Diseño Técnico: Módulo Estratégico

## 1. Arquitectura de la Solución (Capa Directiva)
**Patrón Arquitectónico:** Monolito Modular Serverless (Pragmático / Solo-Dev).
Este módulo agrupa los casos de uso **CU-E01 al CU-E06**, los cuales comparten un propósito puramente analítico y de control para la dirección de la empresa.

*   **Frontend (Presentación):** Next.js (App Router) alojado en un PaaS (ej. Vercel). El frontend utiliza *React Server Components* (RSC) para proteger la lógica financiera y *Client Components* para la interactividad (Gráficos, Modales, Formularios).
*   **Backend (Capa de Servicios):** Rutas de API de Next.js (`/api/v1/estrategico/*`) implementando el patrón Backend-For-Frontend (BFF). Todo el código backend reside en el mismo repositorio que el frontend.
*   **Capa de Datos Híbrida:** 
    *   **PocketBase (Operativa):** Base de datos relacional rápida (SQLite) que maneja las sesiones de usuario y los metadatos transaccionales (ej. CRUD de Metas Estratégicas - CU-E05).
    *   **MonetDB (Analítica):** Motor columnar Data Warehouse que provee vistas pre-agregadas súper rápidas para los tableros analíticos (BSC, Finanzas, Uptime, Compliance, RRHH). La base de datos debe estar **conectada siempre vía TLS 1.3** (`sslmode=require`) para cumplir con la Constitución.

## 2. Modelo de Base de Datos Unificado

### 2.1 Tablas Operativas (PocketBase)
*   **`users`**: Autenticación central (OAuth/Password+MFA). Campos clave: `role` (`SUPER_ADMIN`, `C_LEVEL_EXEC`).
*   **`strategic_targets` (CU-E05)**: Almacena las metas trimestrales definidas manualmente por la dirección.
    *   `id` (String UUID, PK)
    *   `kpi_name` (String) - Identificador del KPI (ej. `finance_arr`).
    *   `target_value` (Decimal) - El valor a alcanzar.
    *   `quarter` (String) - Ej. `2025-Q1`.

### 2.2 Vistas Analíticas (MonetDB)
Para garantizar tiempos de carga $\leq$ 3 segundos y evitar consultas OLTP pesadas en vivo, MonetDB alojará **Vistas (`VIEW`)** o tablas consolidadas por el pipeline ETL:
*   **`vw_bsc_monthly` (CU-E01):** Consolidado de los KPIs de negocio aeronáutico (cancellation_rate, avg_dep_delay, total_flights).
*   **`vw_financial_metrics` (CU-E02):** Métricas de rentabilidad (Gross Margin, LTV, CAC, NRR).
*   **`vw_uptime_telemetry` (CU-E03):** Latencia p95 y disponibilidad de endpoints clave.
*   **`vw_compliance_controls` (CU-E04):** Estado booleano de auditorías internas (Pass/Fail).
*   **`vw_sre_retention` (CU-E06):** Métricas de turnos de los ingenieros, horas extra y riesgo de fuga.

## 3. Endpoints de Servicios
| Método | Ruta (`/api/v1/estrategico/*`) | Uso Principal | Base de Datos |
| :--- | :--- | :--- | :--- |
| `GET` | `/bsc/summary` | Dashboard principal (Semáforos). | MonetDB |
| `GET` | `/finance/metrics` | Métricas de rentabilidad (ARR, LTV). | MonetDB |
| `GET` | `/engineering/health` | Dashboard técnico (Uptime, Latencia). | MonetDB |
| `GET` | `/hr/burnout` | Análisis de riesgo de ingenieros. | MonetDB |
| `GET` | `/targets` | Obtener metas configuradas. | PocketBase |
| `POST/PUT` | `/targets` | Definir/Actualizar metas trimestrales. | PocketBase |

*(Nota: Todos los endpoints verifican el token de PocketBase y exigen rol de administración).*

## 4. Componentes y Clases Principales
Al unificar el módulo, maximizamos la reutilización de código en React:

### 4.1 Componentes React (Reutilizables y Responsivos)
Todos los componentes estarán estilizados con **Tailwind CSS** para asegurar que el dashboard sea responsivo y funcional en smartphones y tabletas gerenciales.
*   **`KpiTrafficLightWidget`:** Recibe un valor actual, una meta y reglas de semáforo. Renderiza Verde/Amarillo/Rojo (Usado en CU-E01, CU-E03, CU-E04). Se adapta usando clases `md:flex-row flex-col`.
*   **`HistoricalChartModal`:** Un gráfico de líneas de `Recharts` que grafica series temporales en *drill-down*. Envuelto en un `ResponsiveContainer` para colapsar en pantallas pequeñas.
*   **`PrintToPdfButton`:** Componente transversal que invoca `window.print()` y oculta la barra de navegación para exportar informes financieros/técnicos limpios (Usado en todos los CU analíticos).

### 4.2 Lógica Backend
*   **`StrategicRepository` (Capa de Acceso a Datos):** Una clase Singleton en Node.js que encapsula dos clientes: el SDK de PocketBase (para leer/escribir metas y validar tokens) y un cliente SQL nativo para ejecutar `SELECT` sobre las vistas de MonetDB.

## 5. Flujo de Datos Global
1.  **Carga Seed e Ingesta:** El importador Docker (`importer`, CU-O22) carga `flights_raw` de forma incremental en PocketBase a las 02:00 AM. El ETL Python (`etl_flights_to_monetdb.py`, CU-O21) transforma e inserta en MonetDB a las 03:00 AM. Las vistas analíticas se refrescan de forma automática al finalizar.
2.  **Configuración:** El Desarrollador (Dueño) usa la UI para establecer las metas del `2025-Q1` (CU-E05). Esto se guarda instantáneamente en PocketBase.
3.  **Visualización:** El usuario navega al tablero BSC. El Frontend (RSC) solicita los datos al BFF (Next.js API).
4.  **Cruce de Datos (Join Lógico):** El Backend extrae el *Valor Actual* de MonetDB (`vw_bsc_monthly`) y lo cruza con el *Valor Meta* de PocketBase (`strategic_targets`).
5.  **Cálculo y Respuesta:** El Backend calcula los colores del semáforo y devuelve un JSON unificado al Frontend.
6.  **Exportación:** El usuario presiona "Exportar Reporte". El cliente ejecuta la exportación local (PDF vía CSS) o consume un endpoint `/export/csv` para descargar la data cruda.

## 6. Dependencias con Otros Módulos
*   **Módulo Operativo (ETL & Auth):** Este módulo estratégico no "crea" datos financieros ni de telemetría (salvo las Metas). Su dependencia principal es con los pipelines ETL (Módulo Operativo) que mantienen MonetDB actualizado. Si el ETL falla, los datos mostrados en estos tableros estarán desactualizados.

## 7. Decisiones Técnicas y Justificación
*   **Unificación del BFF (Backend-For-Frontend):** 
    *   *Por qué:* En lugar de tener un microservicio para Finanzas (CU-E02) y otro para RRHH (CU-E06), todas las rutas residen en la misma aplicación Next.js. Esto minimiza el frío de arranque (Cold Starts) en entornos Serverless y permite compartir la lógica de conexión a bases de datos.
*   **Separación Estricta PocketBase/MonetDB en el Cruce de Datos:** 
    *   *Por qué:* Las Metas (Targets) son mutables (CRUD manual por el usuario), por ende pertenecen a PocketBase. Los resultados históricos son masivos (Millones de filas sumarizadas), por ende pertenecen a MonetDB. El "cruce" se hace en la memoria del Backend de Next.js (cruzando dos pequeños JSONs) lo que resulta más rápido que intentar forzar conectores complejos entre dos bases de datos distintas.
*   **UI Centralizada para Exportación (Print CSS):** 
    *   *Por qué:* Para un Solo-Dev, generar PDFs cifrados desde Node.js consume muchísima memoria y tiempo de cómputo. Utilizar el motor del navegador del cliente (`@media print`) traslada el costo computacional al usuario y acelera infinitamente el desarrollo (Time-To-Market).
*   **Mitigación de Timeouts en Serverless (Cold Starts):**
    *   *Por qué:* Vercel tiene un timeout estricto de 10-15s en cuentas gratuitas. Si MonetDB entra en estado *Scale-to-Zero* (apagado por inactividad), la API fallará (HTTP 504). Para mitigarlo, se establece que **la instancia de MonetDB será Always-On (24/7)** en una VPS económica, evitando cold-starts de la base de datos y garantizando el SLA de 3 segundos.
