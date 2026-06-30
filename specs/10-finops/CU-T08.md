# Especificación de Caso de Uso: CU-T08

## 1. Nombre de la Funcionalidad
**Analizar Costos Cloud y Optimizar**

## 2. Objetivo
Proveer visibilidad granular y monitoreo continuo sobre el gasto de infraestructura cloud de la empresa, identificando desperdicios y oportunidades de reducción de costos mediante sugerencias (FinOps).

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / SRE Lead
*   **Sistemas Externos / Actores Secundarios:** AWS Cost Explorer API, Grafana (Panel FinOps).

## 4. Contexto del Problema
Los costos cloud en aplicaciones analíticas y de Big Data (clusters de PaaS, ingesta de TB de datos, Data Warehouses) pueden salirse de control rápidamente. Es necesario tener visibilidad diaria y no esperar a la factura a fin de mes para descubrir un "pico" provocado por un loop infinito en un script o recursos no utilizados (orphan resources).

## 5. Requisitos Funcionales
*   **RF-T08-001:** El sistema debe consumir los datos diariamente desde la API de Panel de facturación del PaaS y presentarlos en un dashboard (Grafana FinOps).
*   **RF-T08-002:** El sistema debe desglosar los costos utilizando las etiquetas de Terraform (Tags: `Environment`, `Project`, `Owner`).
*   **RF-T08-003:** El sistema debe enviar una alerta a Slack (canal `#finops`) si el gasto diario de cualquier servicio excede el forecast en más de un 20%.
*   **RF-T08-004:** El sistema debe identificar proactivamente recursos "Zombie" o inactivos (ej. volúmenes EBS sin asociar a instancias, IPs elásticas huérfanas, instancias de base de datos sin conexiones).

## 6. Requisitos No Funcionales
*   **RNF-T08-001:** Los reportes de gastos proyectados deben considerar los descuentos aplicados previamente (ej. Reserved Instances, Savings Plans) para ofrecer una métrica de costo neto (Net Unblended Cost) precisa.

## 7. Reglas de Negocio
*   **RN-T08-001 (Política de Alerta):** Toda desviación de gasto superior a \$100 diarios frente a la media de la semana pasada dispara una advertencia amarilla.
*   **RN-T08-002 (Eliminación de Basura):** Los entornos efímeros (ej. despliegues creados específicamente para pruebas E2E de un Pull Request) deben auto-destruirse a las 24 horas. Si sobreviven y generan costos, se cuenta como violación a la política.

## 8. Entradas
*   Datos estructurados desde el proveedor cloud (JSON/CSV) vía API Billing.
*   Filtros UI:
    *   Rango de fechas.
    *   Filtro por tag (ej. `Environment: Staging`).

## 9. Salidas
*   **Alertas Slack:** Mensaje detallando el servicio culpable del pico (ej. Transferencia S3, Computo EC2).
*   **Reportes PDF/Excel:** Tabla de oportunidades de rightsizing (Reducción de tamaño de instancias).

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Detección y alerta temprana de pico de gasto
**Dado** que un desarrollador despliega accidentalmente un bucle en el pipeline ETL que realiza millones de transferencias PUT a S3
**Cuando** el script de conciliación de costos lee la API de Billing del día
**Entonces** el sistema detecta que el gasto en `AmazonS3` sobrepasó el 20% del forecast
**Y** envía inmediatamente una alerta roja al canal de `#finops` y notifica al SRE Lead.

### Escenario 2: Análisis de Rightsizing (ajuste de tamaño)
**Dado** que el Desarrollador (Tú) está analizando oportunidades de ahorro
**Cuando** ingresa a la pestaña "Recomendaciones" del dashboard
**Entonces** el sistema muestra que los nodos del cluster EKS `worker-group-b` utilizan en promedio solo 15% de CPU
**Y** sugiere cambiar el tipo de instancia (ej. de `m5.2xlarge` a `m5.xlarge`), estimando un ahorro de $1,200 mensuales.

## 11. Criterios de Aceptación
*   **CA-T08-001:** La suma total del dashboard interno debe coincidir con un margen de error menor al 1% con la factura real emitida por el proveedor (salvo discrepancias por impuestos locales aplicados a fin de mes).
*   **CA-T08-002:** El dashboard debe cargar las gráficas de evolución de gastos de los últimos 6 meses en un tiempo máximo de respuesta inferior a 5 segundos.

## 12. Restricciones
*   El dashboard depende de la actualización de facturación por parte de AWS (suele tener retraso de 12-24 horas, no es tiempo real a nivel milisegundo).

## 13. Fuera de Alcance
*   Compra y compromiso automático de Instancias Reservadas (Savings Plans). El sistema sugiere, pero la compra exige aprobación administrativa y click humano en la consola nativa del proveedor.

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Desfase de facturación:** El dashboard muestra la fecha de facturación del proveedor, no la fecha de consumo; se documenta explícitamente para evitar confusiones.
*   **Acceso financiero:** Solo roles `FINOPS_MANAGER` y `C_LEVEL_EXEC` pueden ver costos agregados y proyecciones.
