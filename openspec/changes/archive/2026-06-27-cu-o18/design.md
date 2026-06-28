## Context
Evitar fuga de datos y exploits conocidos.

## Decisions
- Crearemos `backend/src/security/security_scanner.py`.
- **Regla RN-O18-002:** Escanear archivos en busca de palabras clave como `password=`, `api_key=`, `secret=` (Simulando GitGuardian).
- Simular escaneo de `requirements.txt` (SCA) y fallar si existe `requests==2.10.0` (CVE crítico).
