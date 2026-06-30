# Plan Técnico: BI Estratégico

## Objetivo
Dashboards BSC, finanzas (ARR/LTV/CAC), SRE/SLA, compliance y eNPS/people analytics.

## Casos de uso incluidos
- CU-O06
- CU-E01
- CU-E02
- CU-E03
- CU-E04
- CU-E06

## Usuarios principales
- Founder
- C_LEVEL_EXEC
- BOARD_MEMBER

## Arquitectura
- Capa de presentación: Next.js (App Router) en rontend/src/app/dashboard/* y rontend/src/app/api/v1/*.
- Capa de dominio: módulos Python bajo ackend/src/ organizados por responsabilidad.
- Capa de datos: PocketBase para configuración/operacional; MonetDB para analítica; S3 para artefactos ML.

## Modelo de datos
Pendiente de detalle en Fase 2. Las colecciones/tablas/vistas relevantes se definen en los CUs listados arriba.

## Endpoints / Componentes / Integraciones
- /api/v1/estrategico/bsc/summary
- /api/v1/estrategico/finance/metrics
- /api/v1/estrategico/engineering/health
- /api/v1/estrategico/compliance/controls
- /api/v1/estrategico/hr/burnout

## Dependencias
- Módulos upstream: ver matriz de dependencias en specs/000-sistema-general/matriz-usuarios-modulos.md.

## Decisiones técnicas
- Cada CU conserva su ID original (CU-OXX, CU-TXX, CU-EXX) para mantener trazabilidad con OpenSpec archivado.
- Las acceptance criteria internas de los CUs se unificarán al namespace CA-05-NNN en Fase 2.
