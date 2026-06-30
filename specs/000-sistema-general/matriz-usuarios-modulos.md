# Matriz de Usuarios × Módulos

Fuente única de verdad para roles y permisos de SkyAnalytics.

## Módulos

| ID | Carpeta | Dominio | CUs incluidos |
|---|---|---|---|
| 01 | `specs/01-identidad-acceso` | Identidad y Acceso | CU-O01, CU-O12 |
| 02 | `specs/02-api-vuelos` | API de Vuelos | CU-O02 |
| 03 | `specs/03-data-pipeline` | Data Pipeline | CU-O03, CU-O04, CU-O17, CU-O21, CU-O22, CU-O23, CU-T04 |
| 04 | `specs/04-ml` | Machine Learning | CU-O05, CU-O20, CU-T05 |
| 05 | `specs/05-bi-estrategico` | BI Estratégico | CU-O06, CU-E01, CU-E02, CU-E03, CU-E04, CU-E06 |
| 06 | `specs/06-observabilidad-sre` | Observabilidad y SRE | CU-O07, CU-O09, CU-O10, CU-O11, CU-O13 |
| 07 | `specs/07-soporte` | Soporte y Operaciones | CU-O08, CU-O14, CU-O15 |
| 08 | `specs/08-devex` | Developer Experience | CU-O16, CU-T07 |
| 09 | `specs/09-seguridad` | Seguridad | CU-O18, CU-T06 |
| 10 | `specs/10-finops` | FinOps | CU-O19, CU-T08 |
| 11 | `specs/11-growth-monetization` | Growth y Monetización | CU-T01, CU-T02, CU-T03, CU-T10 |
| 12 | `specs/12-resilience-testing` | Resiliencia | CU-T09 |
| 13 | `specs/13-okr-talento` | OKR y Talento | CU-E05 |

## Matriz de permisos

| Usuario / Módulo | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SUPER_ADMIN` | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD | CRUD |
| `C_LEVEL_EXEC` | R | R | R | R | CRUD | R | R | R | R | R | R | R | CRUD |
| `BOARD_MEMBER` | R | R | — | — | CRUD (Finance) | R | — | — | R | R | — | — | R |
| `OPERATOR` | R | API | R | R | R | R | R | R | R | R | R | R | R |
| `SRE` | R | R | CRUD | R | R | CRUD | R | R | R | R | R | CRUD | R |
| `DATA_ENGINEER` | — | — | CRUD | R | R | R | — | — | — | — | — | — | — |
| `ML_ENGINEER` | — | — | R | CRUD | R | R | — | — | — | — | — | — | — |
| `FINOPS_MANAGER` | — | — | — | — | — | — | — | — | — | CRUD | — | — | — |
| `SECOPS` | R | — | — | — | — | R | — | — | CRUD | — | — | — | — |
| `GROWTH_PM` | — | — | — | — | — | — | — | — | — | — | CRUD | — | — |
| `DEVREL` | — | — | — | — | — | — | — | CRUD | — | — | — | — | — |
| `CUSTOMER_SUCCESS` | — | — | — | — | R (eNPS) | — | CRUD | — | — | — | — | — | — |
| `TENANT_ADMIN` | R (own) | API | — | — | — | — | — | — | — | — | — | — | — |
| `CLIENT_API` | — | API | — | — | — | — | — | — | — | — | — | — | — |

## Leyenda

- **C** = Create
- **R** = Read
- **U** = Update
- **D** = Delete
- **API** = Acceso mediante API Key (M2M), no UI
- **—** = Sin acceso por defecto

## Notas

- `SUPER_ADMIN` tiene acceso total a todos los módulos.
- `TENANT_ADMIN` solo ve y administra su propio tenant (row-level security).
- **Alias usados en specs:**
  - `Desarrollador (Tú)` se refiere al `Founder` / `Solo-Founder` operando como SRE/Data/ML Engineer según el contexto del módulo.
  - `Desarrollador (Dueño)` se refiere al `C_LEVEL_EXEC` / `Founder` con visión estratégica.
  - `Auditores Externos`, `Clientes B2B` y `On-Call` son perfiles transversales mapeados a `BOARD_MEMBER`, `CLIENT_API` y `SRE` respectivamente.
- Los permisos se implementan mediante:
  - **PocketBase collection rules** para datos operativos/configuración.
  - **Next.js middleware + RBAC** para rutas del frontend.
  - **FastAPI dependencies** para endpoints backend.
- Esta matriz es la fuente única de verdad para definir reglas de acceso en `pb_schema.json`, `frontend/src/middleware.ts` y futuras políticas `rbac_policies`.
