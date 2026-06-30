# Plan Técnico: Growth y Monetización

## Objetivo
Campañas growth HubSpot, publicación en RapidAPI, guardias IaC y pricing A/B testing.

## Casos de uso incluidos
- CU-T01
- CU-T02
- CU-T03
- CU-T10

## Usuarios principales
- Growth PM
- Product Manager

## Arquitectura
- Capa de presentación: Next.js (App Router) en rontend/src/app/dashboard/* y rontend/src/app/api/v1/*.
- Capa de dominio: módulos Python bajo ackend/src/ organizados por responsabilidad.
- Capa de datos: PocketBase para configuración/operacional; MonetDB para analítica; S3 para artefactos ML.

## Modelo de datos
Pendiente de detalle en Fase 2. Las colecciones/tablas/vistas relevantes se definen en los CUs listados arriba.

## Endpoints / Componentes / Integraciones
- /api/v1/tactico/hubspot
- /api/v1/tactico/rapidapi
- /api/v1/tactico/cicd/guard
- /api/v1/tactico/growth/abtest

## Dependencias
- Módulos upstream: ver matriz de dependencias en specs/000-sistema-general/matriz-usuarios-modulos.md.

## Decisiones técnicas
- Cada CU conserva su ID original (CU-OXX, CU-TXX, CU-EXX) para mantener trazabilidad con OpenSpec archivado.
- Las acceptance criteria internas de los CUs se unificarán al namespace CA-11-NNN en Fase 2.
