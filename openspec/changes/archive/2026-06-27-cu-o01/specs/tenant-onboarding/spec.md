## ADDED Requirements

### Requirement: Validación de Email Corporativo
El sistema SHALL interceptar el intento de registro y cruzar el dominio del correo con una lista de rechazo (blacklist) de proveedores gratuitos (gmail.com, yahoo.com, outlook.com).

#### Scenario: Rechazo automático de email genérico
- **WHEN** el usuario envía `analytics-test@gmail.com`
- **THEN** la función Python retorna una excepción `ValueError("Por favor utiliza un correo corporativo válido")` deteniendo la transacción de base de datos.
