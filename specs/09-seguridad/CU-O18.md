# Especificación de Caso de Uso: CU-O18

## 1. Nombre de la Funcionalidad
**Ejecutar Pipeline de Seguridad SAST/DAST en CI/CD**

## 2. Objetivo
Automatizar la detección temprana de vulnerabilidades de software y malas prácticas de seguridad (DevSecOps) integrando análisis de código estático (SAST) y dinámico (DAST) directamente en el ciclo de vida de desarrollo de la plataforma, bloqueando el pase a producción de código inseguro.

## 3. Actores Involucrados
*   **Actor Principal:** Sistema CI/CD (Pipeline automatizado)
*   **Sistemas Externos / Actores Secundarios:** SonarQube (SAST), OWASP ZAP (DAST), Snyk (Software Composition Analysis), GitHub Actions.

## 4. Contexto del Problema
Cumplir con SOC 2 y la política Zero Trust de SkyAnalytics significa que la seguridad no es una revisión trimestral, sino un proceso continuo. Si un desarrollador introduce una dependencia vulnerable (ej. un paquete npm hackeado) o deja un endpoint susceptible a inyección SQL, los datos de las aerolíneas se exponen masivamente.

## 5. Requisitos Funcionales
*   **RF-O18-001:** El pipeline de integración continua (CI) debe ejecutar escaneos SAST (SonarQube) sobre el código fuente de backend y frontend en cada Pull Request.
*   **RF-O18-002:** El pipeline debe ejecutar un Software Composition Analysis (Snyk/Dependabot) para identificar librerías de terceros (Open Source) que contengan CVEs (Common Vulnerabilities and Exposures) conocidos.
*   **RF-O18-003:** Tras un despliegue exitoso al entorno de Staging, el pipeline debe disparar pruebas DAST (OWASP ZAP) simulando ataques web comunes (XSS, SQLi, CSRF) contra la aplicación corriendo.
*   **RF-O18-004:** El pipeline debe fallar de manera forzosa (Hard Block) si se descubre una vulnerabilidad con severidad Alta o Crítica (CVSS > 7.0).

## 6. Requisitos No Funcionales
*   **RNF-O18-001 (Performance de Pipeline):** Los escaneos SAST y SCA deben ser incrementales y paralelizados para no añadir más de 3 minutos de retraso a la compilación estándar.
*   **RNF-O18-002:** Falsos positivos marcados por los desarrolladores deben ser auditables por el equipo de seguridad para evitar evasión maliciosa de las reglas.

## 7. Reglas de Negocio
*   **RN-O18-001 (Quality Gate):** El código no puede fusionarse si tiene una Deuda Técnica de Seguridad (Security Debt) de clasificación C o peor (según los umbrales de SonarQube).
*   **RN-O18-002 (Escáner de Secretos):** Está estrictamente prohibido commitear contraseñas, tokens de AWS, o API Keys. Si el pre-commit hook o el pipeline detecta un patrón de credencial (TruffleHog / GitGuardian), el commit se rechaza inmediatamente.

## 8. Entradas
*   Código fuente (Ramas de Git).
*   Manifiestos de dependencias (`package.json`, `requirements.txt`).
*   URL del entorno de Staging (para DAST).

## 9. Salidas
*   **Reportes:** Informe PDF/HTML detallado de vulnerabilidades.
*   **Estado de GitHub:** Checks marcados con Cruz Roja (Fallo) o Check Verde (Éxito).
*   **Alerta:** Mensaje en Slack (`#security-alerts`) si se halla una vulnerabilidad CVSS Crítica en dependencias transitivas productivas.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Prevención de exposición de secretos
**Dado** que un desarrollador novato accidentalmente incluye la contraseña de la Base de Datos en un archivo `config.py`
**Cuando** intenta ejecutar `git commit` y enviarlo al repositorio (Push)
**Entonces** el escáner de secretos de GitHub Actions intercepta la cadena de texto coincidente con alta entropía
**Y** aborta el pipeline instantáneamente con el error "Secret Leak Detected: Database Password"
**Y** notifica al equipo de DevSecOps para que rotten esa contraseña por precaución (CU-O12).

### Escenario 2: Vulnerabilidad en paquete de terceros detectada
**Dado** que el backend utiliza la librería `requests v2.10.0`
**Cuando** se publica un CVE crítico en internet para esa versión específica
**Entonces** Snyk escanea el árbol de dependencias nocturnamente
**Y** detecta la librería vulnerable en la rama principal de Producción
**Y** crea un Pull Request automático subiendo la versión de `requests` a la versión parchada segura (`v2.11.0`).

## 11. Criterios de Aceptación
*   **CA-O18-001:** Las pruebas DAST en el entorno de Staging deben usar credenciales de prueba; no pueden bajo ningún motivo ejecutar ataques de alteración destructiva (Write/Delete) contra bases de datos que no estén diseñadas para restablecerse automáticamente.

## 12. Restricciones
*   Los análisis DAST completos (que tardan horas) no se ejecutan por cada Pull Request. Solo se ejecutan una vez a la semana o tras un despliegue de un Release candidato en Staging.

## 13. Fuera de Alcance
*   Auditorías manuales de "Penetration Testing" y Red Teaming externo. El CI/CD solo cubre vulnerabilidades conocidas o detectables por herramientas estáticas y dinámicas automatizadas.
