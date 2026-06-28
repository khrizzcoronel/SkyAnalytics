## Context

El proyecto SkyAnalytics requiere monitorear métricas clave de salud financiera como el Gross Margin, ARR y NRR. Los datos para este cálculo provienen fundamentalmente del motor columnar analítico (MonetDB), que ya se alimenta asíncronamente desde orígenes externos como Stripe (Ingresos) y AWS (Costo Cloud).

## Goals / Non-Goals

**Goals:**
- Mostrar un panel financiero con ARR, LTV/CAC, Gross Margin y NRR consolidado.
- Reutilizar el componente existente de exportación a PDF (`PrintToPdfButton`) pero integrando una firma visual de seguridad (Marca de agua).
- Mantener los tiempos de respuesta del dashboard menores a 3 segundos.

**Non-Goals:**
- Procesamiento transaccional de reembolsos, cobros o ajustes a clientes en Stripe. Todo es "Read Only" desde la perspectiva de la API.
- Generar PDFs desde el backend de Node.js.

## Decisions

- **Cálculo de Métricas Delegado:** Los cálculos complejos como NRR y Gross Margin no se harán en el Backend de Next.js, sino que se extraerán de vistas pre-calculadas en MonetDB (Ej: `vw_financial_metrics`) actualizadas por el ETL.
  - *Rationale:* Mantiene la API limpia, cumple con el SLA de 3s (O(1) lectura), y respeta la arquitectura donde Python/dbt en el Módulo Operativo hace el trabajo pesado.
- **Marca de Agua CSS:** La marca de agua para trazabilidad de la exportación será un div posicionado de forma absoluta (`position: absolute`) en CSS, visible únicamente al usar `@media print`. Contendrá el email/rol decodificado del JWT en la interfaz del cliente.
  - *Rationale:* Evita la complejidad de generar PDFs binarios.

## Risks / Trade-offs

- **Trade-off de Frescura:** Existe un *lag* de hasta 24 horas (debido a la ejecución nocturna del ETL).
  - *Mitigación:* Informar visualmente al usuario en el frontend la fecha de última actualización de los datos (`Last Updated: Yesterday`).
