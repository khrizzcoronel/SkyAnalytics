---
module: 01-identidad-acceso
primary_user: SRE
---
## ADDED Requirements

### Requirement: Key Generation and Hashing
El sistema operativo SHALL generar API Keys criptográficamente fuertes utilizando entropía del sistema (ej. `secrets.token_urlsafe(32)`).
El sistema MUST guardar en la base de datos únicamente un Hash de la llave de Producción, utilizando algoritmos como SHA-256.

#### Scenario: Almacenamiento seguro
- **WHEN** el script de Python genera la llave `sk_live_abc123...`
- **THEN** guarda el hash `e3b0c4429...` en la columna `api_key_hash` del Tenant
- **AND** retorna la llave en texto plano *una sola vez* al invocador para su visualización inicial.
