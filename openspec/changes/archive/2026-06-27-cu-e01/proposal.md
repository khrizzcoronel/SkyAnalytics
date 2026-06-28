## Why

Para tomar decisiones estratégicas basadas en datos, la alta dirección necesita una visión unificada de los 4 pilares del Balanced Scorecard (Finanzas, Cliente, Procesos Internos, Aprendizaje). Actualmente, esta información se encuentra dispersa. Se requiere un dashboard gerencial consolidado de alto rendimiento que cargue rápidamente información desde el Data Warehouse (MonetDB) y la cruce con las metas (PocketBase).

## What Changes

- **Dashboard Unificado**: Creación de un tablero con indicadores clave (KPIs) extraídos de múltiples tablas de hechos.
- **Semaforización**: Indicadores visuales (Verde, Amarillo, Rojo) evaluados dinámicamente contra las metas del trimestre.
- **Drill-down Histórico**: Al hacer clic en un KPI, se mostrará una gráfica de líneas con la evolución de los últimos 12 meses (LTM).
- **Exportación a PDF**: Funcionalidad de impresión nativa (`window.print()`) con estilos CSS dedicados.
- **Seguridad**: Autenticación estricta con MFA y validación de roles (`SUPER_ADMIN`, `C_LEVEL_EXEC`).

## Capabilities

### New Capabilities
- `bsc-dashboard`: Visualización principal del tablero Balanced Scorecard, widgets de KPIs con lógica de semáforos y modal de gráfico histórico.
- `pdf-export`: Funcionalidad para ocultar barras de navegación y optimizar la vista para impresión a PDF.

### Modified Capabilities
- 

## Impact

- **Frontend**: Nuevos componentes en Next.js (App Router), utilizando Tailwind CSS y Recharts.
- **Backend**: Nueva ruta API (`/api/v1/estrategico/bsc/summary`) que implementa el patrón BFF para unir datos de PocketBase y MonetDB en memoria.
- **Seguridad**: Middleware de Next.js para forzar autenticación JWT, verificación de claims MFA y control de acceso basado en roles (RBAC).
