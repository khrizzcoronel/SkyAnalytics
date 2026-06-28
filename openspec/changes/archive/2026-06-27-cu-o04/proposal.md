## Why

Ingerir datos en la capa de Staging (CU-O03) es el primer paso, pero antes de que los datos puedan usarse para Analítica o Machine Learning, deben cumplir contratos estrictos de calidad (Data Contracts). Si los datos de Staging entran al Core con esquemas rotos (Schema Drift) o valores lógicamente imposibles, los Dashboards Estratégicos que creamos fallarán o mostrarán valores irreales, destruyendo la confianza en la plataforma.

## What Changes

- **Suite de Calidad de Datos (Pydantic)**: Crearemos un validador exhaustivo que revisa el 100% de los datos de Staging antes de moverlos al Core.
- **Circuit Breaker**: Lógica que detiene inmediatamente el pipeline y arroja error si el umbral de fallas supera el límite de tolerancia (ej. 1%).
- **Promoción a Core**: Si la validación pasa, los datos sanos se insertan en `Fact_Flight`.

## Capabilities

### New Capabilities
- `data-quality-suite`: Módulo de validación de esquemas y reglas de negocio.
- `circuit-breaker-guard`: Componente que aborta transacciones (abort promotion) cuando hay Schema Drift masivo.

### Modified Capabilities
- 

## Impact

- **Backend (Python)**: Agregaremos scripts en `backend/src/quality/`.
- **Confiabilidad**: SkyAnalytics asegura que todo dato visible en los dashboards es 100% confiable y verificado.
