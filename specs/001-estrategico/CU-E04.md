# Especificación de Caso de Uso: CU-E04

## 1. Nombre de la Funcionalidad
**Revisar Cumplimiento Normativo (Compliance)**

## 2. Objetivo
Permitir al Desarrollador (Tú) y a Auditores Externos evaluar y verificar el estado de cumplimiento de las normativas de seguridad, privacidad y operatividad (Buenas prácticas de seguridad, Higiene de seguridad, GDPR, y regulaciones IATA) mediante un diagnóstico visual del avance de controles.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Desarrollador (Tú) de Compliance
*   **Sistemas Externos / Actores Secundarios:** Herramientas de escaneo SAST/DAST (SonarQube, OWASP), AWS Config / Security Hub.

## 4. Contexto del Problema
SkyAnalytics procesa datos sensibles y requiere certificaciones robustas (Buenas prácticas de seguridad/ Higiene de seguridad) para vender licencias a clientes Enterprise y gubernamentales. Llevar un control manual de las evidencias técnicas es propenso a errores y omisiones, por lo que se requiere un panel automatizado de compliance.

## 5. Requisitos Funcionales
*   **RF-E04-001:** El sistema debe consolidar un listado de controles técnicos asociados a cada marco normativo (SOC 2, ISO, GDPR).
*   **RF-E04-002:** El sistema debe marcar automáticamente como "Conforme" los controles técnicos que pueden validarse por API (ej. cifrado KMS activo, MFA forzado para usuarios IAM).
*   **RF-E04-003:** El sistema debe resaltar en rojo los gaps (brechas de seguridad) o controles manuales pendientes de evidencia.
*   **RF-E04-004:** El sistema debe generar un reporte completo en PDF adjuntando el estado de todos los controles técnicos para enviarse a la firma auditora.

## 6. Requisitos No Funcionales
*   **RNF-E04-001:** Todas las evidencias (archivos PDF de políticas, logs de auditoría) deben almacenarse en buckets S3 con propiedad de Inmutabilidad (Object Lock) para prevenir alteraciones de evidencia.
*   **RNF-E04-002:** El reporte exportado debe firmarse digitalmente garantizando su autenticidad.

## 7. Reglas de Negocio
*   **RN-E04-001 (GDPR Data Residency):** Cualquier almacenamiento de datos de usuarios europeos fuera del cluster `eu-central-1` generará un fallo automático de compliance clasificado como Crítico.
*   **RN-E04-002 (Cifrado Mandatorio):** El control de cifrado en reposo y en tránsito no admite excepciones (Zero Trust). Si AWS Security Hub detecta un recurso no cifrado, el control Buenas prácticas de seguridadfalla automáticamente.

## 8. Entradas
*   Filtros UI:
    *   `marco_normativo` (Enum: SOC2, ISO27001, GDPR, IATA)
*   Subida de Archivos:
    *   Políticas documentales manuales (PDF).

## 9. Salidas
*   **Payload JSON:**
    *   `{ framework, compliance_score_percentage, controls: [{ id, name, status, evidence_link }] }`
*   **UI:** Matriz de cumplimiento con indicadores de estado, lista de gaps y botón de exportación.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Validación automatizada de control criptográfico
**Dado** que el Desarrollador (Tú) visualiza el marco "Buenas prácticas de seguridad"
**Cuando** revisa el control "CC6.7: Transmisión y almacenamiento de información"
**Entonces** el sistema valida con AWS Config que todos los volúmenes EBS tienen AES-256 habilitado
**Y** marca el control como "Completado Automáticamente".

### Escenario 2: Detección de Gap en GDPR
**Dado** que el Desarrollador (Tú) está evaluando la preparación para GDPR
**Cuando** el sistema detecta que se ejecutó un volcado de logs con IPs europeas hacia un cluster de US
**Entonces** el sistema marca el control "Data Residency" en Rojo (Fallido)
**Y** prioriza su remediación en el dashboard de Gaps.

## 11. Criterios de Aceptación
*   **CA-E04-001:** El cálculo del score de cumplimiento es exacto (Controles Pasados / Controles Totales * 100).
*   **CA-E04-002:** Un Desarrollador (Tú) con permisos de "Solo Lectura" puede generar reportes y descargar evidencias, pero no puede marcar un control manual como "Completado". Solo el Desarrollador (Tú) o el VP pueden aprobar controles manuales.

## 12. Restricciones
*   El dashboard depende de la latencia de ingestión de AWS Security Hub, la cual puede tener un retraso de hasta 6 horas para recursos recientemente creados.

## 13. Fuera de Alcance
*   Autocorrección de vulnerabilidades de infraestructura (Las brechas de Buenas prácticas de seguridaddeben solucionarse modificando el código Scripts básicos de despliegue, no mediante botones en este dashboard).
