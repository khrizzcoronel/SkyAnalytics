# Especificación de Caso de Uso: CU-O16

## 1. Nombre de la Funcionalidad
**Validar Especificaciones OpenAPI en CI/CD**

## 2. Objetivo
Garantizar que todo cambio realizado a los contratos de la API (archivos OpenAPI/Swagger) cumpla con los estándares de estilo corporativos, sea retrocompatible, y no introduzca "breaking changes" que afecten a los clientes B2B.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador Backend / Sistema CI/CD
*   **Sistemas Externos / Actores Secundarios:** Spectral (Linter), GitHub Actions, Gateway simplificado (API Gateway).

## 4. Contexto del Problema
SkyAnalytics sigue una filosofía "API-First". Si un desarrollador cambia el tipo de dato de una respuesta de `integer` a `string` sin avisar, o elimina un campo, las aplicaciones de las aerolíneas que consumen la API se romperán (Outage). Es mandatorio validar estructuralmente el contrato antes de que ese código llegue a producción.

## 5. Requisitos Funcionales
*   **RF-O16-001:** El pipeline de CI/CD debe activarse automáticamente ante cualquier cambio en archivos `.yaml` o `.json` dentro del directorio de especificaciones de API.
*   **RF-O16-002:** El sistema debe ejecutar el Linter `Spectral` aplicando las reglas de estilo (Style Guide) definidas por el Desarrollador (Tú) (ej. nombres de campos en `snake_case`, descripciones obligatorias).
*   **RF-O16-003:** El sistema debe ejecutar una herramienta de validación de retrocompatibilidad (ej. `openapi-diff`) comparando la rama actual contra la rama `main`.
*   **RF-O16-004:** Si se detecta un *Breaking Change* (ej. eliminación de un endpoint o campo), el pipeline debe fallar y bloquear el Pull Request.

## 6. Requisitos No Funcionales
*   **RNF-O16-001:** La validación estática completa del contrato debe ejecutarse en menos de 10 segundos durante la fase inicial del pipeline de integración continua.

## 7. Reglas de Negocio
*   **RN-O16-001 (Política de Breaking Changes):** Los breaking changes están prohibidos en versiones de API activas (v1). Cualquier cambio que rompa la compatibilidad debe forzosamente empaquetarse bajo un nuevo prefijo de versión en la URI (ej. `/v2/`).
*   **RN-O16-002 (Documentación Mandatoria):** Todo endpoint nuevo declarado en la especificación debe incluir campos obligatorios: `summary`, `description`, y al menos un ejemplo de respuesta HTTP 200 y HTTP 400.

## 8. Entradas
*   Archivos `openapi.yaml` (Contrato API modificado).

## 9. Salidas
*   **Log de CI/CD:** Reporte de Spectral (Errores de estilo).
*   **Log de Diff:** Listado de cambios compatibles o incompatibles (`openapi-diff`).
*   **Estado:** Éxito o Falla del Check en GitHub.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Bloqueo de un Breaking Change
**Dado** que un desarrollador elimina la propiedad `delay_minutes` del esquema de respuesta de Vuelos para reemplazarla por una estructura anidada
**Cuando** crea el Pull Request
**Entonces** la herramienta `openapi-diff` compara la especificación propuesta contra la que está en Producción
**Y** detecta una ruptura de compatibilidad (eliminación de campo requerido)
**Y** el pipeline falla con el mensaje: "Breaking Change detectado. Por favor versión su API a v2."
**Y** bloquea el Merge automático.

### Escenario 2: Validación de estilo (Linter)
**Dado** que un desarrollador añade un nuevo endpoint usando CamelCase (`flightDetails`)
**Cuando** se ejecuta el Linter Spectral
**Entonces** el Linter detecta la violación a la regla de estilo `RN-O16-002` (requiere `snake_case`)
**Y** el pipeline falla solicitando al desarrollador que renicknamee el endpoint a `flight_details`.

## 11. Criterios de Aceptación
*   **CA-O16-001:** Un desarrollador no puede hacer "bypass" o saltarse este check en las ramas protegidas de GitHub bajo ninguna circunstancia.

## 12. Restricciones
*   La validación es puramente estática. El pipeline de CI debe combinarse con pruebas de integración reales (CU-T09) para validar que el código implementado realmente hace lo que el contrato promete.

## 13. Fuera de Alcance
*   Generación de los SDKs (Esa funcionalidad posterior se describe en el CU-T07 "Mantener Developer Portal").
