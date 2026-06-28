## ADDED Requirements

### Requirement: Caché (In-Memory)
El sistema SHALL retener en un diccionario la respuesta de la API la primera vez que se consulta un vuelo. 

#### Scenario: Cache Hit
- **WHEN** un cliente consulta `/v1/flights/AA123` por segunda vez
- **THEN** la respuesta se sirve del diccionario `FAKE_REDIS_CACHE` 
- **AND** el campo interno `_cached` retorna `True`.
