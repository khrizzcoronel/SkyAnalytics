---
module: 05-bi-estrategico
primary_user: C_LEVEL_EXEC
---
## ADDED Requirements

### Requirement: Exportación a PDF (Client-Side)
El sistema SHALL permitir al usuario exportar el tablero actual a formato PDF invocando la funcionalidad nativa de impresión del navegador. El componente `PrintToPdfButton` debe estar disponible en la vista principal.

#### Scenario: Exportación exitosa a PDF
- **WHEN** el usuario hace clic en el botón de exportación a PDF
- **THEN** el sistema invoca `window.print()` y las reglas `@media print` de CSS ocultan la barra de navegación lateral y superior, ajustando los gráficos a una cuadrícula imprimible.
