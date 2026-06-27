# Especificación de Caso de Uso: CU-T10

## 1. Nombre de la Funcionalidad
**Validar Estrategia de Pricing**

## 2. Objetivo
Gestionar, simular y desplegar variantes de planes de precios (Pricing) en el mercado, evaluando métricas como la Disposición a Pagar (Willingness to Pay) y la conversión mediante experimentación A/B.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Desarrollador (Dueño)
*   **Sistemas Externos / Actores Secundarios:** Herramienta de A/B Testing (Optimizely / VWO), Stripe (Gestión de suscripciones), CRM.

## 4. Contexto del Problema
Para un producto SaaS B2B, el pricing nunca es estático. El Desarrollador (Dueño) y el VP de Marketing necesitan ajustar los precios de las APIs predictivas y los dashboards para maximizar ingresos y penetración, pero un cambio brusco puede incrementar el churn (cancelaciones) o ahuyentar prospectos. Se requiere experimentación basada en datos empíricos.

## 5. Requisitos Funcionales
*   **RF-T10-001:** El sistema (plataforma de experimentación) debe permitir configurar divisiones de tráfico (Split Routing) hacia dos variantes (A/B) de la página pública de precios (Pricing Page).
*   **RF-T10-002:** El sistema debe capturar eventos de analítica desde ambas variantes de precios, registrando Clics en "Subscribe", Tasa de abandono de carrito, y Suscripciones Exitosas.
*   **RF-T10-003:** El sistema debe registrar las entrevistas de retroalimentación cualitativas de "Willingness to Pay" en un repositorio central, categorizando la percepción de valor del prospecto.
*   **RF-T10-004:** El equipo debe poder consultar el panel de experimentación en tiempo real para ver qué variante tiene la mayor significancia estadística.

## 6. Requisitos No Funcionales
*   **RNF-T10-001:** El desvío de tráfico de A/B testing debe ejecutarse en el Edge (CDN - Cloudflare Workers/CloudFront Functions) para evitar latencia visible por el usuario y problemas de "Flickering" (parpadeo visual de la UI).
*   **RNF-T10-002:** La segmentación del tráfico debe ser "Sticky" basada en cookies (Un visitante que ve el Precio B hoy, debe seguir viendo el Precio B si regresa mañana desde el mismo dispositivo).

## 7. Reglas de Negocio
*   **RN-T10-001 (Significancia Estadística):** Un experimento no se considera concluyente ni accionable hasta que alcance una significancia estadística superior al 95% (p-value < 0.05) y un volumen mínimo de tráfico preestablecido.
*   **RN-T10-002 (Integridad de Clientes Existentes):** Los experimentos de precios aplicados en la web pública (front-page) aplican exclusivamente para adquisición de NUEVOS clientes. Los clientes suscritos existentes mantienen el precio anterior bloqueado en su contrato de Stripe (Grandfathering).

## 8. Entradas
*   Páginas web codificadas: Versión A (Control / Precios actuales), Versión B (Challenger / Nuevos precios).
*   Filtros UI del Dashboard de AB Test: Rango de fechas, Métricas de conversión.

## 9. Salidas
*   **UI Dashboard Analítico:** Reporte detallado mostrando conversiones, CVR, y el ganador estadístico.
*   **Configuraciones API:** Integración final del nuevo plan de precios con Stripe para su despliegue oficial.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Ejecución y victoria del experimento de Pricing
**Dado** que el Desarrollador (Tú) ha activado un A/B test (50% Variante A \$499, 50% Variante B \$599)
**Cuando** el experimento alcanza 10,000 visitas por grupo y una significancia del 96%
**Entonces** el panel muestra que la Variante B (\$599) tiene el mismo CVR de suscripciones que la Variante A
**Y** concluye que la Disposición a Pagar soporta el aumento de precio
**Y** recomienda desplegar la Variante B a producción al 100%.

### Escenario 2: Protección de clientes actuales (Grandfathering)
**Dado** que los nuevos precios (Variante B) se han aplicado en producción
**Cuando** un cliente antiguo con sesión activa y suscripción de \$499 revisa su panel de facturación interno
**Entonces** el sistema le sigue cobrando \$499 y su plan interno mantiene el identificador heredado (legacy plan)
**Y** el nuevo precio de \$599 solo es visible en el Landing Page de adquisición.

## 11. Criterios de Aceptación
*   **CA-T10-001:** El script del experimento (A/B testing snippet) carga en un tiempo imperceptible (menor a 50ms) en la capa Edge.
*   **CA-T10-002:** Toda suscripción generada bajo un entorno de prueba en Stripe durante el diseño del A/B test debe utilizar APIs de Stripe Sandbox y nunca tarjetas reales.

## 12. Restricciones
*   No se puede alterar el precio de un modelo de suscripción Enterprise que tenga contrato a largo plazo sin un aviso legal de al menos 60 días, independientemente de lo que dicten las métricas del test.

## 13. Fuera de Alcance
*   Creación y manipulación física del sistema de facturación. Esto lo gestiona 100% Stripe Billing. SkyAnalytics solo reacciona a los eventos (webhooks) de pago exitoso.
