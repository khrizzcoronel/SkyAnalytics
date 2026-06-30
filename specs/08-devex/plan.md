# Plan Técnico: Developer Experience

## Objetivo
Validación OpenAPI en CI, Developer Portal Mintlify, generación de SDKs y sandbox interactivo.

## Casos de uso incluidos
- CU-O16
- CU-T07

## Usuarios principales
- DevRel
- Developer

## Arquitectura
- Capa de presentación: Next.js (App Router) en rontend/src/app/dashboard/* y rontend/src/app/api/v1/*.
- Capa de dominio: módulos Python bajo ackend/src/ organizados por responsabilidad.
- Capa de datos: PocketBase para configuración/operacional; MonetDB para analítica; S3 para artefactos ML.

## Modelo de datos
Pendiente de detalle en Fase 2. Las colecciones/tablas/vistas relevantes se definen en los CUs listados arriba.

## Endpoints / Componentes / Integraciones
- /api/v1/tactico/devex/sandbox
- Mintlify portal

## Dependencias
- Módulos upstream: ver matriz de dependencias en specs/000-sistema-general/matriz-usuarios-modulos.md.

## Decisiones técnicas
- Cada CU conserva su ID original (CU-OXX, CU-TXX, CU-EXX) para mantener trazabilidad con OpenSpec archivado.
- Las acceptance criteria internas de los CUs se unificarán al namespace CA-08-NNN en Fase 2.
