# Especificación de Caso de Uso: CU-O17

## 1. Nombre de la Funcionalidad
**Validar Data Contracts en Pipeline ETL**

## 2. Objetivo
Asegurar que los productores de datos (sistemas origen) no rompan silenciosamente los esquemas de información esperados por los consumidores de datos (pipelines de ML y Dashboards), validando *Data Contracts* explícitos antes de la ingestión en el Data Warehouse.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** dbt (Validación de Esquema), Apache Kafka / GitHub Actions, Schema Registry.

## 4. Contexto del Problema
A diferencia del CU-O04 (que valida reglas de negocio estadísticas), este caso se enfoca en la ruptura estructural a nivel de esquema (*Schema Drift*). Si el equipo que desarrolla el microservicio de Reservas cambia el nombre de la columna `user_id` a `account_id` sin avisar, todo el ecosistema de analítica posterior colapsa de forma encadenada. Los Data Contracts previenen esto.

## 5. Requisitos Funcionales
*   **RF-O17-001:** El sistema debe mantener un repositorio versionado de Contratos de Datos (Data Contracts) en formato YAML que especifique esquemas, tipos y propietarios de los datos.
*   **RF-O17-002:** Durante el pipeline de CI/CD del equipo Productor de datos, se debe validar si sus cambios estructurales rompen el contrato actual pactado con el equipo Consumidor.
*   **RF-O17-003:** Durante el pipeline de Ingesta ETL (Consumidor), se debe contrastar el esquema real de los datos entrantes contra el Contrato almacenado en el Schema Registry.
*   **RF-O17-004:** Si el esquema entrante rompe el contrato, la ingesta debe abortarse y aislarse.

## 6. Requisitos No Funcionales
*   **RNF-O17-001 (Baja Latencia):** La validación del esquema (mediante protobuf/Avro o JSON Schema) en arquitecturas de streaming (Kafka) debe realizarse en milisegundos por mensaje.

## 7. Reglas de Negocio
*   **RN-O17-001 (Evolución de Esquemas Compatible):** Agregar nuevas columnas opcionales al final del registro se considera un cambio "Forward-Compatible" y se acepta.
*   **RN-O17-002 (Evolución de Esquemas Incompatible):** Eliminar una columna, cambiar un tipo de dato (ej. String a Integer), o renombrar un campo se considera un "Breaking Schema Change" y es rechazado automáticamente por el Schema Registry.

## 8. Entradas
*   Data Contract en YAML (`dataset: flights, version: 1, schema: [...]`).
*   Datos entrantes (Mensajes JSON/Avro o Archivos Parquet).

## 9. Salidas
*   **Validación:** Pass/Fail del validador de esquema.
*   **Registro:** Actualización del Schema Registry si hay un cambio compatible.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Cambio Backward-Compatible aprobado
**Dado** que el equipo de Productor (Microservicio de Vuelos) decide agregar un nuevo campo `wifi_available (boolean)`
**Cuando** validan su código en el CI/CD contra el Contrato de Datos vigente
**Entonces** el validador de esquemas determina que es un cambio no destructivo
**Y** permite el despliegue del productor
**Y** actualiza la versión del Data Contract a `v1.1`.

### Escenario 2: Bloqueo de Schema Drift Incompatible
**Dado** que el proveedor externo elimina el campo `flight_number` y lo reemplaza por `flight_id_hash`
**Cuando** el proceso de ETL (CU-O03) intenta cargar el nuevo lote de datos
**Entonces** el validador de Data Contracts choca contra la especificación pactada `v1`
**Y** aborta la ejecución con el error "Schema Violation: missing required field 'flight_number'"
**Y** los datos se depositan en el bucket de Dead Letter Queue (DLQ).

## 11. Criterios de Aceptación
*   **CA-O17-001:** El equipo Consumidor (Desarrollador (Tú)s) debe ser notificado automáticamente por correo/Slack 30 días antes de que un equipo Productor ejecute una migración planificada de un "Breaking Change" (Deprecation Plan).

## 12. Restricciones
*   Los contratos de datos no se gestionan en hojas de cálculo, deben estar obligatoriamente alojados como código (Docs-as-Code) en el repositorio central.

## 13. Fuera de Alcance
*   Transformación mágica de los datos para que coincidan con el contrato antiguo (El contrato valida y detiene, no reescribe la historia).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Errores ETL:** Si ingresan datos basura, se **aislarán en una tabla de cuarentena**, permitiendo que el resto del lote válido se cargue en la base de datos para no dejar vacíos los dashboards.
