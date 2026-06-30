# SkyAnalytics Inc.

**Drive:** `https://drive.google.com/drive/folders/1f9FfqWsVkM63CCfhutV755ouBE61dDS6?usp=sharing`  
**Github:** `https://github.com/khrizzcoronel/SkyAnalytics.git`

## Especificación de Requisitos de Software (SRS)
*Basado en el Estándar IEEE 830*  
*Khriz Coronel*  
*Versión 1.0*

---

## 1. Introducción

### 1.1. Propósito
El propósito de este documento es definir la Especificación de Requisitos de Software (SRS) para la plataforma SaaS corporativa **SkyAnalytics**. Este documento sirve como contrato técnico detallado para guiar el desarrollo de la arquitectura híbrida (transaccional y analítica) del sistema, alineando las metas comerciales delineadas en el *Balanced Scorecard* con la ejecución técnica.

### 1.2. Alcance
El sistema **SkyAnalytics** es una plataforma unificada para la industria aeronáutica. Proporciona ingesta automatizada de datos de vuelo, modelos predictivos de Machine Learning, y tableros interactivos (*dashboards*) para el monitoreo estratégico y táctico. El sistema abarca:
- **Capa Estratégica:** Visualización de KPIs de negocio, salud financiera y metas corporativas.
- **Capa Táctica (Command Center):** Monitoreo de integraciones de terceros (Sentry, GitHub), FinOps y reglas RBAC.
- **Capa Operativa (Headless):** Ingesta y limpieza masiva de datos (ETL), orquestación vía GitHub Actions, y despliegue efímero de entrenamiento ML (Instancias Spot).

### 1.3. Definiciones, Acrónimos y Abreviaturas
- **SRS:** Software Requirements Specification.
- **BFF:** Backend-For-Frontend. Patrón arquitectónico donde el servidor actúa como capa intermedia dedicada a servir a un UI específico.
- **RBAC:** Role-Based Access Control.
- **ETL:** Extract, Transform, Load.
- **Zero Trust:** Filosofía de seguridad donde ninguna conexión de red es confiable por defecto (Ej. usar Túneles SSH para conexiones internas).

### 1.4. Referencias
- Documento de Perfil Estratégico y Corporativo (`docs/analisis.tex`).
- Constitución de Arquitectura (SkyAnalytics `CONSTITUTION.md`).
- Especificaciones y Planes de Diseño Técnico (Módulos 001, 002 y 003).

---

## 2. Descripción General

### 2.1. Perspectiva del Producto
SkyAnalytics se enmarca en un modelo de arquitectura **Monolito Modular Serverless**.
La aplicación principal se construye utilizando **Next.js (App Router)** y se despliega en un proveedor PaaS Serverless (Vercel). 
La persistencia de datos utiliza un enfoque híbrido:
- **PocketBase (Operativa y Staging):** Base de datos ligera (SQLite) alojada en una VPS, responsable de la autenticación de usuarios, roles (RBAC), configuración del sistema, alertas, límites FinOps y de actuar como la capa intermedia de Staging (`flights_raw`) para el dataset semilla.
- **MonetDB (Analítica):** Motor columnar Data Warehouse especializado en procesamiento de grandes volúmenes de datos. Almacena las tablas de hechos (*Fact Tables*) estructuradas en estrella alimentadas por el ETL y expone vistas materializadas para lectura instantánea. En este motor se consolida el entrenamiento ML.

### 2.2. Funciones del Producto
Las funciones del producto se dividen en 3 módulos principales:
1. **Módulo Estratégico (Analítica Directiva):** Tableros de resumen (*Balanced Scorecard*), métricas financieras, telemetría y reportes de cumplimiento (exportables a PDF nativo).
2. **Módulo Táctico (Command Center):** Gestión centralizada de accesos de usuario, rotación de secretos en el pipeline CI/CD, monitoreo de presupuesto Cloud (FinOps), y proxy de logs de Sentry.
3. **Módulo Operativo (Backbone):** Trabajos programados vía GitHub Actions que ejecutan flujos ETL en Python (Pandas/Polars) con cuarentena de datos corruptos, y despliegue automatizado de modelos de ML en instancias efímeras (AWS Spot).

### 2.3. Características del Usuario
El sistema está diseñado para 3 niveles de actores internos:
- **`SUPER_ADMIN`:** CTO o líder técnico. Tiene control total sobre el Módulo Táctico (secretos, presupuesto, roles).
- **`C_LEVEL_EXEC`:** Directivos y VP. Consumen el Módulo Estratégico para observar KPIs y establecer metas.
- **`OPERATOR`:** Ingenieros de Datos y ML. Diseñan y vigilan el Módulo Operativo.

### 2.4. Restricciones y Suposiciones
- **Enfoque Solo-Dev / Bajo Presupuesto:** El sistema prohíbe el uso de infraestructuras pesadas permanentemente encendidas (ej. Apache Airflow o AWS RDS PostgreSQL multicapa).
- **Protección contra Timeouts:** Dado el entorno Serverless, las respuestas HTTP a APIs de terceros deben usar caché (`revalidate: 60`) y el entrenamiento de ML debe delegarse completamente a instancias externas.

---

## 3. Requisitos Específicos

### 3.1. Requisitos de Interfaces Externas
El sistema integrará y consumirá datos de las siguientes APIs externas como "Single Source of Truth":
- **GitHub REST API:** Para lectura de estado de pipelines de CI/CD e inyección de Secrets de entorno.
- **Sentry API:** Para proxy en vivo de registros de errores.
- **Stripe API / Webhooks:** Para conciliación de pagos en tiempo real.
- **AWS Cost Explorer / PaaS Billing API:** Para auditoría financiera FinOps.

### 3.2. Requisitos Funcionales por Módulo

#### 3.2.1. Módulo Estratégico (Capa Directiva)
| ID Requisito | Descripción del Caso de Uso | Dependencia |
| :--- | :--- | :--- |
| RF-E01 (BSC) | El sistema debe renderizar el Balanced Scorecard con semaforización (Verde, Amarillo, Rojo) contra las metas LTM. | MonetDB |
| RF-E02 (Finanzas) | El sistema debe calcular dinámicamente el ARR, Gross Margin, LTV, y CAC forzando la moneda USD. | MonetDB |
| RF-E03 (Telemetría) | El sistema debe mostrar el SLA y Uptime de los servicios para auditar el *Error Budget*. | MonetDB |
| RF-E05 (Metas) | El `SUPER_ADMIN` podrá configurar metas trimestrales vía CRUD. | PocketBase |
| RF-E06 (Export) | Las vistas analíticas deben proveer un botón para invocar `window.print()` con CSS `@media print`. | N/A |

#### 3.2.2. Módulo Táctico (Command Center)
| ID Requisito | Descripción del Caso de Uso | Dependencia |
| :--- | :--- | :--- |
| RF-T01 (RBAC) | Permitir definir matrices de permisos asociadas a Roles. | PocketBase |
| RF-T02 (Logs) | Extraer y mostrar errores desde Sentry usando una tabla virtualizada (Infinite Scroll). | Sentry API |
| RF-T03 (Secrets) | Proveer un formulario seguro para inyectar credenciales (Ej. DB_PASSWORD) directo a GitHub Secrets. | GitHub API |
| RF-T08 (FinOps) | Definir un presupuesto en PocketBase. Si el gasto del PaaS supera el 90%, enviar Webhook a Slack. | AWS API |

#### 3.2.3. Módulo Operativo (Backbone)
| ID Requisito | Descripción del Caso de Uso | Dependencia |
| :--- | :--- | :--- |
| RF-O01 (Cron ETL) | GitHub Actions orquestará el pipeline ETL Python diario a las 02:00 AM. | GitHub Actions |
| RF-O02 (Cuarentena) | Si el ETL encuentra datos corruptos, no debe crashear; debe desviarlos a la tabla `Quarantine_Data`. | MonetDB |
| RF-O03 (Backups) | El cron de backups debe generar un volcado cifrado y enviarlo a AWS S3. | S3/KMS |
| RF-O04 (ML Spot) | El script ML levantará una instancia Spot, entrenará, subirá el modelo a S3 y ejecutará `shutdown -h now`. | AWS EC2 |

### 3.3. Requisitos de Rendimiento
- **Tiempo de Respuesta (SLA):** Las llamadas al Backend-For-Frontend (BFF) del Módulo Estratégico deben resolverse en $\leq$ 3.0 segundos consultando las Vistas Materializadas de MonetDB.
- **Disponibilidad (Uptime):** La arquitectura tolerante a fallos debe apuntar a un Uptime del 99.99%.
- **Caché en Proxy:** Las peticiones a APIs de terceros (Sentry, GitHub) en el Módulo Táctico deben ser cacheadas obligatoriamente durante al menos 60 segundos (`revalidate: 60`) para prevenir bloqueos por límite de cuota (Rate Limit 429).

### 3.4. Atributos del Sistema de Software (Seguridad)
Basados en las directivas de la Constitución (Zero Trust y Cifrado), el sistema impone las siguientes políticas:
- **Zero Trust y Túneles:** Los servicios expuestos (ETL en GitHub Actions) no accederán al puerto abierto de MonetDB en internet público. Es obligatorio levantar un Túnel efímero (SSH / Tailscale) en el *Runner* antes de iniciar la ingesta.
- **Cifrado en Tránsito:** Toda comunicación hacia MonetDB requiere estrictamente `sslmode=require` (TLS 1.3).
- **Cifrado en Reposo:** El disco de la VPS que contiene el archivo SQLite de PocketBase y la Data de MonetDB debe estar cifrado a nivel de volumen (AWS EBS Encryption o LUKS AES-256). Los backups enviados a S3 deben usar KMS.
- **Autenticación Segura:** Las cuentas con roles administrativos requerirán soporte para MFA, interceptando accesos no autorizados en el *Middleware* de Next.js antes de la ejecución del código.
