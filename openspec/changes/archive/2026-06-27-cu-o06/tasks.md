## 1. Setup Bi Manager

## 1. Setup Bi Manager

- [x] 1.1 Crear la carpeta `backend/src/bi/`.
- [x] 1.2 Crear el script `cache_manager.py`.

## 2. Implementar Refresco por Tenant

- [x] 2.1 Implementar la función `refresh_materialized_view(tenant_id)` que simule una ejecución asíncrona de `REFRESH MATERIALIZED VIEW CONCURRENTLY`.
- [x] 2.2 Implementar la función `purge_bi_cache(tenant_id)` que simule una llamada HTTP a la API del BI (ej. Superset) para invalidar el dashboard específico de ese tenant.

## 3. Pruebas y Aislamiento

- [x] 3.1 Crear un bloque `__main__` en el que se invoque el refresco para `tenant_123` y `tenant_456` para comprobar por consola que los logs respetan el aislamiento de clientes y no cruzan información.
