## Why
DevSecOps requiere validación continua. Necesitamos escanear secretos filtrados (Hardcoded Passwords) y dependencias vulnerables en el CI/CD antes de fusionar cualquier código.

## What Changes
- `security_scanner.py`: Script que simula escáner de secretos y Software Composition Analysis (SCA/Snyk).

## Capabilities
- `sast-dast-pipeline`: Validaciones estáticas y de dependencias para bloquear commits con contraseñas o CVEs.
