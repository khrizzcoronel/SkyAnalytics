# Checklist de Validación: Identidad y Acceso

## CU-O01 — Registrar Tenant y Autogenerar API Keys
- [ ] **CA-O01-001:** Un intento de recuperar una API Key existente debe resultar en la revocación de la antigua y la generación de una nueva, previa autenticación MFA.
- [ ] **CA-O01-002:** El enlace de verificación de correo pierde total validez luego de 24 horas, requiriendo que el usuario solicite uno nuevo.

## CU-O12 — Rotar Credenciales y Auditar Accesos IAM
- [ ] **CA-O12-001:** La rotación de credenciales no genera fallos de conexión a la base de datos (`Connection Refused` o `FATAL: password authentication failed`) reflejados en los logs de la aplicación durante la transición.
