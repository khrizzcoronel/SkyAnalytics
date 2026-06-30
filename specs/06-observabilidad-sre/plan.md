# Plan Técnico: Observabilidad y SRE

## Objetivo
Telemetría OpenTelemetry, logs PII-scrubbed, error budget, changelog automático, post-mortem y DR drills.

## Casos de uso incluidos
- CU-O07
- CU-O09
- CU-O10
- CU-O11
- CU-O13

## Usuarios principales
- SRE
- DevOps

## Arquitectura
- Capa de presentación: Next.js (App Router) en rontend/src/app/dashboard/* y rontend/src/app/api/v1/*.
- Capa de dominio: módulos Python bajo ackend/src/ organizados por responsabilidad.
- Capa de datos: PocketBase para configuración/operacional; MonetDB para analítica; S3 para artefactos ML.

## Modelo de datos
Pendiente de detalle en Fase 2. Las colecciones/tablas/vistas relevantes se definen en los CUs listados arriba.

## Endpoints / Componentes / Integraciones
- OTel collector
- GitHub Actions

## Dependencias
- Módulos upstream: ver matriz de dependencias en specs/000-sistema-general/matriz-usuarios-modulos.md.

## Decisiones técnicas
- Cada CU conserva su ID original (CU-OXX, CU-TXX, CU-EXX) para mantener trazabilidad con OpenSpec archivado.
- Las acceptance criteria internas de los CUs se unificarán al namespace CA-06-NNN en Fase 2.
