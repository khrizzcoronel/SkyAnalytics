---
module: 02-api-vuelos
primary_user: CLIENT_API
---
## ADDED Requirements

### Requirement: Consulta de Vuelos Endpoint
El sistema SHALL exponer la ruta `GET /v1/flights/{flight_id}` y retornar la información del vuelo y su predicción en formato JSON.

#### Scenario: Consulta estándar
- **WHEN** el cliente hace un request a `/v1/flights/AA123`
- **THEN** el sistema retorna JSON con `{ "flight_id": "AA123", "status": "ON_TIME", "prediction_delay_minutes": 5 }`.
