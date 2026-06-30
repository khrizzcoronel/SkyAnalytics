## 1. Importador Incremental de Vuelos

- [x] 1.1 Crear `backend/import/import_flights.py`.
- [x] 1.2 Implementar lectura por chunks de 100k filas desde CSV.
- [x] 1.3 Implementar checkpoint JSON con reanudación.
- [x] 1.4 Generar IDs deterministas `fl<13digitos>`.
- [x] 1.5 Crear `backend/import/Dockerfile` para contenedor one-shot.
- [ ] 1.6 Completar spec `CU-O22.md` con secciones 8-13.
- [ ] 1.7 Añadir tests pytest de resumabilidad e idempotencia.
- [ ] 1.8 Documentar comando `docker-compose run --rm importer` en README.
