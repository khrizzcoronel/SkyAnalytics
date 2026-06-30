# Especificación de Caso de Uso: CU-O11

## 1. Nombre de la Funcionalidad
**Publicar Changelog Semanal en Developer Portal**

## 2. Objetivo
Automatizar la recolección, categorización y publicación de los cambios (Release Notes / Changelog) realizados en la API durante la semana, comunicándolos proactivamente a la comunidad de desarrolladores B2B para minimizar fricciones de integración.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** GitHub (Release API), Mintlify (Developer Portal), SendGrid (Email).

## 4. Contexto del Problema
Cuando una API evoluciona rápidamente (Continuous Deployment), los consumidores externos pierden el hilo de qué endpoints se agregaron o qué campos se modificaron. Si no se comunican los *Breaking Changes* o las nuevas características (Features), los clientes enfrentan errores silenciosos y el equipo de soporte se satura.

## 5. Requisitos Funcionales
*   **RF-O11-001:** El sistema (Script CI/CD) debe analizar todos los commits integrados en la rama principal desde el último Tag de Release.
*   **RF-O11-002:** El sistema debe categorizar cada commit basándose en las convenciones de Conventional Commits (ej. `feat:`, `fix:`, `docs:`, `BREAKING CHANGE:`).
*   **RF-O11-003:** El sistema debe compilar un archivo Markdown consolidado y publicarlo en la sección "Changelog" del Developer Portal.
*   **RF-O11-004:** El sistema debe enviar un correo electrónico resumido a todos los desarrolladores suscritos a la lista "API Updates".

## 6. Requisitos No Funcionales
*   **RNF-O11-001:** El proceso de generación de Changelog debe ejecutarse de manera desatendida (cronjob) todos los viernes a las 16:00 UTC.

## 7. Reglas de Negocio
*   **RN-O11-001 (Semantic Versioning):** Si el script detecta la etiqueta `BREAKING CHANGE` en al menos un commit, la nueva versión generada incrementará su versión `MAJOR` (ej. de v1.4.2 a v2.0.0).
*   **RN-O11-002 (Depuración de mensajes):** Commits etiquetados como `chore:` o `ci:` no deben incluirse en el Changelog público, ya que son ruido irrelevante para los consumidores externos.

## 8. Entradas
*   Historial de commits de Git.
*   Firma del release anterior.

## 9. Salidas
*   **Archivo Markdown:** `changelog-vX.Y.Z.md` subido a Mintlify.
*   **Correos Electrónicos:** Enviados vía API de SendGrid.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Generación exitosa de Changelog Menor (Nuevas Features)
**Dado** que es viernes a las 16:00 UTC y existen 3 commits de tipo `feat:` y 2 de tipo `fix:`
**Cuando** el script de Release se ejecuta
**Entonces** genera la versión v1.5.0
**Y** crea un documento Markdown agrupando los "Features" y "Bug Fixes"
**Y** actualiza el Developer Portal y envía el boletín informativo.

### Escenario 2: Intento de Changelog sin cambios públicos
**Dado** que durante la semana solo se fusionaron commits de infraestructura (`chore:` y `ci:`)
**Cuando** el script de Release analiza el historial
**Entonces** determina que no hay impacto en los consumidores de la API
**Y** cancela silenciosamente la creación del release
**Y** no envía ningún correo para evitar fatiga de notificaciones en los usuarios.

## 11. Criterios de Aceptación
*   **CA-O11-001:** El Changelog generado siempre incluye hipervínculos directos a los PRs originales en GitHub para proveer mayor contexto técnico.

## 12. Restricciones
*   Solo los desarrolladores registrados (Tenants válidos) que hayan hecho opt-in recibirán correos de Changelog, cumpliendo estrictamente con las normativas anti-spam (CAN-SPAM/GDPR).

## 13. Fuera de Alcance
*   Redacción manual de tutoriales profundos para las nuevas features. El Changelog es un listado técnico conciso; los tutoriales se manejan en el CU-T07.

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Comunicación de Incidentes:** Ante caídas o mantenimientos, el sistema actualizará una **Status Page estática** y enviará un **Correo electrónico automático** a todos los usuarios registrados para mantener transparencia proactiva.
