## Context

El Módulo Operativo requiere aprovisionar recursos para nuevos clientes (Tenants). Esto incluye crear registros en bases de datos (PostgreSQL / PocketBase) y generar credenciales de API para interactuar con los pipelines de SkyAnalytics.

## Goals / Non-Goals

**Goals:**
- Validar correos corporativos utilizando una lista negra de dominios (Gmail, Hotmail, etc.).
- Aprovisionar un registro Tenant con un UUID.
- Generar dos llaves criptográficas seguras (`sk_test_...` y `sk_live_...`).
- Almacenar exclusivamente el Hash (SHA-256 / bcrypt) de las llaves, nunca el texto plano.
- Proveer un webhook o función para validar las API Keys en el Gateway en menos de 5ms.

**Non-Goals:**
- Crear el UI completo del registro en esta fase (nos enfocaremos puramente en la lógica Backend operativa en Python / Node).
- Configurar servidores SMTP reales (usaremos mocks o logs para la verificación de email).

## Decisions

- **Lenguaje Base para Operaciones:** El Módulo Operativo utilizará **Python 3.11+** por su rica ecosistema en scripts de orquestación y criptografía, tal como dicta el `plan.md` del módulo.
- **Lógica de Hashing:** Se usará la librería estándar `hashlib` o `passlib` de Python para aplicar KDF (Key Derivation Function) a la `Live_Key` generada aleatoriamente mediante `secrets`.
- **Estructura de Directorios:** El código operativo vivirá en la carpeta raíz `backend/` separada del monolito Next.js (`web/`).
- **Compensación de Errores (Rollback):** Si el aprovisionamiento de la API Key falla, se aplicará un patrón de "Saga coreografiada" simple para eliminar (rollback) el Tenant creado parcialmente.

## Risks / Trade-offs

- **Complejidad del Rollback:** Hacer rollback en PostgreSQL si falla una llamada externa puede requerir control manual transaccional `BEGIN/ROLLBACK`.
  - *Mitigación:* Se usará SQLAlchemy o un conector asíncrono con *Context Managers* en Python para asegurar la atomicidad de las transacciones.
