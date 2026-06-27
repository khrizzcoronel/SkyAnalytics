# Especificación de Caso de Uso: CU-T06

## 1. Nombre de la Funcionalidad
**Configurar Alertas de Seguridad**

## 2. Objetivo
Gestionar, configurar y desplegar políticas automatizadas de alerta ante posibles amenazas o brechas de seguridad perimetrales e internas, garantizando tiempos de respuesta ultracortos.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** Rate Limiter en código (Web Application Firewall), Alertas básicas, Notificaciones de Slack, Slack.

## 4. Contexto del Problema
SkyAnalytics está expuesta a ataques DDoS, intentos de inyección SQL, exfiltración de datos y escaneos automatizados. No contar con un sistema de alertas proactivo viola los compromisos Buenas prácticas de seguridade Higiene de seguridad. Se necesita una matriz de reglas automatizada que escale incidentes a los guardias (On-Call) dependiendo de su severidad.

## 5. Requisitos Funcionales
*   **RF-T06-001:** El sistema debe integrar eventos provenientes de WAF, GuardDuty y herramientas de IAM Access Analyzer hacia un hub central (Sentry / Logs AlertManager o AWS Security Hub).
*   **RF-T06-002:** El SRE debe poder definir reglas declarativas (en Scripts básicos de despliegue) que especifiquen umbrales de disparo (ej. más de 1000 requests 401 desde una misma IP en 1 min).
*   **RF-T06-003:** El sistema debe rutear las alertas críticas de seguridad hacia Notificaciones de Slack, saltándose los filtros de "no molestar" del ingeniero en guardia.
*   **RF-T06-004:** El sistema debe automatizar respuestas de Nivel 1 (ej. bloqueo Logsral de una IP sospechosa en el WAF) sin intervención humana (Auto-remediación).

## 6. Requisitos No Funcionales
*   **RNF-T06-001:** La latencia de disparo desde la detección de la anomalía hasta la recepción de la alerta en Notificaciones de Slack no debe superar los 2 minutos.
*   **RNF-T06-002:** Todos los disparos de alertas y auto-remediaciones deben generar un rastro de auditoría inmutable en Archivos de Log / CloudTrail.

## 7. Reglas de Negocio
*   **RN-T06-001 (Clasificación de Severidad):** 
    *   *Sev1 (Crítico):* Exfiltración masiva, acceso root comprometido, DDoS masivo que degrada Uptime.
    *   *Sev2 (Alto):* Escaneo de puertos detectado, fallos masivos de login (fuerza bruta).
    *   *Sev3 (Medio/Bajo):* Accesos anómalos a consolas no críticas.
*   **RN-T06-002 (Escalamiento Zero-Trust):** Cualquier actividad detectada sin el debido cifrado TLS 1.3 se levanta como Sev2.

## 8. Entradas
*   Reglas de configuración en código (`.tf` / YAML files).
*   Logs crudos de acceso o hallazgos de servicios externos.

## 9. Salidas
*   **Payload JSON:** Alertas enviadas al webhook de Notificaciones de Slack y Slack.
*   **Reglas aplicadas:** Cambios aplicados automáticamente al firewall (WAF Rules).

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Ataque de fuerza bruta auto-remediado
**Dado** que un atacante realiza 500 intentos de inicio de sesión fallidos desde una IP en Rusia
**Cuando** el Rate Limiter en código detecta la superación del umbral definido (Regla Rate Limit Auth)
**Entonces** el sistema bloquea automáticamente la IP por 24 horas (Auto-remediación)
**Y** envía una alerta de nivel Medio/Bajo al canal de `#security-alerts` en Slack sin despertar al SRE.

### Escenario 2: Notificación crítica de escalamiento
**Dado** que Alertas básicas detecta actividad de minería de criptomonedas en un pod de PaaS (indicando compromiso de host)
**Cuando** la alerta entra al hub de seguridad central
**Entonces** el sistema clasifica la alerta como Sev1
**Y** dispara una llamada telefónica y SMS de Notificaciones de Slack al SRE en guardia (On-Call) inmediatamente.

## 11. Criterios de Aceptación
*   **CA-T06-001:** Las reglas de alerta deben estar versionadas en Git; un cambio directo en la consola de AWS es detectado como 'Drift' y revertido en la siguiente sincronización.
*   **CA-T06-002:** El bloqueo automático (WAF) debe ejecutarse exitosamente en menos de 10 segundos tras superar el umbral.

## 12. Restricciones
*   Ninguna regla automática debe bloquear rangos de IP pertenecientes a servicios troncales de la empresa (Listas Blancas estáticas).

## 13. Fuera de Alcance
*   Análisis forense profundo (La alerta es solo el gatillo; el análisis se realiza como parte del Post-Mortem CU-O13).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Comunicación de Incidentes:** Ante caídas o mantenimientos, el sistema actualizará una **Status Page estática** y enviará un **Correo electrónico automático** a todos los usuarios registrados para mantener transparencia proactiva.
