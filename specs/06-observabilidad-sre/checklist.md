# Checklist de Validación: Observabilidad y SRE

## CU-O07 — Monitorear Telemetría de Contenedores
- [ ] **CA-O07-001:** Toda aplicación en el cluster que no exponga un endpoint de métricas estándar hace fallar los pipelines de despliegue de CI/CD.

## CU-O09 — Ejecutar Backup y Prueba de Restauración
- [ ] **CA-O09-001:** La prueba de restauración automática jamás interrumpe, bloquea ni consume rendimiento (I/O) de la base de datos en producción.

## CU-O10 — Revisar Error Budget y Congelar Deploys
- [ ] **CA-O10-001:** Los despliegues hacia entornos no productivos (Desarrollo, Staging) nunca son bloqueados por las restricciones del Error Budget. Solo el pase a Producción está penalizado.

## CU-O11 — Publicar Changelog Semanal en Developer Portal
- [ ] **CA-O11-001:** El Changelog generado siempre incluye hipervínculos directos a los PRs originales en GitHub para proveer mayor contexto técnico.

## CU-O13 — Realizar Post-Mortem de Incidente
- [ ] **CA-O13-001:** Los Action Items generados a raíz del Post-Mortem deben heredar automáticamente un nivel de prioridad P1 (Bloqueador) y entrar al inicio del backlog del siguiente sprint (CU-O15).
