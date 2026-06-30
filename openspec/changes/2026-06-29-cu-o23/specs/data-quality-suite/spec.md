## ADDED Requirements

### Requirement: Data Drift Monitoring via PSI
El sistema SHALL calcular el Population Stability Index (PSI) de la variable `dep_delay` en `vw_delay_analysis` comparando un baseline histórico contra los datos más recientes.

#### Scenario: Drift severo detectado
- **WHEN** el monitor semanal ejecuta
- **THEN** calcula PSI entre el 80% de datos más antiguos y el 20% más recientes
- **AND** si PSI > 0.25 envía alerta a Slack #data-ops
- **AND** reporta estado Red/Yellow/Green.

### Requirement: Configurable Slack Alerting
El monitor SHALL usar `SLACK_WEBHOOK_URL` para enviar notificaciones; si no está configurado, imprime el alerta en logs sin fallar.

#### Scenario: Falta webhook
- **WHEN** `SLACK_WEBHOOK_URL` no está definido
- **THEN** el monitor calcula PSI y reporta estado
- **AND** continúa sin error aunque no envíe Slack.
