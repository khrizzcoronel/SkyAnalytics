## Why
Es necesario automatizar la detección y contención de amenazas de seguridad como los ataques de fuerza bruta, para garantizar que la plataforma cumpla con SOC 2 y no dependa de intervención humana inmediata.

## What Changes
- `frontend/app/api/v1/tactico/security/alert/route.ts`: Endpoint simulando las reglas del WAF y el Hub de Seguridad.

## Capabilities
- `security-alerter`: Auto-remediación, clasificación (Sev1, Sev2, Sev3) y escalamiento a Slack.
