# Especificación de Caso de Uso: CU-O23

## 1. Nombre de la Funcionalidad
**Monitorear Drift del Dataset de Vuelos**

## 2. Objetivo
Evaluar y alertar sobre desviaciones estadísticas significativas (Data Drift) en el dataset de vuelos entrante comparado contra el baseline histórico, con el fin de detectar de forma temprana degradación en el rendimiento de los modelos predictivos de Machine Learning.

## 3. Actores Involucrados
- **Actor Principal:** GitHub Actions (Cron) / Sistema
- **Sistemas Secundarios:** MonetDB, Slack

## 4. Contexto del Problema
Los modelos de Machine Learning asumen que la distribución de los datos futuros es similar a la del pasado. Eventos atípicos (huelgas de aerolíneas, tormentas severas, o cambios estructurales en rutas) modifican el comportamiento real de los retrasos. Si esto ocurre sin notificar, las predicciones del modelo se vuelven inválidas.

## 5. Requisitos Funcionales
- **RF-O23-001:** El sistema debe ejecutar una auditoría de distribución estadística de forma semanal (lunes 06:00 AM).
- **RF-O23-002:** Debe extraer los últimos retrasos registrados en `vw_delay_analysis` y compararlos contra el histórico.
- **RF-O23-003:** Debe calcular el índice PSI (Population Stability Index) para el campo `dep_delay`.
- **RF-O23-004:** Si el PSI > 0.25 (Drift crítico), debe notificar inmediatamente a `#data-ops` en Slack.
- **RF-O23-005:** Si el PSI está entre 0.1 y 0.25 (Drift moderado), debe registrar un aviso en los logs.

## 6. Requisitos No Funcionales
- **RNF-O23-001 (Performance):** El análisis de drift sobre 100K filas no debe tardar más de 2 minutos.

## 7. Escenarios (Gherkin)

### Escenario 1: Datos estables sin acción necesaria
- **DADO** que la auditoría semanal se inicia
- **CUANDO** el PSI de los retrasos de vuelos es 0.04
- **ENTONCES** el monitor registra estado "Estable"
- **Y** no envía alertas.

## 8. Reglas de Negocio
- **RN-O23-001 (División baseline/challenger):** El 80% de datos más antiguos (ordenados por `fl_date`) conforman el baseline; el 20% más reciente es el challenger.
- **RN-O23-002 (Umbrales PSI):**
  - `< 0.1` → Estado Estable (verde)
  - `0.1 - 0.25` → Drift Moderado (amarillo)
  - `> 0.25` → Drift Crítico (rojo)
- **RN-O23-003 (Alerta crítica):** Solo el estado rojo dispara notificación a Slack `#data-ops`.

## 9. Entradas
| Campo | Tipo | Descripción |
|---|---|---|
| `vw_delay_analysis` | Vista MonetDB | Datos limpios de retrasos con `fl_date` y `dep_delay`. |
| `SLACK_WEBHOOK_URL` | Env var | Webhook para alertas (opcional). |

## 10. Salidas
| Campo / Objeto | Tipo | Descripción |
|---|---|---|
| `psi_value` | float | Valor de Population Stability Index calculado. |
| `drift_status` | string | `stable` / `warning` / `critical`. |
| `slack_notification` | HTTP POST | Mensaje a `#data-ops` solo si `critical`. |

## 11. Criterios de Aceptación
- **CA-O23-001:** El cronjob `drift-monitor.yml` ejecuta los lunes a las 06:00 AM UTC.
- **CA-O23-002:** Con PSI = 0.04 el estado es `stable` y no se envía alerta.
- **CA-O23-003:** Con PSI = 0.38 el estado es `critical` y se envía alerta a Slack.

## 12. Restricciones
- Requiere al menos 1,000 registros en `vw_delay_analysis` para que el análisis sea estadísticamente significativo.
- MonetDB debe estar disponible.
- El campo `dep_delay` debe estar presente y no ser nulo en todos los registros analizados.

## 13. Fuera de Alcance
- Reentrenamiento automático del modelo (`CU-O05`).
- Análisis causal del drift.
- Monitoreo de drift de features individuales (se limita a `dep_delay`).

## 14. Aclaraciones Globales (Speckit-Clarify)
- **Logs 30 días:** Los estados de drift se registran en logs con retención de 30 días.

