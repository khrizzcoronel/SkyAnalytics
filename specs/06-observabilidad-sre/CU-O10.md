# Especificación de Caso de Uso: CU-O10

## 1. Nombre de la Funcionalidad
**Revisar Error Budget y Congelar Deploys**

## 2. Objetivo
Garantizar la estabilidad sistémica implementando políticas estrictas de control de calidad, deteniendo inmediatamente la introducción de nuevo código o features (congelamiento de despliegues) cuando el nivel de errores supera el margen permitido por el Service Level Agreement (SLA).

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Sistema de CI-CD
*   **Sistemas Externos / Actores Secundarios:** Grafana LGTM stack (Observabilidad), GitHub Actions.

## 4. Contexto del Problema
SkyAnalytics ofrece SLAs del 99.0% (Best Effort), lo que otorga un Error Budget mensual total de 432 minutos de caída permitida. Si durante un mes los incidentes ya consumieron el 80% (~345.6 minutos), el sistema debe congelar los despliegues de nuevas funcionalidades para evitar violar el contrato legal. Subir "nuevas funcionalidades" en ese momento es un riesgo enorme. El equipo debe priorizar arreglar problemas de confiabilidad (estabilización) antes de añadir innovación.

## 5. Requisitos Funcionales
*   **RF-O10-001:** Grafana LGTM stack debe calcular continuamente el "Presupuesto de Errores Consumido" basado en la ventana rotatoria de los últimos 30 días.
*   **RF-O10-002:** El sistema debe integrar la alerta de "Error Budget Agotado" con el sistema de CI/CD (GitHub Actions).
*   **RF-O10-003:** Cuando se activa el estado de alerta crítica (>80% consumido), el sistema (CI/CD) debe desactivar o bloquear la ejecución exitosa de cualquier pipeline hacia Producción que no esté marcado con la etiqueta `Hotfix` o `Reliability`.
*   **RF-O10-004:** El sistema debe restaurar automáticamente el pipeline y permitir los despliegues de *features* una vez que la ventana de 30 días avanza y el Error Budget disponible regresa a niveles seguros (ej. < 50% consumido).

## 6. Requisitos No Funcionales
*   **RNF-O10-001:** La comprobación del estado del Error Budget por parte de GitHub Actions debe resolverse en tiempo constante y sin introducir dependencias débiles que ralenticen los PRs de infraestructura crítica.

## 7. Reglas de Negocio
*   **RN-O10-001 (Regla de Congelamiento - Feature Freeze):** Al consumirse el 80% del Error Budget mensual (~345.6 minutos de caída detectada para SLA 99.0%), se bloquean TODOS los *Merge* de nuevas características a la rama principal.
*   **RN-O10-002 (Excepciones de Freeze):** Las correcciones inmediatas a incidentes de producción (Hotfixes) y las tareas exclusivas de resiliencia (ej. refactor de queries pesadas, aumento de memoria) están exentas del congelamiento, previa aprobación de dos roles SRE (Doble validación).

## 8. Entradas
*   Estado del SLO desde Grafana LGTM stack/Grafana API.
*   Etiquetas en el Pull Request de GitHub (`feature`, `bugfix`, `hotfix`).

## 9. Salidas
*   **Acción:** Aprobación (Status Checks en Verde) o Bloqueo (Cruz Roja) del Pull Request en la interfaz de código.
*   **Notificación:** Broadcast a toda el área de Ingeniería anunciando el estado de "Feature Freeze".

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Despliegue bloqueado por agotamiento de Budget
**Dado** que la semana pasada hubo un incidente grave que consumió el 85% del Error Budget del mes
**Cuando** un desarrollador intenta fusionar (Merge) un Pull Request etiquetado como `feature/nuevo-dashboard`
**Entonces** el pipeline de GitHub consulta el API de SLOs
**Y** rechaza la compilación con un error: "Despliegue bloqueado. Error Budget > 80%. Solo se permiten Hotfixes."
**Y** el desarrollador no puede enviar su código a Producción.

### Escenario 2: Aprobación de emergencia (Hotfix) bajo Freeze
**Dado** que la plataforma está en estado "Feature Freeze" (Budget al 90%)
**Cuando** un SRE sube un Pull Request etiquetado como `hotfix/fuga-memoria-redis`
**Y** otro SRE aprueba el código (Review)
**Entonces** el pipeline detecta la excepción autorizada
**Y** permite que los cambios de estabilización lleguen a Producción.

## 11. Criterios de Aceptación
*   **CA-O10-001:** Los despliegues hacia entornos no productivos (Desarrollo, Staging) nunca son bloqueados por las restricciones del Error Budget. Solo el pase a Producción está penalizado.

## 12. Restricciones
*   Nadie, incluyendo el Desarrollador (Tú), puede evadir sistémicamente un "Feature Freeze" forzando un despliegue normal de funcionalidades si el sistema no lo marca como Hotfix rastreable.

## 13. Fuera de Alcance
*   Devolución automática de cobros a los clientes en caso de violar el 100% del SLA (El billing se gestiona en Stripe, no en el CI/CD).
