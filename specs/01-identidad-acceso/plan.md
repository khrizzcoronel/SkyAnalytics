# Plan Técnico: Identidad y Acceso

## Objetivo
Onboarding de tenants, generación de API keys, autenticación M2M y auditoría/rotación de credenciales IAM.

## Casos de uso incluidos
- CU-O01
- CU-O12

## Usuarios principales
- Cliente B2B
- SRE
- SUPER_ADMIN

## Arquitectura
- Capa de presentación: Next.js (App Router) en rontend/src/app/dashboard/* y rontend/src/app/api/v1/*.
- Capa de dominio: módulos Python bajo ackend/src/ organizados por responsabilidad.
- Capa de datos: PocketBase para configuración/operacional; MonetDB para analítica; S3 para artefactos ML.

## Modelo de datos
Pendiente de detalle en Fase 2. Las colecciones/tablas/vistas relevantes se definen en los CUs listados arriba.

## Endpoints / Componentes / Integraciones
- POST /api/v1/auth/login
- POST /api/v1/tenants
- GET /v1/flights/{id}

## Dependencias
- Módulos upstream: ver matriz de dependencias en specs/000-sistema-general/matriz-usuarios-modulos.md.

## Decisiones técnicas
- Cada CU conserva su ID original (CU-OXX, CU-TXX, CU-EXX) para mantener trazabilidad con OpenSpec archivado.
- Las acceptance criteria internas de los CUs se unificarán al namespace CA-01-NNN en Fase 2.
