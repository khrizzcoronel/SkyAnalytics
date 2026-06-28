## Why

Cuando hay cientos de analistas de distintas aerolíneas (Tenants) entrando a ver sus KPIs a las 8 AM, la base de datos colapsaría si calculara los promedios en vivo. La solución en BI (Business Intelligence) es pre-calcular esos datos (Vistas Materializadas) y almacenarlos en caché. Una vez que termina el ETL (CU-O03), debemos disparar automáticamente el refresco de estas cachés.

## What Changes

- **Gestor de Vistas Materializadas**: Simulación de un componente que ejecuta el `REFRESH MATERIALIZED VIEW` en la base de datos de forma paralela.
- **Cache Invalidation Stub**: Script que simule el llamado a un motor BI (como Superset o Metabase) para purgar su caché vieja e inyectar la nueva data.

## Capabilities

### New Capabilities
- `bi-cache-manager`: Responsable de coordinar las actualizaciones pre-calculadas para que los dashboards carguen en < 1.5s.
- `tenant-data-isolation`: Garantiza que al refrescar datos, no crucemos fronteras de clientes.

### Modified Capabilities
- 

## Impact

- **Backend (Python)**: Carpeta `backend/src/bi/` para los orquestadores de Caché.
- **Performance**: Cero tiempos de espera en el Frontend (Next.js) para los clientes, sin importar si tienen 10 años de historia de vuelos.
