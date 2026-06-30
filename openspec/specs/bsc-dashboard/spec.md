---
module: 05-bi-estrategico
primary_user: C_LEVEL_EXEC
---
## ADDED Requirements

### Requirement: Autenticación y Control de Acceso (RBAC)
El sistema MUST verificar el token JWT y el soporte de Autenticación Multifactor (MFA) del usuario. Solamente usuarios con roles `SUPER_ADMIN` o `C_LEVEL_EXEC` pueden acceder a los datos del tablero BSC.

#### Scenario: Acceso con rol no autorizado
- **WHEN** un usuario con rol `OPERATOR` intenta consultar el endpoint del BSC
- **THEN** el sistema retorna HTTP `403 Forbidden` y genera un log de auditoría.

#### Scenario: Acceso con credenciales válidas
- **WHEN** el `C_LEVEL_EXEC` con MFA validado consulta el dashboard
- **THEN** el sistema responde con el payload JSON de KPIs en menos de 2 segundos.

### Requirement: Consolidación y Semaforización de KPIs
El sistema SHALL cargar KPIs desde MonetDB y cruzarlos con las metas de PocketBase, evaluando semáforos: Verde (>= 100%), Amarillo (80%-99.9%), Rojo (< 80%). Para procesos/uptime: Verde (>= 99.0%), Amarillo (95%-98.9%), Rojo (< 95%).

#### Scenario: Evaluación Financiera por debajo del umbral
- **WHEN** el ARR actual es menor al 80% de la meta trimestral
- **THEN** el sistema retorna el indicador con el estado de semáforo Rojo.

#### Scenario: Evaluación de Uptime en zona de precaución
- **WHEN** la disponibilidad del sistema es 98.0%
- **THEN** el widget de Uptime se renderiza en Amarillo.

### Requirement: Drill-down Histórico (LTM)
El sistema MUST permitir desglosar un KPI para ver su historia detallada. Al solicitar la serie temporal, por defecto debe cargar los últimos 12 meses (LTM).

#### Scenario: Consulta histórica de ARR
- **WHEN** el usuario hace clic sobre el widget de ARR
- **THEN** el sistema entrega una serie de datos de 12 puntos y despliega un gráfico de líneas (`HistoricalChartModal`).
