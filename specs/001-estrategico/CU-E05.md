# Especificación de Caso de Uso: CU-E05

## 1. Nombre de la Funcionalidad
**Definir Metas Estratégicas Trimestrales**

## 2. Objetivo
Proveer un entorno interactivo y colaborativo para que el el desarrollador evalúe resultados pasados, simule escenarios futuros y defina formalmente los Objetivos y Resultados Clave (OKRs) de SkyAnalytics para el próximo trimestre.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Dueño) / Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** Motor de Simulación Financiera/ML, Slack (para notificaciones automáticas de comunicación de OKRs).

## 4. Contexto del Problema
Para asegurar que los niveles tácticos y operativos remen en la misma dirección, las metas del Balanced Scorecard deben ajustarse cada trimestre. Fijar metas poco realistas desmotiva al equipo, mientras que metas laxas frenan el crecimiento. Se requiere un módulo de simulación y fijación de objetivos que encadene la estrategia hasta la operación.

## 5. Requisitos Funcionales
*   **RF-E05-001:** El sistema debe cargar los OKRs del trimestre anterior y mostrar su porcentaje final de cumplimiento.
*   **RF-E05-002:** El sistema debe incluir un motor de simulación ("What-if") que permita al Desarrollador (Dueño) proyectar escenarios de ARR basados en variaciones de tasa de churn, CAC y nuevos clientes mensuales.
*   **RF-E05-003:** El sistema debe permitir la creación de nuevos OKRs (Objetivo cualitativo + Key Results cuantitativos), asignando un líder o responsable táctico a cada uno.
*   **RF-E05-004:** El sistema debe notificar automáticamente vía Slack a los líderes de área una vez que los OKRs trimestrales son aprobados y publicados por el Desarrollador (Dueño).

## 6. Requisitos No Funcionales
*   **RNF-E05-001:** La herramienta de simulación de proyecciones financieras debe ser interactiva y responder a los cambios de parámetros de entrada (sliders) en menos de 500 milisegundos.
*   **RNF-E05-002:** Los registros de creación y modificación de OKRs deben persistirse con un rastro de auditoría inmutable (Event Sourcing o tablas Logsrales).

## 7. Reglas de Negocio
*   **RN-E05-001 (Estructura de OKRs):** Cada Objetivo Estratégico debe poseer como mínimo 1 y como máximo 5 Key Results cuantitativos medibles.
*   **RN-E05-002 (Cierre de Trimestre):** Una vez que un trimestre finaliza y sus metas son publicadas en estado "Cerrado", no pueden ser modificadas retroactivamente.

## 8. Entradas
*   Variables de Simulación (Sliders en UI):
    *   `estimated_new_customers` (Entero)
    *   `projected_churn_rate` (Float, ej. 0.02)
    *   `cac_budget` (Float)
*   Datos de Formulario OKR:
    *   `objective_title`, `key_results` (Array de objetos con meta numérica), `assignee_id`.

## 9. Salidas
*   **Payload JSON:** Confirmación de publicación de OKRs.
*   **Eventos:** Disparo de Webhook / API a Slack notificando los nuevos objetivos al canal general de la compañía.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Simulación y definición de metas realista
**Dado** que el Desarrollador (Dueño) está planificando el Q4
**Cuando** ajusta la tasa de churn esperada al 0.5% y simula el impacto en el ARR
**Entonces** el sistema proyecta que se alcanzará la meta anual de ingresos
**Y** el Desarrollador (Dueño) guarda el Key Result "Reducir churn al 0.5% en Q4" asignándolo al VP de Customer Success.

### Escenario 2: Notificación automática tras publicación
**Dado** que el borrador de los OKRs del próximo trimestre está completo
**Cuando** el Desarrollador (Dueño) hace clic en "Publicar y Oficializar Metas"
**Entonces** el sistema cambia el estado de los OKRs a "Activos"
**Y** envía un resumen automatizado al canal `#anuncios-globales` en Slack
**Y** actualiza los tableros de BSC (CU-E01) para apuntar a los nuevos objetivos.

## 11. Criterios de Aceptación
*   **CA-E05-001:** El módulo de simulación previene proyecciones matemáticas imposibles (ej. establecer un Churn Rate negativo).
*   **CA-E05-002:** Las metas cuantitativas ingresadas en este módulo se reflejan instantáneamente como las "metas" (líneas base) en los semáforos del CU-E01.

## 12. Restricciones
*   Solo los usuarios con rol de `Desarrollador (Dueño)` pueden hacer "Publish" final de los OKRs trimestrales.

## 13. Fuera de Alcance
*   Desglose detallado de las tareas diarias por desarrollador para alcanzar estos OKRs (La gestión a nivel ticket se hace en GitHub Issues, CU-O15).
