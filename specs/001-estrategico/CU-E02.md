# Especificación de Caso de Uso: CU-E02

## 1. Nombre de la Funcionalidad
**Analizar ARR y Rentabilidad**

## 2. Objetivo
Proveer a la alta dirección (Desarrollador (Dueño)) herramientas analíticas para monitorear el Ingreso Recurrente Anual (ARR), el Costo de Adquisición de Clientes (CAC), el Valor del Tiempo de Vida del Cliente (LTV) y el Margen Bruto, garantizando visibilidad total sobre la rentabilidad del modelo SaaS.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Dueño)
*   **Sistemas Externos / Actores Secundarios:** Stripe Test Mode de Pagos (fuente externa), PocketBase (Operativa) y MonetDB (Analítica) (Data Warehouse).

## 4. Contexto del Problema
Para sostener el crecimiento de SkyAnalytics, el Desarrollador (Dueño) requiere comprender la procedencia de los ingresos y controlar el costo de infraestructura frente al revenue (Margen Bruto). Integrar los datos de suscripciones y facturación cloud de manera unificada es esencial para proyectar el flujo de caja y presentar reportes a la ti mismo.

## 5. Requisitos Funcionales
*   **RF-E02-001:** El sistema debe calcular y mostrar el ARR consolidado y desglosado por plan de suscripción (Freemium, Pro, Enterprise).
*   **RF-E02-002:** El sistema debe calcular el ratio LTV/CAC utilizando los datos históricos de permanencia y el gasto de marketing registrado.
*   **RF-E02-003:** El sistema debe mostrar el Gross Margin (Margen Bruto) deduciendo el gasto de infraestructura cloud del ARR mensualizado.
*   **RF-E02-004:** El sistema debe alertar visualmente si existe una anomalía negativa en la retención neta de ingresos (NRR < 100%).
*   **RF-E02-005:** El sistema debe permitir la exportación del reporte financiero consolidado mensual en formato PDF encriptado o CSV estandarizado.

## 6. Requisitos No Funcionales
*   **RNF-E02-001:** El cálculo analítico masivo de cohortes financieras no debe exceder los 3 segundos de respuesta mediante la ejecución de queries columnares en PocketBase (Operativa) y MonetDB (Analítica).
*   **RNF-E02-002:** Los datos financieros en tránsito y en reposo deben cumplir estrictamente con el estándar AES-256 para prevenir fugas de información.
*   **RNF-E02-003:** Toda exportación financiera debe llevar una marca de agua digital con la fecha, hora y el ID del usuario que la generó (trazabilidad de auditoría).

## 7. Reglas de Negocio
*   **RN-E02-001 (Fórmula Gross Margin):** `((ARR - Costo Cloud Anualizado) / ARR) * 100`. La meta estratégica es $\geq$ 75%.
*   **RN-E02-002 (Fórmula NRR):** `((ARR Inicial + Expansión - Churn) / ARR Inicial) * 100`. La meta es $\geq$ 110%.
*   **RN-E02-003 (Acceso de Seguridad):** Acceso restringido exclusivamente a roles `Desarrollador (Dueño)` y `BOARD_MEMBER`.

## 8. Entradas
*   Token JWT válido con claim `mfa_verified`.
*   Filtros en UI:
    *   `periodo` (String: Q1, Q2, YTD, etc.)
    *   `segmento_cliente` (String: Enterprise, SMB, Todo)

## 9. Salidas
*   **Payload JSON:**
    *   Métricas agregadas: `{ arr_total, ltv_cac_ratio, gross_margin, nrr, mrr_churn }`
    *   Datos de gráfico de barras: `[ { mes, new_arr, expansion_arr, churned_arr } ]`
*   **UI:** Paneles de visualización financiera y botón de exportación segura.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Análisis de Gross Margin exitoso
**Dado** que el Desarrollador (Dueño) ha accedido al módulo de Finanzas
**Cuando** selecciona la vista de "Margen Bruto" para el último trimestre
**Entonces** el sistema cruza los ingresos reales (Stripe) contra la facturación cloud (Panel de facturación del PaaS vía ETL)
**Y** muestra un margen bruto del 78% con indicador en verde (por encima del 75% esperado).

### Escenario 2: Generación de reporte financiero mensual
**Dado** que el Desarrollador (Dueño) está en la vista financiera
**Cuando** hace clic en "Exportar Reporte Mensual"
**Entonces** el sistema compila los datos en un PDF protegido
**Y** agrega la marca de agua con el nombre del Desarrollador (Dueño) y el timestamp actual
**Y** descarga el archivo en menos de 5 segundos.

## 11. Criterios de Aceptación
*   **CA-E02-001:** Las fórmulas de ARR, NRR y LTV coinciden exactamente con los modelos estandarizados en `dbt` y verificados por las suites de Validaciones nativas (Pydantic/Zod).
*   **CA-E02-002:** Un usuario con rol `Desarrollador (Tú)` intentando acceder a la rentabilidad global recibe un HTTP `403`.
*   **CA-E02-003:** El PDF exportado no puede ser editado sin romper la firma digital del documento.

## 12. Restricciones
*   Los datos mostrados tienen un desfase (lag) máximo de 24 horas (correspondiente a la ingesta diaria del ETL financiero), no son en tiempo real exacto (streaming).

## 13. Fuera de Alcance
*   Procesamiento de pagos o devoluciones a clientes (Stripe se encarga del procesamiento, SkyAnalytics solo lee la facturación).
