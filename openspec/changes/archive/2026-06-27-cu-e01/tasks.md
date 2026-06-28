## 1. Backend API (BFF) y Seguridad

- [x] 1.1 Implementar ruta API `/api/v1/estrategico/bsc/summary` en Next.js (App Router).
- [x] 1.2 Configurar el Middleware de Next.js para validar JWT, claims MFA y roles permitidos (`SUPER_ADMIN`, `C_LEVEL_EXEC`).
- [x] 1.3 Desarrollar la conexión a PocketBase para extraer metas trimestrales y MonetDB para extraer datos LTM.
- [x] 1.4 Programar el cruce de datos en memoria y la evaluación de semáforos (Verde/Amarillo/Rojo) según reglas de negocio.

## 2. Componentes Frontend (React / Tailwind CSS)

- [x] 2.1 Desarrollar componente responsivo `KpiTrafficLightWidget` que muestre el valor, meta y color de semáforo.
- [x] 2.2 Implementar `HistoricalChartModal` con la librería Recharts para visualizar tendencias de 12 meses.
- [x] 2.3 Construir componente `PrintToPdfButton` que invoque `window.print()` y definir estilos CSS `@media print` para ocultar la navegación.

## 3. Ensamblaje y Pruebas

- [x] 3.1 Integrar la vista `/dashboard/bsc` conectando los componentes UI con la API mediante SWR o React Query.
- [x] 3.2 Validar escenario de error (HTTP 403 Forbidden) ingresando con rol `OPERATOR`.
- [x] 3.3 Validar que el botón PDF oculte correctamente el menú lateral durante la exportación.
