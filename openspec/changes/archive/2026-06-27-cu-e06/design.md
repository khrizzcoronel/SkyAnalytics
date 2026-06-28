## Context
Prevenir fuga de talento midiendo cultura.

## Decisions
- Crearemos `backend/src/strategic/people_analytics.py`.
- Lógica `calculate_enps(responses)` (Promotores - Detractores).
- **Regla CA-E06-002:** Si un equipo tiene < 3 respuestas, ocultar resultado para evitar desanonimización (N/A).
- Mostrar sugerencias (ej. "Entrevistas 1:1") si el eNPS cae por debajo de 10.
