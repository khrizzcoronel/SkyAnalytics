# Especificación de Caso de Uso: CU-E06

## 1. Nombre de la Funcionalidad
**Analizar Retención de Talento y eNPS**

## 2. Objetivo
Evaluar y monitorear la salud de la cultura organizacional (Remote-First), la retención del talento clave, la satisfacción laboral (employee Net Promoter Score - eNPS) y la eficiencia general del proceso de onboarding técnico.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Dueño) / VP People
*   **Sistemas Externos / Actores Secundarios:** Herramientas de RRHH/Encuestas Internas (Typeform / Google Forms), GitHub/GitLab (métricas DORA de productividad).

## 4. Contexto del Problema
SkyAnalytics opera bajo una cultura 100% remota (Remote-First). La rotación de desarrolladores y SREs (fuga de cerebros) representa un riesgo masivo para la estabilidad del producto. El liderazgo necesita identificar proactivamente los signos de agotamiento (burnout) y medir cuán rápido los nuevos ingresos se vuelven productivos (Time-to-Productivity).

## 5. Requisitos Funcionales
*   **RF-E06-001:** El sistema debe importar y calcular el eNPS corporativo total y segmentado por equipo (Data, SRE, Frontend, ML, etc.) basado en las respuestas anonimizadas de las encuestas trimestrales.
*   **RF-E06-002:** El sistema debe identificar "equipos en zona de riesgo" (aquellos cuyo eNPS caiga por debajo de 10 o presenten renuncias recientes consecutivas).
*   **RF-E06-003:** El sistema debe calcular el "Time-to-Productivity", definido como la cantidad de días hábiles transcurridos desde el alta de un ingeniero en el IAM hasta su primer *Pull Request* fusionado a producción.
*   **RF-E06-004:** El sistema debe calcular y mostrar la tasa de retención de talento anual frente al benchmark objetivo ($>$ 90%).

## 6. Requisitos No Funcionales
*   **RNF-E06-001:** Anonimato absoluto. El sistema no debe exponer bajo ninguna circunstancia metadatos que permitan inferir la identidad de quien respondió una encuesta eNPS (Cumplimiento de Privacidad Interna).
*   **RNF-E06-002:** La sincronización de eventos de Pull Requests desde GitHub para el cálculo de productividad debe manejarse asíncronamente mediante Webhooks sin generar cuellos de botella en la base de datos transaccional.

## 7. Reglas de Negocio
*   **RN-E06-001 (Cálculo eNPS):** `% Promotores (calificación 9-10) - % Detractores (calificación 0-6)`. Meta: $> 40$ (excelencia).
*   **RN-E06-002 (Cálculo Time-to-Productivity):** El PR considerado debe tener aprobaciones formales (Reviews) y estar fusionado en la rama `main` o `master`. Meta: $<$ 5 días hábiles.

## 8. Entradas
*   Subida de respuestas de encuestas (CSV) o integración por API.
*   Filtros UI:
    *   `equipo_id` (UUID o 'All')
    *   `semestre_año` (String, ej. '2026-H1')

## 9. Salidas
*   **Payload JSON:**
    *   `{ enps_score, promoters_pct, passives_pct, detractors_pct, retention_rate_annual, avg_time_to_productivity_days }`
*   **UI:** Gráficos de tendencias, comparativas entre equipos y alertas de riesgo de fuga de talento.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Análisis de Onboarding ágil
**Dado** que el VP de People revisa las métricas de Aprendizaje y Crecimiento
**Cuando** evalúa la métrica de Time-to-Productivity del equipo de Frontend del último trimestre
**Entonces** el sistema consulta los webhooks almacenados de GitHub cruzados con las fechas de contratación
**Y** muestra que el promedio es de 3.5 días (cumpliendo la meta de $<$ 5 días).

### Escenario 2: Identificación de riesgo de Burnout
**Dado** que se cargaron los resultados de la encuesta eNPS del Q3
**Cuando** el Desarrollador (Dueño) ingresa al dashboard segmentado por equipos
**Entonces** el sistema marca el equipo de "Desarrollador (Tú)" en Rojo con un eNPS de 5
**Y** despliega una sugerencia visual recomendando "Iniciar entrevistas 1:1 de retención y revisión de guardias on-call".

## 11. Criterios de Aceptación
*   **CA-E06-001:** El cálculo de eNPS debe coincidir matemáticamente (a dos decimales) con la fórmula estándar de la industria.
*   **CA-E06-002:** Si un equipo tiene menos de 3 respuestas en una encuesta, la puntuación de eNPS de ese equipo específico se oculta (`N/A`) para evitar desanonimización de los empleados.

## 12. Restricciones
*   La plataforma no guarda nombres ni correos electrónicos en las tablas de `Fact_Satisfaccion_Interna`. Las llaves foráneas se asocian genéricamente por "Departamento".

## 13. Fuera de Alcance
*   Gestión y pago de nómina (Payroll) o contratación operativa (ATS). Esto es exclusivamente un módulo de *People Analytics*.
