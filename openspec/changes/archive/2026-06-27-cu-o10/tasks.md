## 1. Módulo CI/CD

## 1. Módulo CI/CD

- [x] 1.1 Crear carpeta `backend/src/cicd/`.
- [x] 1.2 Implementar `error_budget_gate.py` con una función `check_deployment_allowed(budget_consumed, pr_label)`.
- [x] 1.3 Implementar lógica: Si `budget_consumed > 80` y `pr_label` no es `hotfix` ni `reliability`, bloquear (lanzar excepcion o retornar False).
- [x] 1.4 Simular un Feature bloqueado y un Hotfix permitido.
