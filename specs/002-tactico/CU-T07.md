# Especificación de Caso de Uso: CU-T07

## 1. Nombre de la Funcionalidad
**Mantener Developer Portal y SDKs**

## 2. Objetivo
Gestionar, publicar y actualizar la documentación técnica interactiva y las librerías cliente (SDKs) que los desarrolladores B2B utilizan para consumir la API predictiva, reduciendo el "Time-to-First-Value" (TTFV).

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** Mintlify (Portal de Docs), OpenAPI Generator, NPM/PyPI/Maven (Repositorios de paquetes).

## 4. Contexto del Problema
Un API sin buena documentación y SDKs resulta difícil de integrar, lo que ahuyenta a los desarrolladores de aerolíneas que desean soluciones *plug-and-play*. Si la documentación se desactualiza respecto a la API real, ocurren errores de integración masivos. Es vital un flujo automatizado de actualización de docs.

## 5. Requisitos Funcionales
*   **RF-T07-001:** El sistema de CI/CD debe disparar la auto-generación de SDKs (para Python, JavaScript y Java) utilizando `OpenAPI Generator` ante cada release oficial (tag en Git) de los contratos OpenAPI 3.1.
*   **RF-T07-002:** El sistema debe publicar automáticamente los paquetes generados en los registros públicos (npm, PyPI) con versionado SemVer correspondiente.
*   **RF-T07-003:** El sistema debe compilar y desplegar la documentación interactiva en el Developer Portal (basado en Mintlify) inyectando la nueva especificación OpenAPI.
*   **RF-T07-004:** El portal debe proveer un entorno "Sandbox" donde los usuarios puedan hacer llamadas de prueba (Mock) con datos sintéticos interactivos.

## 6. Requisitos No Funcionales
*   **RNF-T07-001:** El tiempo máximo entre el merge de un Release a la rama principal y la visibilidad de la nueva documentación en el portal no debe exceder los 15 minutos.
*   **RNF-T07-002:** La documentación generada debe ser totalmente responsiva (Responsive Web Design) y accesible (WCAG 2.1).

## 7. Reglas de Negocio
*   **RN-T07-001 (Política SemVer):** Si el linter detecta que un cambio en OpenAPI es un *breaking change* (ej. eliminación de un campo requerido), la publicación forzará un salto de versión mayor (Major) tanto en los SDKs como en la documentación.
*   **RN-T07-002 (Autenticación del Sandbox):** Las llamadas al Sandbox no requieren un API Key corporativa real, pero sí un token Logsral generado en el navegador para evitar abusos (rate limit de 10 req/minuto estricto).

## 8. Entradas
*   Archivos `openapi.yaml` actualizados en la rama principal.
*   Archivos Markdown complementarios (tutoriales, guías conceptuales).

## 9. Salidas
*   **Páginas web:** Sitios de documentación estáticos generados.
*   **Archivos / Paquetes:** `.tar.gz`, archivos `.whl`, desplegados a PyPI, NPM.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Automatización de SDK y documentación
**Dado** que el equipo de backend introduce un nuevo endpoint para consultar clima (añadido al OpenAPI)
**Cuando** se aprueba el Pull Request y se crea el tag `v1.2.0`
**Entonces** el pipeline de CI genera las librerías `skyanalytics-node v1.2.0` y `skyanalytics-python v1.2.0`
**Y** las publica en NPM y PyPI
**Y** actualiza el portal de Mintlify mostrando el nuevo endpoint con ejemplos interactivos de llamada.

### Escenario 2: Prueba exitosa en Sandbox
**Dado** que un desarrollador visitante lee la documentación del nuevo endpoint de clima
**Cuando** presiona el botón "Try It Out" en la sección de Sandbox
**Entonces** el Developer Portal realiza una llamada al endpoint Mocking
**Y** le retorna un JSON de ejemplo con predicción climática sintética en menos de 1 segundo.

## 11. Criterios de Aceptación
*   **CA-T07-001:** Los SDKs generados automáticamente pasan suites de pruebas de compilación y empaquetado interno antes de ser liberados a los registros públicos.
*   **CA-T07-002:** El enlace de cada endpoint en la documentación dirige exactamente a la especificación Swagger/OpenAPI incrustada sin errores 404.

## 12. Restricciones
*   El Developer Portal debe alojarse en la periferia mediante una CDN (CloudFront/Cloudflare) para garantizar acceso de baja latencia a nivel global y alta disponibilidad.

## 13. Fuera de Alcance
*   Creación manual de foros comunitarios (La comunidad se maneja en plataformas asíncronas externas como Slack, Discord o GitHub Discussions).
