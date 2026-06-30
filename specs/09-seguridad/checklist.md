# Checklist de Validación: Seguridad

## CU-O18 — Ejecutar Pipeline de Seguridad SAST/DAST en CI/CD
- [ ] **CA-O18-001:** Las pruebas DAST en el entorno de Staging deben usar credenciales de prueba; no pueden bajo ningún motivo ejecutar ataques de alteración destructiva (Write/Delete) contra bases de datos que no estén diseñadas para restablecerse automáticamente.

## CU-T06 — Configurar Alertas de Seguridad
- [ ] **CA-T06-001:** Las reglas de alerta deben estar versionadas en Git; un cambio directo en la consola de AWS es detectado como 'Drift' y revertido en la siguiente sincronización.
- [ ] **CA-T06-002:** El bloqueo automático (WAF) debe ejecutarse exitosamente en menos de 10 segundos tras superar el umbral.
