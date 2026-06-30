# Especificación de Caso de Uso: CU-O22

## 1. Nombre de la Funcionalidad
**Importar Dataset flights_raw de forma Incremental**

## 2. Objetivo
Cargar el dataset semilla `flight_data_2024.csv` conteniendo 7.08 millones de filas en la tabla `flights_raw` de PocketBase. La importación se realiza de forma incremental (100,000 registros por ejecución) para evitar timeouts y consumo excesivo de memoria en SQLite.

## 3. Actores Involucrados
- **Actor Principal:** Desarrollador (Manual) / Docker Engine
- **Sistemas Secundarios:** PocketBase (SQLite)

## 4. Contexto del Problema
Un archivo de 1.25 GB no puede ser procesado por una base de datos transaccional SQLite en una sola transacción sin bloquear la base de datos o fallar por límites de memoria. El proceso debe correr de forma aislada, pausarse tras un volumen determinado y poder reanudarse exactamente desde el último registro procesado.

## 5. Requisitos Funcionales
- **RF-O22-001:** El importador debe leer el archivo CSV desde una ruta compartida en un volumen de Docker.
- **RF-O22-002:** El sistema debe mantener un archivo de checkpoint JSON conteniendo el número de la última fila procesada con éxito.
- **RF-O22-003:** Cada ejecución del importador procesa exactamente 100,000 filas.
- **RF-O22-004:** La escritura debe ser directa a la base de datos SQLite de PocketBase (`pb_data/data.db`) usando transacciones por lotes para maximizar la velocidad.
- **RF-O22-005:** Las claves primarias (`id`) de los registros deben generarse de forma determinista para garantizar idempotencia.

## 6. Requisitos No Funcionales
- **RNF-O22-001 (Idempotencia):** Re-ejecutar el script sobre un bloque ya importado no debe duplicar las filas.

## 7. Escenarios (Gherkin)

### Escenario 1: Primera ejecución exitosa
- **DADO** que el archivo de checkpoint no existe
- **CUANDO** el contenedor `importer` se activa
- **ENTONCES** importa los registros del 0 al 100,000
- **Y** registra el checkpoint en 100,000.

## 8. Reglas de Negocio
- **RN-O22-001 (Checkpoint único):** El archivo `/data/importer_checkpoint.json` es la única fuente de verdad para la fila de reanudación.
- **RN-O22-002 (IDs deterministas):** Cada registro recibe un `id` determinista `fl` + índice de 13 dígitos, garantizando idempotencia ante re-ejecuciones.
- **RN-O22-003 (Tamaño de chunk fijo):** Cada ejecución procesa exactamente 100,000 filas o el remanente del archivo si es menor.

## 9. Entradas
| Campo | Tipo | Descripción |
|---|---|---|
| `flight_data_2024.csv` | Archivo CSV | Dataset semilla BTS 2024 (~1.25 GB, 7.08M filas). |
| `importer_checkpoint.json` | Archivo JSON | Última fila procesada con éxito. |
| `pb_data/data.db` | SQLite | Base de datos de PocketBase montada como volumen. |

## 10. Salidas
| Campo / Objeto | Tipo | Descripción |
|---|---|---|
| `flights_raw` | Tabla PocketBase | Registros importados en lotes. |
| `importer_checkpoint.json` | Archivo JSON | `last_row` y `updated_at` actualizados. |

## 11. Criterios de Aceptación
- **CA-O22-001:** Una ejecución fresca importa exactamente 100,000 filas y el checkpoint avanza a 100,000.
- **CA-O22-002:** Ejecutar el importador dos veces seguidas sin modificar el CSV produce el mismo estado final (idempotencia vía `INSERT OR REPLACE`).
- **CA-O22-003:** Interrumpir el proceso en la fila 250,001 y reanudarlo continúa desde esa fila sin duplicados.

## 12. Restricciones
- El schema de `flights_raw` debe existir en PocketBase antes de ejecutar el importador.
- El archivo CSV debe seguir el formato BTS 2024 con los 35 campos esperados.
- El contenedor debe tener acceso de escritura al volumen `pb_data` y al volumen `importer_data`.

## 13. Fuera de Alcance
- Validación de calidad de datos (se realiza en `CU-O04` durante el ETL).
- Transformación a Star Schema (`CU-O21`).
- Importación vía HTTP API de PocketBase (se usa acceso directo a SQLite por volumen compartido).

## 14. Aclaraciones Globales (Speckit-Clarify)
- **Dataset semilla BTS 2024:** Es la fuente primaria oficial; otros datasets requieren aprobación arquitectónica.

