# Especificación de Caso de Uso: CU-T09

## 1. Nombre de la Funcionalidad
**Ejecutar Pruebas de Carga y Chaos Engineering**

## 2. Objetivo
Garantizar la resiliencia del ecosistema SkyAnalytics mediante la simulación de picos de tráfico extremo (pruebas de carga) y la inyección intencional de fallos en infraestructura (Chaos Engineering), validando así las políticas de auto-escalado y el tiempo de recuperación (MTTR).

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** Dashboard Básico / Sentry k6 (Load Testing), Litmus Chaos (Chaos Engineering), Notificaciones de Slack (Validación de alarmas).

## 4. Contexto del Problema
SkyAnalytics promete alta disponibilidad a clientes de clase mundial. Esperar a que ocurra una falla real (ej. caída de zona de disponibilidad AWS, pico de usuarios durante Black Friday) para probar la arquitectura es inaceptable. Se deben ensayar los fallos controladamente (GameDays) para estar preparados.

## 5. Requisitos Funcionales
*   **RF-T09-001:** El sistema (vía CI/CD o runner dedicado) debe permitir la ejecución de scripts de prueba de carga con k6 simulando hasta 10,000 usuarios concurrentes reales (VUs) llamando a los endpoints de la API.
*   **RF-T09-002:** El sistema de Chaos Engineering debe permitir inyectar fallos de forma segura en entornos de *Staging*: matar pods aleatorios en PaaS/Serverless (Pod Delete), simular latencia de red, saturar memoria/CPU, y fallar la base de datos (DB Failover).
*   **RF-T09-003:** Durante cualquier prueba de Chaos, el sistema de alertas habitual (Sentry / Logs/Notificaciones de Slack) DEBE dispararse como si fuera un evento real.
*   **RF-T09-004:** El sistema debe registrar las métricas de degradación y el tiempo exacto que le tomó a la infraestructura auto-repararse (MTTR).

## 6. Requisitos No Funcionales
*   **RNF-T09-001 (Aislamiento de Explosión):** Las pruebas de Chaos Engineering deben restringirse estrictamente por namespaces (ej. `namespace=staging`) y tags, con mecanismos de aborto automático (Kill switch) si detectan fugas de latencia hacia el entorno de Producción.
*   **RNF-T09-002:** Las pruebas de carga deben ser distribuidas geográficamente, no originadas desde una sola IP o data center, para probar la eficacia de las CDNs globalmente.

## 7. Reglas de Negocio
*   **RN-T09-001 (Latencia Esperada bajo Carga):** Incluso bajo una carga simulada de 10,000 VUs concurrentes, los endpoints clave (ej. consulta de clima) deben mantener una latencia en el percentil 95 (p95) $\leq$ 500ms. Si supera este umbral, la prueba se considera fallida.
*   **RN-T09-002 (Criterio de Resiliencia PaaS):** Tras eliminar aleatoriamente el 30% de los pods operativos de un microservicio, el HPA (Horizontal Pod Autoscaler) debe reestablecer la capacidad total en menos de 3 minutos sin botar peticiones (ejecución exitosa de Graceful Shutdowns).

## 8. Entradas
*   Scripts JS de k6 (Comportamiento de los usuarios simulados, flujos, credenciales).
*   Manifiestos de Chaos (YAML defining The Chaos Experiment in Litmus).

## 9. Salidas
*   **Reportes de k6:** Resumen de throughput (req/s), errores HTTP (%), métricas p90, p95, p99.
*   **Reportes Chaos:** Resultado del experimento (Pass/Fail) y registro de métricas de resiliencia del cluster.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Validación exitosa del Auto-escalado
**Dado** que el entorno de Staging está estable
**Cuando** se ejecuta una prueba k6 inyectando 5,000 peticiones por segundo
**Entonces** el monitor de PaaS detecta el pico de CPU en los pods
**Y** el HPA incrementa dinámicamente el número de pods de 3 a 15
**Y** el reporte final muestra un 0% de respuestas `HTTP 503 Service Unavailable`.

### Escenario 2: Experimento de Chaos (Blackhole Network)
**Dado** que está planificado un GameDay de resiliencia
**Cuando** el SRE inyecta un experimento de partición de red aislando la conexión entre el API y la Base de Datos principal
**Entonces** el API debe realizar Failover al nodo secundario de lectura de la base de datos
**Y** las consultas de lectura deben continuar sin interrupción
**Y** Notificaciones de Slack debe notificar al equipo la pérdida de conexión del nodo maestro.

## 11. Criterios de Aceptación
*   **CA-T09-001:** El aborto de emergencia de una prueba (Kill Switch) cancela toda generación de tráfico y detiene los scripts de caos en menos de 5 segundos.
*   **CA-T09-002:** Las pruebas deben incluir llamadas autenticadas; no basta hacer pings a los endpoints públicos sin tokens.

## 12. Restricciones
*   Por políticas corporativas y contratos SLAs de Producción, los experimentos destructivos (Chaos) no se ejecutarán directamente en clústeres de Producción, sino en un entorno gemelo de Staging idéntico en infraestructura.

## 13. Fuera de Alcance
*   Pruebas manuales funcionales (QA UI Testing). k6 se centra puramente en protocolo HTTP/gRPC de backend y carga masiva.
