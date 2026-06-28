## Why

Actualmente no existe un proceso automatizado para registrar clientes corporativos (Tenants) en el sistema. Esto produce un cuello de botella operativo, ya que el alta manual retrasa la entrega de valor. Además, necesitamos un sistema robusto que genere y encripte automáticamente las API Keys (Sandbox y Live) para que el cliente pueda integrarse con SkyAnalytics inmediatamente.

## What Changes

- **Registro de Tenant**: Creación de un flujo de registro validando que el correo pertenezca a un dominio corporativo (rechazo a Gmail/Hotmail).
- **Proceso Asíncrono de Aprovisionamiento**: Una vez registrado el Tenant en la base de datos PostgreSQL, se generarán claves de API seguras (SHA-256 KDF).
- **Verificación de Email**: Envío de correo con token JWT caducable a las 24 horas.
- **One-time Display**: Interfaz donde la API Key de Producción solo se muestra una vez al usuario.

## Capabilities

### New Capabilities
- `tenant-onboarding`: Flujo de registro y validación de correo corporativo.
- `api-key-provisioning`: Servicio Python para generar API Keys criptográficas y guardar solo sus hashes (KDF).

### Modified Capabilities
- 

## Impact

- **Backend (Python)**: Creación de scripts/servicios en Python para manejar la lógica de hashing y aprovisionamiento.
- **Base de Datos**: Creación de tabla `Tenants` y `ApiKeys` en PostgreSQL/PocketBase.
- **Seguridad**: Implementación de políticas de Zero Trust y cifrado para las credenciales.
