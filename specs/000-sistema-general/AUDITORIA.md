# REPORTE DE AUDITORÍA SDD — SkyAnalytics

> Fecha de auditoría: 2026-06-29
> Metodología: Spec Driven Development (SDD) + OpenSpec
> Arquitectura objetivo: 3 niveles (Operativo / Táctico / Estratégico)
> Stack: Python (FastAPI) backend, Next.js frontend, PocketBase (OLTP), MonetDB (OLAP), Docker

---

## Resumen ejecutivo

| Indicador | Valor |
|---|---|
| **Estado general del proyecto** | **PARCIAL** |
| **Specs completas y correctas** | ~90 % (36/40 CUs con spec completa; CU-O21..O24 mínimas) |
| **Implementación backend real** | ~35 % (reglas implementadas como scripts demo; ETL/ML/Quarantine parcialmente reales) |
| **Implementación frontend real** | ~25 % (solo 3 dashboards estratégicos; 8 endpoints tácticos huérfanos; sin tests) |
| **Servicios Docker configurados** | 5 de 5 (frontend, backend, pocketbase, importer, monetdb) — sin .env.example, sin healthchecks, backend con CMD incorrecto |
| **Cambios OpenSpec archivados** | 36/40 CUs (160/160 tasks marcadas `[x]`) |
| **CUs sin carpeta OpenSpec** | 4 (CU-O21, CU-O22, CU-O23, CU-O24) |

**Conclusión:** El proyecto tiene una **estructura SDD muy sólida** (40 CUs especificados, 36 changes OpenSpec archivados, Constitución detallada), pero la implementación real es todavía un **prototipo avanzado**: módulos de soporte/growth/seguridad son scripts stdout, el backend no expone el flight API en producción, el frontend usa mocks, faltan tests automáticos y Docker carece de hardening operacional. No está listo para producción.

---

## Specs

### ✅ Lo que está completo y correcto

- **`specs/000-sistema-general/CONSTITUTION.md`** (65 líneas): define nombre, propósito, stack, arquitectura cloud-native, especificación API-first, contratos de datos, ADRs, SemVer, Spectral, PR reviews, Zero Trust, TLS 1.3, AES-256, gestión de secretos, SAST/DAST, separación OLTP/OLAP, backups, pruebas de calidad/performance/chaos/ML drift, SLAs, RPO/RTO, Error Budget, cultura remote-first y FinOps.
- **Módulo Estratégico (`specs/001-estrategico/`)**: 6 CUs (CU-E01..CU-E06), todos con plantilla 13-secciones completa. Total: 26 RF, 15 RNF, 14 RN, 15 CA. Incluye `plan.md` (7 secciones), `tasks.md` (10 tareas / 3 fases) y `checklist.md` (31 ítems / 19 IDs).
- **Módulo Táctico (`specs/002-tactico/`)**: 10 CUs (CU-T01..CU-T10), plantilla completa. Total: 41 RF, 19 RNF, 20 RN, 20 CA. Incluye `plan.md`, `tasks.md` (6 tareas / 3 fases) y `checklist.md` (19 ítems).
- **Módulo Operativo (`specs/003-operativo/`) CU-O01..CU-O20**: 20 CUs con plantilla completa. Total: 89 RF, ~31 RNF, ~37 RN, 25 CA. Incluye `plan.md`, `tasks.md` (10 tareas / 5 fases) y `checklist.md` (15 ítems).
- **Reglas globales resueltas** en `CONSTITUTION.md` L59-65: Rate Limiting Soft Limit 1h, ETL cuarentena, logs 30 días, secretos vía GitHub Secrets, Status Page + email, dataset BTS 2024 con importador incremental + checkpoint.

### âš ï¸ Lo que está incompleto o tiene problemas menores

- **`README.md` prácticamente vacío** (2 líneas): sin descripción, arquitectura ni instrucciones de uso.
- **CU-O21..O24 son specs mínimas**: solo contienen secciones 1–7. Faltan Reglas de Negocio, Entradas/Salidas, Criterios de Aceptación, Restricciones y Fuera de Alcance.
- **Plan/tasks/checklist del módulo operativo excluyen CU-O21..O24**: su scope dice explícitamente "CU-O01 al CU-O20" (`plan.md` L5, `tasks.md` L3, `checklist.md` L3), aunque `tasks.md` luego referencia CU-O21/O22/O24 en TASK-O00-A/B/C — contradicción interna.
- **Doble namespace de Criterios de Aceptación**: las specs usan `CA-OXX-NNN` / `CA-TXX-NNN` / `CA-EXX-NNN`, pero `tasks.md` y `checklist.md` usan un namespace cruzado `CA-{F,B,E,S,P}-NN` (Functional/Business/Error/Security/Performance). No existe mapeo entre ambos, por lo que la trazabilidad 1:1 es imposible. Afecta a los 3 módulos.
- **Inconsistencias cross-documento detectadas**:
  - Cron ETL: 02:00 (`plan.md` §4.2 / `tasks.md` TASK-O05) vs 03:00 (CU-O21 RF-O21-001 / `checklist.md` CA-F01).
  - Bucket S3 ML: `s3://skyanalytics-ml/` (CU-O05 RF-O05-002, CU-O24 RF-O24-004) vs `skyanalytics-ml-models` (`plan.md` §2.2 / `tasks.md` TASK-O02).
  - SLA dashboard BSC: 2 s p95 (RNF-E01-001 / CA-E01-003) vs 3 s (`plan.md` §7 / `checklist.md` CA-P01).
  - Semáforo Yellow: 80–99.9 % de meta (RN-E01-001) vs "hasta 5 % bajo meta" (`checklist.md` CA-B01) — discrepancia de 15 %.
  - Error Budget: RF-E03-002 dice "~4.38 minutos al mes" (equivale a SLA 99.99 %), pero Constitución y CU-E03 definen SLA 99.0 % (que da 432 min/mes).
  - Drift en módulo táctico: `plan.md` §2.1 y `tasks.md` atribuyen `rbac_policies` a CU-T01 y logs/Sentry a CU-T02, pero CU-T01.md real es "Gestión de Campañas de Growth Hacking/HubSpot" y CU-T02.md real es "Configurar y Publicar API en RapidAPI". Los documentos de soporte están desfasados respecto a las specs reales.
  - `vw_sre_retention` en `plan.md` estratégico describe "turnos de ingenieros, horas extra y riesgo de fuga" (enfoque SRE), pero CU-E06 trata de eNPS / Time-to-Productivity / retención de talento.
  - Taxonomía de roles incompleta: se mencionan `SUPER_ADMIN`, `C_LEVEL_EXEC`, `BOARD_MEMBER`, `OPERATOR`, `VP`, `VP People`, `FINOPS_MANAGER`, `Desarrollador (Dueño)`, pero `plan.md` solo enumera `SUPER_ADMIN` y `C_LEVEL_EXEC` en `users.role`.
- **Artefactos de plantilla corruptos** en 18+ archivos: tokens como `temporal`, `temporalmente`, `temporales`, `Buenas prácticas de seguridadde`, `Desarrollador (Tú)ing`, `Desarrollador (Tú)s`, `Stack LGTM (Archivos de Log, Dashboard Básico / Sentry, Logs, Sentry / Logs)`, `Scripts básicos de despliegue`, `Tracking básico o local`. Parece resultado de sustitución automática de marcas de herramientas.
- **Sección 14 "Aclaraciones Globales" inconsistente**: presente en CU-T01, T02, T03, T05, T06; ausente en CU-T04, T07, T08, T09, T10.
- **CU-T08** tiene solo 1 RNF (el resto de CUs tienen 2).
- **CU-O12** duplica la sección "## 14. Aclaraciones Globales".
- **CU-O20** se contradice: RF-O20-001 dice "una única instancia GPU", pero el Escenario 1 habla de "4 nodos AWS p4d.24xlarge (Data Parallelism)".
- **RN-T02-001** define cuotas Freemium y Pro pero no especifica el plan "Ultra" mencionado en RF-T02-002.
- **17 de 24 CUs operativos** no tienen una tarea explícita vinculada en `tasks.md` (solo CU-O03, O20, O21, O22, O24 y parcialmente O05/O06 están cubiertos).

### âŒ Lo que falta o tiene problemas críticos

- **`README.md` vacío** — sin descripción de proyecto ni setup.
- **4 CUs sin carpeta OpenSpec**: CU-O21, CU-O22, CU-O23, CU-O24 no tienen `openspec/changes/archive/...` correspondiente. Faltan proposal, design, tasks y spec delta.
- **Sin matriz de trazabilidad CU → RF → endpoint → vista → test** en ningún lugar del repo.

---

## Backend

### ✅ Implementado correctamente

- **ETL PocketBase → MonetDB Star Schema** (`backend/src/etl/etl_flights_to_monetdb.py`): crea `dim_airline`, `dim_airport`, `dim_date`, `fact_flights` y vistas `vw_bsc_monthly`, `vw_delay_analysis`; usa watermark incremental `MAX(pb_created)`; carga por batches de 2000 filas; cumple RF-O21-001..005 y RNF-O21-002.
- **Importador CSV incremental** (`backend/import/import_flights.py`): 100k filas por run, checkpoint JSON, IDs deterministas `fl<13digitos>`, `INSERT OR REPLACE` idempotente; cumple RF-O22-001..005.
- **Data Contract Pydantic** (`backend/src/quality/contracts.py`): validación completa del esquema BTS con rangos plausibles.
- **Cobertura reglas de negocio**: 32 módulos Python implementan RN/CA de casi todos los CUs (Post-Mortem blameless, eNPS privacidad <3 respuestas, OKR quantitative KR, IAM revocación >90 días, FinOps PR gate, etc.).

### âš ï¸ Implementado parcialmente

- **`api_server.py` (CU-O02)**: implementa `GET /v1/flights/{flight_id}` con rate-limit HTTP 429 y caché, pero **no está desplegado** porque `backend/Dockerfile` CMD ejecuta `src/tactical/data_quality_monitor.py`. Además usa `FAKE_REDIS_CACHE` y `API_USAGE` en memoria (se reinician al recrear contenedor).
- **Tenant onboarding (CU-O01)**: genera y hashea API keys (`backend/src/services/api_key_service.py`), pero **no persiste en PocketBase** (`backend/src/tenant_onboarding.py` L24-28 admite "omitimos la conexión real"). No existe colección `tenants` en `pb_schema.json`.
- **Quarantine (CU-O04/RF-O02)**: `backend/src/etl/data_validator.py` escribe filas corruptas a CSV (`quarantine_flights.csv`) en lugar de a una tabla `Quarantine_Data` en MonetDB como indica `plan.md` §2.1.
- **ML/Feature engineering**: `feature_engineering.py` y `train_xgboost_model.py` conectan con MonetDB/S3, pero usan `MONETDB_PASS = "skyanalytics_secure"` hardcoded como fallback (violación Zero Trust).
- **26 módulos tácticos/estratégicos/de soporte** son scripts de demostración (`__main__` con prints stdout); no integran S3/Slack/Pinecone/GitHub/Stripe/Linear reales. Ejemplos: `faq_rag_indexer.py` usa md5+keyword en vez de vector store real; `security_scanner.py` tiene CVE DB hardcoded de 1 línea.
- **Acceso a PocketBase por SQLite directo**: `import/import_flights.py` y `etl/etl_flights_to_monetdb.py` abren `/pb_data/data.db` con `sqlite3` en lugar de usar la HTTP API de PocketBase. Esto es una desviación arquitectónica de la Constitución.

### âŒ No implementado o incorrecto

- **Dependencias faltantes en `backend/requirements.txt`**: `passlib`, `boto3`, `joblib`, `email-validator` son importadas pero no listadas. `pip install -r requirements.txt` falla.
- **Bug Pydantic en `api_server.py`**: campo `_cached` con guion bajo → Pydantic v2 lo trata como atributo privado y no lo expone.
- **Código legacy**: `backend/src/etl/ingestion_job.py` declara "NO USAR EN PRODUCCIÓN" y usa schema distinto al BTS; `backend/src/etl/generate_mock_csv.py` usa schema `flight_id/departure_date/airline/status/monto_pago` que no alimenta el ETL real.
- **Hardcoded PII**: `backend/src/support/post_mortem_generator.py` incluye `"kacor"` en `BANNED_NAMES`, inconsistente con RN-O07 de redacción de PII.
- **Sin framework de tests**: solo existe `backend/src/quality/test_quality.py` como script manual; no hay `pytest`, `unittest` ni carpeta `tests/`.
- **Backend Dockerfile CMD incorrecto**: ejecuta `data_quality_monitor.py` (script demo) en lugar de `api_server.py`.
- **Tres módulos solapados de circuit-breaker**: `tactical/data_quality_monitor.py`, `quality/data_quality_suite.py`, `etl/data_contract_validator.py` guardan lo mismo con nombres de campo diferentes.

---

## Frontend

### ✅ Vistas completas

- 3 dashboards estratégicos reales con `fetch`:
  - `/dashboard/bsc` (CU-E01)
  - `/dashboard/finance` (CU-E02)
  - `/dashboard/engineering` (CU-E03, con polling 30 s)
- 7 componentes React: `KpiTrafficLightWidget`, `HistoricalChartModal` (recharts), `PrintToPdfButton`, `WatermarkedPdfButton`, `PrintSlaReportButton`, `EndpointHealthTable`, `ErrorBudgetGauge`.
- 8 endpoints tácticos implementados como Next.js Route Handlers en `src/app/api/v1/tactico/*` (CU-T01..T10).
- Stack moderno: Next.js 16.2.9, React 19.2.4, TypeScript 5, Tailwind v4.

### âš ï¸ Vistas parciales

- **`/estrategico` y `/tactico` (páginas top-level)** son mocks estáticos con cards hardcoded, sin fetch; duplican conceptualmente a `/dashboard/*`.
- **`StrategicRepository.ts` es 100 % mock** con `// TODO` para PocketBase SDK y MonetDB ODBC.
- **`HistoricalChartModal.tsx`** usa `Math.random()` para datos históricos — distintos en cada click.
- **Middleware de autenticación (`src/middleware.ts`)** es un mock: verifica `token.includes('operator-token')`; no valida JWT firmado ni consulta PocketBase.
- **Identidades hardcoded en exports confidenciales**: `WatermarkedPdfButton user="founder@skyanalytics.com"` y `PrintSlaReportButton customer="Acme Corp - Enterprise Plan"`.
- **Inconsistencia SLA en engineering**: route handler usa `TOTAL_ERROR_BUDGET_SECONDS = 262.8` (â‰ˆ4.38 min, SLA 99.99 %), pero el UI dice "Objetivo SLA Garantizado: 99.0 %".
- **8 endpoints `/api/v1/tactico/*` huérfanos**: ninguno es consumido por la UI.

### âŒ Vistas faltantes / bugs críticos

- **No existe `@media print` CSS** en `globals.css` ni en ningún archivo. Las clases `print-hide`, `print-watermark`, `internal-infra` no están definidas. Resultado: los exports PDF no ocultan botones, no muestran watermark y **filtran IPs internas de pods** (columna "Internal Pod IP" generada con `Math.random()` en `EndpointHealthTable`). Bug de privacidad/SOC2.
- **Sidebar no enlaza a `/dashboard/*`**: los únicos dashboards reales solo son accesibles por URL directa.
- **Theme clash**: shell usa fondo oscuro (`#050505` en `globals.css`) mientras los dashboards usan Tailwind light (`bg-white`), produciendo fondos mezclados.
- **Sin formularios**: 0 elementos `<form>`, sin zod/yup, sin validación client-side.
- **Sin login real, role model, ni sesión**.
- **Sin tests**: 0 archivos `*.test.*`, sin jest/vitest/playwright, sin script `test` en `package.json`.
- **`RAPIDAPI_PROXY_SECRET` con fallback hardcoded** `test_secret_123` en `docker-compose.yml` y route handler.
- **`recharts` usado solo en 1 mock modal**; las áreas de gráfico en `/estrategico` son texto placeholder.

---

## Docker

### ✅ Servicios configurados

- `docker-compose.yml` define 5 servicios: `frontend`, `backend`, `pocketbase`, `importer`, `monetdb`.
- Volúmenes persistentes: `pb_data`, `monetdb_data`, `importer_data`.
- `pocketbase` usa imagen oficial `ghcr.io/muchobien/pocketbase:latest` en puerto 8090.
- `monetdb` usa imagen oficial `monetdb/monetdb:latest` en puerto 50000.
- `importer` construye desde `backend/import/Dockerfile` con `restart: "no"`.

### âš ï¸ Servicios con problemas

- **`backend` CMD inútil en producción**: `backend/Dockerfile` L11 ejecuta `src/tactical/data_quality_monitor.py` (demo) en lugar de exponer `api_server.py`. No publica puerto 8000 en `docker-compose.yml`.
- **`frontend` no depende de `backend`**: `depends_on` solo incluye `pocketbase`.
- **`pocketbase` no monta `pb_schema.json`**: el schema debe importarse manualmente.
- **Volúmenes compartidos `pb_data` entre `pocketbase` e `importer`**: write-contention posible en SQLite.

### âŒ No configurados

- **No existe `.env.example` ni `.env`**: 0 archivos encontrados. Variables críticas sin documentar: `MONETDB_PASS`, `RAPIDAPI_PROXY_SECRET`, etc.
- **Sin healthchecks** en ningún servicio.
- **Sin `depends_on` con condition**: `backend` depende de `monetdb` pero no espera a que esté sano.
- **`backend` no expone puertos**: el flight API no es accesible externamente con `docker-compose up`.
- **Sin network explícita**: usa bridge por defecto.
- **PocketBase expuesto en HTTP 8090 sin proxy TLS**: Constitución exige TLS 1.3.
- **`MONETDB_PASS` default hardcoded** `"skyanalytics_secure"` en `docker-compose.yml` L21 y L55.

---

## OpenSpec

### ✅ Cambios aplicados y archivados

- 36 carpetas archivadas en `openspec/changes/archive/2026-06-27-cu-*/` para CU-E01..E06, CU-T01..T10, CU-O01..O20.
- Cada change contiene `proposal.md`, `design.md`, `tasks.md` y `specs/<capability>/spec.md`.
- **160 tasks en total, 100 % marcadas `[x]`** (0 pendientes).
- `openspec/specs/` contiene 50 capability specs consolidadas, representando el estado acumulado actual.
- Cobertura 100 % en Estratégico (6/6) y Táctico (10/10).

### âš ï¸ Cambios pendientes / parciales

- `openspec/config.yaml` tiene las secciones `context` y `rules` como template comentado; no están rellenas.

### âŒ Cambios sin implementar / faltantes

- **4 CUs sin carpeta OpenSpec**: CU-O21, CU-O22, CU-O23, CU-O24. Son la columna vertebral del pipeline de datos (Star Schema ETL, import incremental, drift monitoring, feature engineering).
- **No hay changes in-flight**: `openspec/changes/` solo contiene `archive/`; 0 propuestas activas.
- **Discrepancia "done" vs realidad**: los 160 tasks están `[x]`, pero gran parte del código correspondiente son scripts stdout/demo sin integración real. El mark refleja "script entregado", no "feature operacional en producción".
- **Algunas capabilities no tienen change propio**: `tenant-data-isolation`, `centralized-logger`, `champion-challenger-evaluator` aparecen como side-effects de otros changes.

---

## Lista de acciones prioritarias

1. **[CRÍTICO] Escribir `README.md`** — actualmente casi vacío (2 líneas). Documentar arquitectura, decisiones SDD, comando `docker-compose up`, variables .env y mapeo CU→módulo→endpoint.

2. **[CRÍTICO] Crear `.env.example`** con `MONETDB_PASS`, `RAPIDAPI_PROXY_SECRET`, `NODE_ENV`, `SENTRY_DSN`, `SLACK_WEBHOOK_URL`, `STRIPE_SECRET_KEY`, `HUBSPOT_API_KEY`, etc. Eliminar defaults hardcoded en `docker-compose.yml` y en archivos Python.

3. **[CRÍTICO] Arreglar `@media print` CSS** en `frontend/src/app/globals.css` — actualmente los exports PDF filtran IPs internas de pods y no ocultan botones/watermark. Bug de privacidad/SOC2.

4. **[CRÍTICO] Completar `backend/requirements.txt`** añadiendo `passlib`, `boto3`, `joblib`, `email-validator` (y deps de test). Sin esto `pip install -r requirements.txt` falla.

5. **[CRÍTICO] Persistir tenants en PocketBase**: crear colección `tenants` en `pb_schema.json` y completar `backend/src/tenant_onboarding.py` para insertar vía HTTP API en lugar de "simular".

6. **[CRÍTICO] Implementar `Quarantine_Data` como tabla MonetDB** (no CSV) según `plan.md` §2.1.

7. **[CRÍTICO] Crear OpenSpec changes para CU-O21..O24** — actualmente no existen en `openspec/changes/`.

8. **[IMPORTANTE] Reorganizar físicamente `specs/` por dominios funcionales + usuarios** (dejar de usar 001/002/003 por objetivo). Crear carpetas como `01-identidad-acceso`, `03-data-pipeline`, `04-ml`, `05-bi-estrategico`, etc.

9. **[IMPORTANTE] Completar specs mínimas CU-O21..O24** con secciones 8-13 (RN, Entradas/Salidas, CA, Restricciones, Fuera de Alcance).

10. **[IMPORTANTE] Unificar namespace de CAs**: eliminar `CA-{F,B,E,S,P}-NN` y adoptar `CA-<MOD>-NNN` en todos los plan/tasks/checklist.

11. **[IMPORTANTE] Reconciliar 8 inconsistencias cross-doc**: cron ETL, bucket S3 ML, SLA dashboard, semáforo Yellow, error budget, drift táctico CU-T01/T02, `vw_sre_retention`, taxonomía de roles.

12. **[IMPORTANTE] Limpiar artefactos de template** (`temporal*`, `Buenas prácticas de seguridadde*`, `Desarrollador (Tú)s`, `Stack LGTM (...)`, `Scripts básicos de despliegue`, etc.) en 18+ archivos de specs.

13. **[IMPORTANTE] Wire-up frontend**: sidebar enlaces a `/dashboard/*`, conectar 8 endpoints tácticos a vistas del Command Center, `StrategicRepository` real con PocketBase SDK y MonetDB ODBC.

14. **[IMPORTANTE] Implementar login y RBAC reales** con PocketBase Auth + JWT firmado + middleware de verificación real.

15. **[IMPORTANTE] Añadir tests**: `pytest` en backend (ETL, validator, API, import), `vitest`/`playwright` en frontend (route handlers tácticos, middleware, dashboards).

16. **[IMPORTANTE] Desplegar flight API real**: cambiar `backend/Dockerfile` CMD a `uvicorn api_server:app` y publicar puerto 8000 en `docker-compose.yml`.

17. **[IMPORTANTE] Añadir healthchecks en Docker** y `depends_on` con `condition: service_healthy`.

18. **[MEJORA] Reconciliar roles**: lista canónica en `CONSTITUTION.md` (`SUPER_ADMIN`, `C_LEVEL_EXEC`, `BOARD_MEMBER`, `OPERATOR`, `SRE`, `DATA_ENGINEER`, `ML_ENGINEER`, `FINOPS_MANAGER`, `SECOPS`, `GROWTH_PM`, `DEVREL`, `CUSTOMER_SUCCESS`, `TENANT_ADMIN`).

19. **[MEJORA] Eliminar código legacy**: `backend/src/etl/ingestion_job.py` y `backend/src/etl/generate_mock_csv.py`.

20. **[MEJORA] Reconciliar 3 módulos solapados de circuit-breaker** (`tactical/data_quality_monitor.py`, `quality/data_quality_suite.py`, `etl/data_contract_validator.py`) bajo un solo SSOT.

21. **[MEJORA] Eliminar PII hardcoded** (`BANNED_NAMES=[...,"kacor"]` en `post_mortem_generator.py`) — hacerlo data-driven vía env.
