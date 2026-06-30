# Plan Técnico: Data Pipeline

## Objetivo
Ingesta incremental CSV, validación de calidad, contratos de datos, ETL a MonetDB Star Schema, drift monitoring y quarantine.

## Casos de uso incluidos
- CU-O03
- CU-O04
- CU-O17
- CU-O21
- CU-O22
- CU-O23
- CU-T04

## Usuarios principales
- Data Engineer
- SRE

## Arquitectura
- Capa de presentación: Next.js (App Router) en rontend/src/app/dashboard/* y rontend/src/app/api/v1/*.
- Capa de dominio: módulos Python bajo ackend/src/ organizados por responsabilidad.
- Capa de datos: PocketBase para configuración/operacional; MonetDB para analítica; S3 para artefactos ML.

## Modelo de datos
Pendiente de detalle en Fase 2. Las colecciones/tablas/vistas relevantes se definen en los CUs listados arriba.

## Endpoints / Componentes / Integraciones
- N/A - GitHub Actions cron
- /api/v1/tactico/cicd/guard

## Dependencias
- Módulos upstream: ver matriz de dependencias en specs/000-sistema-general/matriz-usuarios-modulos.md.

## Decisiones técnicas
- Cada CU conserva su ID original (CU-OXX, CU-TXX, CU-EXX) para mantener trazabilidad con OpenSpec archivado.
- Las acceptance criteria internas de los CUs se unificarán al namespace CA-03-NNN en Fase 2.
