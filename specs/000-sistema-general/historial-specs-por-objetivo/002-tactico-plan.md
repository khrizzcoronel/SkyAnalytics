# Diseño Técnico: Módulo Táctico

## 1. Arquitectura de la Solución (Capa DevOps / FinOps)
**Patrón Arquitectónico:** Monolito Serverless con Integración de APIs de Terceros (API Composition).
Este módulo agrupa los casos de uso **CU-T01 al CU-T10**, enfocados en la administración de la plataforma, control de costos, seguridad y observabilidad.

*   **Frontend (Presentación):** Next.js (App Router) alojado en Vercel. Interfaz de control táctico ("Command Center").
*   **Backend (Capa de Servicios):** Rutas de API de Next.js (`/api/v1/tactico/*`) actuando como orquestador y *Proxy* seguro. El backend no solo lee bases de datos locales, sino que se comunica mediante tokens seguros con APIs externas.
*   **Capa de Datos y Servicios Híbrida:** 
    *   **PocketBase (Operativa Local):** Almacena las configuraciones editables por el usuario (Políticas RBAC, Umbrales de presupuesto, Reglas de alertas). Para cumplir con la Constitución (AES-256), el archivo SQLite subyacente estará protegido mediante **cifrado a nivel de volumen de disco** (ej. AWS EBS Encryption o LUKS) en la VPS.
    *   **APIs Externas (SSOT - Single Source of Truth):** Para evitar sincronizaciones complejas, métricas como el costo en la nube, logs o estado de CI/CD se consumen directamente "en vivo" desde GitHub API, Sentry API y la API del PaaS/AWS.

## 2. Modelo de Base de Datos y Orígenes de Datos

### 2.1 Tablas Operativas Propias (PocketBase)
*Nota: El esquema completo de PocketBase (incluyendo las tablas de hechos de vuelos, logs de ML y auditoría) está consolidado globalmente en el archivo [pb_schema.json](file:///c:/Users/kacor/OneDrive/Desktop/SkyAnalytics/pb_schema.json). Este módulo táctico gestiona específicamente:*
*   **`rbac_policies` (CU-T01):**
    *   `role_name` (String, PK) - Ej. `OPERATOR`
    *   `permissions` (JSON) - Arreglo de scopes permitidos.
*   **`alert_policies` (CU-T06):**
    *   `id` (UUID)
    *   `metric` (String) - Ej. `api_latency`
    *   `threshold_value` (Decimal) - Umbral de disparo.
    *   `slack_webhook` (String) - Destino de la alerta.
*   **`budget_limits` (CU-T08):**
    *   `month` (String) - Ej. `2025-06`
    *   `max_spend` (Decimal) - Presupuesto máximo (Soft Limit / Hard Limit).

### 2.2 Orígenes de Datos Externos (Third-Party APIs)
*   **Logs y Errores (CU-T02):** Sentry / Logtail API. Dado que la capa gratuita de Sentry solo retiene 14 días, un *Cron Job* operativo extraerá semanalmente los logs históricos hacia un Bucket S3 barato para cumplir con la retención constitucional de 30 días.
*   **CI/CD y Secretos (CU-T03, CU-T04):** GitHub REST API / GraphQL (Para leer el estado de las Actions y actualizar Secrets).
*   **Certificados y Costos (CU-T05, CU-T07):** API del proveedor PaaS (Render/Railway/Vercel) o AWS Cost Explorer (Para métricas Spot).

## 3. Endpoints de Servicios
| Método | Ruta (`/api/v1/tactico/*`) | Uso Principal | Origen de Datos |
| :--- | :--- | :--- | :--- |
| `GET` | `/rbac/policies` | Listar políticas de acceso. | PocketBase |
| `GET` | `/observability/logs` | Consolidar registros de error y auditoría. | Sentry API |
| `GET` | `/cicd/pipelines` | Obtener métricas de éxito/fracaso de deploys. | GitHub API |
| `POST`| `/cicd/secrets` | Rotar/Inyectar secretos de entorno. | GitHub Secrets API |
| `GET` | `/finops/billing` | Obtener costo acumulado vs Límite (CU-T08). | PaaS / AWS API + PocketBase |

*(Nota: Estas rutas están estrictamente protegidas bajo el rol `SUPER_ADMIN`).*

## 4. Componentes y Clases Principales

### 4.1 Componentes React (Reutilizables)
*   **`ThirdPartyStatusBadge`:** Muestra el estado de la conexión a una API externa (ej. GitHub: Online, Sentry: Latency High).
*   **`FinOpsProgressBar`:** Barra de progreso que visualiza el gasto actual de la nube contrastado contra el `max_spend` de PocketBase. Cambia a rojo si supera el 90%.
*   **`LogViewerTable`:** Tabla con virtualización (Infinite Scroll) para renderizar miles de logs obtenidos desde la API de Sentry sin bloquear el navegador.

### 4.2 Lógica Backend
*   **`TacticalIntegrationsService`:** Clase en Node.js que implementa el patrón `Adapter` para estandarizar las respuestas de las múltiples APIs externas (GitHub, Sentry, AWS). 
*   **`WebhookDispatcher`:** Utilidad que envía notificaciones asíncronas a Slack cuando una alerta táctica (ej. límite de presupuesto alcanzado) se dispara.

## 5. Flujo de Datos Global (Ejemplo: FinOps - CU-T08)
1.  **Configuración:** El Desarrollador define en la UI un presupuesto de \$50 USD/mes. El cliente hace `POST` a `/budgets` y se guarda en **PocketBase**.
2.  **Monitoreo:** El usuario ingresa a la pestaña FinOps. El frontend solicita `/finops/billing`.
3.  **Proxying:** El Backend hace una llamada HTTP segura a la API de facturación del PaaS usando un Token de Servicio (guardado en `.env`).
4.  **Cruce de Datos:** El Backend lee el presupuesto máximo de PocketBase (\$50) y el gasto actual del PaaS (\$42).
5.  **Respuesta y UI:** El Backend devuelve la consolidación al Frontend. Se renderiza la `FinOpsProgressBar` al 84% (Color Naranja).

## 6. Dependencias con Otros Módulos
*   **Nivel Operativo (Infraestructura):** Este módulo monitorea (Logs, Alertas, Costos) a todo el nivel Operativo. Si un servicio operativo genera logs basura o sobre-consume CPU, será visible y alertado a través de las herramientas tácticas.

## 7. Decisiones Técnicas y Justificación
*   **Integración de APIs vs ETL a MonetDB:** 
    *   *Por qué:* A diferencia de los datos financieros (que no cambian cada segundo), los Logs, el estado del CI/CD y los costos Cloud cambian constantemente. Para un Solo-Dev, construir un pipeline ETL para traer datos de GitHub/Sentry a MonetDB es sobreingeniería innecesaria. Es más eficiente consumirlos directamente "on-the-fly" vía API.
*   **Inyección directa a GitHub Secrets (CU-T03):** 
    *   *Por qué:* Elimina la necesidad de acceder a la consola de AWS o al panel web del PaaS. Se cumple la regla de la Constitución de mantener la "Infraestructura/Configuración como Código".
*   **Almacenamiento de Metadatos en PocketBase:** 
    *   *Por qué:* Mantener las reglas de alertas y presupuestos en PocketBase en lugar de archivos duros (JSON/YAML) permite cambiar límites en caliente (Hot-Reload) desde la Interfaz de Usuario sin necesidad de re-desplegar toda la aplicación en Vercel.
*   **Protección contra Rate Limits (Caché):**
    *   *Por qué:* El Command Center lee continuamente de APIs de terceros (GitHub, Sentry). Para evitar ser bloqueados por exceder la cuota (Rate Limit 429), el BFF en Next.js implementará obligatoriamente `Next.js Data Cache` con `revalidate: 60`. Esto significa que múltiples recargas de la UI en menos de 1 minuto consumirán el caché local, disparando solo 1 petición real por minuto hacia la API externa.
