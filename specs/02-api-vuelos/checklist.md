# Checklist de Validación: API de Vuelos

## CU-O02 — Consultar Datos de Vuelo vía API
- [ ] **CA-O02-001:** Las peticiones rechazadas por Rate Limit (429) no deben generar consumo de CPU en los servicios internos ni ser contabilizadas como "Errores 5xx" para el Error Budget del SRE.
- [ ] **CA-O02-002:** Un token revocado en el panel de control debe perder acceso de inmediato (TTL de propagación al Edge $\leq$ 5 segundos).
