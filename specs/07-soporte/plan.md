# Plan Técnico: Soporte y Operaciones

## Objetivo
Triage de bugs, FAQ RAG para deflection, y gestión automatizada de sprints.

## Casos de uso incluidos
- CU-O08
- CU-O14
- CU-O15

## Usuarios principales
- Customer Success
- Product Manager

## Arquitectura
- Capa de presentación: Next.js (App Router) en rontend/src/app/dashboard/* y rontend/src/app/api/v1/*.
- Capa de dominio: módulos Python bajo ackend/src/ organizados por responsabilidad.
- Capa de datos: PocketBase para configuración/operacional; MonetDB para analítica; S3 para artefactos ML.

## Modelo de datos
Pendiente de detalle en Fase 2. Las colecciones/tablas/vistas relevantes se definen en los CUs listados arriba.

## Endpoints / Componentes / Integraciones
- /api/v1/tactico/security/alert (bug severity)
- GitHub/Linear webhooks
- Pinecone/Weaviate vector DB

## Dependencias
- Módulos upstream: ver matriz de dependencias en specs/000-sistema-general/matriz-usuarios-modulos.md.

## Decisiones técnicas
- Cada CU conserva su ID original (CU-OXX, CU-TXX, CU-EXX) para mantener trazabilidad con OpenSpec archivado.
- Las acceptance criteria internas de los CUs se unificarán al namespace CA-07-NNN en Fase 2.
