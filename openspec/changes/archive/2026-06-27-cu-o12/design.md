## Context
Tenemos que garantizar que las contraseñas se renuevan y los accesos excesivos se revocan.

## Decisions
- Crearemos `backend/src/security/secret_rotator.py` y `backend/src/security/iam_auditor.py`.
- Se simulará la conexión a un gestor de secretos y la rotación dinámica.
- La auditoría simulará leer de CloudTrail y revocar automáticamente si `last_used_days > 90`.
