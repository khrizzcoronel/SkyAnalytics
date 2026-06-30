# Especificación de Caso de Uso: CU-O19

## 1. Nombre de la Funcionalidad
**Analizar y Optimizar Costos Cloud (Operativo)**

## 2. Objetivo
Ejecutar rutinas, políticas automatizadas (FinOps) y acciones correctivas a nivel de infraestructura para prevenir el desperdicio de recursos cloud, apagando entornos efímeros, ajustando instancias de cómputo y ejecutando purgas de datos no conformes.

## 3. Actores Involucrados
*   **Actor Principal:** SRE / Ingeniero FinOps
*   **Sistemas Externos / Actores Secundarios:** AWS (Lambda, Auto Scaling Groups, CloudWatch), Infracost.

## 4. Contexto del Problema
A nivel táctico (CU-T08) la gerencia analiza los costos mensualmente y ve reportes agregados. A nivel *Operativo* (este caso), los ingenieros SRE necesitan integrar controles de costos antes del despliegue y herramientas que apaguen automáticamente las fugas de dinero (por ejemplo, entornos de prueba que quedan encendidos todo el fin de semana).

## 5. Requisitos Funcionales
*   **RF-O19-001 (Costeo Predictivo en CI/CD):** El pipeline de Terraform debe invocar a la herramienta `Infracost` en cada Pull Request para calcular el impacto monetario estimado del cambio en infraestructura (ej. "Este PR añadirá \$500 mensuales al gasto AWS").
*   **RF-O19-002 (Apagado Automático - Snoozing):** El sistema debe ejecutar funciones Serverless (AWS Lambda) que detengan temporalmente todas las instancias de cómputo y bases de datos etiquetadas como `Environment=Dev` a las 19:00 horas los viernes, y las enciendan a las 07:00 los lunes.
*   **RF-O19-003 (Limpieza de Basura):** Un script cronológico (Garbage Collector) debe identificar y purgar Snapshots de bases de datos que superen la política de retención máxima sin justificación normativa, IPs elásticas huérfanas y volúmenes EBS desconectados (Unattached).
*   **RF-O19-004:** El ingeniero SRE debe autorizar mediante aprobación manual las purgas destructivas sugeridas por los scripts (en caso de IPs o discos).

## 6. Requisitos No Funcionales
*   **RNF-O19-001 (Resiliencia de Políticas):** Las funciones automatizadas de apagado (Snoozing) no deben depender de agentes internos en las máquinas; se orquestarán exclusivamente a través de las APIs del plano de control del proveedor cloud (AWS API).

## 7. Reglas de Negocio
*   **RN-O19-001 (Excepción de Apagado):** Los recursos con la etiqueta `FinOps-Snooze=False` estarán exentos de las rutinas de apagado de fin de semana (útil para desarrolladores trabajando horas extras).
*   **RN-O19-002 (Umbral de Aprobación de Gasto):** Si el reporte de `Infracost` en un Pull Request predice un incremento en los costos de infraestructura superior al 10% del presupuesto mensual del equipo, el PR requiere obligatoriamente aprobación adicional del Desarrollador (Tú).

## 8. Entradas
*   Archivos Terraform (.tf) analizados por `Infracost`.
*   APIs del plano de control de AWS devolviendo metadatos (Tags) de los recursos activos.

## 9. Salidas
*   **Comentarios en GitHub:** Resumen financiero inyectado en el Pull Request.
*   **Acciones Automáticas:** Detención/Inicio de instancias EC2, purga de volúmenes EBS.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Control de incremento de costos en PR
**Dado** que un SRE intenta cambiar la clase de instancia de la base de datos transaccional de `db.r6g.large` a `db.r6g.4xlarge` en Staging
**Cuando** crea el Pull Request en GitHub
**Entonces** el pipeline ejecuta `Infracost` para parsear los cambios
**Y** agrega un comentario alertando que el costo mensual se incrementará en +\$1,200
**Y** el sistema aplica la regla `RN-O19-002` exigiendo que el Desarrollador (Tú) revise el PR antes del merge para justificar este gasto.

### Escenario 2: Rutina de ahorro de fin de semana (Snoozing)
**Dado** que es viernes a las 19:00 UTC
**Cuando** la función Lambda del Garbage Collector Cloud se dispara
**Entonces** consulta todas las instancias RDS y clústeres EKS que tienen la etiqueta `Environment=Dev`
**Y** pausa/detiene de forma segura dichas instancias
**Y** envía un mensaje a Slack confirmando que "El entorno de desarrollo ha sido suspendido para ahorrar recursos. Reinicio programado para el lunes 07:00 UTC".

## 11. Criterios de Aceptación
*   **CA-O19-001:** La purga de Snapshots caducos no puede eliminar Snapshots marcados con retención legal (Legal Hold), los cuales están protegidos por bloqueos nativos (Object Lock).

## 12. Restricciones
*   Bajo ningún pretexto las rutinas automáticas de FinOps operativas pueden afectar entornos etiquetados como `Environment=Production`, ya que eso comprometería directamente el Uptime del producto cliente.

## 13. Fuera de Alcance
*   Negociación de descuentos con el proveedor de Cloud. (Esta actividad es estrictamente comercial).
