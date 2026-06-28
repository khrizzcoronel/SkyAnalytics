## 1. Data Contracts (Pydantic)

## 1. Data Contracts (Pydantic)

- [x] 1.1 Crear el contrato estricto en `backend/src/quality/contracts.py` usando Pydantic, definiendo el esquema de un `FlightRecord` (vuelo).
- [x] 1.2 Agregar validación de enumeraciones (`Literal['ON_TIME', 'DELAYED', 'CANCELLED']`) y numéricas (`monto_pago > 0`).

## 2. Motor de Calidad y Circuit Breaker

- [x] 2.1 Crear el validador principal en `backend/src/quality/data_quality_suite.py` que reciba un DataFrame y lo itere/valide.
- [x] 2.2 Implementar la lógica del "Circuit Breaker": calcular el % de error. Si `error_rate > 0.01` (1%), lanzar una excepción para abortar.
- [x] 2.3 Si pasa la prueba, invocar un método (stub) `promote_to_core()` que simule la carga a la tabla `Fact_Flight`.

## 3. Pruebas y Ensamblaje

- [x] 3.1 Crear un pequeño test/runner `test_quality.py` que simule un lote de Staging pasando el umbral (deberá promover a Core) y otro fallando el umbral (deberá ser bloqueado).
