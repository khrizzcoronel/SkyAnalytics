# Especificación de Caso de Uso: CU-E01

## 1. Nombre de la Funcionalidad
**Consultar Tablero Balanced Scorecard (BSC)**

## 2. Objetivo
Proveer a la alta dirección (Desarrollador (Dueño)) una vista integral y en tiempo real del estado de salud de la empresa a través del monitoreo de KPIs estratégicos, contrastando los valores actuales frente a las metas establecidas mediante indicadores visuales (semáforos) y análisis histórico.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Dueño)
*   **Sistemas Externos / Actores Secundarios:** Sistema de Identidad (Autenticación MFA / SSO), Data Warehouse (PocketBase (Operativa) y MonetDB (Analítica)).

## 4. Contexto del Problema
Para tomar decisiones estratégicas basadas en datos (Data-Driven), el Desarrollador (Dueño) necesita una visión unificada de los 4 pilares del Balanced Scorecard (Finanzas, Cliente, Procesos Internos, Aprendizaje y Crecimiento). Actualmente, esta información se encuentra dispersa. Se requiere un dashboard gerencial consolidado de alto rendimiento que cargue rápidamente información de múltiples tablas de hechos.

## 5. Requisitos Funcionales
*   **RF-E01-001:** El sistema debe autenticar al usuario soportando dos métodos: inicio de sesión social (OAuth, ej. Google) o Usuario/Contraseña con Autenticación de Múltiples Factores (MFA). Los usuarios solo pueden ser creados por un `SUPER_ADMIN`.
*   **RF-E01-002:** El sistema debe cargar los indicadores clave (KPIs) desde la vista analítica `vw_bsc_monthly` de MonetDB, la cual consolida métricas del negocio aeronáutico (ej. tasa de cancelaciones, promedio de retrasos de salida y total de vuelos) junto a las métricas financieras básicas del SaaS (ARR y NRR, simuladas).
*   **RF-E01-003:** El sistema debe renderizar un indicador visual tipo semáforo (Verde, Amarillo, Rojo) para cada KPI comparando el valor actual con la meta del trimestre.
*   **RF-E01-004:** El sistema debe permitir realizar *drill-down* al hacer clic en un KPI para visualizar un gráfico de líneas con la evolución histórica de los últimos 12 meses.
*   **RF-E01-005:** El sistema debe permitir la exportación de los datos a PDF delegando esta acción a la función de impresión nativa del navegador (`window.print()`), utilizando estilos CSS específicos (`@media print`) para optimizar la vista impresa.

## 6. Requisitos No Funcionales
*   **RNF-E01-001:** El tiempo de carga inicial del dashboard no debe superar los 2 segundos en el percentil 95 (Latencia, de acuerdo con la Constitución).
*   **RNF-E01-002:** Las comunicaciones entre el Dashboard (Frontend) y las APIs (Backend) deben estar obligatoriamente cifradas bajo TLS 1.3.
*   **RNF-E01-003:** La frescura de los datos mostrados en el dashboard debe ser igual o inferior a 5 minutos, respetando la restricción de arquitectura general.
*   **RNF-E01-004:** El dashboard debe ser *Responsive* y accesible desde dispositivos móviles (Tabletas y Smartphones gerenciales).

## 7. Reglas de Negocio
*   **RN-E01-001 (Lógica de Semáforo Financiero y Cliente):** 
    *   **Verde:** Valor actual $\geq$ 100% de la meta.
    *   **Amarillo:** Valor actual entre 80% y 99.9% de la meta.
    *   **Rojo:** Valor actual $<$ 80% de la meta.
*   **RN-E01-002 (Lógica de Semáforo Procesos - Uptime/Errores):** 
    *   **Verde:** Uptime $\geq$ 99.0% (Best Effort).
    *   **Amarillo:** Uptime entre 95.0% y 98.9%.
    *   **Rojo:** Uptime $<$ 95.0%.
*   **RN-E01-003 (Privilegios):** Exclusivamente los roles `SUPER_ADMIN` o `C_LEVEL_EXEC` tienen permiso para visualizar este dashboard. Cualquier otra solicitud debe ser denegada con un código `403 Forbidden`.

## 8. Entradas
*   **Credenciales de Sesión:** Token JWT válido con Claims de MFA verificado (`amr: ["mfa"]`).
*   **Filtros de Búsqueda (Opcionales en Drill-down):**
    *   `startDate` (ISO 8601, por defecto: inicio del mes hace exactamente un año - LTM)
    *   `endDate` (ISO 8601, por defecto: día de hoy)
    *   `kpi_id` (String UUID)

## 9. Salidas
*   **Payload JSON (GraphQL / REST):**
    *   Lista de objetos KPI: `{ kpi_id, nombre, valor_actual, valor_meta, porcentaje_cumplimiento, estado_semaforo, tendencia }`
    *   Serie temporal (en caso de drill-down): `[ { fecha, valor } ]`
*   **UI:** Interfaz gráfica renderizada en React/Next.js con widgets de KPIs y gráficos de serie temporal.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Visualización exitosa del Tablero BSC (Happy Path)
**Dado** que el Desarrollador (Dueño) ha iniciado sesión con MFA exitosamente y tiene el rol `C_LEVEL_EXEC`
**Cuando** navega a la ruta `/dashboard/bsc`
**Entonces** el sistema consulta los KPIs de PocketBase (Operativa) y MonetDB (Analítica) a través de la API
**Y** renderiza los 4 pilares estratégicos con sus respectivos semáforos en menos de 2 segundos.

### Escenario 2: Intento de acceso sin permisos suficientes
**Dado** que un usuario con el rol `OPERATOR` ha iniciado sesión
**Cuando** intenta forzar el acceso a la ruta o API `/dashboard/bsc`
**Entonces** el sistema debe denegar el acceso
**Y** retornar un mensaje HTTP `403 Forbidden` informando la carencia de privilegios.
**Y** debe generar un log de auditoría de seguridad (Security Alert).

### Escenario 3: Interacción de Drill-down histórico
**Dado** que el Desarrollador (Dueño) está visualizando el Tablero BSC
**Cuando** hace clic en el KPI "ARR (Ingreso Recurrente)"
**Entonces** el sistema solicita la serie temporal de los últimos 12 meses
**Y** despliega un gráfico de líneas sobreponiendo el rendimiento histórico mes a mes.

## 11. Criterios de Aceptación
*   **CA-E01-001:** El dashboard renderiza correctamente los colores verde, amarillo y rojo basándose estrictamente en las reglas de negocio RN-E01-001 y RN-E01-002.
*   **CA-E01-002:** Las pruebas de integración aseguran que un token sin el claim MFA o sin el rol correspondiente es rechazado por el API Gateway.
*   **CA-E01-003:** La prueba de carga (k6) confirma que el endpoint del tablero responde en $\leq$ 2 segundos (p95) bajo carga concurrente esperada.
*   **CA-E01-004:** El gráfico de drill-down muestra al menos 12 puntos de datos continuos si existe historial, o llena con ceros (0) los meses sin datos.

## 12. Restricciones
*   El cálculo pesado de los KPIs no debe hacerse en tiempo de solicitud (on-the-fly) sobre la base transaccional (PostgreSQL); debe consumirse obligatoriamente del Data Warehouse columnar (PocketBase (Operativa) y MonetDB (Analítica)) previamente calculado por el pipeline ETL.
*   La UI no debe almacenar temporalmente (cachear en navegador local) información financiera sin encriptar.

## 13. Fuera de Alcance
*   Modificación de metas estratégicas desde esta misma pantalla (Esto corresponde al CU-E05: Definir Metas Estratégicas Trimestrales).
*   Alertas en tiempo real por push o email (Se manejan en casos de uso tácticos/operativos mediante Notificaciones de Slack o notificaciones asíncronas).
