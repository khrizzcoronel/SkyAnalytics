# Checklist de Validación: Módulo Estratégico (QA / UAT)

Este documento contiene los criterios de aceptación y casos de prueba para validar la correcta implementación de los casos de uso **CU-E01 al CU-E06** (Capa Directiva).

## 1. Requisitos Funcionales y Flujos Exitosos (Happy Paths)

### Tableros Analíticos (CU-E01, CU-E02, CU-E03, CU-E04, CU-E06)
- `[ ]` **CA-F01:** Verificar que el dashboard principal (CU-E01) carga los 4 pilares (CSAT, Uptime, ARR, Churn) y muestra correctamente el semáforo (Verde, Amarillo, Rojo) cruzando contra las metas actuales.
- `[ ]` **CA-F02:** Verificar que al hacer clic en un KPI (Drill-down), se abre el `HistoricalChartModal` mostrando una gráfica lineal con la tendencia de los Últimos 12 Meses (LTM).
- `[ ]` **CA-F03:** Verificar que el tablero de Finanzas (CU-E02) calcula y renderiza correctamente el Gross Margin, LTV, CAC y NRR.
- `[ ]` **CA-F04:** Verificar que el botón "Exportar a PDF" invoca correctamente la API de impresión del navegador (`window.print()`) y la hoja de estilos CSS oculta el menú lateral/navbar en el documento resultante.

### Gestión de Metas (CU-E05)
- `[ ]` **CA-F05:** Verificar que un usuario con rol adecuado puede hacer un `POST` a `/api/v1/estrategico/targets` y crear una nueva meta para el próximo trimestre.
- `[ ]` **CA-F06:** Verificar que al actualizar una meta en la interfaz (Ej. subir meta de ARR), los semáforos del dashboard (CU-E01) cambian de color inmediatamente tras recargar la vista.

## 2. Reglas de Negocio

- `[ ]` **CA-B01 (Lógica de Semáforos):** Verificar que un valor por encima de la meta se renderiza en **Verde**. Un valor hasta 5% por debajo de la meta se renderiza en **Amarillo** (Warning). Un valor más de 5% por debajo se renderiza en **Rojo**.
- `[ ]` **CA-B02 (Temporalidad):** Verificar que si no se selecciona un filtro de fecha, el sistema asume implícitamente el rango LTM (Last Twelve Months) para los gráficos históricos.
- `[ ]` **CA-B03 (Moneda):** Verificar que todas las métricas financieras (CU-E02) se formatean estrictamente en USD (Dólares Estadounidenses) independientemente del locale del cliente.

## 3. Escenarios de Error y Flujos Alternativos

- `[ ]` **CA-E01 (Ausencia de Datos):** Verificar que si MonetDB no tiene datos para un mes específico (ej. mes actual incompleto), el gráfico histórico no se rompe y muestra una línea punteada o un valor `0` debidamente señalizado.
- `[ ]` **CA-E02 (Fallo de Origen MonetDB):** Provocar la caída temporal del túnel hacia MonetDB. Verificar que el BFF de Next.js atrapa el error y muestra un estado vacío elegante (`EmptyState`) en lugar de arrojar una pantalla blanca de la muerte (White Screen of Death) en React.
- `[ ]` **CA-E03 (Error de Conexión a PocketBase):** Simular caída de PocketBase. Verificar que al intentar guardar una meta (CU-E05) el frontend muestra un `Toast` rojo de error: "No se pudo guardar la configuración".

## 4. Aspectos de Seguridad (Constitución)

- `[ ]` **CA-S01 (Control de Acceso - RBAC):** Iniciar sesión con un usuario estándar (ej. Rol `OPERATOR`). Intentar acceder a `/api/v1/estrategico/*`. Verificar que el sistema devuelve **HTTP 403 Forbidden**.
- `[ ]` **CA-S02 (MFA Obligatorio):** Iniciar sesión con un usuario `SUPER_ADMIN` que no ha completado el reto MFA. Verificar que la API bloquea el acceso requiriendo la claim `amr: ["mfa"]` en el token JWT.
- `[ ]` **CA-S03 (Encriptación en Tránsito):** Interceptar el tráfico de red (ej. Chrome DevTools). Verificar que los endpoints consumidos exigen **HTTPS (TLS 1.3)**.
- `[ ]` **CA-S04 (Rate Limiting):** Lanzar 150 peticiones consecutivas al endpoint `/api/v1/estrategico/bsc/summary`. Verificar que el sistema devuelve **HTTP 429 Too Many Requests** según el Soft Limit global de la constitución.

## 5. Aspectos de Rendimiento y SLA

- `[ ]` **CA-P01 (SLA de Respuesta):** Medir el TTFB (Time to First Byte) de la ruta del dashboard principal. Verificar que la base de datos híbrida (MonetDB + PocketBase en memoria) resuelve la petición en **$\leq$ 3.0 segundos**.
- `[ ]` **CA-P02 (Caché Client-Side):** Navegar entre el CU-E01 (Dashboard) y el CU-E02 (Finanzas) repetidas veces. Verificar que las métricas cargan instantáneamente sin disparar nuevas llamadas a la API gracias a SWR / React Query.
- `[ ]` **CA-P03 (Responsive UI):** Emular un iPhone SE (375px) en el navegador. Verificar que los componentes Tailwind (como el `KpiTrafficLightWidget`) colapsan a diseño apilado vertical (`flex-col`) y son legibles sin *scroll* horizontal.
