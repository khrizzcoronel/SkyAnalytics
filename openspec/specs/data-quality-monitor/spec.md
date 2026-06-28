## ADDED Requirements

### Requirement: Circuit Breaker de ETL
El sistema MUST validar campos nulos y schema drift, bloqueando los datos corruptos.

#### Scenario: Schema Drift
- **WHEN** un dato viene sin el `flight_id` (nulo)
- **THEN** el sistema aísla los datos en cuarentena y alerta a Slack.
