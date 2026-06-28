## ADDED Requirements

### Requirement: Cálculo de Rentabilidad
El sistema SHALL mostrar los KPIs financieros (ARR, LTV, CAC, Gross Margin) leyendo directamente la vista `vw_financial_metrics` del Data Warehouse (MonetDB).

#### Scenario: Visualización exitosa de métricas
- **WHEN** un usuario de alto nivel (BOARD_MEMBER o C_LEVEL) accede al dashboard de finanzas
- **THEN** el sistema carga y muestra el Gross Margin en menos de 3 segundos

### Requirement: Alerta NRR Anómalo
El sistema MUST proporcionar una advertencia visual si la Retención Neta de Ingresos (NRR) cae por debajo del 100%.

#### Scenario: Churn excesivo detectado
- **WHEN** el valor del NRR reportado es 98%
- **THEN** la interfaz resalta la métrica en color rojo y añade un ícono de advertencia.
