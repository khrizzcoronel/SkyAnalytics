## Why

Para asegurar la rentabilidad sostenible de SkyAnalytics, el Desarrollador (Dueño) requiere visibilidad detallada del ingreso recurrente (ARR) y del costo de infraestructura (Gross Margin). Actualmente, esta información requiere consultas manuales que consumen tiempo.

## What Changes

- **Métricas Financieras Consolidadas**: Se añadirá un panel con métricas críticas como ARR, LTV, CAC y Gross Margin (%).
- **Alerta de NRR**: Un indicador visual que alertará si la Retención Neta de Ingresos cae por debajo del 100%.
- **Exportación Segura**: Funcionalidad de generación de reporte mensual en PDF (client-side) incorporando una marca de agua de seguridad (trazabilidad).
- **Seguridad**: Autenticación estricta con roles `BOARD_MEMBER` y `SUPER_ADMIN`.

## Capabilities

### New Capabilities
- `finance-dashboard`: Visualización de métricas financieras de alto nivel calculadas a partir del Data Warehouse analítico.
- `watermarked-export`: Generación de reportes de exportación que incluyen una marca de agua digital con la fecha e identidad del generador.

### Modified Capabilities
- 

## Impact

- **Frontend**: Nuevas rutas y componentes React dentro de `/dashboard/finance`.
- **Backend**: Nueva ruta API en el BFF (`/api/v1/estrategico/finance/metrics`) para el consumo eficiente de MonetDB.
- **Seguridad**: Ampliación del middleware para permitir roles `BOARD_MEMBER` en la ruta `/finance`.
