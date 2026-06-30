# Plan Técnico: OKR y Talento

## Objetivo
Simulador what-if de metas trimestrales y publicación de OKRs vinculados al BSC.

## Casos de uso incluidos
- CU-E05

## Usuarios principales
- Founder
- C_LEVEL_EXEC

## Arquitectura
- Capa de presentación: Next.js (App Router) en rontend/src/app/dashboard/* y rontend/src/app/api/v1/*.
- Capa de dominio: módulos Python bajo ackend/src/ organizados por responsabilidad.
- Capa de datos: PocketBase para configuración/operacional; MonetDB para analítica; S3 para artefactos ML.

## Modelo de datos
Pendiente de detalle en Fase 2. Las colecciones/tablas/vistas relevantes se definen en los CUs listados arriba.

## Endpoints / Componentes / Integraciones
- /api/v1/estrategico/targets
- PocketBase strategic_targets

## Dependencias
- Módulos upstream: ver matriz de dependencias en specs/000-sistema-general/matriz-usuarios-modulos.md.

## Decisiones técnicas
- Cada CU conserva su ID original (CU-OXX, CU-TXX, CU-EXX) para mantener trazabilidad con OpenSpec archivado.
- Las acceptance criteria internas de los CUs se unificarán al namespace CA-13-NNN en Fase 2.
