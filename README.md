# SkyAnalytics

SkyAnalytics es una plataforma SaaS B2B de inteligencia aeronáutica predictiva. Convierte macrodatos históricos y en tiempo real del Bureau of Transportation Statistics (BTS) en APIs predictivas y dashboards self-service para aerolíneas, agencias de viaje, operadores logísticos y entidades gubernamentales.

## Arquitectura

El sistema sigue **Spec Driven Development (SDD)** con **Spec Kit** y **OpenSpec**.

- **Frontend:** Next.js 16 (App Router) + React 19 + TypeScript + Tailwind v4
- **Backend:** Python 3.11 + FastAPI (flight API) + scripts ETL/ML
- **Bases de datos híbridas:**
  - **PocketBase** (SQLite): OLTP, autenticación, tenants, metas estratégicas, budgets.
  - **MonetDB** (columnar): OLAP, star schema `fact_flights`, vistas analíticas.
- **Ingeniería de datos:** ETL incremental PocketBase → MonetDB, quarantine, data contracts, drift PSI, feature engineering.
- **Machine Learning:** XGBoost/LightGBM, MLflow tracking, registry, champion/challenger, deep learning spot.
- **Contenedores:** Docker + docker-compose.

## Estructura del repositorio

```
SkyAnalytics/
├── backend/              # Python backend, ETL, ML, security, ops
│   ├── src/              # Código fuente por dominio
│   ├── import/           # Importador incremental CSV → PocketBase
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/             # Next.js App Router
│   ├── src/app/          # Pages y API routes
│   ├── src/components/   # Componentes React
│   └── Dockerfile
├── specs/                # Especificaciones SDD
│   ├── 000-sistema-general/   # Constitución, auditoría, plan de corrección
│   ├── 01-identidad-acceso/   # CU-O01, CU-O12
│   ├── 02-api-vuelos/         # CU-O02
│   ├── 03-data-pipeline/      # CU-O03, CU-O04, CU-O17, CU-O21..O24, CU-T04
│   ├── 04-ml/                 # CU-O05, CU-O20, CU-T05
│   ├── 05-bi-estrategico/     # CU-O06, CU-E01..E04, CU-E06
│   ├── 06-observabilidad-sre/ # CU-O07, CU-O09..O11, CU-O13
│   ├── 07-soporte/            # CU-O08, CU-O14, CU-O15
│   ├── 08-devex/              # CU-O16, CU-T07
│   ├── 09-seguridad/          # CU-O18, CU-T06
│   ├── 10-finops/             # CU-O19, CU-T08
│   ├── 11-growth-monetization/# CU-T01..T03, CU-T10
│   ├── 12-resilience-testing/ # CU-T09
│   └── 13-okr-talento/        # CU-E05
├── openspec/             # Changes y capabilities OpenSpec
│   ├── changes/archive/  # Historial de changes (congelado)
│   ├── changes/          # Changes activos
│   └── specs/            # Capabilities consolidadas
├── docker-compose.yml    # Orquestación local
├── .env.example          # Variables de entorno de ejemplo
└── pb_schema.json        # Schema base de PocketBase
```

## Requisitos

- Docker Engine 24+
- Docker Compose v2+
- (Opcional) Python 3.11+ y Node.js 20+ para desarrollo local fuera de Docker
- Cuentas externas (solo en producción): Stripe, HubSpot, Sentry, AWS, Slack, Pinecone/Weaviate, etc.

## Configuración inicial

1. Copiar variables de entorno:

```bash
cp .env.example .env
# Edita .env con tus secretos reales
```

2. Levantar la infraestructura:

```bash
docker-compose up -d
```

3. Importar el schema de PocketBase (si no se monta automáticamente):

```bash
docker-compose exec pocketbase /usr/local/bin/pocketbase superuser upsert email@example.com password
# Luego importar pb_schema.json vía UI o API
```

4. Ejecutar el importador de vuelos:

```bash
docker-compose run --rm importer
# Repetir hasta completar el dataset (7.08M filas, 1.25 GB)
```

5. Ejecutar el ETL a MonetDB:

```bash
docker-compose exec backend python src/etl/etl_flights_to_monetdb.py
```

6. Acceder:
   - Frontend: http://localhost:3000
   - PocketBase Admin: http://localhost:8090/_/
   - Backend API: http://localhost:8000
   - MonetDB: localhost:50000

## Desarrollo

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.api_server:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Tests

```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm run test        # vitest
npm run test:e2e    # playwright
```

## Variables de entorno principales

Ver `.env.example` para la lista completa. Las más críticas:

| Variable | Descripción |
|---|---|
| `MONETDB_PASS` | Contraseña del admin de MonetDB |
| `RAPIDAPI_PROXY_SECRET` | Secret para validar requests de RapidAPI |
| `POCKETBASE_URL` | URL base de PocketBase (`http://pocketbase:8090` en Docker) |
| `POCKETBASE_ADMIN_EMAIL` / `POCKETBASE_ADMIN_PASSWORD` | Credenciales superuser |
| `S3_ML_BUCKET` | Bucket S3 para modelos/features (`skyanalytics-ml`) |
| `SLACK_WEBHOOK_URL` | Webhook para alertas drift/error budget |
| `SENTRY_DSN` / `SENTRY_TOKEN` | Telemetría SRE |
| `STRIPE_SECRET_KEY` | Datos financieros CU-E02 |
| `HUBSPOT_API_KEY` | Integración growth CU-T01 |

## Decisiones técnicas clave

- **OLTP vs OLAP:** PocketBase para transacciones/configuración; MonetDB para analítica masiva.
- **API-First:** contratos definidos en specs antes de implementar.
- **Zero Trust:** secretos solo por variables de entorno; sin valores por defecto en código/compose.
- **Tolerancia a fallos parciales:** filas corruptas van a `Quarantine_Data` sin abortar el ETL.
- **Dataset semilla:** BTS 2024, importado incrementalmente con checkpoint JSON.

## Seguridad

- TLS 1.3 para datos en tránsito (producción vía Caddy/nginx).
- AES-256 para datos en reposo (S3 KMS, MonetDB TLS).
- RBAC con roles definidos en `specs/000-sistema-general/CONSTITUTION.md`.
- SAST/DAST en CI/CD.

## Más información

- `specs/000-sistema-general/CONSTITUTION.md` — reglas globales del sistema.
- `specs/000-sistema-general/AUDITORIA.md` — estado actual del proyecto.
- `specs/000-sistema-general/PLAN_CORRECCION.md` — plan de corrección y mejora.

## Licencia

Privado — SkyAnalytics.
