## Context
Garantizamos la integridad de los datos en el punto de ingestión.

## Decisions
- Crearemos `backend/src/etl/data_contract_validator.py`.
- **Regla RN-O17-001:** Permitiremos añadir columnas (Forward-Compatible).
- **Regla RN-O17-002:** Bloquearemos si se elimina una columna pactada o cambia su tipo (Breaking Schema Change).
