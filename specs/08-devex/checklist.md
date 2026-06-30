# Checklist de Validación: Developer Experience

## CU-O16 — Validar Especificaciones OpenAPI en CI/CD
- [ ] **CA-O16-001:** Un desarrollador no puede hacer "bypass" o saltarse este check en las ramas protegidas de GitHub bajo ninguna circunstancia.

## CU-T07 — Mantener Developer Portal y SDKs
- [ ] **CA-T07-001:** Los SDKs generados automáticamente pasan suites de pruebas de compilación y empaquetado interno antes de ser liberados a los registros públicos.
- [ ] **CA-T07-002:** El enlace de cada endpoint en la documentación dirige exactamente a la especificación Swagger/OpenAPI incrustada sin errores 404.
