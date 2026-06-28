## Context
Definición de estrategia trimestral alineada a ingresos.

## Decisions
- Crearemos `backend/src/strategic/okr_simulator.py`.
- Lógica `simulate_arr(churn_rate, new_customers, cac)` que estime ingresos proyectados.
- Lógica `publish_okrs(okrs)` que guarde los OKRs y notifique por consola (simulando Slack).
- **Regla RN-E05-001 (Estructura de OKRs):** Cada objetivo requiere al menos un resultado clave cuantitativo.
