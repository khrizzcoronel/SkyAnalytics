## ADDED Requirements

### Requirement: Detección de Secretos y Vulnerabilidades
El pipeline MUST fallar instantáneamente si detecta credenciales en texto claro o dependencias con CVE crítico.

#### Scenario: Secret Leak Bloqueado
- **WHEN** un commit incluye un `config.py` con `db_password="123"`
- **THEN** el escáner falla por "Secret Leak Detected".
