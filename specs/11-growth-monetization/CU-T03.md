# Especificación de Caso de Uso: CU-T03

## 1. Nombre de la Funcionalidad
**Gestionar Infraestructura con Terraform (IaC)**

## 2. Objetivo
Centralizar, versionar y automatizar el aprovisionamiento de toda la infraestructura cloud (AWS, PaaS, CDN, BDs) mediante Infrastructure as Code (Terraform), eliminando cambios manuales (ClickOps) y garantizando la reproducibilidad de entornos.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** AWS (Cloud Provider), GitHub Actions (CI/CD Pipeline).

## 4. Contexto del Problema
SkyAnalytics exige un Uptime del 99.0% (Best Effort) y arquitectura multi-región. Modificar recursos cloud manualmente en la consola web de AWS introduce inconsistencias, riesgos de seguridad y hace imposible un *Disaster Recovery* rápido (RTO $\leq$ 15 min). La infraestructura debe tratarse como software.

## 5. Requisitos Funcionales
*   **RF-T03-001:** Todos los recursos (VPCs, EKS Clusters, RDS, S3, IAM Roles) deben estar declarados en archivos `.tf`.
*   **RF-T03-002:** El estado de Terraform (`Terraform.tfstate`) debe almacenarse de forma remota, segura (S3) y bloqueada para prevenir condiciones de carrera (DynamoDB lock).
*   **RF-T03-003:** El sistema de CI/CD debe ejecutar automáticamente `Terraform plan` al crear un Pull Request y postear el plan de ejecución como comentario en GitHub.
*   **RF-T03-004:** El sistema de CI/CD debe ejecutar `Terraform apply` únicamente cuando el Pull Request es aprobado por al menos otro SRE y fusionado a la rama `main`.
*   **RF-T03-005:** Se deben implementar escaneos de seguridad estática de infraestructura (ej. `tfsec` o `checkov`) en el pipeline para detectar malas configuraciones (ej. buckets públicos).

## 6. Requisitos No Funcionales
*   **RNF-T03-001 (Trazabilidad):** Cada recurso creado debe incluir etiquetas (Tags) obligatorias: `Environment`, `Project`, `Owner`, `ManagedBy=Terraform`.
*   **RNF-T03-002 (Inmutabilidad):** Los entornos (Dev, Staging, Prod) deben ser 100% reproducibles ejecutando los manifiestos desde cero.

## 7. Reglas de Negocio
*   **RN-T03-001 (Zero ClickOps):** Los permisos de los ingenieros SRE en la consola de AWS son de solo lectura (`ReadOnlyAccess`). Las modificaciones con permisos de escritura solo pueden ser ejecutadas por el Rol IAM de GitHub Actions.
*   **RN-T03-002 (Destrucción Protegida):** Recursos con estado en producción (Bases de datos, KMS Keys) deben tener activado `prevent_destroy = true` a nivel de Terraform.

## 8. Entradas
*   Código Terraform (`.tf` files) modificado en un Pull Request.
*   Variables de entorno y secretos inyectados por GitHub Secrets / .env secrets durante el pipeline.

## 9. Salidas
*   **Log de Ejecución:** Salida en consola de `Terraform apply`.
*   **Infraestructura real:** Recursos aprovisionados, modificados o eliminados en AWS.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Aprovisionamiento seguro vía PR
**Dado** que un SRE necesita añadir una réplica de base de datos
**Cuando** sube los cambios en Terraform y crea un Pull Request
**Entonces** GitHub Actions ejecuta `Terraform plan` y escanea con `tfsec`
**Y** al no encontrar violaciones de seguridad, el plan se adjunta al PR
**Cuando** el Desarrollador (Tú) aprueba y fusiona el PR
**Entonces** el pipeline ejecuta automáticamente `Terraform apply` aprovisionando la réplica en AWS.

### Escenario 2: Bloqueo de infraestructura insegura
**Dado** que un desarrollador crea un PR que configura un bucket S3 para ser de acceso público
**Cuando** el pipeline ejecuta el escáner `tfsec`
**Entonces** el escáner detecta la violación de política (Buckets públicos prohibidos por SOC 2)
**Y** el pipeline falla inmediatamente
**Y** bloquea el botón de Merge, impidiendo que el cambio llegue a producción.

## 11. Criterios de Aceptación
*   **CA-T03-001:** Es imposible aplicar cambios en producción sin que queden registrados en el historial de commits de Git.
*   **CA-T03-002:** Si el pipeline de Terraform falla a la mitad de un apply, el mecanismo de lock en DynamoDB previene ejecuciones simultáneas corruptas.

## 12. Restricciones
*   El pipeline de GitHub Actions debe asumir un rol (OIDC - OpenID Connect) temporal en AWS, quedando estrictamente prohibido el uso de Access Keys permanentes a nivel de repositorio.

## 13. Fuera de Alcance
*   Aprovisionamiento y configuración interna del software de los contenedores (Terraform gestiona la infraestructura base (PaaS/EKS), pero los servicios se despliegan vía Helm o ArgoCD).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Gestión de Secretos:** Las contraseñas y llaves de API se inyectarán de forma segura utilizando **GitHub Secrets** durante el pipeline de CI/CD, sin intervención manual en el panel del PaaS.
