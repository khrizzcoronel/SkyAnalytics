## Context

La alta dirección requiere un tablero de control (Balanced Scorecard - BSC) para visualizar en tiempo real el cumplimiento de los cuatro pilares estratégicos (Finanzas, Cliente, Procesos Internos, Aprendizaje). La información histórica (hechos) reside en MonetDB y las metas trimestrales se gestionan en PocketBase. El entorno de despliegue principal es un entorno Serverless (Vercel), lo cual impone límites estrictos de latencia (SLA < 3s) y manejo del estado.

## Goals / Non-Goals

**Goals:**
- Consolidar la visualización de los 4 pilares en un único dashboard.
- Proveer semaforización (Verde, Amarillo, Rojo) evaluada dinámicamente según reglas de negocio predefinidas.
- Permitir un análisis tipo *drill-down* histórico (tendencia LTM - últimos 12 meses) para cada indicador.
- Permitir la exportación del estado actual a PDF de manera eficiente.

**Non-Goals:**
- Proveer una interfaz para definir o modificar las metas estratégicas trimestrales desde esta misma pantalla (cubierto en CU-E05).
- Generar o enviar alertas push en tiempo real ante desviaciones (cubierto por notificaciones tácticas en Slack).

## Decisions

- **Patrón Backend-For-Frontend (BFF):** El cruce de datos entre el valor histórico (MonetDB) y la meta actual (PocketBase) se realizará *on-the-fly* en memoria dentro de una función *Serverless* de Next.js (`/api/v1/estrategico/bsc/summary`), en lugar de intentar migraciones ETL cruzadas o federaciones de bases de datos costosas.
  - *Rationale:* Mantiene la complejidad técnica baja para el *Solo-Dev* y minimiza los tiempos de arranque (Cold Starts) compartiendo un único pipeline API.
- **Client-Side PDF Export (`window.print`):** En lugar de generar binarios PDF en el backend con Node.js (lo cual consume muchísima RAM en Vercel), la exportación delegará la carga al motor del navegador del usuario utilizando media queries de CSS (`@media print`).
  - *Rationale:* Transfiere el costo computacional al cliente, asegurando respuesta instantánea y ahorrando costos operativos.
- **Autenticación en Middleware:** Todas las rutas del tablero BSC están resguardadas por el *Next.js Middleware*, validando el token JWT, requerimiento de MFA y garantizando los roles `SUPER_ADMIN` o `C_LEVEL_EXEC`.

## Risks / Trade-offs

- **Riesgo (Timeouts Serverless):** Las consultas complejas analíticas podrían exceder el timeout de la cuenta gratuita de Vercel si MonetDB debe despertarse desde un estado suspendido.
  - *Mitigación:* Forzar que la instancia VPS de MonetDB permanezca *Always-On* (24/7), eliminando el *Cold Start* a nivel de base de datos y garantizando latencia p95 <= 2s.
- **Riesgo (Seguridad de Tránsito):** Las consultas hacia la VPS pública exponen datos financieros en bruto.
  - *Mitigación:* Se obligará a conectar Next.js con MonetDB exclusivamente bajo el parámetro `sslmode=require` (TLS 1.3).
