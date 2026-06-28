## ADDED Requirements

### Requirement: Trazabilidad y Scrubbing
El sistema MUST inyectar un `TraceID` en cada log y MUST enmascarar datos PII (ej. tarjetas de crédito).

#### Scenario: Scrubbing de Logs
- **WHEN** el sistema intenta loggear `Pago fallido con tarjeta 4532...`
- **THEN** el logger automático enmascara a `Pago fallido con tarjeta ****...`
