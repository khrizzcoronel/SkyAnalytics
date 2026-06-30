# PLAN DE CORRECCIÓN Y MEJORA — SkyAnalytics

> Generado tras auditoría SDD del 2026-06-29.
> Alcance: correcciones puntuales (Fase 0) + reorganización por dominios + implementación real + tests + Docker hardened.
> Principios acordados:
> - Reorganización física completa de `specs/` por dominios funcionales y usuarios.
> - 36 changes OpenSpec archivados se congelan como historial; los nuevos cambios van en carpetas nuevas.
> - "TODO real primero": cada módulo se entrega con integraciones reales y tests, no scripts stdout.

---

## FASE 0 — CORRECCIONES CRÍTICAS (stop the bleeding)

**Duración estimada:** 2-3 días.  
**Objetivo:** arreglar los problemas que bloquean el setup, la seguridad básica y la privacidad antes de cualquier reestructuración mayor.

### F0.1 — Documentación y configuración

| ID | Tarea | Archivo(s) | Criterio de aceptación |
|---|---|---|---|
| F0.1.1 | Escribir `README.md` con descripción, arquitectura, setup paso a paso, variables de entorno y mapeo CU→módulo→endpoint. | `README.md` | Un nuevo dev puede levantar el proyecto con `docker-compose up` siguiendo solo el README. |
| F0.1.2 | Crear `.env.example` con todas las variables obligatorias y opcionales. | `.env.example` | `cp .env.example .env && docker-compose up` funciona en local (con valores dummy donde aplique). |
| F0.1.3 | Eliminar defaults hardcoded de secretos en `docker-compose.yml`. | `docker-compose.yml` L10-L11, L21, L55 | Ningún secret tiene valor por defecto en el compose; todo se lee del `.env`. |

### F0.2 — Backend básico funcional

| ID | Tarea | Archivo(s) | Criterio de aceptación |
|---|---|---|---|
| F0.2.1 | Añadir dependencias faltantes a `requirements.txt`: `passlib`, `boto3`, `joblib`, `email-validator`, `pytest`, `pytest-asyncio`, `httpx`, `moto`. | `backend/requirements.txt` | `pip install -r requirements.txt` finaliza sin error. |
| F0.2.2 | Crear colección `tenants` en `pb_schema.json` y completar `tenant_onboarding.py` para persistir vía HTTP API de PocketBase. | `pb_schema.json`, `backend/src/tenant_onboarding.py` | Ejecutar `onboard_new_tenant(...)` crea un registro en PocketBase y devuelve keys one-time. |
| F0.2.3 | Implementar `Quarantine_Data` como tabla MonetDB real en el ETL. | `backend/src/etl/etl_flights_to_monetdb.py`, `backend/src/etl/data_validator.py` | Filas corruptas terminan en `Quarantine_Data` de MonetDB; el proceso no aborta. |
| F0.2.4 | Eliminar passwords hardcoded (`MONETDB_PASS`) en ETL/ML; leer siempre de env. | `backend/src/etl/etl_flights_to_monetdb.py`, `backend/src/ml/feature_engineering.py`, `backend/src/ml/train_xgboost_model.py` | Si falta `MONETDB_PASS`, el proceso falla explícitamente con `KeyError`, no usa default. |
| F0.2.5 | Corregir `FlightResponse` en `api_server.py` (renombrar `_cached` a `cached`). | `backend/src/api_server.py` | El endpoint serializa correctamente el campo `cached: bool`. |
| F0.2.6 | Cambiar `backend/Dockerfile` CMD para exponer `api_server` vía uvicorn en puerto 8000. | `backend/Dockerfile` | `docker run backend` levanta FastAPI en `0.0.0.0:8000`. |
| F0.2.7 | Eliminar `BANNED_NAMES` hardcoded (incluye `"kacor"`); leer desde env. | `backend/src/support/post_mortem_generator.py` | `POSTMORTEM_BANNED_NAMES` puede configurarse sin modificar código. |
| F0.2.8 | Eliminar archivos legacy `ingestion_job.py` y `generate_mock_csv.py`. | `backend/src/etl/ingestion_job.py`, `backend/src/etl/generate_mock_csv.py` | No quedan referencias en el repo. |

### F0.3 — Frontend básico funcional

| ID | Tarea | Archivo(s) | Criterio de aceptación |
|---|---|---|---|
| F0.3.1 | Añadir bloque `@media print` con reglas para `.print-hide`, `.print-watermark`, `.internal-infra`. | `frontend/src/app/globals.css` | Imprimir `/dashboard/engineering` oculta IPs internas, muestra watermark y oculta botones. |
| F0.3.2 | Añadir al sidebar enlaces a `/dashboard/bsc`, `/dashboard/finance`, `/dashboard/engineering`. | `frontend/src/app/layout.tsx` | Usuario navega a dashboards reales sin escribir URL. |
| F0.3.3 | Unificar theme (elegir dark o light; aplicar globalmente). | `frontend/src/app/globals.css`, 3 dashboards | No hay fondos mezclados. |
| F0.3.4 | Reconciliar Error Budget: route handler usa 432 min/mes (99.0 % SLA). | `frontend/src/app/api/v1/estrategico/engineering/health/route.ts`, `frontend/src/app/dashboard/engineering/page.tsx` | Gauge y texto muestran coherencia con SLA 99.0 %. |
| F0.3.5 | Añadir `clearInterval` en el `setInterval` del dashboard engineering. | `frontend/src/app/dashboard/engineering/page.tsx` | Al desmontar el componente se detiene el polling. |
| F0.3.6 | Instalar vitest + @testing-library/react + playwright y añadir script `test`. | `frontend/package.json` | `npm run test` ejecuta sin error (aunque aún no haya tests). |

### F0.4 — Docker hardened

| ID | Tarea | Archivo(s) | Criterio de aceptación |
|---|---|---|---|
| F0.4.1 | Publicar puerto `8000:8000` para el servicio `backend`. | `docker-compose.yml` | El flight API es alcanzable externamente. |
| F0.4.2 | Añadir healthchecks a `pocketbase`, `monetdb`, `backend`, `frontend`. | `docker-compose.yml` | `docker compose ps` muestra todos `healthy` tras el arranque. |
| F0.4.3 | Cambiar `depends_on` a `condition: service_healthy`. | `docker-compose.yml` | `backend` no inicia hasta que `monetdb` y `pocketbase` estén sanos. |
| F0.4.4 | Montar `pb_schema.json` en `pocketbase` con bootstrap automático. | `docker-compose.yml`, script opcional | Al levantar, PocketBase tiene las colecciones definidas. |

### F0.5 — OpenSpec

| ID | Tarea | Archivo(s) | Criterio de aceptación |
|---|---|---|---|
| F0.5.1 | Crear OpenSpec changes para CU-O21, CU-O22, CU-O23, CU-O24. | `openspec/changes/2026-06-29-cu-o21/...` etc. | Cada change tiene `proposal.md`, `design.md`, `tasks.md` y `specs/<capability>/spec.md`. |
| F0.5.2 | Rellenar `openspec/config.yaml` (quitar comentarios de template en context/rules). | `openspec/config.yaml` | El archivo de configuración describe el proyecto real, no plantilla. |

---

## FASE 1 — REORGANIZACIÓN FÍSICA POR DOMINIOS Y USUARIOS

**Duración estimada:** 2-3 días.  
**Objetivo:** migrar de `specs/001,002,003` (por nivel de objetivo) a `specs/01..13` (por dominio funcional + usuario dueño).

### Nueva taxonomía de módulos

| Carpeta | Dominio | CUs migrados | Usuario principal |
|---|---|---|---|
| `01-identidad-acceso` | Auth, Tenant, IAM | CU-O01, CU-O12 | Cliente B2B, SRE |
| `02-api-vuelos` | Flight API, rate-limit, cache | CU-O02 | Cliente B2B (M2M) |
| `03-data-pipeline` | ETL, ingest, quarantine, quality, contracts, drift | CU-O03, CU-O04, CU-O17, CU-O21, CU-O22, CU-O23, CU-O24, CU-T04 | Data Engineer |
| `04-ml` | Training, Champion, Features, DL, Registry | CU-O05, CU-O20, CU-T05 | ML Engineer |
| `05-bi-estrategico` | BI refresh, BSC, Finance, SRE/SLA, Compliance, eNPS | CU-O06, CU-E01, CU-E02, CU-E03, CU-E04, CU-E06 | Founder/C-Level |
| `06-observabilidad-sre` | Telemetry, Error Budget, Changelog, Post-Mortem, DR | CU-O07, CU-O09, CU-O10, CU-O11, CU-O13 | SRE |
| `07-soporte` | Bug triage, FAQ RAG, Sprints | CU-O08, CU-O14, CU-O15 | Customer Success, PM |
| `08-devex` | OpenAPI lint, Developer Portal, SDKs | CU-O16, CU-T07 | DevRel |
| `09-seguridad` | SAST/DAST, Security Alerts | CU-O18, CU-T06 | SecOps |
| `10-finops` | Cloud cost | CU-O19, CU-T08 | FinOps |
| `11-growth-monetization` | Growth, RapidAPI, IaC guard, Pricing A/B | CU-T01, CU-T02, CU-T03, CU-T10 | Growth PM |
| `12-resilience-testing` | Chaos, load tests | CU-T09 | SRE |
| `13-okr-talento` | OKR simulator | CU-E05 | Founder |

### Tareas Fase 1

| ID | Tarea | Criterio de aceptación |
|---|---|---|
| F1.1 | Actualizar `CONSTITUTION.md` con los 13 módulos, roles canónicos y matriz de permisos. | Constitución describe la nueva organización sin ambigüedades. |
| F1.2 | Crear las 13 carpetas y mover los 40 archivos `CU-*.md` preservando IDs. | `glob specs/**/*.md` muestra la nueva estructura; ningún CU se pierde. |
| F1.3 | Crear para cada módulo: `plan.md`, `tasks.md`, `checklist.md`, `usuarios.md`. | Cada módulo tiene 4 documentos de soporte. |
| F1.4 | Crear `specs/000-sistema-general/matriz-usuarios-modulos.md`. | Tabla cruzada usuario × módulo × acciones publicada. |
| F1.5 | Borrar carpetas legacy `specs/001-estrategico`, `specs/002-tactico`, `specs/003-operativo`. | No quedan carpetas numeradas por objetivo. |
| F1.6 | Crear OpenSpec change `2026-06-29-reorganizacion-modulos` (proposal/design/tasks/spec). | Change propuesto con la nueva taxonomía; se archiva al final de la fase. |
| F1.7 | Actualizar `openspec/specs/*` con frontmatter `module` y `primary_user`. | Cada `spec.md` declara a qué módulo y usuario pertenece. |

---

## FASE 2 — TRAZABILIDAD Y CIERRE DE GAPS EN SPECS

**Duración estimada:** 2 días.  
**Objetivo:** specs internamente consistentes, completas y trazables.

### F2.1 — Completar specs mínimas

| ID | Tarea | Archivo(s) |
|---|---|---|
| F2.1.1 | Completar CU-O21 con RN, Entradas, Salidas, CA, Restricciones, Fuera de Alcance. | `specs/03-data-pipeline/CU-O21.md` |
| F2.1.2 | Completar CU-O22 con las mismas secciones. | `specs/03-data-pipeline/CU-O22.md` |
| F2.1.3 | Completar CU-O23 con las mismas secciones. | `specs/03-data-pipeline/CU-O23.md` |
| F2.1.4 | Completar CU-O24 con las mismas secciones. | `specs/03-data-pipeline/CU-O24.md` |

### F2.2 — Unificar namespace de Criterios de Aceptación

| ID | Tarea | Archivo(s) |
|---|---|---|
| F2.2.1 | Definir esquema `CA-<MOD>-<NNN>` donde `<MOD>` es código corto del módulo nuevo. | Documento en `specs/000-sistema-general/` |
| F2.2.2 | Renombrar `CA-{F,B,E,S,P}-NN` a `CA-<MOD>-NNN` en todos los `checklist.md` y `tasks.md`. | 13 módulos |
| F2.2.3 | Actualizar los `CA-OXX/TXX/EXX-NNN` internos de los 40 CUs al nuevo esquema. | 40 CU specs |

Códigos de módulo:
- `IDN` = 01-identidad-acceso
- `APV` = 02-api-vuelos
- `DAT` = 03-data-pipeline
- `ML` = 04-ml
- `BIE` = 05-bi-estrategico
- `OBS` = 06-observabilidad-sre
- `SOP` = 07-soporte
- `DVX` = 08-devex
- `SEC` = 09-seguridad
- `FIN` = 10-finops
- `GRW` = 11-growth-monetization
- `RES` = 12-resilience-testing
- `OKR` = 13-okr-talento

### F2.3 — Reconciliar inconsistencias cross-doc

| ID | Tema | Decisión | Archivos a actualizar | Estado |
|---|---|---|---|---|
| F2.3.1 | Cron ETL | 03:00 AM (gana RNF-O21-001). | `CU-O03.md`, `CU-O21.md` | ✅ Hecho |
| F2.3.2 | Bucket S3 ML | `skyanalytics-ml` (gana CU-O05/O24). | `CU-O05.md`, `CU-O24.md` | ✅ Hecho |
| F2.3.3 | SLA dashboard BSC | 2 s p95 (gana RNF-E01-001). | `CU-E01.md` | ✅ Hecho |
| F2.3.4 | Semáforo Yellow | 80–99.9 % de meta (gana RN-E01-001). | `CU-E01.md` | ✅ Hecho |
| F2.3.5 | Error Budget | 432 min/mes para SLA 99.0 %. | `CU-E03.md`, `CU-O10.md`, `CONSTITUTION.md` | ✅ Hecho |
| F2.3.6 | Drift táctico CU-T01/T02 | CU-T01 = HubSpot Growth, CU-T02 = RapidAPI. Reescribir `11-growth-monetization/plan.md`, `tasks.md`, `checklist.md`. | Módulo 11 | ✅ Hecho (reorganización Fase 1) |
| F2.3.7 | `vw_sre_retention` | Renombrar a `vw_people_analytics`, ajustar columnas al scope CU-E06. | `CU-E06.md` | ✅ Hecho (reorganización Fase 1) |
| F2.3.8 | Roles | Lista canónica en `CONSTITUTION.md`; actualizar specs con roles permitidos. | `CONSTITUTION.md`, `matriz-usuarios-modulos.md` | ✅ Hecho |

### F2.4 — Limpiar artefactos de template

| ID | Patrón a limpiar | Reemplazo | Estado |
|---|---|---|---|
| F2.4.1 | `temporal*`, `temporalmente`, `temporales` | Palabra correcta según contexto ("enlace", "regional", "temporal", etc.) | ✅ Hecho (son usos legítimos) |
| F2.4.2 | `Buenas prácticas de seguridadde*`, `...requiere*`, `...y*` | "seguridad de", "seguridad requiere", "seguridad y" | ✅ Hecho (reemplazado por SOC 2 / ISO 27001) |
| F2.4.3 | `Desarrollador (Tú)ing`, `...s`, `el equipo de Desarrollador (Tú)s` | "Ingeniería", "desarrolladores" | ✅ Hecho |
| F2.4.4 | `Stack LGTM (Archivos de Log, Dashboard Básico / Sentry, Logs, Sentry / Logs)` | "Grafana LGTM stack" | ✅ Hecho |
| F2.4.5 | `Scripts básicos de despliegue` | "Terraform" (cuando se refiere a IaC) | ✅ Hecho |
| F2.4.6 | `Tracking básico o local` | "MLflow" | ✅ Hecho |
| F2.4.7 | `Feast Feature Store / S3` | "Feast Feature Store / S3" | ✅ Hecho |
| F2.4.8 | `Panel de facturación del PaaS API` | "AWS Cost Explorer API" | ✅ Hecho |
| F2.4.9 | `Rate Limiter en código (Web Application Firewall)` | "WAF (AWS)" | ✅ Hecho |
| F2.4.10 | `Alertas básicas` | "GuardDuty" | ✅ Hecho |

### F2.5 — Cerrar gaps de CAs y secciones

| ID | Tarea | Archivo(s) | Estado |
|---|---|---|---|
| F2.5.1 | Añadir CA para "failover recommendation" en CU-E03. | `05-bi-estrategico/CU-E03.md` | ✅ Hecho |
| F2.5.2 | Añadir CAs para inmutabilidad (RNF-E04-001) y firma digital (RNF-E04-002) en CU-E04. | `05-bi-estrategico/CU-E04.md` | ✅ Hecho |
| F2.5.3 | Añadir CAs para Event Sourcing (RNF-E05-002) y Slack notification (RF-E05-004) en CU-E05. | `13-okr-talento/CU-E05.md` | ✅ Hecho |
| F2.5.4 | Añadir CA para anonimato absoluto (RNF-E06-001) en CU-E06. | `05-bi-estrategico/CU-E06.md` | ✅ Hecho |
| F2.5.5 | Decidir y documentar Status Page: crear CU-O25 en `11-growth-monetization` o reformular como regla transversal. | `CONSTITUTION.md`, `11-growth-monetization/` | ✅ Hecho (regla transversal en `CONSTITUTION.md`) |
| F2.5.6 | Definir cuota "Ultra" en RN-T02-001. | `11-growth-monetization/CU-T02.md` | ✅ Hecho |
| F2.5.7 | Añadir sección 14 faltante a CU-T04, T07, T08, T09, T10. | `11-growth-monetization/`, `08-devex/`, `10-finops/`, `12-resilience-testing/` | ✅ Hecho |

### F2.6 — OpenSpec gaps

| ID | Tarea | Archivo(s) |
|---|---|---|
| F2.6.1 | Actualizar OpenSpec changes CU-O21..O24 con el template completo post-F2.1. | `openspec/changes/2026-06-29-cu-o21/...` |
| F2.6.2 | Crear capability specs delta para CU-O21..O24 en `openspec/specs/`. | `openspec/specs/etl-star-schema/`, `.../raw-importer/`, `.../drift-monitor/`, `.../feature-engineering/` |

---

## FASE 3 — IMPLEMENTACIÓN REAL POR MÓDULO

**Duración estimada:** 4-6 semanas FT (o 3-4 meses part-time).  
**Objetivo:** sustituir cada script demo por un servicio real con integraciones externas, tests y Docker hardened.

Cada sub-fase sigue el mismo ritual:
1. Sustituir demo por integración real (PocketBase HTTP, Slack, S3, GitHub, Stripe, Linear, HubSpot, Sentry, AWS, etc.).
2. Añadir tests pytest/vitest que cubran â‰¥80 % de RN/CA del módulo.
3. Añadir healthcheck y config `.env`.
4. Documentar en README del módulo.

---

### 3A — `01-identidad-acceso` + `02-api-vuelos` (backbone cliente)

**Duración:** 4-5 días.

| ID | Tarea | Archivo(s) |
|---|---|---|
| F3A.1 | Colección `tenants` en `pb_schema.json` con RBAC. | `pb_schema.json` |
| F3A.2 | Persistencia real en PocketBase HTTP API. | `backend/src/tenant_onboarding.py` |
| F3A.3 | Login endpoint `/api/v1/auth/login` y middleware JWT real. | `backend/src/api_server.py` nuevo módulo auth |
| F3A.4 | Cache real con Redis; rate-limit por tenant en Redis. | `backend/src/api_server.py`, `docker-compose.yml` (servicio redis) |
| F3A.5 | Endpoint `/v1/flights/{id}` consulta MonetDB real (`vw_delay_analysis`). | `backend/src/api_server.py` |
| F3A.6 | Tests pytest: tenant CRUD, key hash/verify, API 401/429/200, cache hit/miss. | `backend/tests/` |
| F3A.7 | Docker: backend CMD uvicorn, puerto 8000, healthcheck `/api/health`. | `backend/Dockerfile`, `docker-compose.yml` |

---

### 3B — `03-data-pipeline` + `04-ml` (backbone datos y ML)

**Duración:** 5-7 días.

| ID | Tarea | Archivo(s) |
|---|---|---|
| F3B.1 | `Quarantine_Data` MonetDB real; unificar `data_validator` + `data_quality_suite` + `data_contract_validator` bajo `quality/contracts.py` como SSOT. | `backend/src/etl/*`, `backend/src/quality/*`, `backend/src/tactical/data_quality_monitor.py` |
| F3B.2 | Upload S3 real con KMS AES-256 en feature engineering. | `backend/src/ml/feature_engineering.py` |
| F3B.3 | ML training con S3 real + MLflow tracking local (o hosted). | `backend/src/ml/train_xgboost_model.py` |
| F3B.4 | Drift monitor con Slack webhook real. | `backend/src/quality/dataset_drift_monitor.py` |
| F3B.5 | MLOps registry persistente en MLflow. | `backend/src/tactical/mlops_registry.py` |
| F3B.6 | DL experiment runner con EC2 Spot real o `DL_SIMULATE=true`. | `backend/src/ml/dl_experiment_runner.py` |
| F3B.7 | Workflows GitHub Actions: ETL 03:00, features Sundays 05:00, drift Mondays 06:00. | `.github/workflows/` |
| F3B.8 | Tests pytest para ETL idempotencia, quarantine, drift PSI, ML registry, feature upload. | `backend/tests/` |
| F3B.9 | Docker: servicios `mlflow`, `redis`; healthchecks. | `docker-compose.yml` |

---

### 3C — `05-bi-estrategico` + `13-okr-talento` (dashboards del Founder)

**Duración:** 5-7 días.

| ID | Tarea | Archivo(s) |
|---|---|---|
| F3C.1 | `StrategicRepository.ts` real: PocketBase SDK + MonetDB ODBC/query. | `frontend/src/lib/services/StrategicRepository.ts` |
| F3C.2 | Route handlers reales: `/bsc/summary`, `/bsc/history/:kpi`, `/finance/metrics`, `/engineering/health`, `/compliance/controls`, `/hr/burnout`, `/targets`. | `frontend/src/app/api/v1/estrategico/**/*` |
| F3C.3 | Finance dashboard consume Stripe API real. | `frontend/src/app/api/v1/estrategico/finance/metrics/route.ts` |
| F3C.4 | Engineering dashboard consume Sentry API real. | `frontend/src/app/api/v1/estrategico/engineering/health/route.ts` |
| F3C.5 | Compliance dashboard consume AWS Security Hub real. | `backend/src/strategic/compliance_dashboard.py` + route |
| F3C.6 | eNPS analyzer consume Typeform API y guarda en PocketBase `enps_responses`. | `backend/src/strategic/people_analytics.py` |
| F3C.7 | OKR simulator persiste en `strategic_targets` y notifica Slack real. | `backend/src/strategic/okr_simulator.py` |
| F3C.8 | `HistoricalChartModal.tsx` consume datos reales de `/bsc/history/:kpi`. | `frontend/src/components/HistoricalChartModal.tsx` |
| F3C.9 | Tests vitest/playwright para dashboards; pytest para backend estratégico. | `frontend/`, `backend/tests/` |

---

### 3D — `06-observabilidad-sre` + `09-seguridad` + `10-finops` + `12-resilience-testing`

**Duración:** 5-7 días.

| ID | Tarea | Archivo(s) |
|---|---|---|
| F3D.1 | OpenTelemetry logger con OTLP exporter a `otel-collector`. | `backend/src/telemetry/logger.py`, `docker-compose.yml` |
| F3D.2 | Error Budget gate como GitHub Action real leyendo Sentry. | `backend/src/cicd/error_budget_gate.py`, `.github/workflows/error-budget-gate.yml` |
| F3D.3 | Changelog generator con GitHub Release API. | `backend/src/cicd/changelog_generator.py`, `.github/workflows/release.yml` |
| F3D.4 | Post-mortem publish a GitHub Issues o Notion. | `backend/src/support/post_mortem_generator.py` |
| F3D.5 | DR drill como cron monthly con notificación Slack. | `backend/src/dr/dr_drill_simulator.py`, `.github/workflows/dr-drill.yml` |
| F3D.6 | SAST/DAST real: SonarQube + Snyk/Trivy en PR. | `.github/workflows/sast-scan.yml` |
| F3D.7 | IAM auditor con AWS IAM API real. | `backend/src/security/iam_auditor.py` |
| F3D.8 | Secret rotator con AWS Secrets Manager o GitHub Secrets API. | `backend/src/security/secret_rotator.py` |
| F3D.9 | OpenAPI lint con Spectral en PR. | `.github/workflows/openapi-lint.yml` |
| F3D.10 | Security alerter con GuardDuty/WAF real. | `frontend/src/app/api/v1/tactico/security/alert/route.ts`, backend equivalente |
| F3D.11 | FinOps con AWS Cost Explorer + Infracost en PR. | `backend/src/ops/finops_optimizer.py`, `.github/workflows/iac-guard.yml` |
| F3D.12 | Chaos engineering con Litmus/k6 real en staging. | `frontend/src/app/api/v1/tactico/chaos/experiment/route.ts`, `.github/workflows/chaos.yml` |
| F3D.13 | Tests pytest/vitest para cada módulo. | `backend/tests/`, `frontend/` |

---

### 3E — `07-soporte` + `11-growth-monetization`

**Duración:** 4-5 días.

| ID | Tarea | Archivo(s) |
|---|---|---|
| F3E.1 | Bug triage crea/etiqueta GitHub Issues reales. | `backend/src/support/support_triage.py` |
| F3E.2 | FAQ RAG con Pinecone/Weaviate real + embeddings `text-embedding-3-small`. | `backend/src/support/faq_rag_indexer.py` |
| F3E.3 | Sprint webhook con GitHub/Linear real y validación HMAC. | `backend/src/pm/agile_board_webhook.py` |
| F3E.4 | HubSpot growth sync real. | `frontend/src/app/api/v1/tactico/hubspot/route.ts` |
| F3E.5 | RapidAPI gateway real con proxy-secret sin default. | `frontend/src/app/api/v1/tactico/rapidapi/route.ts` |
| F3E.6 | IaC guard con tfsec/checkov real en PR. | `frontend/src/app/api/v1/tactico/cicd/guard/route.ts`, `.github/workflows/iac-guard.yml` |
| F3E.7 | Pricing A/B con Optimizely/VWO real + Stripe grandfathering. | `frontend/src/app/api/v1/tactico/growth/abtest/route.ts` |
| F3E.8 | Tests pytest/vitest para cada integración. | `backend/tests/`, `frontend/` |

---

### 3F — `08-devex` (Developer Portal y SDKs)

**Duración:** 3-4 días.

| ID | Tarea | Archivo(s) |
|---|---|---|
| F3F.1 | Mintlify real bajo `docs/portal/` con deploy en Vercel. | `docs/portal/mint.json` |
| F3F.2 | OpenAPI Generator GH Action publicando SDKs a NPM/PyPI/Maven. | `.github/workflows/sdk-publish.yml` |
| F3F.3 | Sandbox endpoint con auth real y datos mock. | `frontend/src/app/api/v1/tactico/devex/sandbox/route.ts` |
| F3F.4 | Tests para SDK generation y sandbox. | `frontend/`, `.github/workflows/` |

---

### 3G — Frontend unificado (UI, auth, navegación)

**Duración:** 5-7 días.

| ID | Tarea | Archivo(s) |
|---|---|---|
| F3G.1 | Página `/login` con PocketBase Auth (email/password + TOTP MFA). | `frontend/src/app/login/page.tsx` |
| F3G.2 | Middleware real: validar JWT con JWKS de PocketBase, extraer rol. | `frontend/src/middleware.ts` |
| F3G.3 | Contexto de sesión (`useSession`) para identidades dinámicas. | `frontend/src/lib/context/SessionContext.tsx` |
| F3G.4 | Sidebar completa con 13 módulos, respetando permisos por rol. | `frontend/src/app/layout.tsx` |
| F3G.5 | Vistas del Command Center táctico conectadas a los 8 endpoints `/api/v1/tactico/*`. | `frontend/src/app/dashboard/growth/page.tsx`, `.../finops/page.tsx`, etc. |
| F3G.6 | Formularios con `react-hook-form` + `zod`. | vistas tácticas |
| F3G.7 | Types de dominio (`lib/types/*.ts`), eliminar `any` masivo. | `frontend/src/lib/types/` |
| F3G.8 | Tests vitest + Playwright E2E para login, RBAC, dashboards, exports. | `frontend/` |

---

### 3H — Dockerización final + CI/CD

**Duración:** 2-3 días.

| ID | Tarea | Archivo(s) |
|---|---|---|
| F3H.1 | `.env.example` completo (~30 variables). | `.env.example` |
| F3H.2 | `docker-compose.yml` con healthchecks, `depends_on condition: service_healthy`, sin defaults hardcoded. | `docker-compose.yml` |
| F3H.3 | Servicio `caddy` o `nginx` con TLS automático para frontend y pocketbase. | `docker-compose.yml`, `Caddyfile` |
| F3H.4 | MonetDB con TLS 1.3 (`sslmode=require`). | `docker-compose.yml`, docs |
| F3H.5 | CI/CD GitHub Actions: `ci.yml`, `cd.yml`, ETL cron, ML cron, drift cron, SAST, IaC guard, OpenAPI lint, release/changelog. | `.github/workflows/` |
| F3H.6 | Validar `docker-compose up` end-to-end healthy. | validación manual + smoke tests |

---

## Resumen de fases y duraciones

| Fase | Duración estimada | Entregables principales |
|---|---|---|
| **Fase 0** — Correcciones críticas | 2-3 días | README, .env.example, requirements fix, print CSS, quarantine MonetDB, tenant persist, Dockerfile backend, OpenSpec CU-O21..O24 |
| **Fase 1** — Reorganización por dominios | 2-3 días | 13 carpetas specs/, 40 CUs migrados, 13 plan/tasks/checklist/usuarios, CONSTITUTION actualizada, matriz usuario-módulo, OpenSpec reorg change |
| **Fase 2** — Trazabilidad y gaps en specs | 2 días | 40 specs completas, namespace CA unificado, 8 inconsistencias reconciliadas, artefactos limpios |
| **Fase 3A** — Identidad + API Vuelos | 4-5 días | Login real, tenant persist, Redis cache, rate-limit, flight API real en producción |
| **Fase 3B** — Data Pipeline + ML | 5-7 días | ETL real, quarantine MonetDB, MLflow tracking, drift Slack, feature upload S3, GH Actions cron |
| **Fase 3C** — BI Estratégico + OKR | 5-7 días | Dashboards reales (BSC/Finance/Engineering/Compliance/eNPS/OKR), StrategicRepository real |
| **Fase 3D** — Observabilidad + Seguridad + FinOps + Resilience | 5-7 días | OTel, error-budget gate, changelog, DR drill, SAST/DAST, IAM, secret rotation, FinOps, chaos |
| **Fase 3E** — Soporte + Growth | 4-5 días | GitHub Issues triage, Pinecone RAG, Linear webhook, HubSpot, RapidAPI, pricing A/B |
| **Fase 3F** — DevEx | 3-4 días | Mintlify portal, SDK generation, sandbox auth |
| **Fase 3G** — Frontend unificado | 5-7 días | Login, RBAC real, sidebar, Command Center táctico, formularios, types, tests |
| **Fase 3H** — Docker + CI/CD final | 2-3 días | Healthchecks, TLS, Caddy, GH Actions full pipeline |

**Total estimado:** 6-8 semanas full-time; 3-4 meses part-time.

---

## Próximo paso inmediato

Una vez aprobado este plan, comenzar **Fase 0**:

1. Escribir `README.md`.
2. Crear `.env.example`.
3. Corregir `backend/requirements.txt`.
4. Arreglar `@media print` CSS.
5. Crear colección `tenants` y persistir onboarding.
6. Implementar `Quarantine_Data` en MonetDB.
7. Cambiar `backend/Dockerfile` CMD a uvicorn.
8. Crear OpenSpec changes CU-O21..O24.

¿Autorizas iniciar la ejecución de la Fase 0?
