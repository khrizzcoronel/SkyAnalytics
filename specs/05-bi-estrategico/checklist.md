# Checklist de Validación: BI Estratégico

## CU-E01 — Consultar Tablero Balanced Scorecard (BSC)
- [ ] **CA-E01-001:** El dashboard renderiza correctamente los colores verde, amarillo y rojo basándose estrictamente en las reglas de negocio RN-E01-001 y RN-E01-002.
- [ ] **CA-E01-002:** Las pruebas de integración aseguran que un token sin el claim MFA o sin el rol correspondiente es rechazado por el API Gateway.
- [ ] **CA-E01-003:** La prueba de carga (k6) confirma que el endpoint del tablero responde en $\leq$ 2 segundos (p95) bajo carga concurrente esperada.
- [ ] **CA-E01-004:** El gráfico de drill-down muestra al menos 12 puntos de datos continuos si existe historial, o llena con ceros (0) los meses sin datos.

## CU-E02 — Analizar ARR y Rentabilidad
- [ ] **CA-E02-001:** Las fórmulas de ARR, NRR y LTV coinciden exactamente con los modelos estandarizados en `dbt` y verificados por las suites de Validaciones nativas (Pydantic/Zod).
- [ ] **CA-E02-002:** Un usuario con rol `Desarrollador (Tú)` intentando acceder a la rentabilidad global recibe un HTTP `403`.
- [ ] **CA-E02-003:** El PDF exportado no puede ser editado sin romper la firma digital del documento.

## CU-E03 — Evaluar Uptime Global y Cumplimiento SLA
- [ ] **CA-E03-001:** Las métricas mostradas en la UI coinciden exactamente con los registros crudos de PromQL ejecutados directamente contra el cluster.
- [ ] **CA-E03-002:** El reporte PDF generado para los clientes no expone IPs internas, nombres de nodos PaaS ni información sensible de infraestructura, solo SLAs y porcentajes.
- [ ] **CA-E03-003:** Cuando una región supera el 1% de errores 5xx, el dashboard muestra una recomendación explícita de failover activo-activo y resalta la región degradada.

## CU-E04 — Revisar Cumplimiento Normativo (Compliance)
- [ ] **CA-E04-001:** El cálculo del score de cumplimiento es exacto (Controles Pasados / Controles Totales * 100).
- [ ] **CA-E04-002:** Un Desarrollador (Tú) con permisos de "Solo Lectura" puede generar reportes y descargar evidencias, pero no puede marcar un control manual como "Completado". Solo el Desarrollador (Tú) o el VP pueden aprobar controles manuales.
- [ ] **CA-E04-003:** Las evidencias PDF y logs de auditoría se almacenan en S3 con Object Lock activo (modo Governance o Compliance), garantizando inmutabilidad durante el período de retención exigido.
- [ ] **CA-E04-004:** Cada reporte de compliance exportado en PDF incluye una firma digital (SHA-256 + certificado) verificable sin conexión.

## CU-E06 — Analizar Retención de Talento y eNPS
- [ ] **CA-E06-001:** El cálculo de eNPS debe coincidir matemáticamente (a dos decimales) con la fórmula estándar de la industria.
- [ ] **CA-E06-002:** Si un equipo tiene menos de 3 respuestas en una encuesta, la puntuación de eNPS de ese equipo específico se oculta (`N/A`) para evitar desanonimización de los empleados.
- [ ] **CA-E06-003:** El sistema nunca almacena nombre, correo, identificador de empleado ni cualquier otro dato directamente identificable junto a la respuesta de eNPS; solo se conserva el departamento y la timestamp.
- [ ] **CA-E06-004:** Las respuestas abiertas de texto libre son opcionales y, si se almacenan, se someten a detección automática de PII antes de persistirse.

## CU-O06 — Refrescar Dashboards BI
- [ ] **CA-O06-001:** El refresco ocurre sin bloqueos (Locks) que interrumpan consultas de lectura concurrentes por parte de usuarios finales (`CONCURRENTLY`).
