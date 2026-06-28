## Context

El paso CU-O03 nos dejó datos en la tabla `Staging` (en nuestro simulador, en memoria o stub). Ahora debemos someter esa tabla a pruebas rigurosas antes de que lleguen a `Fact_Flight`.

## Goals / Non-Goals

**Goals:**
- Utilizar Pydantic para definir el **Data Contract** exacto de la tabla de Vuelos.
- Crear un validador que tome los datos del Staging, valide cada fila contra el modelo de Pydantic, y calcule el porcentaje de errores.
- Si los errores superan el umbral (ej. 1%), lanzar una excepción que detenga la promoción (Circuit Breaker).
- Si pasa, promover los datos a la tabla Core.

**Non-Goals:**
- Integrar dbt (Data Build Tool) real. Simularemos el paso de transformación/promoción en Python.
- Generar el reporte HTML estático en este sprint; nos enfocaremos en la lógica dura de rechazo/promoción en consola.

## Decisions

- **Uso de Pydantic para el Data Contract:** Pydantic es la herramienta estándar en Python moderno para validación de datos. Permite validar tipos, Enums (ej. solo "ON_TIME", "DELAYED", "CANCELLED") y establecer reglas customizadas.
- **Tolerancia a Errores (Soft vs Hard):** Si el error es menor a la tolerancia permitida, las filas buenas pasan a Producción (`Fact_Flight`) y las malas se quedan atrás. Si el error sobrepasa, **ninguna fila** pasa a Producción.

## Risks / Trade-offs

- **Performance en Python:** Validar millones de filas fila-por-fila con Pydantic puede ser lento comparado con SQL nativo o Grandes Expresiones (Great Expectations).
  - *Mitigación:* Para el volumen actual, Pydantic es suficiente y permite definir reglas de negocio muy complejas fácilmente en código. A futuro se puede migrar a dbt tests si el volumen lo exige.
