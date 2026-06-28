## Context

Después del ETL diario y la validación (CU-O03 y CU-O04), los datos crudos residen en `Fact_Flight`. Las consultas analíticas pesadas (sumas, promedios) deben estar listas *antes* de que el cliente inicie sesión.

## Goals / Non-Goals

**Goals:**
- Simular la actualización Concurrente de Vistas Materializadas.
- Simular la invalidación de la caché del servidor BI.
- Asegurar que la lógica sea aisable por "Tenant" (Ej: Refrescar la vista de Delta Airlines independientemente de la de American Airlines).

**Non-Goals:**
- No instalaremos un motor de BI real como Apache Superset (eso se hace por Docker en fase de despliegue).
- No instalaremos Redis para la caché; usaremos salidas de consola (Mocks) para demostrar el circuito de eventos.

## Decisions

- **Aislamiento por Tenant:** Se pasará el `tenant_id` como argumento al script. La caché se invalida solo para ese inquilino, asegurando la privacidad (RN-O06-001).
- **Asincronía (Simulada):** En un escenario de millones de registros, un "REFRESH" toma segundos o minutos. Utilizaremos programación secuencial simple en el simulador, pero denotaremos en el código que debería ser un subproceso asíncrono para escalar a cientos de Tenants.

## Risks / Trade-offs

- **Bloqueos de BD (Locks):** Si se hace un refresco bruto, las tablas se bloquean e impiden que los usuarios lean datos.
  - *Mitigación:* Se dejará claro en el código SQL (Simulado) que se debe usar el comando `CONCURRENTLY` (típico en PostgreSQL/MonetDB) para actualizar la caché de fondo sin bloquear a los lectores.
