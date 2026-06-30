---
module: 05-bi-estrategico
primary_user: C_LEVEL_EXEC
---
## ADDED Requirements

### Requirement: Trazabilidad en Exportación (Marca de Agua)
Toda exportación a PDF MUST incluir una marca de agua visible que identifique el nombre o email del usuario autenticado que generó el reporte, junto con un sello de tiempo (timestamp).

#### Scenario: Exportación segura a PDF
- **WHEN** un usuario con permisos hace clic en exportar PDF
- **THEN** el sistema inyecta en el DOM un contenedor visible solo para CSS `@media print` que muestra texto diagonal con el formato "Confidencial - Exportado por [Usuario] - [Fecha/Hora]".
