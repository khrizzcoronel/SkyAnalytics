## ADDED Requirements

### Requirement: Sanitización de Exportación SLA
El documento exportado en PDF para el cumplimiento del SLA SHALL omitir detalles confidenciales de la infraestructura (Ej. Nodos internos, IDs de Kubernetes, IPs).

#### Scenario: Exportar reporte para Enterprise
- **WHEN** el usuario hace clic en el botón de exportación en el tablero de ingeniería
- **THEN** la tabla de nodos internos es ocultada en el archivo PDF resultante mediante la regla CSS `@media print { .internal-infra { display: none !important; } }`.
