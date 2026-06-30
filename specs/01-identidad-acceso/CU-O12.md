# Especificación de Caso de Uso: CU-O12

## 1. Nombre de la Funcionalidad
**Rotar Credenciales y Auditar Accesos IAM**

## 2. Objetivo
Garantizar la seguridad de la infraestructura interna ejecutando la rotación periódica automatizada de secretos (Tokens, Passwords, API Keys internas) y generando auditorías trimestrales de los permisos de los usuarios para revocar privilegios excesivos.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** Variables de Entorno (.env), AWS IAM, AWS CloudTrail.

## 4. Contexto del Problema
Las contraseñas de bases de datos de producción y los tokens de proveedores externos (ej. Stripe, SendGrid) a menudo quedan "olvidados" y nunca se cambian. Si un ex-empleado retiene una copia, o si se filtran, el sistema está comprometido de por vida. SOC 2 requiere rotación regular y auditoría de accesos.

## 5. Requisitos Funcionales
*   **RF-O12-001:** Variables de Entorno (.env) debe conectarse a PostgreSQL dinámicamente para revocar la contraseña actual del usuario de la aplicación y generar una nueva cada 30 días, inyectándola en los pods de PaaS/Serverless sin tiempo de inactividad.
*   **RF-O12-002:** El sistema debe ejecutar un script mensual que analice el uso de permisos IAM en AWS CloudTrail, identificando roles o permisos concedidos a empleados que no han sido utilizados en los últimos 90 días.
*   **RF-O12-003:** El sistema debe generar un reporte de auditoría IAM ("Access Review") en formato PDF para que el CISO (o Desarrollador (Tú)) lo apruebe formalmente cada trimestre.

## 6. Requisitos No Funcionales
*   **RNF-O12-001 (Zero Downtime):** La rotación de credenciales de la base de datos debe utilizar el patrón de "Overlap" (mantener válida la clave vieja por 5 minutos mientras se propagan los nuevos secretos a las aplicaciones).

## 7. Reglas de Negocio
*   **RN-O12-001 (Principio de Menor Privilegio):** Cualquier permiso IAM detectado como "No utilizado en 90 días" debe ser revocado automáticamente (Auto-remediación) y el usuario debe re-solicitarlo si lo necesita.
*   **RN-O12-002 (MFA Obligatorio):** Todos los accesos de empleados a cuentas cloud o de .env secrets requieren Autenticación Multifactor (MFA) por hardware (YubiKey) o aplicación móvil.

## 8. Entradas
*   Disparador de expiración TTL (Time-To-Live) en .env secrets.
*   Registros de CloudTrail (JSON).

## 9. Salidas
*   Nuevos secretos inyectados a través del *.env secrets Agent Injector* en PaaS/Serverless.
*   Reporte de auditoría PDF.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Rotación dinámica de credencial de base de datos
**Dado** que han transcurrido 30 días desde la última rotación de la contraseña del usuario `app-prod` en PostgreSQL
**Cuando** .env secrets detecta que el TTL del secreto ha expirado
**Entonces** genera una nueva contraseña aleatoria de 32 caracteres y actualiza PostgreSQL
**Y** actualiza el secreto en el clúster de PaaS
**Y** reinicia ordenadamente (Rolling Update) los pods de la API para que adopten la nueva credencial sin botar tráfico.

### Escenario 2: Detección de permisos huérfanos (Orphan Permissions)
**Dado** que el script de auditoría IAM trimestral se ejecuta
**Cuando** analiza los accesos del `Dev_Senior_Role`
**Entonces** detecta que el permiso `s3:DeleteBucket` no ha sido invocado por ningún desarrollador en los últimos 180 días
**Y** remueve la política del rol
**Y** registra la remediación en el reporte de cumplimiento SOC 2.

## 11. Criterios de Aceptación
*   **CA-O12-001:** La rotación de credenciales no genera fallos de conexión a la base de datos (`Connection Refused` o `FATAL: password authentication failed`) reflejados en los logs de la aplicación durante la transición.

## 12. Restricciones
*   Los secretos "Estáticos" que no pueden ser rotados dinámicamente por la aplicación destino (ej. un Token maestro de un proveedor obsoleto) deben reportarse en un panel de "Riesgo Aceptado" renovable manualmente cada 6 meses.

## 13. Fuera de Alcance
*   Offboarding manual de empleados (La desactivación de la cuenta de GSuite / IdP principal apaga automáticamente el acceso IAM mediante Single Sign-On).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Retención de Logs:** Los registros de acceso y errores se retendrán durante **30 días** en el almacenamiento de logs, priorizando la capacidad de diagnóstico histórico sobre el ahorro extremo de costos.

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Gestión de Secretos:** Las contraseñas y llaves de API se inyectarán de forma segura utilizando **GitHub Secrets** durante el pipeline de CI/CD, sin intervención manual en el panel del PaaS.
