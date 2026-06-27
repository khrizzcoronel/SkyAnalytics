# Especificación de Caso de Uso: CU-O01

## 1. Nombre de la Funcionalidad
**Registrar Tenant y Autogenerar API Keys**

## 2. Objetivo
Automatizar el flujo completo de *Onboarding* técnico de un nuevo cliente corporativo (Tenant), aprovisionando su espacio en base de datos y generándole instantáneamente credenciales de acceso (API Keys) seguras para reducir el tiempo al primer valor (TTFV).

## 3. Actores Involucrados
*   **Actor Principal:** Cliente B2B (Aerolínea / Agencia)
*   **Sistemas Externos / Actores Secundarios:** API Gateway (Gateway simplificado), Servicio IAM, Servicio de Email (SendGrid/HubSpot).

## 4. Contexto del Problema
Cuando un cliente B2B decide utilizar SkyAnalytics, un proceso manual de alta retrasa su integración, generando fricción. Se necesita un *self-service onboarding* donde el cliente ingrese sus datos y reciba inmediatamente acceso al entorno Sandbox y Producción mediante llaves criptográficas.

## 5. Requisitos Funcionales
*   **RF-O01-001:** El sistema debe validar la unicidad del dominio del correo corporativo y la razón social para evitar registros duplicados.
*   **RF-O01-002:** El sistema debe crear un registro de `Tenant` lógico en la base de datos PostgreSQL, asignándole un `UUID` único.
*   **RF-O01-003:** El servicio IAM debe interactuar con el API Gateway para aprovisionar automáticamente un "Consumer" y generarle dos API Keys: `Test_Key` (Sandbox) y `Live_Key` (Producción).
*   **RF-O01-004:** El sistema debe requerir verificación de correo electrónico mediante un enlace Logsral de 24 horas antes de revelar las API Keys en el dashboard.
*   **RF-O01-005:** Las API Keys de Producción deben mostrarse por única vez (One-time display) en texto plano; posteriormente solo se mostrará un hash enmascarado (ej. `sk_live_...4f8a`).

## 6. Requisitos No Funcionales
*   **RNF-O01-001 (Performance):** El proceso completo de registro, validación y aprovisionamiento en el API Gateway no debe exceder los 5 segundos.
*   **RNF-O01-002 (Seguridad en reposo):** Las API Keys reales jamás deben guardarse en texto plano en la base de datos de SkyAnalytics; solo se almacena su hash SHA-256 (KDF).

## 7. Reglas de Negocio
*   **RN-O01-001 (Restricción de Correo):** No se permiten registros con correos electrónicos genéricos gratuitos (Gmail, Yahoo, Hotmail). Solo dominios corporativos válidos.
*   **RN-O01-002 (Plan por Defecto):** A todo nuevo Tenant se le asigna por defecto el plan `Freemium` con un Hard Limit de 1,000 peticiones mensuales.

## 8. Entradas
*   Formulario Web: `nombre_empresa`, `email_corporativo`, `password`, `pais`.
*   Token de Verificación (vía URL de correo).

## 9. Salidas
*   **Payload JSON:** Confirmación de registro exitoso.
*   **UI Dashboard:** Visualización One-time de las credenciales generadas.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Onboarding exitoso y generación de API Key
**Dado** que un representante de "Delta Airlines" completa el formulario con su correo corporativo válido
**Y** hace clic en el enlace de verificación recibido por email
**Cuando** inicia sesión por primera vez
**Entonces** el sistema aprovisiona el Tenant `delta-airlines-prod` en el API Gateway
**Y** muestra la pantalla de bienvenida revelando la `Live_API_Key` por única vez.

### Escenario 2: Intento de registro con correo genérico
**Dado** que un usuario intenta registrarse con `analytics-test@gmail.com`
**Cuando** envía el formulario de registro
**Entonces** el sistema rechaza la solicitud
**Y** muestra el error "Por favor utiliza un correo corporativo válido"
**Y** no se crea ningún registro en la base de datos.

## 11. Criterios de Aceptación
*   **CA-O01-001:** Un intento de recuperar una API Key existente debe resultar en la revocación de la antigua y la generación de una nueva, previa autenticación MFA.
*   **CA-O01-002:** El enlace de verificación de correo pierde total validez luego de 24 horas, requiriendo que el usuario solicite uno nuevo.

## 12. Restricciones
*   El aprovisionamiento del API Gateway debe ser asíncrono o compensable. Si Gateway simplificado falla en generar la key, el registro del Tenant en Postgres debe aplicar un Rollback automático.

## 13. Fuera de Alcance
*   Creación de sub-usuarios dentro del Tenant (eso es gestión de Roles RBAC interna, fuera del registro inicial).
