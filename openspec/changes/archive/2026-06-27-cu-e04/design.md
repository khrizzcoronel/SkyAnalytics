## Context
Validar el estado de SOC2 y GDPR.

## Decisions
- Crearemos `backend/src/strategic/compliance_dashboard.py`.
- **Regla RN-E04-001 (GDPR Data Residency):** Datos en regiones distintas a `eu-central-1` generan un fallo crítico.
- **Regla RN-E04-002 (Cifrado Mandatorio):** Recursos no cifrados fallan el control de Seguridad.
