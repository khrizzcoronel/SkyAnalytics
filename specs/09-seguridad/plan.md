# Plan Técnico: Seguridad

## Objetivo
Pipeline SAST/DAST/SCA, alertas de seguridad WAF/GuardDuty, auto-remediación y auditoría.

## Casos de uso incluidos
- CU-O18
- CU-T06

## Usuarios principales
- SecOps
- SRE

## Arquitectura
- Capa de presentación: Next.js (App Router) en rontend/src/app/dashboard/* y rontend/src/app/api/v1/*.
- Capa de dominio: módulos Python bajo ackend/src/ organizados por responsabilidad.
- Capa de datos: PocketBase para configuración/operacional; MonetDB para analítica; S3 para artefactos ML.

## Modelo de datos
Pendiente de detalle en Fase 2. Las colecciones/tablas/vistas relevantes se definen en los CUs listados arriba.

## Endpoints / Componentes / Integraciones
- SonarQube
- Snyk
- OWASP ZAP
- GitHub Actions

## Dependencias
- Módulos upstream: ver matriz de dependencias en specs/000-sistema-general/matriz-usuarios-modulos.md.

## Decisiones técnicas
- Cada CU conserva su ID original (CU-OXX, CU-TXX, CU-EXX) para mantener trazabilidad con OpenSpec archivado.
- Las acceptance criteria internas de los CUs se unificarán al namespace CA-09-NNN en Fase 2.
