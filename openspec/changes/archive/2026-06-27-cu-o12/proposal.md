## Why
La rotación manual de secretos (contraseñas de BD, tokens) y la auditoría de permisos IAM a menudo se olvidan, lo cual es un riesgo crítico de seguridad y viola SOC 2. Se debe automatizar.

## What Changes
- `secret_rotator.py`: Script que simula la rotación de un secreto expirado (TTL).
- `iam_auditor.py`: Script que busca permisos huérfanos sin uso en >90 días.

## Capabilities
- `iam-auditor`: Reglas para revocar permisos no utilizados (Principio de Menor Privilegio).
