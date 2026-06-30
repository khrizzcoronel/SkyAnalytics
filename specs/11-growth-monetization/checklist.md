# Checklist de Validación: Growth y Monetización

## CU-T01 — Gestionar Campañas de Growth Hacking
- [ ] **CA-T01-001:** Un registro masivo de 500 leads simultáneos no degrada el rendimiento de la API principal, encolando correctamente las peticiones a HubSpot.
- [ ] **CA-T01-002:** Si la API de HubSpot cae, el sistema debe reintentar el envío del evento de conversión (Retry pattern con Exponential Backoff).

## CU-T02 — Configurar y Publicar API en RapidAPI
- [ ] **CA-T02-001:** El linter Spectral del CI/CD debe fallar si la especificación OpenAPI contiene parámetros incompatibles con el importador de RapidAPI.
- [ ] **CA-T02-002:** El rate limiting implementado localmente debe concordar con el rate limiting del plan configurado en RapidAPI para prevenir facturación excesiva o fugas de cómputo.

## CU-T03 — Gestionar Infraestructura con Terraform (IaC)
- [ ] **CA-T03-001:** Es imposible aplicar cambios en producción sin que queden registrados en el historial de commits de Git.
- [ ] **CA-T03-002:** Si el pipeline de Terraform falla a la mitad de un apply, el mecanismo de lock en DynamoDB previene ejecuciones simultáneas corruptas.

## CU-T10 — Validar Estrategia de Pricing
- [ ] **CA-T10-001:** El script del experimento (A/B testing snippet) carga en un tiempo imperceptible (menor a 50ms) en la capa Edge.
- [ ] **CA-T10-002:** Toda suscripción generada bajo un entorno de prueba en Stripe durante el diseño del A/B test debe utilizar APIs de Stripe Sandbox y nunca tarjetas reales.
