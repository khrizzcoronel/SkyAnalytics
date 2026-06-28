## Context
Simulador de Chaos Engineering.

## Decisions
- Crearemos `frontend/app/api/v1/tactico/chaos/experiment/route.ts`.
- **Regla RN-T09-001:** Validar latencia bajo caos. Si latencia p95 > 500ms, el experimento falla.
- **Regla RNF-T09-001:** Abortar (kill switch) si se ejecuta en namespace distinto a staging.
