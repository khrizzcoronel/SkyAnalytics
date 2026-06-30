# Especificación de Caso de Uso: CU-O06

## 1. Nombre de la Funcionalidad
**Refrescar Dashboards BI**

## 2. Objetivo
Automatizar y optimizar la actualización de los conjuntos de datos subyacentes que alimentan los dashboards de Inteligencia de Negocios (BI) usados por los clientes B2B, asegurando tiempos de carga imperceptibles.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Sistema Automático
*   **Sistemas Externos / Actores Secundarios:** Motor BI (ej. Apache Superset, Metabase), Base de datos OLAP (PocketBase (Operativa) y MonetDB (Analítica)).

## 4. Contexto del Problema
Cuando cientos de aerolíneas consultan sus dashboards operativos a la vez, ejecutar consultas SQL en vivo de agregación masiva ("group by") sobre el Data Warehouse bloquea los hilos de conexión (Thread Exhaustion) y retrasa la carga de la página. Se necesita pre-calcular los resultados (Vistas Materializadas) y refrescar la caché del BI en intervalos regulares.

## 5. Requisitos Funcionales
*   **RF-O06-001:** El sistema debe ejecutar consultas de creación y refresco de vistas materializadas (`REFRESH MATERIALIZED VIEW`) en PocketBase (Operativa) y MonetDB (Analítica) al finalizar el pipeline de Ingesta (CU-O03).
*   **RF-O06-002:** El sistema debe invocar la API del motor de BI para invalidar y reconstruir la caché de los dashboards correspondientes al Tenant actualizado.
*   **RF-O06-003:** El sistema debe monitorear el tiempo de reconstrucción de las vistas. Si demora más de lo configurado, debe lanzar un "Slow Query Alert".

## 6. Requisitos No Funcionales
*   **RNF-O06-001 (Latencia UI):** El pre-cálculo de datos garantiza que el usuario final perciba un tiempo de carga del dashboard siempre inferior a 1.5 segundos.
*   **RNF-O06-002 (Escalabilidad):** El refresco de vistas materializadas de distintos Tenants debe paralelizarse siempre que el uso del CPU del servidor OLAP no supere el 80%.

## 7. Reglas de Negocio
*   **RN-O06-001 (Aislamiento Multi-Tenant):** Un refresco de datos nunca debe cruzar los límites del Tenant. Las vistas materializadas son instanciadas estrictamente utilizando filtros de "Row-Level Security" o esquemas separados por cliente.
*   **RN-O06-002 (Caché Stale):** En caso de fallo de refresco, el motor BI devolverá la caché "stale" (vencida) del día anterior en vez de una pantalla de error, mostrando un pequeño banner de "Datos desactualizados".

## 8. Entradas
*   Señal (Webhook) desde el orquestador ETL indicando el fin de la carga de datos.
*   Parámetros: `TenantID`.

## 9. Salidas
*   Datos cacheados listos en el motor de presentación (Redis/BI Cache).

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Refresco exitoso del Dashboard de un Cliente
**Dado** que el proceso ETL de "Delta Airlines" (Tenant A) ha finalizado exitosamente
**Cuando** GitHub Actions llama a la API de BI para refrescar sus paneles
**Entonces** el motor OLAP ejecuta el REFRESH de sus vistas materializadas en 10 segundos
**Y** purga la caché antigua
**Y** la próxima vez que un usuario de "Delta" se loguee, el dashboard cargará los datos de hoy en $\leq$ 1.5s.

## 11. Criterios de Aceptación
*   **CA-O06-001:** El refresco ocurre sin bloqueos (Locks) que interrumpan consultas de lectura concurrentes por parte de usuarios finales (`CONCURRENTLY`).

## 12. Restricciones
*   El refresco masivo solo ocurre fuera de horarios pico o bajo demanda estrictamente necesaria para evitar congestión de la red y base de datos.

## 13. Fuera de Alcance
*   Creación visual de nuevos gráficos (Esto lo hace el usuario final en modo self-service en el BI).
