## 1. ETL PocketBase → MonetDB Star Schema

- [x] 1.1 Crear script `backend/src/etl/etl_flights_to_monetdb.py`.
- [x] 1.2 Implementar lectura incremental desde `flights_raw` con watermark `MAX(pb_created)`.
- [x] 1.3 Crear tablas de dimensiones y hechos en MonetDB.
- [x] 1.4 Generar vistas `vw_bsc_monthly` y `vw_delay_analysis`.
- [ ] 1.5 Completar spec `CU-O21.md` con secciones 8-13 (RN, Entradas, Salidas, CA, Restricciones, Fuera de Alcance).
- [ ] 1.6 Añadir tests pytest de idempotencia y carga de quarantine.
- [ ] 1.7 Configurar GitHub Actions cron `etl-flights.yml` a las 03:00 UTC.
