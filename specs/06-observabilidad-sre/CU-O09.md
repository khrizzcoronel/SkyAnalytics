# Especificación de Caso de Uso: CU-O09

## 1. Nombre de la Funcionalidad
**Ejecutar Backup y Prueba de Restauración**

## 2. Objetivo
Asegurar la durabilidad y disponibilidad de los datos transaccionales y de configuración mediante políticas de copia de seguridad inmutables y la ejecución periódica de simulacros de restauración para garantizar el RTO y RPO exigidos por la normativa SOC 2.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) (Supervisión automatizada)
*   **Sistemas Externos / Actores Secundarios:** AWS RDS / PostgreSQL, S3 Glacier (Cold Storage), AWS Backup.

## 4. Contexto del Problema
SkyAnalytics almacena metadatos de configuración de miles de tenants. Un error humano (ej. `DROP TABLE`), un ataque de Ransomware, o un fallo masivo en el centro de datos principal podría borrar toda la información de facturación y perfiles. Realizar copias no basta; hay que validar rigurosamente que las copias *realmente se pueden restaurar* de forma expedita (RTO $\leq$ 15 min).

## 5. Requisitos Funcionales
*   **RF-O09-001:** El sistema de base de datos (PostgreSQL/AWS RDS) debe generar snapshots (instantáneas) incrementales cada 5 minutos y un snapshot completo (Full Backup) cada 24 horas a las 01:00 UTC.
*   **RF-O09-002:** El sistema debe copiar los snapshots completos a otra región física (Cross-Region Backup) para proteger contra desastres naturales en el sitio primario.
*   **RF-O09-003:** El orquestador automatizado debe levantar un entorno aislado semanalmente y restaurar la base de datos a partir del último backup.
*   **RF-O09-004:** El sistema debe ejecutar consultas de verificación (checksums, conteo de filas, validez de esquemas) sobre la base restaurada para validar su integridad.
*   **RF-O09-005:** Tras la validación exitosa, el sistema destruye el entorno aislado y genera un reporte auditable indicando el tiempo real de restauración tomado.

## 6. Requisitos No Funcionales
*   **RNF-O09-001 (Inmutabilidad):** Los backups alojados en almacenamiento frío no deben poder ser borrados ni modificados por ningún usuario, ni siquiera el usuario Root, durante un periodo de retención de 90 días (Object Lock / WORM).
*   **RNF-O09-002 (Cifrado):** Todo snapshot en reposo utiliza cifrado AES-256 manejado por claves maestras rotadas KMS.

## 7. Reglas de Negocio
*   **RN-O09-001 (Política RPO y RTO):** 
    *   RPO (Recovery Point Objective): $\leq$ 5 Minutos (Máxima pérdida de datos admisible).
    *   RTO (Recovery Time Objective): $\leq$ 15 Minutos (Tiempo máximo que la DB puede estar fuera de servicio antes de levantar desde la réplica).

## 8. Entradas
*   Disparador cron programado.
*   Snapshots generados por RDS.

## 9. Salidas
*   **Evidencias de Cumplimiento:** Registro (Log) inmutable del resultado de la prueba de restauración.
*   **Alertas:** En caso de que la prueba de restauración tarde más de 15 minutos, notifica a Notificaciones de Slack.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Simulacro de restauración (DR Drill) exitoso
**Dado** que es domingo y se dispara el cron job de DR Drill
**Cuando** el script solicita la restauración del último snapshot en una VPC aislada
**Entonces** RDS provee la base de datos totalmente operativa en 11 minutos
**Y** el script de integridad confirma que la tabla `tenants` posee los 34,500 registros exactos que estaban al momento del backup
**Y** se marca el control de resiliencia como PASSED (CU-E04).

### Escenario 2: Falla de RTO detectada
**Dado** que el tamaño de la base de datos ha crecido drásticamente este trimestre
**Cuando** se ejecuta la prueba de restauración
**Entonces** RDS levanta la base, pero el proceso toma 18 minutos
**Y** el sistema detecta que viola la política RN-O09-001 (RTO $\leq$ 15 min)
**Y** alerta al SRE para que incremente la capacidad de red de provisionamiento de disco (IOPS) del snapshot para futuras restauraciones.

## 11. Criterios de Aceptación
*   **CA-O09-001:** La prueba de restauración automática jamás interrumpe, bloquea ni consume rendimiento (I/O) de la base de datos en producción.

## 12. Restricciones
*   El acceso a las llaves KMS maestras para descifrar los backups debe seguir un protocolo de control dual (se requieren aprobaciones separadas de Desarrollador (Tú) y CISO) en caso de un desastre masivo.

## 13. Fuera de Alcance
*   Backup de contenedores Docker (La infraestructura inmutable se regenera desde el código, solo se hace backup de los datos/estado persistente).
