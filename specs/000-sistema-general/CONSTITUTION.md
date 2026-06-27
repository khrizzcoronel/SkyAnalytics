# Constitución del Sistema SkyAnalytics

## 1. Nombre y Propósito General del Sistema
**Nombre del Sistema:** SkyAnalytics
**Propósito General:** SkyAnalytics es una plataforma SaaS B2B y un ecosistema de datos diseñado para proveer inteligencia aeronáutica predictiva accionable. Su objetivo es convertir macrodatos (Big Data) históricos y en tiempo real en APIs predictivas y dashboards self-service. Está enfocado en aerolíneas, agencias de viaje, operadores logísticos y entidades gubernamentales para optimizar operaciones comerciales, predecir retrasos, evaluar impacto climático y mejorar rutas.

## 2. Stack Tecnológico
El ecosistema adopta un enfoque moderno, *cloud-native* y orientado a alta disponibilidad:

*   **Infraestructura y Despliegue:** Plataforma PaaS (Render/Railway) o Serverless gestionado mediante Infrastructure as Code (IaC) con Scripts básicos de despliegue.
*   **API y Gateway:** API Gateway del framework. Soporte para APIs REST y GraphQL.
*   **Bases de Datos:** Arquitectura híbrida compuesta por **PocketBase** (Base de Datos Operativa/Transaccional basada en SQLite) y **MonetDB** (Data Warehouse columnar masivo para Analítica).
*   **Ingeniería de Datos:** GitHub Actions (Cron) (orquestación), dbt (transformación), Validaciones nativas (Pydantic/Zod) (validación de calidad).
*   **Machine Learning (MLOps):** Tracking básico o local (tracking y registry), Archivos Parquet locales, XGBoost / LightGBM (modelos core), SHAP (explainability), y Whisper/TrOCR (Deep Learning para NLP/OCR).
*   **CI/CD:** GitHub Actions.
*   **Observabilidad:** Logs estándar y Sentry para errores y Notificaciones de Slack.
*   **Documentación y SDKs:** Mintlify (Developer Portal), OpenAPI Generator (SDKs en Python, JS, Java).

## 3. Reglas de Arquitectura
*   **Cloud-Native y Alta Disponibilidad:** Arquitectura basada en servicios sobre contenedores. Despliegue Single-region con auto-scaling horizontal y CDNs multi-proveedor (CloudFront/Cloudflare).
*   **Specification-Driven Development:** El diseño de APIs debe regirse estrictamente por la filosofía *API-First*, utilizando contratos OpenAPI 3.1 como fuente única de verdad.
*   **Data Contracts:** Se deben establecer contratos de datos formales entre productores y consumidores para asegurar la compatibilidad y evitar rupturas silenciosas (schema drift).
*   **Gestión de Decisiones:** Toda decisión arquitectónica crítica debe documentarse obligatoriamente mediante *Architecture Decision Records* (ADRs).

## 4. Estándares de Código
*   **Versionado:** Todo el código y la infraestructura deben estar versionados en Git. Se debe seguir un modelo estricto de **Semantic Versioning (SemVer)** para releases y APIs.
*   **Linter de APIs:** Los contratos OpenAPI deben validarse automáticamente con **Spectral linter** para asegurar consistencia estilística y evitar breaking changes no documentados.
*   **Control de Calidad (PRs):** Todo cambio en código o infraestructura requiere revisión por pares (PR review) antes de ser fusionado (*merged*) y aplicado (*applied*).

## 5. Reglas de Seguridad Generales
*   **Filosofía Zero Trust:** No se confía por defecto en ningún tráfico interno ni externo.
*   **Cifrado:** Obligatorio el cifrado End-to-End. **TLS 1.3** para datos en tránsito y **AES-256** para datos en reposo (KMS).
*   **Gestión de Secretos:** Prohibido almacenar credenciales en código. Uso exclusivo de **Variables de Entorno (.env)** con rotación automática mensual.
*   **DevSecOps:** Ejecución obligatoria de escaneos estáticos (SAST - SonarQube) y dinámicos (DAST - OWASP ZAP) en el pipeline de CI/CD. Vulnerabilidades críticas o altas bloquean automáticamente el merge.
*   **Auditoría y Compliance:** La arquitectura debe diseñarse previendo el cumplimiento estricto de normativas Buenas prácticas de seguridad, Higiene de seguridad, GDPR y lineamientos IATA. Auditorías IAM trimestrales obligatorias.

## 6. Reglas de Base de Datos
*   **Separación de Cargas:** Separación estricta entre transaccional (OLTP) y analítica (OLAP).
*   **Backups:** Ejecución diaria automatizada hacia cold storage (S3 Glacier Deep Archive) con encriptación.
*   **Integridad:** Ejecución de pruebas de restauración semanales en entornos aislados verificando *checksums*, *row counts* e integridad referencial.

## 7. Estándares de Pruebas
*   **Calidad de Datos:** Validaciones rigurosas post-ingesta (nulos, rangos plausibles, frescura) mediante suites de **Validaciones nativas (Pydantic/Zod)**.
*   **Rendimiento y Carga:** Ejecución de simulaciones periódicas con **k6** evaluando latencias (p95, p99) y throughput bajo miles de usuarios concurrentes.
*   **Chaos Engineering:** Ejecución de simulaciones de fallos (Chaos Experiments) mensuales en staging (fallos de red, kill pods aleatorios, failover de DB) para validar resiliencia y MTTR.
*   **Machine Learning:** Pruebas rigurosas de drift de modelos (PSI) en producción. Reentrenamiento automatizado con validación A/B testing / Shadow Mode previo a su exposición total.

## 8. Restricciones Generales del Proyecto
*   **SLAs de Rendimiento:** La frescura de los datos servidos por la API debe ser menor a 5 minutos.
*   **Uptime y Resiliencia:** Objetivo innegociable de disponibilidad global $\geq$ 99.0% (Best Effort).
*   **Recuperación ante Desastres (DR):** RPO (Recovery Point Objective) $\leq$ 5 minutos; RTO (Recovery Time Objective) $\leq$ 15 minutos.
*   **Gestión de Incidentes:** Tiempo de primera respuesta a tickets $\leq$ 2 horas. Resolución de incidentes críticos $\leq$ 15 min (MTTR). Todo incidente de severidad alta requiere un Post-Mortem "blameless" en menos de 72 horas.
*   **Error Budget:** Si el consumo del presupuesto de error (Error Budget) supera el 80% en un mes (aprox. 3.5 min de caída), se **congelan los despliegues de nuevas funcionalidades** hasta recuperar estabilidad.

## 9. Decisiones Técnicas Transversales
*   **Cultura Remote-First:** Operación diseñada para equipos distribuidos globalmente, favoreciendo fuertemente el trabajo asíncrono, automatizaciones (Slack bots), documentación profunda y métricas DORA (velocity, cycle time).
*   **Gestión de Costos FinOps:** El gasto cloud no es un tema posterior; se requiere monitoreo de anomalías financieras, rightsizing y alertas de desviación diaria vs forecast como parte integral del desarrollo operativo (SRE).

## Reglas Globales Resueltas (Speckit-Clarify)
1. **Rate Limiting:** Soft Limit de 1 hora.
2. **ETL:** Datos corruptos a cuarentena (tolerancia a fallos parciales).
3. **Logs:** Retención obligatoria de 30 días.
4. **Secretos:** Inyectados vía GitHub Secrets (CI/CD).
5. **Incidentes:** Status Page + Email automático a usuarios.
