# Checklist de Validación: Resilience Testing

## CU-T09 — Ejecutar Pruebas de Carga y Chaos Engineering
- [ ] **CA-T09-001:** El aborto de emergencia de una prueba (Kill Switch) cancela toda generación de tráfico y detiene los scripts de caos en menos de 5 segundos.
- [ ] **CA-T09-002:** Las pruebas deben incluir llamadas autenticadas; no basta hacer pings a los endpoints públicos sin tokens.
