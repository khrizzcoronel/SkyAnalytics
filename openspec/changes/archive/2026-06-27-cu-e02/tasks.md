## 1. Backend API y Auth

- [x] 1.1 Implementar ruta API `/api/v1/estrategico/finance/metrics` en Next.js.
- [x] 1.2 Extender el Middleware para validar el acceso a la ruta `/dashboard/finance` y permitir el rol `BOARD_MEMBER`.
- [x] 1.3 Conectar API con MonetDB (`vw_financial_metrics`) para extraer ARR, CAC, LTV y Gross Margin.

## 2. Frontend Componentes

- [x] 2.1 Desarrollar panel financiero con widgets numéricos para ARR, LTV/CAC y Gross Margin.
- [x] 2.2 Implementar lógica visual para la alerta de NRR (rojo si < 100%).
- [x] 2.3 Crear componente `WatermarkedPdfButton` heredando la lógica de impresión pero inyectando el div de marca de agua confidencial en el DOM.

## 3. Integración Final

- [x] 3.1 Ensamblar la página `/dashboard/finance` consumiendo la API de finanzas.
- [x] 3.2 Verificar que el PDF exportado renderice el texto en diagonal "Confidencial - Exportado por..." solo en modo impresión.
