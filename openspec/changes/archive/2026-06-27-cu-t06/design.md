## Context
Bloqueo de IPs y Alertas.

## Decisions
- Crearemos `frontend/app/api/v1/tactico/security/alert/route.ts`.
- **Regla RN-T06-001:** Si hay fallos masivos de login, es clasificado como Sev2 (Fuerza Bruta) y se bloquea la IP por 24h.
- Si hay crypto-minería o exfiltración masiva, es Sev1 y alerta vía SMS simulado a los SRE.
