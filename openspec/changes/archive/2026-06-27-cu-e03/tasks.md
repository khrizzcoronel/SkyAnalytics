## 1. Backend API (Uptime)

- [x] 1.1 Extender `StrategicRepository` con el método `fetchSreTelemetry()` para simular/conectar la lectura de `vw_uptime_telemetry`.
- [x] 1.2 Implementar ruta API `/api/v1/estrategico/engineering/health` que calcule el remanente del Error Budget.
- [x] 1.3 Extender el Middleware para validar el acceso a la ruta `/dashboard/engineering`.

## 2. Frontend Componentes (SRE)

- [x] 2.1 Desarrollar el componente Gauge (Medidor) para el Error Budget utilizando CSS cónico o un SVG simple.
- [x] 2.2 Desarrollar la tabla de Desglose de Endpoints con condicionales de clase (`internal-infra`) para que ciertas columnas no se impriman.
- [x] 2.3 Implementar botón `PrintSlaReportButton` que reúna la funcionalidad de PDF e imprima el reporte filtrado.

## 3. Integración Final

- [x] 3.1 Ensamblar la página `/dashboard/engineering` con Polling cada 30 segundos (vía `useEffect` + `setInterval`).
- [x] 3.2 Validar visualmente el cambio de color rojo si la simulación de Uptime baja del 99.0%.
