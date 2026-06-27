::: titlepage
**SkyAnalytics Inc.**\
**Drive:**
`https://drive.google.com/drive/folders/1f9FfqWsVkM63CCfhutV755ouBE61dDS6?usp=sharing`\
**Github:** `https://github.com/khrizzcoronel/SkyAnalytics.git`\
**Perfil Estratégico y Corporativo**\
*Análisis Documental Estratégico*\
*Khriz Coronel*\
*Versión 3.0*\
:::

# Desarrollo y Organización Empresarial

## Nivel Estratégico

Define el rumbo de la organización a largo plazo. La alta dirección
(CEO, CTO) traza la misión, visión, alianzas estratégicas y objetivos
globales. Se materializa en 10 Objetivos Estratégicos (OE1--OE10). Las
decisiones en este nivel determinan el posicionamiento competitivo de
SkyAnalytics como referente mundial en inteligencia aeronáutica.

## Nivel Táctico

Traduce la estrategia en planes concretos por área a mediano plazo. Los
líderes de área (VP Marketing, CTO, SRE Lead, Data Engineer Lead, ML
Engineer Lead) definen campañas, presupuestos, configuración de
infraestructura y metodologías. Se concreta en 22 Objetivos Tácticos
(OT1--OT22).

## Nivel Operativo

Ejecución de tareas diarias y semanales a corto plazo. Ingenieros,
analistas y SREs sostienen la operación: pipelines de datos,
entrenamiento de modelos, monitoreo de infraestructura, atención de
tickets y documentación. Se especifica en 34 Objetivos Operativos
(OP1--OP34).

Los actores del sistema se dividen en los niveles Estratégico, Táctico,
Operativo y Externos. Véase la tabla detallada de Actores del Sistema en
la Sección 3.

# Estrategia de SkyAnalytics Inc.

Actividad: ingesta y análisis profundo de macrodatos (Big Data) de
vuelos históricos y en tiempo real, APIs predictivas REST/GraphQL,
modelos de Machine Learning para predicción de retrasos, clima severo y
optimización de rutas, dashboards self-service para aerolíneas, agencias
de viaje, operadores logísticos y entidades gubernamentales. Plataforma
SaaS con modelo de suscripción corporativa.

## Misión

Proveer inteligencia accionable, precisa y oportuna al ecosistema de la
aviación global, permitiendo a nuestros clientes optimizar drásticamente
sus operaciones comerciales, minimizar la incertidumbre en sus procesos
logísticos y elevar la calidad de la experiencia que ofrecen a sus
propios pasajeros mediante decisiones puramente guiadas por datos.

## Visión

Posicionarnos para el año 2028 como la firma líder y el referente
tecnológico mundial en el análisis predictivo del mercado aeronáutico.
Aspiramos a ser el ecosistema de datos subyacente y el aliado
estratégico indispensable para cualquier actor de la industria que
busque operar con la máxima eficiencia y absoluta confiabilidad técnica.

## Objetivo Estratégico General

Convertir datos aeronáuticos globales en inteligencia accionable y
rentable para cada actor de la industria, mediante una plataforma SaaS
de APIs predictivas, infraestructura cloud de alta disponibilidad
(99.99%), modelos de Machine Learning auditables con explainability
(SHAP) y una cultura Remote-First de innovación continua, asegurando
crecimiento financiero sostenido, excelencia operativa y confianza
normativa absoluta (SOC 2, ISO 27001, GDPR, IATA).

## Balanced Scorecard por Perspectiva

### Perspectiva Financiera

  ----------------------- ------------------- -------------------------------------------------------------- --------------------- ------------------------------------------------ ---------------------
  Incrementar ARR         ARR                 Suma suscripciones activas $\times$ 12                         Duplicar anualmente   Growth Hacking, automatización marketing, SDKs   CEO
  Reducir CAC             Costo Adquisición   Gasto marketing / clientes nuevos                              \< \$500 enterprise   SEO, contenido técnico, comunidad                VP Marketing
  Mejorar LTV/CAC         Ratio LTV/CAC       LTV / CAC                                                      \> 3x                 Customer Success automatizado, expansión         VP Customer Success
  Sostener margen bruto   Gross Margin        (ARR - costo cloud) / ARR $\times$ 100                         \> 75%                Optimización infra, serverless mixta             CTO
  Expandir clientes       NRR                 (ARR inicial + expansión - churn) / ARR inicial $\times$ 100   \> 110%               Planes escalonados, upselling                    VP Ventas
  ----------------------- ------------------- -------------------------------------------------------------- --------------------- ------------------------------------------------ ---------------------

  : KPIs de la Perspectiva Financiera

### Perspectiva del Cliente

  ---------------------- ------------ ---------------------------------------------- -------------------------------- -------------------------------------------- ----------------------
  Mejorar satisfacción   NPS          \% promotores - % detractores                  \> 50 enterprise / \> 30 SMB     Encuestas trimestrales, feedback loop        VP Customer Success
  Reducir churn          Churn Rate   Clientes cancelados / total $\times$ 100       \< 0.5% enterprise / \< 2% SMB   Health scoring, alertas riesgo, onboarding   Customer Success Mgr
  Acelerar valor         TTFV         Tiempo registro $\rightarrow$ primer insight   \< 15 min                        Sandbox instantáneo, datos sintéticos        Developer Advocate
  Calidad soporte        CSAT         Satisfechos / encuestados $\times$ 100         \> 90%                           Chatbot IA nivel 1, portal autoservicio      VP Customer Success
  ---------------------- ------------ ---------------------------------------------- -------------------------------- -------------------------------------------- ----------------------

  : KPIs de la Perspectiva del Cliente

### Perspectiva de Procesos Internos

  --------------------------- ---------------- --------------------------------------------- ------------------------------------- ---------------------------------------------------- --------------------
  Garantizar disponibilidad   Uptime           (Tiempo total - caído) / total $\times$ 100   $\geq$ 99.99%                         Multi-región activo-activo, CDN, chaos engineering   SRE Lead
  Gestionar riesgo            Error Budget     Tiempo indisponible / tiempo total mensual    $\leq$ 80% consumido (4.38 min/mes)   Congelar deploys si \> 80%                           SRE Lead
  Frescura de datos           Data Freshness   \% datos en API \< 5 min                      \> 95%                                Streaming pipelines, monitoreo lag                   Data Engineer Lead
  Recuperación rápida         MTTR             Tiempo recuperación / \# incidentes Sev1/2    \< 15 min                             Runbooks automatizados, on-call, post-mortems        SRE Lead
  --------------------------- ---------------- --------------------------------------------- ------------------------------------- ---------------------------------------------------- --------------------

  : KPIs de la Perspectiva de Procesos Internos

### Perspectiva de Aprendizaje y Crecimiento

  --------------------- ------------------------ -------------------------------------------------- ------------------- ----------------------------------------------------- -----------------
  Satisfacción equipo   eNPS                     \% promotores - % detractores (interna)            \> 40               Cultura Remote-First, feedback 360                    CEO / VP People
  Onboarding rápido     Time-to-Productivity     Días hasta primer deploy                           \< 5 días hábiles   Documentación interna, mentor, entorno automatizado   CTO
  Retener talento       Tasa Retención           Empleados permanecen / total inicio $\times$ 100   \> 90% anual        Plan carrera IC, formación, revisiones                VP People
  Innovación abierta    Publicaciones Técnicas   Artículos + charlas + contribuciones / trimestre   $\geq$ 4            Presupuesto conferencias, blog técnico                CTO
  --------------------- ------------------------ -------------------------------------------------- ------------------- ----------------------------------------------------- -----------------

  : KPIs de la Perspectiva de Aprendizaje y Crecimiento

**Nota metodológica eNPS:** Medición trimestral mediante encuesta
interna anónima.\
Umbral mínimo de participación: 70 % del equipo.\
Interpretación: $> 40$ = zona de excelencia \|$10$--$40$ = zona de
mejora \|$< 10$ = zona crítica.

## Cuadro Resumen del Balanced Scorecard

  ------------- ---------------------- ---------------------- ---------------------
  Financiera    Incrementar ARR        ARR                    Duplicar anualmente
  Financiera    Reducir adquisición    CAC                    \< \$500 enterprise
  Financiera    Eficiencia comercial   LTV/CAC                \> 3x
  Financiera    Margen bruto           Gross Margin           \> 75%
  Financiera    Expandir clientes      NRR                    \> 110%
  Cliente       Satisfacción           NPS                    \> 50 enterprise
  Cliente       Reducir churn          Churn Rate             \< 0.5% enterprise
  Cliente       Velocidad valor        TTFV                   \< 15 min
  Cliente       Soporte                CSAT                   \> 90%
  Procesos      Disponibilidad         Uptime                 $\geq$ 99.99%
  Procesos      Riesgo                 Error Budget           $\leq$ 80%
  Procesos      Frescura               Data Freshness         \> 95%
  Procesos      Recuperación           MTTR                   \< 15 min
  Aprendizaje   Equipo                 eNPS                   \> 40
  Aprendizaje   Onboarding             Time-to-Productivity   \< 5 días
  Aprendizaje   Retención              Retención anual        \> 90%
  Aprendizaje   Innovación             Publicaciones          $\geq$ 4/trim
  ------------- ---------------------- ---------------------- ---------------------

  : Cuadro resumen del Balanced Scorecard de SkyAnalytics

# Gestión y Casos de Uso del Sistema

En esta sección se detallan los objetivos y casos de uso que dan vida
operativa a la estrategia del sistema propuesto.

## Actores del Sistema

  --------------------------------- ------------------------------------------------------------------- -------------------
  CEO/Founder                       Define visión, BSC, alianzas                                        Estratégico
  CTO                               Arquitectura, stack, decisiones técnicas, presupuesto cloud         Estratégico
  VP Customer Success               Estrategia retención, churn, NPS, expansión                         Táctico
  VP Marketing                      Campañas, growth hacking, contenido, comunidad                      Táctico
  VP People                         Cultura Remote-First, retención talento, eNPS interno, onboarding   Táctico
  Data Engineer                     Pipelines ETL, data warehouse, calidad, observabilidad              Táctico/Operativo
  ML Engineer                       Entrena, versiona, despliega, monitorea modelos ML                  Táctico/Operativo
  SRE/DevOps                        Infra cloud, CI/CD, monitoreo, alertas, seguridad                   Táctico/Operativo
  Developer Advocate                Developer Portal, SDKs, docs, Sandbox, comunidad                    Táctico/Operativo
  Cliente B2B (Aerolínea/Agencia)   Consume APIs, dashboards, reporta bugs                              Externo
  Proveedor de Datos Aeronáuticos   Suministra datos crudos de vuelos, clima                            Externo
  Auditor de Compliance             Verifica SOC 2, ISO 27001, GDPR, IATA                               Externo
  --------------------------------- ------------------------------------------------------------------- -------------------

  : Actores del ecosistema SkyAnalytics por nivel organizacional

## Objetivos Estratégicos, Tácticos y Operativos

### Objetivos Estratégicos (10)

Los Objetivos Estratégicos definen la dirección a largo plazo de
SkyAnalytics. Cada OE se alinea con una o más perspectivas del BSC y se
descompone en objetivos tácticos y operativos para su ejecución en
cascada.

1.  **Penetración Digital (Growth Hacking):** capturar clientes
    internacionales mediante automatización de marketing en HubSpot,
    posicionamiento SEO, contenido técnico de alto valor y construcción
    de comunidad de desarrolladores. La estrategia se apoya en un funnel
    de adquisición que combina tráfico orgánico, campañas segmentadas
    por industria aeronáutica y un programa de referidos. El objetivo es
    alcanzar 50 Beta Testers activos en Q4 2026 y crecer a 500+ clientes
    para 2028.

2.  **Escalabilidad vía Ecosistemas (APIs/SDKs):** adoptar
    Specification-Driven Development con contratos OpenAPI 3.1 para cada
    endpoint. Publicar SDKs auto-generados en Python, JavaScript y Java.
    Listar la API en marketplaces como RapidAPI y construir un Developer
    Portal con documentación interactiva (Mintlify), sandbox con datos
    sintéticos y gestión de API Keys. Esto permite que un desarrollador
    externo se integre en menos de 3 minutos y acelera la adopción
    orgánica.

3.  **Infraestructura Cloud de Alta Disponibilidad:** garantizar uptime
    $\geq$ 99.99 % mediante despliegue multi-región activo-activo sobre
    Kubernetes, con Terraform como Infrastructure as Code. Implementar
    CDNs multi-proveedor para reducir latencia global, auto-scaling
    horizontal basado en métricas de tráfico y Disaster Recovery con RPO
    $\leq$ 5 min y RTO $\leq$ 15 min. La infraestructura se versiona en
    Git y todo cambio pasa por PR review antes del apply.

4.  **Inteligencia de Negocio Centralizada:** consolidar todos los datos
    operativos y financieros en un Data Warehouse columnar (MonetDB) con
    pipelines ETL orquestados por dbt y validados con Great
    Expectations. Exponer dashboards self-service en PowerBI para
    clientes Enterprise, con datos actualizados diariamente y
    segmentación por aerolínea, ruta y período. Implementar precios
    dinámicos basados en patrones de consumo.

5.  **Innovación en IA Aeronáutica (I+D):** desarrollar y mantener
    modelos de Machine Learning para predicción de retrasos, impacto
    climático en rutas y optimización de trayectorias. Implementar ciclo
    MLOps completo con MLflow (tracking y registry), Feast (feature
    store), SHAP (explainability), A/B testing framework y monitoreo de
    drift (PSI). Extender la capacidad con técnicas de Deep Learning
    para OCR de documentos de compliance y Speech-to-Text para análisis
    de feedback cualitativo (OT21, OT22).

6.  **Gobernanza y Compliance:** implementar un marco DevSecOps con Zero
    Trust Architecture, cifrado end-to-end (TLS 1.3 en tránsito, AES-256
    en reposo), escaneo SAST/DAST en cada PR y gestión de secretos con
    HashiCorp Vault. Obtener certificación SOC 2 Tipo II en el año 2 e
    ISO 27001 en el año 3. Cumplir con GDPR mediante residencia de datos
    por región y con los estándares IATA para el manejo de datos
    aeronáuticos.

7.  **Retención mediante Customer Success:** implementar un programa de
    Customer Success que incluye onboarding guiado con sandbox
    instantáneo (TTFV $\leq$ 15 min), health scoring automatizado por
    tenant, alertas tempranas de riesgo de churn, chatbot IA de nivel 1
    con respaldo de knowledge base y portal de autoservicio. Medir NPS
    trimestralmente con meta $>$ 50 en segmento Enterprise y ejecutar
    ciclos de feedback para mejora continua.

8.  **Consolidación de Talento Remote-First:** construir una cultura de
    trabajo asíncrono con ceremonias ágiles optimizadas para equipos
    distribuidos globalmente. Documentar todo proceso mediante ADRs
    (Architecture Decision Records), wikis internas y runbooks de
    guardia. Implementar career track IC (Individual Contributor) con
    revisiones de desempeño 360° semestrales. Meta: retención anual $>$
    90 % y eNPS $>$ 40.

9.  **Calidad y Observabilidad de Datos:** establecer data contracts
    formales entre productores y consumidores de datos, monitorear
    frescura ($<$ 5 min), volumen, schema drift y linaje mediante
    dashboards de observabilidad. Validar cada ingesta con suites de
    Great Expectations y alertar proactivamente ante degradaciones.
    Implementar monitoreo de extremo a extremo con trazas distribuidas
    (Tempo) y correlación de logs (Loki).

10. **Gestión de Producto Data-Driven:** mantener un roadmap público y
    transparente para clientes y comunidad. Priorizar iniciativas con
    metodología RICE (Reach, Impact, Confidence, Effort). Realizar
    investigación continua de usuarios mediante entrevistas, encuestas y
    análisis de comportamiento en la plataforma. Validar pricing con A/B
    testing y entrevistas de willingness-to-pay antes de cada ajuste de
    precios.

### Objetivos Tácticos (22)

Los Objetivos Tácticos traducen la estrategia en iniciativas concretas
por área funcional a mediano plazo (6--18 meses). Cada OT se vincula al
menos a un OE y se descompone en objetivos operativos para su ejecución
diaria.

1.  **Automatizar flujos HubSpot para Beta Testers.** Configurar
    secuencias de email automation, formularios de registro segmentados
    por industria (aerolínea, agencia, logística) y scoring de leads en
    HubSpot. *Responsable: VP Marketing.* *Plazo: Q3 2026.*

2.  **Gestionar programa Early Adopters con registro simplificado y
    Freemium.** Diseñar flujo de registro self-service con email
    verification, autoprovisionamiento de tenant y plan Freemium con
    1.000 API calls/mes. *Responsable: VP Marketing + Developer
    Advocate.* *Plazo: Q3--Q4 2026.*

3.  **Estandarizar contratos OpenAPI 3.1 y GraphQL.** Definir y mantener
    especificaciones OpenAPI 3.1 para todos los endpoints REST, con
    schemas GraphQL complementarios. Validar automáticamente en CI/CD
    con Spectral linter antes de cada merge. *Responsable: CTO.* *Plazo:
    Q3 2026.*

4.  **Publicar API Beta en RapidAPI y Developer Portal.** Configurar
    listing en RapidAPI con planes Freemium/Pro/Enterprise, OAuth2
    client_credentials y rate limits por plan. Publicar documentación
    interactiva auto-generada en el Developer Portal (Mintlify).
    *Responsable: CTO + Developer Advocate.* *Plazo: Q3 2026.*

5.  **Desplegar infraestructura con Terraform (IaC) y CI/CD GitHub
    Actions.** Versionar todos los recursos cloud como módulos
    Terraform. Implementar pipeline CI/CD con GitHub Actions para
    plan/apply automatizado tras PR review. Separar entornos
    dev/staging/prod en cuentas cloud diferentes. *Responsable: SRE
    Lead.* *Plazo: Q3 2026.*

6.  **Configurar CDNs multi-proveedor.** Desplegar CDNs en al menos dos
    proveedores (CloudFront + Cloudflare) con failover automático.
    Configurar caché de respuestas de API con TTL por endpoint y purga
    programada. *Responsable: SRE Lead.* *Plazo: Q4 2026.*

7.  **Construir pipelines ETL con Great Expectations y dbt.** Diseñar
    flujos de ingesta incremental desde SFTP de proveedores,
    transformación con dbt y validación con Great Expectations.
    Orquestar con Airflow. Monitorear duración, volumen y estado de cada
    DAG. *Responsable: Data Engineer Lead.* *Plazo: Q3--Q4 2026.*

8.  **Implementar dashboards PowerBI y self-service para clientes.**
    Construir dashboards ejecutivos internos (BSC, financieros,
    operativos) y dashboards embebidos para clientes Enterprise con
    segmentación por aerolínea, ruta y período. Programar refreshes
    nocturnos. *Responsable: Data Engineer Lead.* *Plazo: Q4 2026.*

9.  **Gestionar ciclo de vida de modelos ML: MLflow, Feast, SHAP, A/B
    testing.** Implementar MLOps pipeline con MLflow para tracking de
    experimentos y model registry, Feast como feature store
    centralizada, SHAP para explainability y framework de A/B testing en
    producción. *Responsable: ML Engineer Lead.* *Plazo: Q4 2026--Q2
    2027.*

10. **Implementar seguridad perimetral, E2E encryption, SAST/DAST en
    CI/CD.** Configurar WAF, DDoS protection, TLS 1.3 en todas las
    comunicaciones, cifrado AES-256 en reposo. Integrar SonarQube (SAST)
    y OWASP ZAP (DAST) en el pipeline de CI/CD. Bloquear merge ante
    vulnerabilidades críticas. *Responsable: SRE Lead.* *Plazo: Q4
    2026--Q1 2027.*

11. **Mantener Developer Portal: documentación interactiva, Sandbox,
    SDKs, bugs.** Construir y mantener portal con Mintlify, sandbox con
    datos sintéticos renovados semanalmente, SDKs auto-generados
    (Python, JS, Java) desde specs OpenAPI y sistema de reporte de bugs
    con triaging NLP. *Responsable: Developer Advocate.* *Plazo: Q4
    2026--Q2 2027.*

12. **Gestionar trabajo en Linear con sprints de 2 semanas.** Configurar
    workspace por equipo, backlog priorizado con RICE, ceremonias ágiles
    asíncronas (daily standup en Slack, planning y retro en
    videollamada). Medir velocity y cycle time por sprint. *Responsable:
    CTO + todos los leads.* *Plazo: continuo desde Q3 2026.*

13. **Mantener documentación interna: ADRs, wiki, runbooks.** Documentar
    toda decisión arquitectónica en ADRs versionados en Git. Mantener
    wiki con onboarding guides, runbooks de incidentes por tipo de
    alerta, y playbooks de operaciones. *Responsable: CTO.* *Plazo:
    continuo desde Q3 2026.*

14. **Monitorear y optimizar costos cloud.** Configurar dashboards de
    costos por servicio y equipo, alertas de anomalías de gasto diario,
    recomendaciones automáticas de rightsizing y detección de recursos
    ociosos. Revisión semanal con CTO y SRE Lead. *Responsable: SRE
    Lead.* *Plazo: continuo desde Q4 2026.*

15. **Implementar stack de observabilidad: Loki, Prometheus, Tempo,
    PagerDuty.** Desplegar Grafana LGTM stack (Loki para logs,
    Prometheus para métricas, Tempo para trazas) con dashboards por
    servicio y alertas configuradas en PagerDuty. Umbrales: CPU $>$ 80%,
    memoria $>$ 85%, tasa errores 5xx $>$ 1%. *Responsable: SRE Lead.*
    *Plazo: Q4 2026.*

16. **Ejecutar pruebas de carga (k6) y chaos engineering.** Diseñar
    escenarios de carga con 10K usuarios concurrentes simulados en k6.
    Ejecutar chaos experiments mensuales en staging (kill pod aleatorio,
    network partition, DB failover) con Litmus Chaos. Documentar
    resultados y MTTR. *Responsable: SRE Lead.* *Plazo: Q1--Q2 2027.*

17. **Establecer fundación legal: ToS, Privacy Policy, DPA, ruta SOC
    2.** Redactar y publicar Términos de Servicio, Política de
    Privacidad y Data Processing Agreement (DPA) con firma de abogados
    especializados en SaaS. Diseñar roadmap de certificación SOC 2 Tipo
    II para auditoría en año 2. *Responsable: CEO + CTO.* *Plazo: Q4
    2026.*

18. **Validar pricing: entrevistas, análisis competitivo, A/B testing.**
    Realizar entrevistas de willingness-to-pay con 15+ prospectos del
    sector aeronáutico. Analizar precios de competidores (FlightAware,
    OAG, Cirium). Ejecutar A/B test en landing page con 2--3 variantes
    de pricing. *Responsable: VP Marketing + CEO.* *Plazo: Q1--Q2 2027.*

19. **Ejecutar ciclo de feedback continuo: entrevistas, NPS, sesiones,
    RICE.** Implementar encuestas NPS trimestrales automatizadas,
    entrevistas cualitativas mensuales con 5 clientes, sesiones de
    co-creación de features y priorización de backlog con metodología
    RICE. *Responsable: VP Customer Success + VP Marketing.* *Plazo:
    continuo desde Q1 2027.*

20. **Publicar 3 artículos técnicos y participar en 2 conferencias en
    fase Beta.** Redactar artículos técnicos sobre arquitectura de la
    plataforma, modelos ML para aviación y lecciones de DevSecOps.
    Someter propuestas de charlas a conferencias de aviación y
    tecnología (IATA, Airline Tech Summit, KubeCon). *Responsable: CTO +
    Developer Advocate.* *Plazo: Q1--Q2 2027.*

21. **Explorar técnicas de Deep Learning para compliance y soporte.**
    Evaluar modelos de OCR con redes neuronales para procesamiento
    automatizado de documentos de auditoría (facturas de proveedores,
    certificados, logs escaneados). Experimentar con NLP avanzado
    (transformers) para clasificación de tickets y análisis de
    sentimiento en feedback de clientes. *Responsable: ML Engineer
    Lead.* *Plazo: Q3--Q4 2027.*

22. **Implementar Speech-to-Text para transcripción de feedback
    cualitativo.** Desplegar pipeline de transcripción automática con
    Whisper o DeepSpeech para entrevistas de feedback de clientes.
    Integrar con sistema de análisis cualitativo para extraer temas
    recurrentes y sentimiento. Medir Word Error Rate (WER) objetivo
    $\leq$ 10%. *Responsable: ML Engineer Lead.* *Plazo: Q1--Q3 2028.*

### Objetivos Operativos (34)

Los Objetivos Operativos ejecutan la acción diaria, semanal y mensual
que sostiene la operación del ecosistema SkyAnalytics. Cada OP describe
una tarea concreta con su herramienta, cadencia y KPI de éxito, y se
mapea a al menos un Caso de Uso operativo para su trazabilidad.

1.  **Gestionar registro automatizado de usuarios.** Monitorear el
    pipeline de registro self-service: verificar email confirmations,
    detectar cuentas duplicadas o fraudulentas, validar que el
    aprovisionamiento de tenant y API Keys se complete en $\leq$ 30
    segundos. *Herramienta: HubSpot + API Gateway.* *Cadencia: diario.*
    *KPI: $\geq$ 99 % registros exitosos.* *CU: CU-O01.*

2.  **Monitorear rate limiting y auto-scaling de la API.** Supervisar
    thresholds de rate limit por tenant y plan, configurar políticas de
    throttling graduado (warning $\rightarrow$ soft limit $\rightarrow$
    hard limit), verificar que el auto-scaling de pods responda en
    $\leq$ 2 minutos ante picos de tráfico. *Herramienta: K8s HPA + API
    Gateway + Prometheus.* *Cadencia: continuo.* *KPI: $\leq$ 1
    incidente de rate limit breach por semana.* *CU: CU-O02.*

3.  **Supervisar ejecución de pipelines ETL diarios.** Monitorear
    duración, volumen ingerido, row count y estado de cada DAG de
    Airflow. En caso de fallo: investigar logs, corregir y re-ejecutar.
    Mantener un scorecard semanal de salud de pipelines. *Herramienta:
    Airflow + dbt + Great Expectations.* *Cadencia: diario.* *KPI: 100 %
    pipelines completados.* *CU: CU-O03.*

4.  **Validar calidad de datos post-ingesta.** Ejecutar suite de Great
    Expectations sobre datos en staging. Verificar: nulos en flight_id y
    departure_time, duplicados, rangos plausibles (retraso
    $\in [0, 1440]$ min), frescura $\leq$ 5 min y conformidad de schema
    contra data contract. Escalar hallazgos al Data Engineer Lead.
    *Herramienta: Great Expectations + Slack.* *Cadencia: tras cada
    ingesta.* *KPI: $\geq$ 95 % datos con frescura $\leq$ 5 min.* *CU:
    CU-O04.*

5.  **Reentrenar modelos ML programados.** Ejecutar pipeline semanal de
    reentrenamiento con features desde Feast. Entrenar XGBoost/LightGBM
    para retrasos y demanda. Loggear métricas en MLflow, comparar MAPE
    contra baseline. Auto-promover a staging si mejora $>$ 2 %.
    *Herramienta: MLflow + Feast + XGBoost.* *Cadencia: semanal.* *KPI:
    MAPE $\leq$ 15 %.* *CU: CU-O05.*

6.  **Verificar drift de modelos en producción.** Monitorear PSI
    (Population Stability Index) y data drift diariamente sobre modelos
    productivos. Alertar al ML Engineer si PSI $>$ 0.2. Disparar
    reentrenamiento automático si se supera el umbral. Documentar causas
    de drift en runbook. *Herramienta: Evidently AI + MLflow +
    PagerDuty.* *Cadencia: diario.* *KPI: modelos con PSI $\leq$ 0.2 en
    95 % del tiempo.* *CU: CU-O05.*

7.  **Refrescar dashboards BI para clientes.** Ejecutar refresh
    programado nocturno de todos los dashboards PowerBI. Validar que los
    KPIs carguen correctamente (verificación visual de widgets clave),
    verificar consistencia numérica contra fuente, loggear duración
    total del refresh. *Herramienta: PowerBI + dbt.* *Cadencia: nocturno
    diario.* *KPI: dashboards actualizados antes de las 06:00 UTC.* *CU:
    CU-O06.*

8.  **Monitorear telemetría de contenedores en tiempo real.** Recolectar
    métricas de CPU, memoria, red y tasa de errores por pod cada 30
    segundos. Visualizar en dashboards de Grafana por servicio.
    Responder a alertas de PagerDuty según severidad en el runbook
    correspondiente. *Herramienta: Prometheus + Grafana + PagerDuty.*
    *Cadencia: continuo.* *KPI: detección de anomalías $\leq$ 2 min.*
    *CU: CU-O07.*

9.  **Configurar y mantener reglas de alerta.** Definir thresholds por
    servicio (CPU $>$ 80 %, memoria $>$ 85 %, errores 5xx $>$ 1 %,
    latencia p95 $>$ 500ms), probar disparo de cada alerta en staging,
    mantener runbooks actualizados, revisar y eliminar falsos positivos
    semanalmente. *Herramienta: Prometheus AlertManager + PagerDuty.*
    *Cadencia: semanal (revisión).* *KPI: $\leq$ 5 % falsos positivos.*
    *CU: CU-O07.*

10. **Ejecutar escaneo SAST/DAST en pipeline de CI/CD.** Integrar
    SonarQube (SAST) y OWASP ZAP (DAST) en GitHub Actions. Bloquear
    merge ante vulnerabilidades con severidad critical o high. Generar
    reporte de seguridad por release. Mantener baseline de falsos
    positivos aceptados documentado. *Herramienta: GitHub Actions +
    SonarQube + OWASP ZAP.* *Cadencia: por cada PR.* *KPI: 0
    vulnerabilidades críticas en producción.* *CU: CU-O18.*

11. **Aplicar parches de seguridad críticos.** Monitorear CVEs de
    dependencias del stack con Dependabot y Snyk. Parchear
    vulnerabilidades críticas en $\leq$ 24 horas, altas en $\leq$ 72
    horas. Actualizar inventory de versiones de paquetes en la wiki.
    *Herramienta: Dependabot + Snyk + GitHub Security Alerts.*
    *Cadencia: continuo.* *KPI: tiempo medio de parche crítico $\leq$ 12
    horas.* *CU: CU-O18.*

12. **Atender tickets de desarrolladores externos.** Triaging automático
    con NLP para clasificar severidad, categoría y prioridad del ticket.
    Responder primera respuesta en $\leq$ 2 horas. Investigar y resolver
    en $\leq$ 24 horas, o escalar a engineering con contexto completo.
    Notificar resolución al reportante. *Herramienta: Linear + chatbot
    IA + Slack.* *Cadencia: continuo.* *KPI: tiempo primera respuesta
    $\leq$ 2 horas.* *CU: CU-O08.*

13. **Documentar FAQs en base de conocimientos del chatbot.** Detectar
    temas recurrentes cuando se acumulan $\geq$ 3 tickets similares en 7
    días. Generar borrador automático de FAQ con NLP. Revisar, editar,
    añadir screenshots y publicar. Actualizar embeddings del chatbot.
    Medir tasa de deflexión resultante. *Herramienta: NLP embeddings +
    KB portal + chatbot IA.* *Cadencia: semanal.* *KPI: tasa de
    deflexión $\geq$ 30 %.* *CU: CU-O14.*

14. **Gestionar sprints en Linear.** Crear tickets desde el roadmap y el
    backlog priorizado. Actualizar estado diario en Slack standup.
    Cerrar sprint con retrospectiva documentada. Medir velocity, cycle
    time y burndown. Ajustar capacidad del próximo sprint según datos
    históricos. *Herramienta: Linear + Slack bot.* *Cadencia: daily +
    cierre de sprint (2 semanas).* *KPI: $\geq$ 85 % tickets completados
    por sprint.* *CU: CU-O15.*

15. **Revisar y optimizar costos cloud semanalmente.** Auditar factura
    cloud desglosada por servicio. Comparar gasto real contra forecast
    mensual. Detectar anomalías de gasto diario ($>$ 20 % desviación).
    Identificar recursos ociosos o sobre-aprovisionados. Generar
    recomendaciones de ahorro y rightsizing. *Herramienta: AWS Cost
    Explorer + Grafana.* *Cadencia: semanal.* *KPI: desviación $\leq$
    5 % vs presupuesto mensual.* *CU: CU-O19.*

16. **Ejecutar backup diario automatizado.** Programar pg_dump de base
    de datos transaccional a las 03:00 UTC. Encriptar backup con KMS
    (AES-256). Subir a cold storage (S3 Glacier Deep Archive). Loggear
    hash SHA-256 de integridad. Verificar tamaño dentro del rango
    esperado. *Herramienta: pg_dump + AWS KMS + S3 Glacier.* *Cadencia:
    diario.* *KPI: backup exitoso 100 % de los días.* *CU: CU-O09.*

17. **Ejecutar prueba de restauración semanal.** Restaurar último backup
    en instancia de prueba aislada. Validar integridad de datos (row
    counts por tabla, checksums, foreign key consistency). Ejecutar
    smoke tests de API sobre la instancia restaurada. Loggear resultado
    y alertar si falla. *Herramienta: pg_restore + script de
    validación + k6 smoke test.* *Cadencia: semanal.* *KPI: restore
    exitoso 100 % de las semanas.* *CU: CU-O09.*

18. **Calcular SLI/SLO y error budget de uptime.** Computar SLI de
    uptime real de los últimos 30 días desde métricas de Prometheus.
    Comparar contra SLO de 99.99 %. Proyectar consumo de error budget a
    fin de mes (target: 4.38 min/mes). Recomendar congelación de deploys
    si consumo $>$ 80 %. *Herramienta: Prometheus + script SLI/SLO.*
    *Cadencia: semanal.* *KPI: uptime real $\geq$ 99.99 %.* *CU:
    CU-O10.*

19. **Ejecutar congelación de deploys si error budget $>$ 80 %.** Si el
    umbral se supera, bloquear pipeline de CI/CD automáticamente vía
    branch protection en GitHub. Notificar a CTO, tech leads y SRE team
    por Slack y PagerDuty con la justificación y el plan de remediación.
    Documentar la congelación en el runbook de incidentes. *Herramienta:
    GitHub Actions + PagerDuty + Slack.* *Cadencia: bajo demanda.* *KPI:
    tiempo detección $\rightarrow$ congelación $\leq$ 5 min.* *CU:
    CU-O10.*

20. **Publicar changelog semanal con Semantic Versioning.** Recolectar
    commits desde el último release tag. Categorizar automáticamente por
    tipo (feat, fix, breaking, docs, chore). Bump version según reglas
    de SemVer. Publicar en Developer Portal. Enviar email a suscriptores
    y publicar en canal #changelog de Slack. *Herramienta: git log +
    release-it + DevPortal CMS.* *Cadencia: semanal (viernes).* *KPI:
    changelog publicado 100 % de los viernes.* *CU: CU-O11.*

21. **Rotar credenciales de servicio mensualmente.** Identificar secrets
    próximos a expirar (API Keys, DB passwords, TLS certs) desde Vault.
    Generar nuevas credenciales. Actualizar K8s secrets y reiniciar
    pods. Verificar que todos los servicios funcionen con las nuevas
    credenciales vía smoke tests. Desactivar credenciales antiguas tras
    período de gracia de 24 horas. *Herramienta: HashiCorp Vault + K8s +
    script smoke test.* *Cadencia: mensual.* *KPI: 0 incidentes por
    credencial expirada.* *CU: CU-O12.*

22. **Auditar accesos IAM trimestralmente.** Revisar todos los roles,
    políticas y accesos de servicio en la cuenta cloud. Identificar
    permisos sobre-asignados (principle of least privilege). Revocar
    accesos de ex-empleados y servicios deprecados. Generar reporte de
    auditoría con hallazgos y acciones tomadas. *Herramienta: AWS IAM
    Access Analyzer + reporte manual.* *Cadencia: trimestral.* *KPI: 0
    accesos no justificados al cierre de auditoría.* *CU: CU-O12.*

23. **Realizar post-mortem blameless $\leq$ 72 horas post-incidente.**
    Generar timeline automático desde logs y métricas del incidente.
    Facilitar reunión blameless con 5 whys, documentar aprendizajes y
    acciones preventivas. Publicar reporte en wiki y crear tickets en
    Linear. *Herramienta: PagerDuty + Linear + wiki.* *Cadencia: $\leq$
    72 horas.* *KPI: 100 % incidentes Sev1/Sev2 con post-mortem.* *CU:
    CU-O13.*

24. **Validar especificaciones OpenAPI 3.1 en CI/CD.** Ejecutar linter
    Spectral sobre cada spec en cada PR. Verificar que no haya breaking
    changes sin bump de versión major. Validar ejemplos de
    request/response incluidos. Asegurar que todos los endpoints tengan
    descripción y tags. *Herramienta: Spectral + OpenAPI Generator +
    GitHub Actions.* *Cadencia: por cada PR.* *KPI: 0 errores de lint en
    specs mergeadas.* *CU: CU-O16.*

25. **Monitorear presencia en marketplace RapidAPI.** Verificar uptime y
    disponibilidad del listing. Responder a reviews y preguntas de
    desarrolladores en $\leq$ 24 horas. Actualizar descripciones de
    planes trimestralmente. Monitorear métricas de adopción: page views,
    subscriptions por plan, churn del marketplace. *Herramienta:
    RapidAPI Dashboard.* *Cadencia: continuo.* *KPI: rating $\geq$ 4.5
    estrellas en marketplace.* *CU: CU-T02.*

26. **Mantener documentación interactiva del Developer Portal.**
    Sincronizar documentación con specs OpenAPI tras cada release.
    Verificar que todos los endpoints tengan ejemplos request/response
    funcionales. Actualizar guías de migración ante breaking changes.
    Revisar analíticas de páginas para identificar endpoints con
    documentación deficiente. *Herramienta: Mintlify + CI pipeline.*
    *Cadencia: tras cada release.* *KPI: docs sincronizadas en $\leq$ 24
    horas post-release.* *CU: CU-T07.*

27. **Ejecutar pruebas de carga semanales en staging.** Simular tráfico
    de 10K usuarios concurrentes con k6. Medir: latencia p95 y p99,
    throughput (req/s), tasa de errores y uso de recursos durante la
    prueba. Comparar contra baseline. Documentar resultados en reporte
    con gráficos. *Herramienta: k6 + Grafana k6 Cloud.* *Cadencia:
    semanal (lunes staging).* *KPI: latencia p95 $\leq$ 500ms bajo 10K
    usuarios concurrentes.* *CU: CU-T09.*

28. **Ejecutar chaos engineering mensualmente.** Inyectar fallos
    controlados en staging: kill de pod aleatorio, network partition
    entre servicios, DB primary failover, latencia inyectada de 500ms.
    Medir MTTR de cada experimento. Documentar hallazgos, tiempo de
    recuperación y recomendaciones en reporte. *Herramienta: Litmus
    Chaos + k6.* *Cadencia: mensual (primer viernes del mes).* *KPI:
    MTTR $\leq$ RTO de 15 minutos en todos los escenarios.* *CU:
    CU-T09.*

29. **Mantener documentación legal y compliance actualizada.** Revisar y
    actualizar ToS, Privacy Policy y DPA ante cambios regulatorios o de
    producto. Publicar registros de procesamiento de datos por región
    (GDPR Art. 30). Mantener evidencias de controles SOC 2 organizadas
    por trust service criteria. *Herramienta: compliance platform +
    wiki + auditor externo.* *Cadencia: trimestral.* *KPI: 100 %
    documentos legales vigentes y actualizados.* *CU: CU-E04.*

30. **Recolectar y analizar feedback de clientes.** Enviar encuestas NPS
    trimestrales automatizadas a todos los usuarios activos (Typeform).
    Recolectar CSAT post-interacción con soporte. Transcribir
    entrevistas cualitativas con Speech-to-Text. Clasificar comentarios
    por tema y sentimiento para alimentar backlog de producto.
    *Herramienta: Typeform + HubSpot + STT engine.* *Cadencia:
    trimestral (NPS) + continuo (CSAT).* *KPI: tasa de respuesta NPS
    $\geq$ 30 %.* *CU: CU-T10.*

31. **Publicar contenido técnico regularmente.** Redactar y publicar
    artículos técnicos en el blog corporativo. Compartir en Dev.to,
    HackerNews y LinkedIn. Preparar y someter propuestas de charlas a
    conferencias (KubeCon, IATA Summit, AI in Aviation). Medir
    engagement y conversiones a registro. *Herramienta: blog CMS +
    Buffer + Google Analytics.* *Cadencia: semanal (artículo) +
    trimestral (conferencia).* *KPI: $\geq$ 1 artículo técnico por
    semana, $\geq$ 2 charlas por año.* *CU: CU-T01.*

32. **Ejecutar experimentos de Deep Learning para OCR.** Explorar
    modelos de OCR con redes neuronales (CRNN + CTC, TrOCR) para
    procesamiento automatizado de: facturas de proveedores de datos,
    certificados de cumplimiento, logs de auditoría escaneados. Comparar
    precisión contra baseline de entrada manual. Registrar experimentos
    en MLflow. *Herramienta: PyTorch / TensorFlow + MLflow.* *Cadencia:
    sprint de experimentación (4 semanas).* *KPI: precisión OCR $\geq$
    95 % en documentos de compliance.* *CU: CU-O20.*

33. **Implementar y mantener pipeline de Speech-to-Text.** Desplegar
    modelo STT (Whisper / DeepSpeech). Integrar con sistema de
    recolección de feedback para transcripción automática de
    entrevistas. Medir Word Error Rate (WER). Reentrenar con vocabulario
    de dominio aeronáutico para mejorar precisión. Extraer temas y
    sentimiento del texto transcrito. *Herramienta: Whisper /
    DeepSpeech + MLflow.* *Cadencia: continuo.* *KPI: WER $\leq$ 10 %.*
    *CU: CU-O20.*

34. **Validar data contracts entre productores y consumidores.** Definir
    y versionar en Git los schema contracts para cada fuente de datos
    externa. Validar en CI que los datos entrantes cumplan el contrato
    (tipos, nulabilidad, rangos). Alertar al Data Engineer Lead ante
    schema drift del proveedor. Mantener changelog de cambios de
    contrato. *Herramienta: Great Expectations + dbt contracts + Git.*
    *Cadencia: por cada ingesta.* *KPI: 0 ingestion failures por schema
    mismatch.* *CU: CU-O17.*

**Trazabilidad OE $\rightarrow$ Perspectiva BSC $\rightarrow$ KPI
$\rightarrow$ Meta**

  ------ ------------------------ ---------------------------- ------------ ------------------ ----------------------------
  OE1    Financiera + Cliente     Beta Testers activos                      $\ge$ 500          OT1, OT2, OT4, OT19
  OE2    Cliente + Procesos       TTFV (min)                   $\le$ 3      $\le$ 1            OT3, OT4, OT11
  OE3    Procesos                 Uptime (%)                   \%           $\ge$ 99.99%       OT5, OT6, OT14, OT15, OT16
  OE4    Financiera + Procesos    Data Freshness               $\ge$ 95%    $\ge$ 98%          OT7, OT8, OT15
  OE5    Aprendizaje + Procesos   MAPE retrasos                $\le$ 15%    $\le$ 8%           OT9, OT13, OT21, OT22
  OE6    Procesos                 Controles cumplidos (%)      \% (SOC 2)   \% (SOC 2 + ISO)   OT10, OT17
  OE7    Cliente                  NPS Enterprise               ---          $>$ 50             OT2, OT11, OT19
  OE8    Aprendizaje              eNPS interno                 $>$ 40       $>$ 50             OT12, OT13, OT20
  OE9    Procesos                 Data Contracts válidos (%)   \%           \%                 OT7, OT15, OT18
  OE10   Cliente + Financiera     Initiatives on track (%)     \%           $\ge$ 90%          OT18, OT19, OT20
  ------ ------------------------ ---------------------------- ------------ ------------------ ----------------------------

  : Trazabilidad de cada Objetivo Estratégico con su perspectiva BSC,
  KPI principal, metas a corto y largo plazo, y objetivos tácticos
  asociados

## Catálogo General de Casos de Uso

  **Código**   **Nombre**                                       **Prior.**   **Nivel**     **Actor Principal**
  ------------ ------------------------------------------------ ------------ ------------- --------------------------
                                                                                           
  **Código**   **Nombre**                                       **Prior.**   **Nivel**     **Actor Principal**
                                                                                           
  CU-E01       Consultar Tablero BSC                                         Estratégico   CEO
  CU-E02       Analizar ARR y Rentabilidad                                   Estratégico   CEO
  CU-E03       Evaluar Uptime Global y SLA                                   Estratégico   CTO
  CU-E04       Revisar Cumplimiento Normativo                                Estratégico   CTO / Auditor
  CU-E05       Definir Metas Estratégicas Trimestrales                       Estratégico   CEO / CTO
  CU-E06       Analizar Retención de Talento y eNPS                          Estratégico   CEO / VP People
                                                                                           
  CU-T01       Gestionar Campañas de Growth Hacking                          Táctico       VP Marketing
  CU-T02       Configurar y Publicar API en RapidAPI                         Táctico       CTO / Developer Advocate
  CU-T03       Gestionar Infraestructura con Terraform                       Táctico       SRE / DevOps
  CU-T04       Monitorear Pipelines ETL y Calidad                            Táctico       Data Engineer
  CU-T05       Entrenar y Versionar Modelos ML                               Táctico       ML Engineer
  CU-T06       Configurar Alertas de Seguridad                               Táctico       SRE / DevOps
  CU-T07       Mantener Developer Portal y SDKs                              Táctico       Developer Advocate
  CU-T08       Analizar Costos Cloud y Optimizar                             Táctico       CTO / SRE
  CU-T09       Ejecutar Pruebas de Carga y Chaos                             Táctico       SRE / DevOps
  CU-T10       Validar Estrategia de Pricing                                 Táctico       VP Marketing / CEO
                                                                                           
  CU-O01       Registrar Tenant y Autogenerar API Keys                       Operativo     Cliente B2B / Sistema
  CU-O02       Consultar Datos de Vuelo vía API                              Operativo     Cliente B2B
  CU-O03       Ejecutar Ingesta Diaria de Datos                              Operativo     Data Engineer / Sistema
  CU-O04       Validar Calidad de Datos en ETL                               Operativo     Data Engineer / Sistema
  CU-O05       Reentrenar Modelo de Retrasos                                 Operativo     ML Engineer
  CU-O06       Refrescar Dashboards BI                                       Operativo     Data Engineer / Sistema
  CU-O07       Monitorear Telemetría de Contenedores                         Operativo     SRE / DevOps
  CU-O08       Atender Ticket de Bug                                         Operativo     Developer Advocate
  CU-O09       Ejecutar Backup y Prueba de Restauración                      Operativo     SRE / DevOps
  CU-O10       Revisar Error Budget y Congelar Deploys                       Operativo     SRE / DevOps
  CU-O11       Publicar Changelog Semanal                                    Operativo     Developer Advocate
  CU-O12       Rotar Credenciales y Auditar IAM                              Operativo     SRE / DevOps
  CU-O13       Realizar Post-Mortem de Incidente                             Operativo     SRE / DevOps
  CU-O14       Documentar FAQ en Base de Conocimientos                       Operativo     Developer Advocate
  CU-O15       Gestionar Sprint en Linear                                    Operativo     Todo el equipo
  CU-O16       Validar Especificaciones OpenAPI en CI/CD                     Operativo     CTO / SRE
  CU-O17       Validar Data Contracts en Pipeline ETL                        Operativo     Data Engineer
  CU-O18       Ejecutar Pipeline Seguridad SAST/DAST en CI/CD                Operativo     SRE / DevOps
  CU-O19       Analizar y Optimizar Costos Cloud                             Operativo     CTO / SRE
  CU-O20       Ejecutar Experimentos de Deep Learning                        Operativo     ML Engineer

  : Catálogo de 36 Casos de Uso del Ecosistema SkyAnalytics

**Nota:** El detalle completo de cada Caso de Uso ---incluyendo
propósito, descripción detallada, precondiciones, flujo principal,
postcondiciones y 180 historias de usuario--- se documenta en el
**Apéndice: Casos de Uso Detallados** al final de este documento.

## Módulos Principales del Sistema

  --------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  API Gateway                 Autenticación OAuth2, Rate Limiting, versionado APIs REST/GraphQL, logging consumo
  Data Ingestion & ETL        Ingesta proveedores, validación Great Expectations, transformación dbt, carga incremental a DW. **BD transaccional:** PocketBase con escalado horizontal planificado según crecimiento de tenants.
  Data Warehouse & BI         Almacenamiento columnar (MonetDB), catálogo datos, dashboards PowerBI, dashboards embebidos clientes
  ML Pipeline                 Entrenamiento, registro (MLflow), feature store (Feast), explainability (SHAP), despliegue, monitoreo drift, A/B testing
  Developer Portal            Documentación interactiva (Mintlify), Sandbox, generación SDKs, gestión API Keys, changelog, reporte bugs
  Billing & Subscriptions     Planes (Freemium, Pro, Enterprise), facturación por uso, pasarela pago
  Observability & Alerting    Logs (Loki), métricas (Prometheus), trazas (Tempo), dashboards (Grafana), alertas PagerDuty/Slack
  Compliance & Security Hub   Escaneo SAST/DAST, secretos, auditoría IAM, registros acceso, reportes cumplimiento, residencia datos
  --------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Módulos principales del ecosistema SkyAnalytics

### Stack Tecnológico por Módulo

  --------------------------- ---------------------------------------------------------------------- -----------------------------------------------------------------------------------------
  API Gateway                 Kong / AWS API GW, OAuth2, JWT, OpenAPI 3.1, Spectral linter           ML Pipeline (predicciones), Data WH (consultas), Billing (planes), Observability (logs)
  Data Ingestion & ETL        Apache Airflow, dbt, Great Expectations, SFTP/S3, PocketBase           Data WH (salida), Observability (logs de DAGs), ML Pipeline (features)
  Data Warehouse & BI         MonetDB (columnar), dbt, PowerBI, catálogo de datos                    API Gateway (servicio datos), Compliance Hub (auditoría de acceso)
  ML Pipeline                 MLflow, Feast (feature store), SHAP, XGBoost, LightGBM, Evidently AI   Data WH (features), API Gateway (predicciones), Observability (métricas de drift)
  Developer Portal            Mintlify, OpenAPI Generator, Sandbox, GitHub Actions                   API Gateway (specs), Observability (estado sandbox)
  Billing & Subscriptions     Stripe / Paddle, PocketBase (tenants), plan engine                     API Gateway (cuotas por plan), Observability (consumo)
  Observability & Alerting    Prometheus, Loki, Tempo, Grafana, PagerDuty, Slack                     Todos los módulos (consumidor de métricas, logs y trazas)
  Compliance & Security Hub   HashiCorp Vault, SonarQube, OWASP ZAP, Dependabot, AWS IAM             CI/CD (pipeline de seguridad), Observability (registros de acceso)
  --------------------------- ---------------------------------------------------------------------- -----------------------------------------------------------------------------------------

  : Stack tecnológico completo por módulo del ecosistema SkyAnalytics

### Diagrama de Dependencias entre Módulos

La siguiente tabla describe las relaciones de dependencia directa entre
módulos. Una dependencia indica que el módulo origen consume servicios,
datos o eventos del módulo destino para su funcionamiento.

  ---------------------- ------------------------ ----------------------------------------------------------
  API Gateway            ML Pipeline              Solicita predicciones en tiempo real (REST)
  API Gateway            Data WH & BI             Consulta datos históricos de vuelos y KPIs
  API Gateway            Billing                  Valida plan activo y cuotas por tenant
  Data Ingestion & ETL   Data WH & BI             Carga transformada incremental al DW
  Data Ingestion & ETL   ML Pipeline              Provee features al feature store (Feast)
  ML Pipeline            Data WH & BI             Lee features históricas y escribe predicciones
  Developer Portal       API Gateway              Consume specs OpenAPI para documentación
  Compliance Hub         CI/CD (GitHub Actions)   Integra SAST/DAST en cada Pull Request
  Observability          Todos los módulos        Recolecta métricas, logs y trazas (consumidor universal)
  Billing                API Gateway              Aplica límites de rate per plan en tiempo real
  ---------------------- ------------------------ ----------------------------------------------------------

  : Dependencias directas entre módulos del ecosistema SkyAnalytics

## Plan de Acción Estratégico

El Plan de Acción detalla las iniciativas concretas requeridas para
ejecutar la estrategia en tres fases. Cada acción incluye dependencias,
responsable y un KPI de éxito medible. Las acciones se organizan por
fase del roadmap: MVP (2026), Growth (2027) y Scale (2028).

  **\#**   **Acción**                                                         **Plazo**     **Dep.**   **Responsable**                    **KPI de Éxito**
  -------- ------------------------------------------------------------------ ------------- ---------- ---------------------------------- ------------------------------------------------------------------------------
                                                                                                                                          
  **\#**   **Acción**                                                         **Plazo**     **Dep.**   **Responsable**                    **KPI de Éxito**
                                                                                                                                          
           Publicar API Beta en RapidAPI                                      Q3 2026       ---        CTO, Developer Advocate            Listing activo con $\ge$ 3 endpoints funcionales
           Automatizar flujos HubSpot para captación                          Q3 2026       ---        VP Marketing                       $\ge$ 200 registros calificados
           Desplegar infra K8s con Terraform (IaC)                            Q3 2026       ---        SRE Lead                            % de recursos cloud versionados en Git
           Construir pipeline ETL con Great Expectations + dbt                Q3--Q4 2026              Data Engineer Lead                 Datos en staging con $\le$ 5 min de lag
           Implementar stack de observabilidad (LGTM)                         Q4 2026                  SRE Lead                           Dashboards operativos + alertas PagerDuty funcionales
           Desarrollar modelo de predicción de retrasos v1                    Q4 2026                  ML Engineer Lead                   MAPE $\le$ 15 % en datos de prueba
           Lanzar Developer Portal + Sandbox                                  Q4 2026                  Developer Advocate                 Desarrollador externo puede hacer primera API call en $\le$ 3 min
           Establecer fundación legal (ToS, DPA, ruta SOC 2)                  Q4 2026       ---        CEO, CTO                           ToS + Privacy + DPA publicados y revisados por abogados
           Configurar autenticación OAuth2 + API Keys                         Q4 2026       , 3        CTO, SRE                           Flujo client_credentials + API Key generación $<$ 30s
           Implementar rate limiting por plan                                 Q4 2026       , 3        SRE Lead                           Rate limits funcionales con headers X-RateLimit-Remaining
           Lanzar plan Freemium con registro self-service                     Q4 2026       , 2, 9     VP Marketing, Developer Advocate   Primeros 50 Beta Testers onboardeados
           Configurar CI/CD con GitHub Actions                                Q3 2026                  SRE Lead                           Pipeline funcional: test $\rightarrow$ build $\rightarrow$ deploy automático
                                                                                                                                          
           Ejecutar pruebas de carga (k6) y chaos engineering                 Q1 2027       , 5        SRE Lead                           Latencia p95 $\le$ 500ms con 10K usuarios concurrentes
           Validar estrategia de pricing con A/B testing                      Q1--Q2 2027              VP Marketing, CEO                  --3 variantes testadas, pricing final definido
           Publicar 3 artículos técnicos + 2 conferencias                     Q1--Q2 2027              CTO, Developer Advocate            $\ge$ 3 artículos en blog + $\ge$ 2 charlas aceptadas
           Implementar MLOps pipeline completo (Feast, SHAP)                  Q1--Q2 2027              ML Engineer Lead                   Feature store operativa + explainability en predicciones
           Optimizar PocketBase para alta concurrencia                        Q2 2027                  CTO, DataEng                       PocketBase optimizado para 1.000+ tenants simultáneos
           Implementar monitoring de costos cloud                             Q2 2027                  SRE Lead                           Dashboard de costos + alertas de anomalía
           Lanzar SDKs auto-generados (Python, JS, Java)                      Q2 2027                  Developer Advocate                 SDKs publicados en npm, PyPI, Maven Central
           Implementar data contracts con validación automática               Q2--Q3 2027              Data Engineer Lead                  % de fuentes con contrato definido y validado
           Iniciar programa SOC 2 Tipo II (monitoreo de controles)            Q3 2027                  CEO, CTO                           Evidencias de controles recolectadas por 6+ meses
           Implementar pipeline SAST/DAST en CI/CD                            Q3 2027                  SRE Lead                           vulnerabilidades críticas en producción
           Lanzar dashboards self-service para clientes                       Q3 2027       , 17       Data Engineer Lead                 Clientes Enterprise pueden ver sus propios dashboards
           Implementar NPS trimestral automatizado + feedback loop            Q3 2027                  VP Customer Success                $\ge$ 30 % tasa de respuesta en encuestas
           Explorar técnicas de Deep Learning (OCR, NLP avanzado)             Q3--Q4 2027   , 16       ML Engineer Lead                   $\ge$ 2 experimentos documentados en MLflow
                                                                                                                                          
           Desplegar infraestructura multi-región activo-activo               Q1 2028       , 17       SRE Lead                           Uptime $\ge$ 99.99 % con failover automático
           Implementar Speech-to-Text para feedback cualitativo               Q1--Q2 2028              ML Engineer Lead                   WER $\le$ 10 % en transcripciones de entrevistas
           Obtener certificación SOC 2 Tipo II                                Q2 2028       , 22       CEO, CTO                           Informe SOC 2 Tipo II emitido por auditor externo
           Lanzar marketplace de integraciones                                Q2 2028       , 19       Developer Advocate, CTO            $\ge$ 5 integraciones listadas por terceros
           Iniciar roadmap ISO 27001                                          Q3 2028                  CTO, SRE                           Gap analysis completado + plan de remediación
           Implementar auto-scaling predictivo con ML                         Q3 2028       , 18       ML Engineer, SRE                   incidentes por saturación de capacidad
           Expandir cobertura de datos a sustentabilidad (emisiones CO$_2$)   Q4 2028       , 20       Data Engineer, CEO                 Métricas de carbono por ruta disponibles vía API

  : Plan de Acción Estratégico con 32 iniciativas distribuidas en 3
  fases

# Análisis Estratégico y de Mercado

## Análisis FODA (SWOT)

El análisis FODA sintetiza las condiciones internas y externas que
enmarcan la estrategia de SkyAnalytics. Sirve como base para la
priorización de iniciativas y la gestión de riesgos.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **F1.** Stack tecnológico moderno y cloud-native: K8s, Terraform, MLflow, Feast, SHAP. Infraestructura 100 % como código desde el día 1.                                                                          **D1.** Equipo inicial reducido (fundadores + contratistas) con riesgo de desgaste en fases de alto crecimiento.
  **F2.** Modelo de negocio SaaS recurrente con margen bruto proyectado $>$ 75 % y baja dependencia de CAPEX inicial.                                                                                               **D2.** Dependencia de un número limitado de proveedores de datos aeronáuticos; cualquier cambio de condiciones contractuales impacta la operación.
  **F3.** Enfoque en explainability (SHAP) y transparencia de modelos, diferenciador clave frente a competidores que operan como cajas negras.                                                                      **D3.** Marca desconocida en un mercado dominado por jugadores establecidos (OAG, Cirium, FlightAware) con relaciones comerciales de décadas.
  **F4.** Cultura Remote-First desde el origen, permitiendo contratar talento global sin restricciones geográficas y con costos competitivos.                                                                       **D4.** PocketBase como base transaccional MVP limita la escalabilidad; requiere optimización para soportar crecimiento de tenants.
  **F5.** Arquitectura orientada a ecosistema (APIs, SDKs, marketplace) que habilita adopción orgánica y efectos de red entre desarrolladores.                                                                      **D5.** Sin certificaciones de seguridad vigentes (SOC 2, ISO 27001) en el lanzamiento, lo cual puede ser bloqueante para clientes Enterprise.
  **F6.** Pipeline de ML maduro con MLOps completo, feature store, A/B testing y monitoreo de drift --- capacidades que los competidores legacy no tienen.                                                          **D6.** Ausencia de datos propios; la propuesta de valor depende de la calidad y disponibilidad de datos de terceros.
                                                                                                                                                                                                                    
  **O1.** Mercado global de aviation analytics en crecimiento: se proyecta USD 4.3B en 2024 a USD 7.8B en 2030 (CAGR 10.3 %). Demanda impulsada por digitalización post-COVID y presión por eficiencia operativa.   **A1.** Competidores establecidos (FlightAware, FlightGlobal, OAG, Cirium) con más recursos, datos propios y relaciones comerciales consolidadas pueden replicar funcionalidades de ML.
  **O2.** Vacío de mercado en el segmento mid-market: aerolíneas regionales, agencias de viaje medianas y operadores logísticos sin acceso a herramientas avanzadas de predictive analytics.                        **A2.** Cambios regulatorios en protección de datos aeronáuticos (IATA, ICAO, GDPR) pueden imponer restricciones sobre el uso y la distribución de datos de vuelo.
  **O3.** Adopción acelerada de APIs como modelo de consumo B2B; las aerolíneas modernizan sus stacks y buscan integraciones vía API en lugar de reportes estáticos.                                                **A3.** Proveedores de datos aeronáuticos pueden lanzar sus propias plataformas de analytics compitiendo directamente, eliminando el intermediario.
  **O4.** Regulaciones de sostenibilidad (CORSIA, EU ETS) que exigen a las aerolíneas reportar y optimizar emisiones; SkyAnalytics puede incorporar métricas de carbono por ruta.                                   **A4.** Concentración de clientes: si los primeros 3--5 clientes Enterprise concentran $>$ 50 % del ARR, la pérdida de uno solo impacta severamente la viabilidad financiera.
  **O5.** Crecimiento del ecosistema de marketplaces de APIs (RapidAPI, AWS Marketplace, Google Cloud Marketplace) que reducen el costo de distribución y adquisición de clientes.                                  **A5.** Avance de modelos LLM generalistas (GPT, Claude, Gemini) que podrían ofrecer predicciones de vuelo básicas como commodity, erosionando la diferenciación técnica si no se profundiza en el dominio.
  **O6.** Alianzas estratégicas con aerolíneas como design partners para co-desarrollar el producto, generando credibilidad y referencias en la industria.                                                          **A6.** Riesgo cambiario y de jurisdicción al operar con clientes y equipo en múltiples países; exposición a fluctuaciones de divisas y complejidad legal.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Matriz FODA de SkyAnalytics Inc.

## Análisis de Mercado

### Tamaño del Mercado (TAM / SAM / SOM)

El mercado global de aviation analytics se estima en USD 4.3 mil
millones en 2024, con proyección de alcanzar USD 7.8 mil millones en
2030 (CAGR 10.3 %). SkyAnalytics se posiciona en la intersección de
aviation data, predictive analytics y plataformas API-first.

  --------- ------------------------------------------------------------------------------------------------------------------ ----------------- -------------------------------------------------------------------------------------------------------------------
  **TAM**   Mercado global de datos y analytics de aviación (software, servicios, consultoría)                                 USD 7.8B          Todas las aerolíneas, aeropuertos, agencias de viaje, operadores logísticos y entes reguladores a nivel global
  **SAM**   Plataformas SaaS de predictive analytics aeronáutico (API-first, modelos ML) para aerolíneas y agencias de viaje   USD 2.1B          Aerolíneas comerciales (Top 200 globales) + Top 500 agencias de viaje y operadores logísticos
  **SOM**   Mercado alcanzable por SkyAnalytics en 5 años con estrategia de penetración orgánica (SEO, APIs, marketplace)      USD 35--50M ARR   Captura de 2--3 % del SAM. Meta aspiracional: 500 clientes activos, ARR promedio \$70--100K por cuenta Enterprise
  --------- ------------------------------------------------------------------------------------------------------------------ ----------------- -------------------------------------------------------------------------------------------------------------------

  : Estimación TAM / SAM / SOM para SkyAnalytics

### Segmentos de Clientes Objetivo

::: tabularx
\>

p2.5cm \>

p3cm \>

p2.2cm \>

p2.2cm X

& & & &\
Aerolíneas Enterprise (Top 50) & Flotas $>$ 100 aeronaves, múltiples
hubs, equipos de datos internos & Predicción de retrasos, optimización
de rutas, dashboards ejecutivos, SLA 99.99 % & Enterprise (USD
5K--20K/mes) & Venta directa con CTO/VP Operations, prueba de concepto
con datos propios, referencias\
Aerolíneas Regionales & Flotas 20--100 aeronaves, 1--2 hubs, equipos
técnicos reducidos & Predicción de retrasos, monitoreo de clima en
rutas, API simple & Pro (USD 500--2K/mes) & Inbound vía contenido
técnico, marketplace RapidAPI, webinars sectoriales\
Agencias de Viaje & B2B/B2C, alto volumen de consultas de vuelos,
necesitan datos en tiempo real & Consulta de disponibilidad, precios y
retrasos vía API para integrar en sus propios sistemas & Pro / API-Only
(basado en volumen) & Documentación de integración excepcional, SDKs,
sandbox instantáneo\
Operadores Logísticos & Carga aérea, cadena de frío, time-critical
shipments & Predicción de retrasos en rutas de carga, optimización de
conexiones & Enterprise / Pro & Casos de uso de ROI cuantificable,
integración con TMS existentes\
Entes Gubernamentales & Autoridades de aviación civil, reguladores de
transporte & Monitoreo de puntualidad de la industria, reportes de
cumplimiento, dashboards sectoriales & Enterprise & Licitaciones,
alianzas con consultoras del sector público\
:::

## Mapa Competitivo

SkyAnalytics compite en el espacio de aviation data intelligence,
diferenciándose por su enfoque API-first, explainability de modelos ML y
cultura Remote-First que permite una estructura de costos más eficiente.

  ---------------------------------- ----------------------------------------- --------------- ------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------
  FlightAware                        Tracking en tiempo real, APIs             \$500--5K/mes   Cobertura global, datos propios, marca consolidada                        APIs legacy (SOAP/XML), sin modelos ML avanzados, explainability nula                            Modelos ML con SHAP, APIs REST/GraphQL modernas, SDKs auto-generados
  FlightGlobal / FlightStats         Datos históricos + analytics              \$1K--10K/mes   Datos históricos extensos (10+ años), relaciones con aerolíneas           Plataforma legacy, UX pobre, integración compleja                                                Dashboards self-service, sandbox instantáneo, TTFV $\leq$ 3 min
  OAG                                Datos de horarios, analytics enterprise   \$2K--15K/mes   Base de datos de horarios más completa del mundo, estándar de industria   Foco en horarios no en predicción, costo prohibitivo para mid-market                             Predicción de retrasos en tiempo real, pricing accesible para aerolíneas regionales
  Cirium (RELX)                      Analytics enterprise, data as a service   \$5K--25K/mes   Respaldo de RELX, datos de flota, integración con banca de inversión      Mercado primario: finanzas, no operaciones. Sin self-service real. Precio extremadamente alto.   Self-service, APIs para desarrolladores, cultura DevRel
  Xweather (anterior AerisWeather)   Datos meteorológicos para aviación        \$200--2K/mes   Meteorología especializada, buenas APIs                                   Solo clima, sin predicción integrada de retrasos ni analytics de vuelo                           Predicción integrada clima + retrasos en un solo endpoint
  ---------------------------------- ----------------------------------------- --------------- ------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------

  : Mapa competitivo de SkyAnalytics vs principales actores del mercado

**Ventaja Competitiva Principal:** SkyAnalytics es el único competidor
que combina APIs modernas (REST/GraphQL), modelos ML con explainability
(SHAP), dashboards self-service y una cultura Remote-First que se
traduce en precios 30--50 % menores que los incumbentes. La ausencia de
sistemas legacy permite iterar 3--5 veces más rápido en features de
producto.

## Modelo de Revenue

### Planes de Suscripción

SkyAnalytics adopta un modelo SaaS con planes escalonados por volumen de
consumo y funcionalidades. La facturación es mensual con descuento por
pago anual. El modelo está diseñado para que los clientes crezcan
orgánicamente de un plan a otro conforme aumenta su dependencia de la
plataforma.

  ---------------- ----------------------------------------------- -------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------
  **Freemium**     \$0/mes                                         API calls/mes, 1 tenant, datos sintéticos en sandbox                 Acceso a 3 endpoints básicos, documentación, sandbox                                                              Comunidad (foro), documentación, sin SLA
  **Pro**          \$500/mes (facturación mensual) o \$5.000/año   API calls/mes, 5 endpoints, 3 usuarios, 1 tenant                     APIs REST + GraphQL, dashboards predefinidos, exportación CSV, webhooks                                           Email en 8h hábiles, SLA 99.9 %
  **Enterprise**   \$2.000--\$20.000/mes (según volumen)           API calls ilimitadas (fair use), usuarios ilimitados, multi-tenant   Todo Pro + dashboards custom, datos reales, SDKs prioritarios, feature store compartido, A/B testing de modelos   Slack compartido, SLA 99.99 %, gerente de cuenta dedicado
  **API-Only**     \$0.01--\$0.05 por API call                     Volumen variable, pago por uso                                       Acceso a todos los endpoints vía API, sin dashboards ni UI                                                        Email en 24h, SLA 99.9 %
  ---------------- ----------------------------------------------- -------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------

  : Planes de suscripción de SkyAnalytics

### Estrategia de Pricing

- **Penetración inicial (2026--2027):** Freemium generoso + Pro a precio
  por debajo del mercado para construir base de usuarios y referencias.

- **Expansión (2027--2028):** Ajuste de pricing validado con A/B testing
  y entrevistas de willingness-to-pay. Introducción de add-ons (más
  endpoints, feature store, entrenamiento custom).

- **Madurez (2028+):** Precios alineados al valor entregado (value-based
  pricing). Descuentos por volumen y contratos anuales. Revenue
  expansion vía upselling de Pro a Enterprise.

## Registro de Riesgos

La gestión de riesgos es un componente esencial del gobierno corporativo
de SkyAnalytics. Cada riesgo identificado se evalúa en probabilidad e
impacto (escala 1--5), y se define una estrategia de mitigación con
responsable asignado.

  ----- ------------------------------------------------------------------------------------- ------- -- -- ------------------------------------------------------------------------------------------------------------------ --------------------
  R01   Proveedor de datos interrumpe el servicio o modifica condiciones                      Media         Contratos con 2+ proveedores alternativos, cláusula de continuidad, caché de datos históricos                      CTO
  R02   Vulnerabilidad de seguridad crítica en producción                                     Baja          SAST/DAST en CI/CD, parches $\leq$ 24h, WAF, Zero Trust, auditorías trimestrales                                   SRE Lead
  R03   Salida de CTO o ML Engineer Lead (key person risk)                                    Media         Documentación exhaustiva (ADRs, runbooks, wiki), bus factor $\geq$ 2 en cada área, plan de sucesión                CEO
  R04   No alcanzar product-market fit en 18 meses                                            Media         Ciclo continuo de feedback, métricas de engagement, pivot temprano si los KPIs de adopción no se alcanzan          CEO
  R05   Competidor grande lanza producto similar con pricing predatorio                       Alta          Diferenciación en explainability y DevRel, nicho mid-market desatendido, switching cost vía integración profunda   CEO
  R06   Ingesta de datos supera capacidad del pipeline y genera lag                           Media         Auto-scaling de workers ETL, alertas de lag, arquitectura de streaming para fuentes críticas                       Data Engineer Lead
  R07   Modelo ML degrada (drift) y entrega predicciones erróneas sin ser detectado           Media         Monitoreo PSI diario, A/B testing en staging, rollback automático, alertas                                         ML Engineer Lead
  R08   Costos cloud superan el presupuesto por error de configuración o ataque               Baja          Alertas de anomalía de gasto diario, budget caps por cuenta, revisión semanal                                      SRE Lead
  R09   Cambio regulatorio restringe el uso de datos aeronáuticos en ciertas jurisdicciones   Baja          Monitoreo regulatorio proactivo, residencia de datos configurable por región, asesoría legal continua              CEO
  R10   Incidente Sev1 no resuelto en $\leq$ 15 minutos por falta de cobertura on-call        Baja          Rotación on-call 24/7, runbooks actualizados, escalation automática, post-mortem obligatorio                       SRE Lead
  R11   Cliente Enterprise concentra $>$ 40 % del ARR                                         Media         Diversificación activa de cartera, límite interno de concentración por cliente, expansión del pipeline de ventas   VP Ventas
  R12   Falla en backup o restore durante un incidente real de pérdida de datos               Baja          Backup diario encriptado + restore semanal verificado, alerta de integridad de backup, DR multi-región             SRE Lead
  ----- ------------------------------------------------------------------------------------- ------- -- -- ------------------------------------------------------------------------------------------------------------------ --------------------

  : Registro de riesgos con probabilidad, impacto, score, mitigación y
  responsable

## Proyección Financiera 3 Años

La proyección financiera presenta un escenario base asumiendo ejecución
exitosa del plan de acción. Las cifras son estimaciones para fines de
planificación estratégica y no constituyen compromisos financieros
vinculantes.

  --------------------- ------------------------------ ---------------------- -------------------- ----------------------------------------------------------- -----------------------------------------------------
  Clientes activos      (Beta)                         -- 200                 \+                   Crecimiento compuesto vía marketing + marketplace           Beta testers no generan revenue en 2026
  ARR                   \$0 (pre-revenue)              \$100K -- \$200K       \$1.5M -- \$3M       ARR = clientes $\times$ ARPU. ARPU crece de \$500 a \$5K+   Primeros pagos estimados Q1 2027
  Costo Cloud Mensual   \$2K -- \$5K                   \$8K -- \$15K          \$25K -- \$50K       Escala con volumen de datos y tráfico API                   Mayor driver: K8s nodos + DB columnar + egress
  Costo Personas        Variable (equipo inicial)      --12 personas          --30 personas        Remote-First contractors + full-time hires                  Principal partida de costo operativo
  Gross Margin          No aplica                       % -- 75 %             $>$ 75 %             (ARR - costo cloud) / ARR                                   Mejora con optimización cloud y economías de escala
  Runway                -- 24 meses (fondeo inicial)   Break-even o Serie A   Rentable o Serie B   Cash flow: ingresos - egresos operativos                    Hito: alcanzar break-even mensual en Q3 2027
  LTV                   No aplica                      \$5K -- \$15K          \$20K -- \$60K       ARPU $\times$ vida media del cliente en meses               Crece con upselling y reducción de churn
  CAC                   No aplica                      \$300 -- \$500         \$200 -- \$400       Gasto marketing + ventas / clientes nuevos                  Decrece con inbound orgánico y referidos
  LTV/CAC               No aplica                      $>$ 3x                 $>$ 5x               LTV / CAC                                                   Indicador de eficiencia comercial
  --------------------- ------------------------------ ---------------------- -------------------- ----------------------------------------------------------- -----------------------------------------------------

  : Proyección financiera estimada a 3 años (escenario base)

# Visión Arquitectónica y Analítica

## Resumen Analítico por Nivel Organizacional

  **Nivel**     **Decisión**              **Técnicas**                    **Casos de Uso**   **Resultado**
  ------------- ------------------------- ------------------------------- ------------------ ---------------------------------------
  Estratégico   Gerencial (largo plazo)   BI, ML, simulación              CU-E01 a E06       Visibilidad 360°, alineación de metas
  Táctico       Planeación por área       Forecasting, optimización       CU-T01 a T10       Eficiencia, control de costos
  Operativo     Ejecución diaria          Reglas, validaciones, alertas   CU-O01 a O20       Confiabilidad, ejecución de pipelines

  : Resumen analítico integrado por nivel organizacional

## Modelo Analítico General del Sistema

  **APIs + Dev Portal**                      $\rightarrow$  **BD Transaccional**                         $\rightarrow$  **ETL + Validación**                $\rightarrow$  **Data Warehouse**                  $\rightarrow$  **BI + ML Pipeline**            $\rightarrow$  **Reportes**
  ----------------------------------------- --------------- ------------------------------------------- --------------- ---------------------------------- --------------- ---------------------------------- --------------- ------------------------------ --------------- -----------------------------------
  REST/GraphQL, OAuth2, Rate Limits, SDKs                   PocketBase, registro tenants, consumo API                   Great Expectations, dbt, Airflow                   MonetDB columnar, catálogo datos                   PowerBI, MLflow, Feast, SHAP                   Dashboards, predicciones, alertas

  : Flujo de datos y componentes del ecosistema SkyAnalytics

## Tablas de Hechos Principales (Fact)

  ------------------- ---------------------------- ------------------------------------------------
  Fact_API_Call       Consumo API por cliente      Total llamadas, latencia, errores, banda
  Fact_Vuelo          Datos de vuelos procesados   Vuelos registrados, puntualidad, cancelaciones
  Fact_Retraso        Predicciones de retraso      Retraso predicho vs real, MAPE, precisión
  Fact_Suscripcion    Ingresos recurrentes         ARR, MRR, expansión, downgrades, churn
  Fact_Ingesta_ETL    Ejecución pipelines          Volumen ingerido, tiempo ejecución, errores
  Fact_Modelo_ML      Desempeño modelos ML         Precisión, recall, drift, tiempo entrenamiento
  Fact_Satisfaccion   Encuestas clientes           NPS, CSAT, comentarios, recomendación
  Fact_Incidente      Incidentes operativos        Tiempo detección, MTTR, severidad
  ------------------- ---------------------------- ------------------------------------------------

  : Tablas de hechos principales del Data Warehouse

## Dimensiones Principales (Dim)

  ---------------- ------------------------------------------------------
  Dim_Tiempo       Día, semana, mes, trimestre, año
  Dim_Aerolinea    Código IATA/ICAO, país, alianza, tipo
  Dim_Aeropuerto   Código IATA/ICAO, ciudad, país, región, zona horaria
  Dim_Ruta         Origen-destino, distancia, tipo ruta
  Dim_Cliente      Empresa B2B, plan, industria, región
  Dim_Plan         Tipo suscripción, límites API, features, precio
  Dim_Endpoint     Endpoint API, versión, método, módulo
  Dim_Empleado     Rol, equipo, seniority, ubicación
  ---------------- ------------------------------------------------------

  : Dimensiones principales del modelo de datos

## Técnicas Usadas por Nivel Organizacional

### Nivel Estratégico

  -------------------------- ------------------------------------------------------------------------
  BI y agregaciones          Consolidar KPIs en dashboards ejecutivos con comparativas históricas
  ML predictivo              Proyectar ARR, churn y demanda de API con modelos de series temporales
  Detección de anomalías     Identificar desviaciones en revenue, uptime y satisfacción
  Segmentación de clientes   Clasificar cuentas por valor, riesgo y potencial de expansión
  Recomendación              Sugerir planes y endpoints a clientes según su perfil de consumo
  Dashboards BSC             Visualizar semáforos y tendencias de todos los KPIs estratégicos
  -------------------------- ------------------------------------------------------------------------

  : Técnicas analíticas del nivel estratégico

### Nivel Táctico

  -------------------------- ------------------------------------------------------------------
  Agregaciones por área      Reportes de consumo API por endpoint, costos cloud por servicio
  Forecasting                Prever picos de tráfico, necesidades de capacidad y presupuesto
  Alertas inteligentes       Disparar notificaciones ante brechas de SLA, calidad o seguridad
  Optimización de recursos   Identificar recursos cloud ociosos y redimensionar instancias
  Análisis de campañas       Medir conversión, ROI y segmentación de campañas de growth
  -------------------------- ------------------------------------------------------------------

  : Técnicas analíticas del nivel táctico

### Nivel Operativo

  -------------------------- ----------------------------------------------------------------------
  Reglas de negocio          Validar rate limits, permisos de plan, autenticación OAuth2
  Validaciones automáticas   Ejecutar suites de Great Expectations tras cada ingesta
  Alertas operativas         Notificar fallos de pipeline, saturación de pods, errores 500
  Recomendaciones simples    Sugerir endpoints relacionados según historial de consumo
  NLP para chatbot           Clasificar tickets, buscar FAQs semánticamente, detectar sentimiento
  -------------------------- ----------------------------------------------------------------------

  : Técnicas analíticas del nivel operativo

## Matriz de Casos de Uso Estratégicos

  ------------------- ------------------------------------- ------------------------------------ ----------------------------
  CU-E01 BSC          BI, agregaciones, semáforos, ML       Consultar sección Tablas de Hechos   Dashboard BSC
  CU-E02 ARR          Agregaciones financieras, anomalías   Consultar sección Tablas de Hechos   Reporte rentabilidad
  CU-E03 Uptime       Agregaciones, MTTR, error budget      Consultar sección Tablas de Hechos   Dashboard SLA/SLO
  CU-E04 Compliance   Agregaciones documentales             Consultar sección Tablas de Hechos   Reporte cumplimiento
  CU-E05 Metas        Simulación, predicción escenarios     Consultar sección Tablas de Hechos   Reporte metas trimestrales
  CU-E06 Talento      Agregaciones, retención               Consultar sección Tablas de Hechos   Dashboard People Analytics
  ------------------- ------------------------------------- ------------------------------------ ----------------------------

  : Matriz de casos de uso estratégicos: técnicas, modelo Fact-Dim y
  reportes

## Matriz de Casos de Uso Tácticos

  ------------------ ----------------------------------- ------------------------------------ --------------------------
  CU-T01 Growth      Segmentación, conversión, scoring   Consultar sección Tablas de Hechos   Reporte campañas
  CU-T02 API         API analytics, monitoreo            Consultar sección Tablas de Hechos   Dashboard uso API
  CU-T03 Infra       Monitoreo tiempo real, alertas      Consultar sección Tablas de Hechos   Dashboard cloud
  CU-T04 ETL         Validación, alertas frescura        Consultar sección Tablas de Hechos   Dashboard calidad
  CU-T05 MLflow      Experimentos, tracking métricas     Consultar sección Tablas de Hechos   Dashboard MLflow
  CU-T06 Security    SAST/DAST, detección vulns          Consultar sección Tablas de Hechos   Reporte vulnerabilidades
  CU-T07 DevPortal   Analíticas tráfico, engagement      Consultar sección Tablas de Hechos   Dashboard portal
  CU-T08 Costos      Análisis costos, anomalías          Consultar sección Tablas de Hechos   Dashboard costos
  CU-T09 Carga       Métricas rendimiento, k6            Consultar sección Tablas de Hechos   Reporte pruebas
  CU-T10 Pricing     A/B testing, WTP                    Consultar sección Tablas de Hechos   Reporte validación
  ------------------ ----------------------------------- ------------------------------------ --------------------------

  : Matriz de casos de uso tácticos: técnicas, modelo Fact-Dim y
  reportes

## Matriz de Casos de Uso Operativos

  ---------------------- --------------------------------------------- ------------------------------------ ------------------------------------------------------
  CU-O01 Registro        Validación duplicados, auto-gen               Consultar sección Tablas de Hechos   API Key, tenant activo
  CU-O02 Consulta        Rate limiting, caching, auth                  Consultar sección Tablas de Hechos   JSON response
  CU-O03 Ingesta         Descarga programada, schema                   Consultar sección Tablas de Hechos   Datos en staging
  CU-O04 Calidad         Great Expectations checks                     Consultar sección Tablas de Hechos   Reporte pass/fail
  CU-O05 Reentrenar      MLflow tracking, comparación                  Consultar sección Tablas de Hechos   Modelo registrado
  CU-O06 Dashboards      Refresh programado, verificación              Consultar sección Tablas de Hechos   Dashboards actualizados
  CU-O07 Telemetría      Recolección métricas, alertas                 Consultar sección Tablas de Hechos   Alertas PagerDuty
  CU-O08 Tickets         Triaging NLP, clasificación                   Consultar sección Tablas de Hechos   Ticket resuelto
  CU-O09 Backup          Backup automático, verificación               Consultar sección Tablas de Hechos   Backup + log restore
  CU-O10 ErrorBudget     Cálculo SLI/SLO, umbrales                     Consultar sección Tablas de Hechos   Decisión congelar/liberar
  CU-O11 Changelog       Generación commits, SemVer                    Consultar sección Tablas de Hechos   Changelog portal
  CU-O12 IAM             Rotación automática, verificación             Consultar sección Tablas de Hechos   Credenciales rotadas
  CU-O13 PostMortem      Documentación, timeline auto                  Consultar sección Tablas de Hechos   Post-mortem + tickets
  CU-O14 FAQ             Clasificación NLP, KB                         Consultar sección Tablas de Hechos   FAQ publicado
  CU-O15 Sprints         Gestión backlog, standups, retrospectivas     Consultar sección Tablas de Hechos   Sprint cerrado con métricas
  CU-O16 OpenAPI         Spectral linter, detección breaking changes   Consultar sección Tablas de Hechos   Spec validada, merge aprobado/bloqueado
  CU-O17 DataContracts   Validación schema, detección drift            Consultar sección Tablas de Hechos   Contrato validado o ingesta pausada
  CU-O18 SAST/DAST       SonarQube + OWASP ZAP, bloqueo críticos       Consultar sección Tablas de Hechos   Reporte de vulnerabilidades por release
  CU-O19 Costos          Análisis anomalías, derechosizing             Consultar sección Tablas de Hechos   Reporte de optimización semanal
  CU-O20 DeepLearning    OCR (CRNN/TrOCR), STT (Whisper), MLflow       Consultar sección Tablas de Hechos   Experimentos documentados con recomendación go/no-go
  ---------------------- --------------------------------------------- ------------------------------------ ------------------------------------------------------

  : Matriz de casos de uso operativos: técnicas, modelo Fact-Dim y
  registros

## Agregaciones Usadas en el Sistema

  ------------------------ -------------------------------------------------------------- -------------------------
  Total API Calls          SUM(llamadas) GROUP BY día, endpoint, cliente                  Facturación, dashboards
  Latencia p95             PERCENTILE(latencia, 0.95) GROUP BY endpoint, hora             Monitoreo SLA
  ARR                      SUM(mrr) WHERE activo $\times$ 12                              Reporte financiero
  Churn Rate               COUNT(cancelados) / COUNT(total) $\times$ 100                  Retención
  NRR                      (ARR inicial + expansión - churn) / ARR inicial $\times$ 100   Crecimiento orgánico
  NPS                      (% promotores - % detractores) $\times$ 100                    Satisfacción
  MAPE                     AVG(ABS(real - predicho) / real) $\times$ 100                  Evaluación ML
  Data Freshness           COUNT(datos \< 5 min) / COUNT(total) $\times$ 100              Calidad datos
  Uptime Real              (tiempo total - caído) / tiempo total $\times$ 100             SLA compliance
  Error Budget Consumido   SUM(tiempo caído mensual) / 4.38 min $\times$ 100              Gestión riesgo
  Tasa Errores API         COUNT(5xx) / COUNT(total) $\times$ 100                         Confiabilidad
  TTFV Promedio            AVG(timestamp_primer_insight - timestamp_registro)             Onboarding
  ------------------------ -------------------------------------------------------------- -------------------------

  : Agregaciones utilizadas en el sistema SkyAnalytics

## Técnicas de IA y Machine Learning Aplicables

### Segmentación de Clientes

Clustering (K-Means, DBSCAN) para agrupar aerolíneas por patrón de
consumo; RFM para clasificar por recencia, frecuencia y monto; Árboles
de decisión para identificar probabilidad de expansión. Entrada:
historial de API calls, plan, industria. Salida: segmento (high-value,
growth, at-risk).

### Predicción de Retrasos de Vuelo

XGBoost/LightGBM con features: aerolínea, aeropuerto, hora,
meteorología, historial de ruta, tráfico del sector, temporada. Salida:
probabilidad y magnitud de retraso, clasificación de severidad, ventana
óptima de salida.

### Predicción de Demanda de API

Prophet / ARIMA / LSTM para prever picos de tráfico por endpoint con
ventanas de 15 minutos, permitiendo auto-scaling proactivo y
dimensionamiento de capacidad.

### Detección de Anomalías

  -------------------------- -------------------------------------------------------
  Errores 500 aumentan       Bug en código, saturación de DB, ataque DDoS
  Consumo API cae            Migración a competidor, fallo de autenticación OAuth2
  Precisión ML degrada       Data drift, feature no disponible en fuente
  Volumen datos anómalo      Error del proveedor, duplicación en ingesta
  Tickets soporte aumentan   Bug no detectado, cambio de API sin documentación
  -------------------------- -------------------------------------------------------

  : Anomalías operativas y sus posibles causas

### NLP para Chatbot de Soporte

Clasificación de tickets para asignar categoría y prioridad
automáticamente; búsqueda semántica con embeddings de documentación;
generación de FAQs agrupando tickets similares; análisis de sentimiento
para detectar clientes frustrados y escalar a un agente humano.

### Recomendación de Endpoints y Planes

Filtrado colaborativo combinado con content-based filtering. Entrada:
historial de API, industria, tamaño de flota. Salida: endpoints
sugeridos y plan recomendado según perfil de consumo.

## Técnicas de Deep Learning Aplicables

  --------------------------------- ---------------------------------------------------------------------------- ----------------
  OCR con redes neuronales          Procesar documentos de compliance, facturas de proveedores                   CU-E04
  Análisis de sentimiento           Interpretar comentarios de encuestas NPS y tickets de soporte                CU-O08, CU-O13
  Clasificación de imágenes         Verificar evidencias de auditoría (screenshots, logs escaneados)             CU-E04
  Detección de anomalías visuales   Monitorear dashboards de Grafana para detectar patrones anómalos             CU-T03
  Speech-to-Text                    Transcribir entrevistas de feedback con clientes para análisis cualitativo   CU-O20
  --------------------------------- ---------------------------------------------------------------------------- ----------------

  : Técnicas de Deep Learning aplicables al ecosistema SkyAnalytics

## Relación entre Registros Operativos y Reportes Gerenciales

:::: center
::: minipage
**Registro Operativo** (API call / Pipeline ETL / Encuesta / Incidente)
$\rightarrow$ **Agregación** (API calls por endpoint, satisfacción
promedio, uptime mensual) $\rightarrow$ **Modelo Fact-Dim**
(Fact_API_Call + Dim_Tiempo + Dim_Cliente + Dim_Endpoint) $\rightarrow$
**Reporte Táctico o Estratégico** (rentabilidad, uptime, fidelización,
calidad de datos) $\rightarrow$ **Decisión** (promoción de plan,
optimización de infraestructura, capacitación, mejora de proceso)
:::
::::

## Ejemplo Completo de Trazabilidad

::: description
OE5 --- Innovación en IA Aeronáutica.

OT9 --- Entrenar modelos ML con MLflow, Feast, SHAP y A/B testing.

OP5 --- Reentrenar modelos con datos frescos, verificar drift.

Estratégico CU-E01 (consultar BSC con KPIs de IA), Táctico CU-T05
(entrenar modelos), Operativo CU-O05 (reentrenar modelo).

Fact_Modelo_ML, Fact_Retraso, Fact_Vuelo + Dim_Tiempo, Dim_Aerolinea,
Dim_Ruta.

MAPE
($\text{AVG}(\lvert\text{real} - \text{predicho}\rvert / \text{real}) \times 100$),
Precisión por ruta, Drift detection rate, Tiempo de entrenamiento,
Experimentos A/B por trimestre.

XGBoost/LightGBM, SHAP explainability, MLflow tracking, Feast feature
store, A/B testing framework, PSI drift monitoring.

Datos de vuelo (Fact_Vuelo) $\rightarrow$ Features en Feast
$\rightarrow$ Entrenamiento en MLflow $\rightarrow$ Predicciones
(Fact_Retraso) $\rightarrow$ Métricas (Fact_Modelo_ML) $\rightarrow$
Dashboard BSC $\rightarrow$ Decisión de mejora del modelo.
:::

## Hoja de Ruta 2026--2028

El roadmap se despliega en siete sub-fases trimestrales con entregables
específicos, hitos de validación y metas intermedias de crecimiento.
Cada sub-fase construye sobre la anterior, siguiendo una progresión
lógica de MVP $\rightarrow$ Growth $\rightarrow$ Scale.

### Fase 1 --- MVP (2026): Validación de Producto

**Q3 2026 --- Fundación Técnica y Legal**

- Despliegue de infraestructura K8s con Terraform (IaC) y CI/CD con
  GitHub Actions.

- Publicación de API Beta con 3 endpoints en RapidAPI, autenticación
  OAuth2 y rate limiting por plan.

- Configuración de flujos HubSpot para captación de Beta Testers.

- Redacción y publicación de ToS, Privacy Policy y DPA.

- Lanzamiento de landing page con registro self-service.

- **Hito:** infraestructura versionada, API pública, documentación legal
  lista.

**Q4 2026 --- Lanzamiento del MVP**

- Construcción del pipeline ETL completo con Great Expectations, dbt y
  MonetDB.

- Entrenamiento del primer modelo de predicción de retrasos (XGBoost)
  con MAPE $\le$ 15 %.

- Implementación del stack de observabilidad (Grafana LGTM + PagerDuty).

- Lanzamiento del Developer Portal interactivo con sandbox de datos
  sintéticos.

- Onboarding de primeros 50 Beta Testers activos.

- **Hito:** MVP funcional, 50 Beta Testers, uptime $\ge$ 99.9 %.

### Fase 2 --- Growth (2027): Escalamiento y Validación Comercial

**Q1 2027 --- Validación de Robustez**

- Ejecución de pruebas de carga con k6 (10K usuarios concurrentes) y
  primeros chaos experiments.

- Inicio de A/B testing de pricing en landing page (2--3 variantes).

- Publicación de primeros 2 artículos técnicos y envío de propuestas a
  conferencias.

- Configuración de CDNs multi-proveedor con failover automático.

- **Hito:** uptime 99.95 % validado, pricing en experimentación.

**Q2 2027 --- Profesionalización del Producto**

- Optimización de PocketBase para escalado horizontal.

- Implementación de MLOps pipeline completo: Feast feature store, SHAP
  explainability, A/B testing.

- Lanzamiento de SDKs auto-generados en Python, JavaScript y Java.

- Dashboard de costos cloud con alertas de anomalía activas.

- **Hito:** SDKs publicados, BD migrada, primeros 100 clientes activos.

**Q3--Q4 2027 --- Crecimiento y Primeros Ingresos**

- Implementación de data contracts con validación automática para todas
  las fuentes.

- Inicio del programa SOC 2 Tipo II: recolección de evidencias de
  controles.

- Lanzamiento de dashboards self-service para clientes Enterprise.

- Implementación de pipeline SAST/DAST en CI/CD.

- Implementación de encuestas NPS trimestrales automatizadas.

- Inicio de experimentos de Deep Learning (OCR para compliance, NLP
  avanzado).

- **Hito:** primeros \$100K ARR, NPS $>$ 30, controles SOC 2 en marcha.

### Fase 3 --- Scale (2028): Liderazgo Global

**Q1--Q2 2028 --- Expansión Geográfica y Certificación**

- Despliegue de infraestructura multi-región activo-activo (al menos 3
  regiones cloud).

- Implementación de pipeline Speech-to-Text para feedback cualitativo
  (WER $\le$ 10 %).

- Obtención de certificación SOC 2 Tipo II (auditoría externa).

- Lanzamiento de marketplace de integraciones con SDK para partners.

- **Hito:** SOC 2 certificado, uptime $\ge$ 99.99 %, presencia
  multi-región.

**Q3--Q4 2028 --- Consolidación y Diversificación**

- Inicio del roadmap de certificación ISO 27001 (gap analysis + plan de
  remediación).

- Implementación de auto-scaling predictivo con modelos ML.

- Expansión de cobertura de datos a métricas de sustentabilidad
  (emisiones CO$_2$ por ruta).

- Construcción de comunidad de desarrolladores con programa de
  embajadores.

- Evaluación de expansión a verticales adyacentes (aviación ejecutiva,
  drones, espacio aéreo urbano).

- **Hito:** $\ge$ 500 clientes activos, ARR duplicado anualmente, NPS
  enterprise $>$ 50.

**Metas Intermedias por Fase**

  ------------- --------------------------- --------------- ------------------------ ----------- -----------------------
  Q3 2026       Pre-revenue                 ---             $\ge$ 99.5 % (staging)   ---         (fundación)
  Q4 2026       Pre-revenue                 ---             $\ge$ 99.9 %             ---         $\ge$ 50 Beta Testers
  Q1--Q2 2027   Primeros \$10K--\$30K MRR   $>$ 20          $\ge$ 99.95 %            $<$ 3 %     $\ge$ 100 clientes
  Q3--Q4 2027   \$100K ARR                  $>$ 30          $\ge$ 99.95 %            $<$ 2 %     $\ge$ 200 clientes
  Q1--Q2 2028   \$300K--\$500K ARR          $>$ 40          $\ge$ 99.99 %            $<$ 1 %     $\ge$ 350 clientes
  Q3--Q4 2028   \$1M+ ARR                   $>$ 50 (Ent.)   $\ge$ 99.99 %            $<$ 0.5 %   $\ge$ 500 clientes
  ------------- --------------------------- --------------- ------------------------ ----------- -----------------------

  : Indicadores clave de progreso por fase del roadmap

## Alineación Vertical: Estratégico $\rightarrow$ Táctico $\rightarrow$ Operativo

  ------------------------------ ---------------------------- ----------------------------------------------------
  OE1 --- Growth Hacking         OT1, OT2, OT4, OT19          OP1, OP2, OP25, OP30, OP31
  OE2 --- APIs y SDKs            OT3, OT4, OT11               OP24, OP25, OP26
  OE3 --- Cloud HA               OT5, OT6, OT14, OT15, OT16   OP8, OP9, OP15, OP16, OP17, OP18, OP19, OP27, OP28
  OE4 --- BI Centralizada        OT7, OT8, OT15               OP3, OP4, OP7
  OE5 --- IA Aeronáutica         OT9, OT13, OT21, OT22        OP5, OP6, OP32, OP33
  OE6 --- Compliance             OT10, OT17                   OP10, OP11, OP21, OP22, OP29
  OE7 --- Customer Success       OT2, OT11, OT19              OP1, OP12, OP13, OP26, OP30
  OE8 --- Talento Remote-First   OT12, OT13, OT20             OP14, OP23, OP29, OP31
  OE9 --- Calidad de Datos       OT7, OT15, OT18              OP3, OP4, OP34
  OE10 --- Gestión de Producto   OT18, OT19, OT20             OP14, OP20, OP30, OP31
  ------------------------------ ---------------------------- ----------------------------------------------------

  : Alineación vertical de objetivos: estratégico $\rightarrow$ táctico
  $\rightarrow$ operativo

**Correspondencia OP $\rightarrow$ Caso de Uso Operativo.** Los 34
Objetivos Operativos se cubren con 20 Casos de Uso Operativos; varios
CUs implementan múltiples OPs relacionados. Cada OP tiene al menos un CU
asignado para garantizar su ejecución y trazabilidad.

  **OP**   **CU**   **Descripción**                                           **Justificación**
  -------- -------- --------------------------------------------------------- ----------------------------------------------------------------------------------------
                                                                              
  **OP**   **CU**   **Descripción**                                           **Justificación**
  OP1      CU-O01   Gestionar registro automatizado                           Validación de email + generación de API Keys + aprovisionamiento de tenant
  OP2      CU-O02   Monitorear rate limit y auto-scaling                      Supervisión de thresholds, throttling graduado y elasticidad de pods
  OP3      CU-O03   Supervisar ejecución de pipelines ETL                     Monitoreo de duración, volumen, estado y re-ejecución de DAGs
  OP4      CU-O04   Validar calidad de datos post-ingesta                     Suite GE: nulos, duplicados, rangos, frescura y schema
  OP5      CU-O05   Reentrenar modelos ML programados                         Entrenamiento semanal, comparación MAPE, auto-promoción
  OP6      CU-O05   Verificar drift de modelos en producción                  Monitoreo PSI diario, alerta si $>$ 0.2, reentrenamiento automático
  OP7      CU-O06   Refrescar dashboards BI                                   Refresh nocturno con verificación de integridad y consistencia
  OP8      CU-O07   Monitorear telemetría de contenedores                     Métricas de CPU/mem/red cada 30s, dashboards Grafana, respuesta a alertas
  OP9      CU-O07   Configurar y mantener reglas de alerta                    Thresholds por servicio, pruebas en staging, revisión de falsos positivos
  OP10     CU-O18   Ejecutar escaneo SAST/DAST en CI/CD                       SonarQube + OWASP ZAP en cada PR, bloqueo por vulnerabilidades críticas
  OP11     CU-O18   Aplicar parches de seguridad críticos                     Monitoreo de CVEs, parches $\le$ 24h, inventory de versiones de paquetes
  OP12     CU-O08   Atender tickets de desarrolladores externos               Triaging NLP, primera respuesta $\le$ 2h, resolución e investigación
  OP13     CU-O14   Documentar FAQs en base de conocimientos                  Detección de temas recurrentes, borrador automático, publicación y medición
  OP14     CU-O15   Gestionar sprints en Linear                               Creación de tickets, standup diario, cierre con retrospectiva documentada
  OP15     CU-O19   Revisar y optimizar costos cloud                          Auditoría semanal, anomalías de gasto, recursos ociosos, recomendaciones
  OP16     CU-O09   Ejecutar backup diario automatizado                       Backup encriptado con KMS, upload a cold storage, log de integridad
  OP17     CU-O09   Ejecutar prueba de restauración semanal                   Restore en instancia aislada, validación de row counts y smoke tests
  OP18     CU-O10   Calcular SLI/SLO y error budget                           Cómputo de uptime 30 días, proyección de consumo, recomendación de congelación
  OP19     CU-O10   Ejecutar congelación de deploys                           Bloqueo de CI/CD automático, notificación a stakeholders, plan de remediación
  OP20     CU-O11   Publicar changelog semanal SemVer                         Recolección de commits, categorización, bump de versión, publicación en portal
  OP21     CU-O12   Rotar credenciales de servicio                            Generación en Vault, actualización en K8s, verificación con smoke tests
  OP22     CU-O12   Auditar accesos IAM trimestralmente                       Revisión de roles y políticas, revocación de accesos injustificados, reporte
  OP23     CU-O13   Realizar post-mortem blameless $\le$ 72h                  Timeline automático, 5 whys, documentación de aprendizajes, tickets de acción
  OP24     CU-O16   Validar especificaciones OpenAPI en CI/CD                 Spectral linter en cada PR, detección de breaking changes, bloqueo de merge
  OP25     CU-T02   Monitorear presencia en marketplace RapidAPI              Uptime del listing, respuesta a reviews, actualización trimestral de planes
  OP26     CU-T07   Mantener documentación interactiva del portal             Sincronización con specs, verificación de ejemplos, guías de migración
  OP27     CU-T09   Ejecutar pruebas de carga semanales en staging            k6 con 10K usuarios, medición de latencia p95 y throughput, reporte
  OP28     CU-T09   Ejecutar chaos engineering mensualmente                   Litmus Chaos, kill pod, network partition, DB failover, medición MTTR
  OP29     CU-E04   Mantener documentación legal y compliance                 Actualización de ToS/DPA, evidencias SOC 2, registros de procesamiento GDPR
  OP30     CU-T10   Recolectar y analizar feedback de clientes                Encuestas NPS + CSAT, transcripción STT, clasificación de sentimiento
  OP31     CU-T01   Publicar contenido técnico regularmente                   Artículos en blog, redes sociales, propuestas de charlas, medición de engagement
  OP32     CU-O20   Ejecutar experimentos de Deep Learning OCR                Entrenamiento de modelos CRNN/TrOCR sobre documentos de compliance, registro en MLflow
  OP33     CU-O20   Implementar pipeline de Speech-to-Text                    Despliegue de Whisper, medición de WER, extracción de temas y sentimiento
  OP34     CU-O17   Validar data contracts entre productores y consumidores   Schema contracts en Git, validación en CI, alerta de drift, bloqueo de ingesta

  : Correspondencia entre los 34 Objetivos Operativos y los Casos de Uso

# Casos de Uso Estratégicos

## CU-E01: Consultar Tablero Balanced Scorecard

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CEO                                                |
+-----------------+----------------------------------------------------+
| Propósito       | Monitorear en tiempo real el desempeño global      |
|                 | contra las metas del BSC.                          |
+-----------------+----------------------------------------------------+
| Precondición    | El CEO accede al sistema con autenticación 2FA.    |
+-----------------+----------------------------------------------------+
| Flujo Principal | El sistema carga KPIs de Fact_Suscripcion,         |
|                 | Fact_API_Call, Fact_Satisfaccion y Fact_Incidente. |
|                 | Renderiza semáforos (verde/amarillo/rojo)          |
|                 | contrastando el valor real contra la meta. El CEO  |
|                 | puede hacer drill-down a la tendencia histórica de |
|                 | cada indicador.                                    |
+-----------------+----------------------------------------------------+
| Postcondición   | vista 360 del estado de la empresa.                |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                  **Para\...**
  ---------- -------------- -------------------------------------------------------------- --------------------------------------------
  HU-E01.1   CEO            visualizar el ARR actual comparado contra la meta anual        evaluar el desempeño financiero
  HU-E01.2   CEO            ver el NPS segmentado por región geográfica                    identificar mercados con baja satisfacción
  HU-E01.3   CEO            comparar el uptime real contra el SLO del 99.99%               verificar la disponibilidad del servicio
  HU-E01.4   CEO            recibir alertas automáticas cuando un KPI entre en zona roja   tomar acción correctiva inmediata
  HU-E01.5   CEO            exportar el tablero BSC completo en formato PDF                presentarlo en reuniones de directorio

------------------------------------------------------------------------

## CU-E02: Analizar ARR y Rentabilidad Mensual

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CEO                                                |
+-----------------+----------------------------------------------------+
| Propósito       | Evaluar ingresos recurrentes, márgenes y           |
|                 | tendencias de crecimiento.                         |
+-----------------+----------------------------------------------------+
| Precondición    | El CEO o CFO selecciona un período de análisis.    |
+-----------------+----------------------------------------------------+
| Flujo Principal | El sistema carga agregaciones de Fact_Suscripcion  |
|                 | y Fact_API_Call. Compara los resultados contra     |
|                 | períodos anteriores. Detecta anomalías con un      |
|                 | algoritmo de desviación estándar. Genera un        |
|                 | reporte financiero detallado.                      |
+-----------------+----------------------------------------------------+
| Postcondición   | diagnóstico financiero actualizado y disponible.   |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                         **Para\...**
  ---------- -------------- --------------------------------------------------------------------- -------------------------------------------
  HU-E02.1   CEO            visualizar el ARR desglosado por plan de suscripción                  entender la composición de ingresos
  HU-E02.2   CEO            comparar el crecimiento mes a mes del ARR                             evaluar la tracción del negocio
  HU-E02.3   CEO            detectar caídas inesperadas de revenue                                investigar posibles causas de fuga
  HU-E02.4   CEO            analizar la tasa de churn versus la expansión de cuentas existentes   medir la salud de la base de clientes
  HU-E02.5   CEO            exportar el reporte financiero mensual                                compartirlo con inversionistas y el board

------------------------------------------------------------------------

## CU-E03: Evaluar Uptime Global y Cumplimiento SLA

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CTO                                                |
+-----------------+----------------------------------------------------+
| Propósito       | Verificar disponibilidad del sistema en tiempo     |
|                 | real en todas las regiones.                        |
+-----------------+----------------------------------------------------+
| Precondición    | El CTO selecciona una ventana temporal.            |
+-----------------+----------------------------------------------------+
| Flujo Principal | El sistema carga datos de uptime por región desde  |
|                 | Prometheus. Calcula el error budget consumido.     |
|                 | Muestra el porcentaje de cumplimiento de SLA       |
|                 | desglosado por endpoint.                           |
+-----------------+----------------------------------------------------+
| Postcondición   | estado de infraestructura verificado y             |
|                 | documentado.                                       |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                   **Para\...**
  ---------- -------------- --------------------------------------------------------------- ----------------------------------------------
  HU-E03.1   CTO            visualizar el uptime por región de despliegue                   identificar zonas con degradación
  HU-E03.2   CTO            comparar el uptime mensual contra el SLO del 99.99%             verificar el cumplimiento contractual
  HU-E03.3   CTO            recibir una alerta cuando exista una brecha de disponibilidad   activar el protocolo de respuesta
  HU-E03.4   CTO            hacer drill-down hasta el nivel de endpoint                     identificar la causa raíz de una caída
  HU-E03.5   CTO            generar automáticamente un reporte de SLA por cliente           entregar transparencia a clientes Enterprise

------------------------------------------------------------------------

## CU-E04: Revisar Cumplimiento Normativo

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CTO / Auditor                                      |
+-----------------+----------------------------------------------------+
| Propósito       | Verificar estado de compliance contra marcos SOC   |
|                 | 2, ISO 27001, GDPR, IATA.                          |
+-----------------+----------------------------------------------------+
| Precondición    | El CTO o Auditor selecciona el marco normativo a   |
|                 | evaluar.                                           |
+-----------------+----------------------------------------------------+
| Flujo Principal | El sistema carga las evidencias de controles       |
|                 | implementados. Muestra un score de cumplimiento    |
|                 | por control. Identifica gaps con semáforo. Genera  |
|                 | un reporte de auditoría exportable.                |
+-----------------+----------------------------------------------------+
| Postcondición   | diagnóstico de compliance actualizado.             |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                  **Para\...**
  ---------- -------------- -------------------------------------------------------------- -------------------------------------------
  HU-E04.1   Auditor        ver el progreso del programa SOC 2 Tipo II                     planificar la auditoría externa
  HU-E04.2   CTO            verificar la residencia de datos por región                    cumplir con las exigencias del GDPR
  HU-E04.3   Auditor        comprobar que el cifrado en tránsito y en reposo está activo   validar el control técnico
  HU-E04.4   CTO            identificar controles no conformes marcados en rojo            priorizar su remediación
  HU-E04.5   Auditor        exportar el reporte de cumplimiento en formato PDF             adjuntarlo al expediente de certificación

------------------------------------------------------------------------

## CU-E05: Definir Metas Estratégicas Trimestrales

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CEO / CTO                                          |
+-----------------+----------------------------------------------------+
| Propósito       | Establecer OKRs y metas del BSC para el próximo    |
|                 | trimestre.                                         |
+-----------------+----------------------------------------------------+
| Precondición    | El equipo C-Level revisa los resultados del        |
|                 | trimestre anterior.                                |
+-----------------+----------------------------------------------------+
| Flujo Principal | Proyecta tendencias con un módulo de simulación.   |
|                 | Define targets cuantitativos por área. Asigna      |
|                 | responsables. Publica las metas a toda la          |
|                 | organización.                                      |
+-----------------+----------------------------------------------------+
| Postcondición   | metas trimestrales definidas y comunicadas.        |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                         **Para\...**
  ---------- -------------- --------------------------------------------------------------------- --------------------------------
  HU-E05.1   CEO            proyectar el ARR del próximo trimestre con simulación de escenarios   fijar metas realistas
  HU-E05.2   CEO            definir OKRs por departamento alineados al BSC                        asegurar cohesión estratégica
  HU-E05.3   CTO            ajustar los targets técnicos según las tendencias de rendimiento      evitar metas inalcanzables
  HU-E05.4   CEO            notificar automáticamente a cada responsable de área                  iniciar la cascada táctica
  HU-E05.5   CEO            hacer seguimiento semanal del progreso contra metas                   corregir desviaciones a tiempo

------------------------------------------------------------------------

## CU-E06: Analizar Retención de Talento y eNPS

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CEO / VP People                                    |
+-----------------+----------------------------------------------------+
| Propósito       | Evaluar satisfacción, retención y productividad    |
|                 | del equipo.                                        |
+-----------------+----------------------------------------------------+
| Precondición    | El CEO carga los resultados de encuestas eNPS      |
|                 | trimestrales.                                      |
+-----------------+----------------------------------------------------+
| Flujo Principal | Segmenta por equipo, seniority y región. Compara   |
|                 | contra el baseline histórico. Identifica áreas de  |
|                 | riesgo de rotación. Recomienda acciones            |
|                 | correctivas.                                       |
+-----------------+----------------------------------------------------+
| Postcondición   | diagnóstico de clima laboral disponible.           |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                           **Para\...**
  ---------- -------------- ----------------------------------------------------------------------- ------------------------------------------
  HU-E06.1   CEO            visualizar la tendencia del eNPS en los últimos cuatro trimestres       evaluar la evolución del clima laboral
  HU-E06.2   VP People      identificar equipos con eNPS en zona de riesgo                          activar planes de retención
  HU-E06.3   CEO            comparar la tasa de retención anual contra benchmarks de la industria   evaluar competitividad
  HU-E06.4   VP People      analizar el time-to-productivity promedio por equipo                    mejorar el proceso de onboarding
  HU-E06.5   CEO            generar un reporte de People Analytics trimestral                       presentarlo en la revisión de directorio

------------------------------------------------------------------------

# Casos de Uso Tácticos

## CU-T01: Gestionar Campañas de Growth Hacking

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | VP Marketing                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Crear y automatizar campañas para captar Beta      |
|                 | Testers.                                           |
+-----------------+----------------------------------------------------+
| Precondición    | El VP Marketing diseña una campaña en HubSpot.     |
+-----------------+----------------------------------------------------+
| Flujo Principal | Segmenta la audiencia por industria y región.      |
|                 | Programa envíos automatizados. Monitorea tasas de  |
|                 | conversión en tiempo real. Optimiza con A/B        |
|                 | testing de contenido.                              |
+-----------------+----------------------------------------------------+
| Postcondición   | campañas activas monitoreadas.                     |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                     **Para\...**
  ---------- -------------- ----------------------------------------------------------------- -----------------------------------------
  HU-T01.1   VP Marketing   crear una secuencia de emails automatizada en HubSpot             nurturar leads de manera escalable
  HU-T01.2   VP Marketing   segmentar la audiencia por industria aeronáutica                  personalizar el mensaje
  HU-T01.3   VP Marketing   ejecutar un A/B test del asunto del email                         maximizar la tasa de apertura
  HU-T01.4   VP Marketing   medir la conversión desde email hasta registro en la plataforma   calcular el ROI de la campaña
  HU-T01.5   VP Marketing   visualizar el ROI de cada campaña en un dashboard                 asignar presupuesto a las más efectivas

------------------------------------------------------------------------

## CU-T02: Configurar y Publicar API en RapidAPI

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CTO / Developer Advocate                           |
+-----------------+----------------------------------------------------+
| Propósito       | Publicar API Beta en marketplaces con planes y     |
|                 | rate limits.                                       |
+-----------------+----------------------------------------------------+
| Precondición    | El CTO valida la spec OpenAPI 3.1.                 |
+-----------------+----------------------------------------------------+
| Flujo Principal | Configura el listing en RapidAPI. Define los       |
|                 | planes (Freemium/Pro/Enterprise) con sus           |
|                 | respectivos rate limits. Configura autenticación   |
|                 | OAuth2. Publica y monitorea la adopción.           |
+-----------------+----------------------------------------------------+
| Postcondición   | API disponible en marketplace.                     |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**         **Deseo\...**                                             **Para\...**
  ---------- -------------------- --------------------------------------------------------- ----------------------------------------
  HU-T02.1   CTO                  validar la especificación OpenAPI 3.1 antes de publicar   garantizar conformidad con el estándar
  HU-T02.2   Developer Advocate   configurar rate limits diferenciados por plan             proteger la infraestructura
  HU-T02.3   CTO                  configurar OAuth2 con flujo client_credentials            asegurar el acceso a la API
  HU-T02.4   Developer Advocate   publicar la API en el marketplace de RapidAPI             alcanzar desarrolladores globales
  HU-T02.5   VP Marketing         ver las analíticas de adopción desde el marketplace       medir el alcance orgánico

------------------------------------------------------------------------

## CU-T03: Gestionar Infraestructura Cloud con Terraform

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | SRE / DevOps                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Administrar todos los recursos cloud como código   |
|                 | versionado.                                        |
+-----------------+----------------------------------------------------+
| Precondición    | El SRE escribe un módulo Terraform para el recurso |
|                 | requerido.                                         |
+-----------------+----------------------------------------------------+
| Flujo Principal | Somete el cambio a PR review por el equipo.        |
|                 | Ejecuta terraform plan y terraform apply. Verifica |
|                 | que los recursos se hayan creado correctamente.    |
|                 | Versiona todo en Git.                              |
+-----------------+----------------------------------------------------+
| Postcondición   | infraestructura 100% como código.                  |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                           **Para\...**
  ---------- -------------- ------------------------------------------------------- ---------------------------------------------------
  HU-T03.1   SRE            definir un módulo Terraform para el clúster K8s         replicar entornos idénticos
  HU-T03.2   SRE            configurar la CDN multi-proveedor vía Terraform         gestionarla como código
  HU-T03.3   SRE            gestionar los registros DNS como código                 evitar configuraciones manuales propensas a error
  HU-T03.4   SRE            versionar todos los cambios de infraestructura en Git   tener trazabilidad completa
  HU-T03.5   SRE            ejecutar rollback de infraestructura vía git revert     recuperar el último estado estable

------------------------------------------------------------------------

## CU-T04: Monitorear Pipelines ETL y Calidad de Datos

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Data Engineer                                      |
+-----------------+----------------------------------------------------+
| Propósito       | Asegurar que los flujos de datos estén saludables  |
|                 | y cumplan estándares.                              |
+-----------------+----------------------------------------------------+
| Precondición    | El Data Engineer ejecuta la suite de Great         |
|                 | Expectations programada.                           |
+-----------------+----------------------------------------------------+
| Flujo Principal | Verifica reglas de frescura, volumen, nulos y      |
|                 | schema. Genera un reporte de calidad consolidado.  |
|                 | Recibe alertas en Slack ante cualquier fallo.      |
+-----------------+----------------------------------------------------+
| Postcondición   | calidad de datos verificada y documentada.         |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**    **Deseo\...**                                                  **Para\...**
  ---------- --------------- -------------------------------------------------------------- ---------------------------------------
  HU-T04.1   Data Engineer   visualizar el estado de ejecución de cada pipeline ETL         detectar fallos rápidamente
  HU-T04.2   Data Engineer   verificar la frescura de los datos por fuente                  asegurar que no haya rezagos
  HU-T04.3   Data Engineer   validar la integridad del schema contra el contrato de datos   prevenir errores en downstream
  HU-T04.4   Data Engineer   recibir una alerta inmediata ante un fallo de validación       iniciar la corrección
  HU-T04.5   CTO             ver un scorecard mensual de calidad de datos                   monitorear la salud del data pipeline

------------------------------------------------------------------------

## CU-T05: Entrenar y Versionar Modelos ML

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | ML Engineer                                        |
+-----------------+----------------------------------------------------+
| Propósito       | Gestionar ciclo de vida completo de modelos ML.    |
+-----------------+----------------------------------------------------+
| Precondición    | El ML Engineer crea un experimento en MLflow.      |
+-----------------+----------------------------------------------------+
| Flujo Principal | Registra hiperparámetros y métricas. Compara       |
|                 | versiones. Registra el modelo campeón. Promueve a  |
|                 | staging. Valida comportamiento y despliega a       |
|                 | producción.                                        |
+-----------------+----------------------------------------------------+
| Postcondición   | modelo versionado en producción.                   |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                **Para\...**
  ---------- -------------- ------------------------------------------------------------ -----------------------------------
  HU-T05.1   ML Engineer    loguear cada experimento con sus hiperparámetros en MLflow   mantener trazabilidad
  HU-T05.2   ML Engineer    comparar dos versiones de modelo visualmente                 seleccionar la de mejor desempeño
  HU-T05.3   ML Engineer    registrar el champion model en el Model Registry             gestionar su ciclo de vida
  HU-T05.4   ML Engineer    promover un modelo a producción vía API de MLflow            automatizar el deployment
  HU-T05.5   ML Engineer    ejecutar rollback a la versión anterior del modelo           revertir una degradación

------------------------------------------------------------------------

## CU-T06: Configurar Alertas de Seguridad y Compliance

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | SRE / DevOps                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Definir monitoreo de seguridad proactivo.          |
+-----------------+----------------------------------------------------+
| Precondición    | El SRE define umbrales de alerta en el sistema de  |
|                 | monitoreo.                                         |
+-----------------+----------------------------------------------------+
| Flujo Principal | Integra escaneos SAST/DAST en el pipeline de       |
|                 | CI/CD. Configura notificaciones a PagerDuty.       |
|                 | Prueba el disparo de alertas en staging. Activa el |
|                 | monitoreo en producción.                           |
+-----------------+----------------------------------------------------+
| Postcondición   | seguridad monitoreada 24/7.                        |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                                 **Para\...**
  ---------- -------------- ----------------------------------------------------------------------------- ------------------------------------
  HU-T06.1   SRE            definir una alerta para vulnerabilidades críticas con SLA de parcheo \< 24h   cumplir la política de seguridad
  HU-T06.2   SRE            configurar una alerta de rate limit breach                                    detectar abusos o ataques
  HU-T06.3   SRE            configurar una alerta de expiración de certificados SSL                       renovarlos antes del vencimiento
  HU-T06.4   SRE            configurar una alerta de acceso no autorizado                                 activar respuesta ante intrusiones
  HU-T06.5   SRE            probar la entrega de alertas a PagerDuty con un incidente simulado            validar el flujo completo

------------------------------------------------------------------------

## CU-T07: Mantener Developer Portal y SDKs

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Developer Advocate                                 |
+-----------------+----------------------------------------------------+
| Propósito       | Mantener documentación, SDKs y sandbox             |
|                 | actualizados.                                      |
+-----------------+----------------------------------------------------+
| Precondición    | El Developer Advocate genera documentación         |
|                 | interactiva desde la spec OpenAPI.                 |
+-----------------+----------------------------------------------------+
| Flujo Principal | Publica SDKs auto-generados para Python,           |
|                 | JavaScript y Java. Actualiza el changelog.         |
|                 | Monitorea analíticas de páginas. Mantiene el       |
|                 | sandbox con datos sintéticos.                      |
+-----------------+----------------------------------------------------+
| Postcondición   | portal actualizado y operativo.                    |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**         **Deseo\...**                                                   **Para\...**
  ---------- -------------------- --------------------------------------------------------------- --------------------------------------------
  HU-T07.1   Developer Advocate   generar documentación interactiva desde la spec OpenAPI         mantenerla sincronizada con el código
  HU-T07.2   Developer Advocate   publicar una nueva versión del SDK de Python                    facilitar la integración de los clientes
  HU-T07.3   Developer Advocate   ver las analíticas de tráfico en las páginas de documentación   identificar endpoints populares
  HU-T07.4   Developer Advocate   gestionar el sandbox con datos sintéticos renovados             ofrecer una experiencia de prueba realista
  HU-T07.5   Developer Advocate   sincronizar automáticamente el changelog con cada release       mantener informada a la comunidad

------------------------------------------------------------------------

## CU-T08: Analizar Costos Cloud y Optimizar Recursos

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CTO / SRE                                          |
+-----------------+----------------------------------------------------+
| Propósito       | Monitorear y optimizar gasto cloud.                |
+-----------------+----------------------------------------------------+
| Precondición    | El CTO revisa el dashboard de costos por servicio  |
|                 | cloud.                                             |
+-----------------+----------------------------------------------------+
| Flujo Principal | Compara el gasto real contra el presupuesto.       |
|                 | Detecta anomalías de gasto con detección de        |
|                 | outliers. Identifica recursos subutilizados.       |
|                 | Genera recomendaciones de optimización.            |
+-----------------+----------------------------------------------------+
| Postcondición   | gasto cloud optimizado.                            |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                   **Para\...**
  ---------- -------------- --------------------------------------------------------------- ------------------------------------------
  HU-T08.1   CTO            visualizar los costos desglosados por servicio cloud            identificar los mayores drivers de gasto
  HU-T08.2   SRE            detectar una anomalía de gasto diario                           investigar posibles fugas
  HU-T08.3   CTO            comparar la tendencia mensual de costos contra el presupuesto   controlar desviaciones
  HU-T08.4   CTO            identificar recursos cloud ociosos                              eliminarlos o redimensionarlos
  HU-T08.5   SRE            generar recomendaciones automáticas de ahorro                   reducir el costo mensual

------------------------------------------------------------------------

## CU-T09: Ejecutar Pruebas de Carga y Chaos Engineering

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | SRE / DevOps                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Validar resiliencia de la plataforma bajo estrés.  |
+-----------------+----------------------------------------------------+
| Precondición    | El SRE define escenarios de prueba en k6.          |
+-----------------+----------------------------------------------------+
| Flujo Principal | Ejecuta la simulación con 10K usuarios             |
|                 | concurrentes. Inyecta caos controlado (matar un    |
|                 | pod aleatorio). Mide el tiempo de recuperación.    |
|                 | Documenta hallazgos en un reporte.                 |
+-----------------+----------------------------------------------------+
| Postcondición   | resiliencia validada.                              |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                **Para\...**
  ---------- -------------- ------------------------------------------------------------ --------------------------------------------------
  HU-T09.1   SRE            ejecutar k6 con un escenario de 10K usuarios concurrentes    validar la capacidad del sistema
  HU-T09.2   SRE            ejecutar un experimento de chaos engineering                 verificar que el sistema se auto-recupera
  HU-T09.3   SRE            medir el tiempo de recuperación tras la inyección de fallo   compararlo contra el RTO
  HU-T09.4   SRE            validar que el auto-scaling responde en menos de 2 minutos   garantizar elasticidad
  HU-T09.5   CTO            revisar el reporte de resiliencia trimestral                 tomar decisiones de inversión en infraestructura

------------------------------------------------------------------------

## CU-T10: Validar Estrategia de Pricing con A/B Testing

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | VP Marketing / CEO                                 |
+-----------------+----------------------------------------------------+
| Propósito       | Probar hipótesis de precios antes del lanzamiento. |
+-----------------+----------------------------------------------------+
| Precondición    | El VP Marketing define una hipótesis de pricing.   |
+-----------------+----------------------------------------------------+
| Flujo Principal | Configura un A/B test en la landing page. Dirige   |
|                 | tráfico 50/50 a cada variante. Mide la conversión. |
|                 | Analiza los resultados estadísticamente.           |
|                 | Selecciona el pricing óptimo.                      |
+-----------------+----------------------------------------------------+
| Postcondición   | pricing validado con datos.                        |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                          **Para\...**
  ---------- -------------- ------------------------------------------------------ ---------------------------------------
  HU-T10.1   VP Marketing   configurar un A/B test en la landing page              comparar dos estructuras de precios
  HU-T10.2   VP Marketing   comparar las tasas de conversión entre variantes       determinar cuál es más efectiva
  HU-T10.3   CEO            medir la willingness-to-pay de los prospectos          definir el precio óptimo
  HU-T10.4   VP Marketing   analizar la tasa de churn por nivel de precio          evitar precios que ahuyenten clientes
  HU-T10.5   CEO            seleccionar el pricing que maximice el ratio LTV/CAC   asegurar rentabilidad a largo plazo

------------------------------------------------------------------------

# Casos de Uso Operativos

## CU-O01: Registrar Tenant y Autogenerar API Keys

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Cliente B2B / Sistema                              |
+-----------------+----------------------------------------------------+
| Propósito       | Permitir registro self-service de nuevos clientes. |
+-----------------+----------------------------------------------------+
| Precondición    | El cliente completa un formulario de registro con  |
|                 | email y datos de empresa.                          |
+-----------------+----------------------------------------------------+
| Flujo Principal | El sistema valida que el email sea único. Genera   |
|                 | una API Key automáticamente. Crea un tenant con    |
|                 | plan Freemium. Envía un email de bienvenida con    |
|                 | enlaces a documentación.                           |
+-----------------+----------------------------------------------------+
| Postcondición   | tenant activo.                                     |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                 **Para\...**
  ---------- -------------- ------------------------------------------------------------- -------------------------------------------
  HU-O01.1   Cliente B2B    registrarme con mi email corporativo                          crear una cuenta rápidamente
  HU-O01.2   Sistema        autogenerar una API Key única por tenant                      habilitar el acceso inmediato
  HU-O01.3   Cliente B2B    verificar mi email mediante un link de confirmación           activar mi cuenta
  HU-O01.4   Cliente B2B    recibir un email de bienvenida con guías rápidas              empezar a usar la API
  HU-O01.5   Sistema        provisionar automáticamente un sandbox para el nuevo tenant   reducir el tiempo hasta el primer insight

------------------------------------------------------------------------

## CU-O02: Consultar Datos de Vuelo vía API REST/GraphQL

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Cliente B2B                                        |
+-----------------+----------------------------------------------------+
| Propósito       | Consultar datos aeronáuticos mediante API.         |
+-----------------+----------------------------------------------------+
| Precondición    | El cliente envía un request HTTP con API Key en    |
|                 | header.                                            |
+-----------------+----------------------------------------------------+
| Flujo Principal | El sistema autentica vía OAuth2. Valida parámetros |
|                 | y rate limit del plan. Ejecuta la query contra el  |
|                 | Data Warehouse. Retorna respuesta en formato JSON. |
|                 | Loggea el consumo para facturación.                |
+-----------------+----------------------------------------------------+
| Postcondición   | datos entregados.                                  |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                **Para\...**
  ---------- -------------- ------------------------------------------------------------ ------------------------------------------
  HU-O02.1   Cliente B2B    consultar vuelos filtrando por aerolínea y rango de fechas   obtener datos específicos
  HU-O02.2   Cliente B2B    filtrar vuelos con retraso mayor a 30 minutos                analizar patrones de impuntualidad
  HU-O02.3   Cliente B2B    paginar resultados grandes con cursores                      manejar eficientemente grandes volúmenes
  HU-O02.4   Cliente B2B    consultar vía GraphQL con campos anidados                    reducir el número de llamadas
  HU-O02.5   Cliente B2B    recibir headers X-RateLimit-Remaining en cada respuesta      gestionar mi cuota de consumo

------------------------------------------------------------------------

## CU-O03: Ejecutar Ingesta Diaria de Datos Aeronáuticos

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Data Engineer / Sistema                            |
+-----------------+----------------------------------------------------+
| Propósito       | Ejecutar ingesta programada de datos desde         |
|                 | proveedores.                                       |
+-----------------+----------------------------------------------------+
| Precondición    | El sistema descarga archivos desde el SFTP del     |
|                 | proveedor de datos.                                |
+-----------------+----------------------------------------------------+
| Flujo Principal | Valida el schema CSV/Parquet. Transforma           |
|                 | timestamps a UTC. Carga los datos a la tabla       |
|                 | staging. Verifica que el row count coincida con lo |
|                 | esperado. Loggea el resultado de la ingesta.       |
+-----------------+----------------------------------------------------+
| Postcondición   | datos en staging.                                  |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**    **Deseo\...**                                               **Para\...**
  ---------- --------------- ----------------------------------------------------------- -------------------------------
  HU-O03.1   Data Engineer   descargar los datos del proveedor vía SFTP programado       automatizar la ingesta
  HU-O03.2   Data Engineer   validar el schema de los archivos antes de cargar           evitar corrupción en staging
  HU-O03.3   Sistema         transformar todas las zonas horarias a UTC                  estandarizar los timestamps
  HU-O03.4   Sistema         cargar los datos validados a la tabla de staging            dejarlos disponibles para ETL
  HU-O03.5   Data Engineer   verificar que el conteo de filas coincida con lo esperado   detectar pérdida de datos

------------------------------------------------------------------------

## CU-O04: Validar Calidad de Datos en Pipeline ETL

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Data Engineer / Sistema                            |
+-----------------+----------------------------------------------------+
| Propósito       | Ejecutar controles de calidad tras la ingesta.     |
+-----------------+----------------------------------------------------+
| Precondición    | El sistema ejecuta la suite de Great Expectations  |
|                 | sobre los datos en staging.                        |
+-----------------+----------------------------------------------------+
| Flujo Principal | Verifica nulos en columnas críticas. Detecta       |
|                 | duplicados. Valida rangos plausibles de valores.   |
|                 | Controla la frescura de los datos. Genera un       |
|                 | reporte pass/fail.                                 |
+-----------------+----------------------------------------------------+
| Postcondición   | calidad verificada.                                |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**    **Deseo\...**                                                    **Para\...**
  ---------- --------------- ---------------------------------------------------------------- -----------------------------------
  HU-O04.1   Data Engineer   verificar que no haya nulos en flight_id y departure_time        garantizar integridad referencial
  HU-O04.2   Sistema         detectar vuelos duplicados por flight_id y fecha                 prevenir métricas infladas
  HU-O04.3   Data Engineer   validar que los valores de retraso estén en un rango plausible   detectar outliers
  HU-O04.4   Sistema         verificar que la frescura de los datos sea menor a 5 minutos     cumplir el SLO de calidad
  HU-O04.5   CTO             visualizar un dashboard pass/fail de calidad por fuente          monitorear la salud del pipeline

------------------------------------------------------------------------

## CU-O05: Reentrenar Modelo de Predicción de Retrasos

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | ML Engineer                                        |
+-----------------+----------------------------------------------------+
| Propósito       | Reentrenar modelo con datos frescos.               |
+-----------------+----------------------------------------------------+
| Precondición    | El sistema obtiene features desde Feast.           |
+-----------------+----------------------------------------------------+
| Flujo Principal | Entrena un modelo XGBoost con los nuevos datos.    |
|                 | Loggea métricas en MLflow. Compara el MAPE contra  |
|                 | la versión anterior. Auto-promueve si mejora.      |
|                 | Alerta al ML Engineer si degrada.                  |
+-----------------+----------------------------------------------------+
| Postcondición   | modelo actualizado o alerta emitida.               |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                           **Para\...**
  ---------- -------------- ------------------------------------------------------- ------------------------------------
  HU-O05.1   ML Engineer    obtener las features desde Feast automáticamente        evitar duplicación de lógica
  HU-O05.2   Sistema        entrenar el modelo XGBoost con los datos frescos        mantenerlo actualizado
  HU-O05.3   ML Engineer    comparar el MAPE del nuevo modelo contra el anterior    decidir si vale la pena promoverlo
  HU-O05.4   Sistema        auto-promover el modelo si supera el umbral de mejora   acelerar el ciclo de deploy
  HU-O05.5   ML Engineer    recibir una alerta si el modelo degrada por drift       investigar y corregir

------------------------------------------------------------------------

## CU-O06: Refrescar Dashboards BI para Clientes

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Data Engineer / Sistema                            |
+-----------------+----------------------------------------------------+
| Propósito       | Actualizar dashboards self-service con datos       |
|                 | recientes.                                         |
+-----------------+----------------------------------------------------+
| Precondición    | El sistema dispara un refresh programado nocturno. |
+-----------------+----------------------------------------------------+
| Flujo Principal | Ejecuta agregaciones precalculadas. Actualiza la   |
|                 | caché de dashboards. Verifica el renderizado       |
|                 | correcto de visualizaciones. Loggea el tiempo      |
|                 | total de refresh.                                  |
+-----------------+----------------------------------------------------+
| Postcondición   | dashboards actualizados.                           |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**    **Deseo\...**                                                 **Para\...**
  ---------- --------------- ------------------------------------------------------------- ------------------------------------------------
  HU-O06.1   Data Engineer   programar el refresh nocturno de dashboards                   que los clientes vean datos frescos al iniciar
  HU-O06.2   Sistema         verificar que todos los KPIs se hayan cargado correctamente   garantizar la integridad visual
  HU-O06.3   Data Engineer   validar que los datos del dashboard coincidan con la fuente   asegurar consistencia
  HU-O06.4   Sistema         trackear la duración del refresh en cada ejecución            detectar degradaciones
  HU-O06.5   SRE             recibir una alerta si el refresh de dashboards falla          reiniciar el proceso

------------------------------------------------------------------------

## CU-O07: Monitorear Telemetría de Contenedores K8s

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | SRE / DevOps                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Monitoreo en tiempo real de infraestructura.       |
+-----------------+----------------------------------------------------+
| Precondición    | Prometheus recolecta métricas de CPU, memoria y    |
|                 | red de los pods.                                   |
+-----------------+----------------------------------------------------+
| Flujo Principal | Evalúa reglas de alerta cada 30 segundos. Dispara  |
|                 | notificación a PagerDuty si un umbral es superado. |
|                 | Loggea el incidente automáticamente. El SRE        |
|                 | ejecuta el runbook correspondiente.                |
+-----------------+----------------------------------------------------+
| Postcondición   | infraestructura monitoreada.                       |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                          **Para\...**
  ---------- -------------- ------------------------------------------------------ ----------------------------------
  HU-O07.1   SRE            monitorear CPU y memoria de cada pod en tiempo real    detectar saturación
  HU-O07.2   SRE            trackear la tasa de errores 500 por endpoint           identificar servicios degradados
  HU-O07.3   SRE            monitorear el pool de conexiones de la base de datos   prevenir agotamiento
  HU-O07.4   Sistema        alertar automáticamente si la memoria supera el 80%    activar respuesta proactiva
  HU-O07.5   Sistema        auto-escalar los pods cuando la CPU supere el 70%      mantener la disponibilidad

------------------------------------------------------------------------

## CU-O08: Atender Ticket de Bug Reportado por Desarrollador

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Developer Advocate                                 |
+-----------------+----------------------------------------------------+
| Propósito       | Triar y resolver bugs reportados por la comunidad. |
+-----------------+----------------------------------------------------+
| Precondición    | Un desarrollador externo reporta un bug en el      |
|                 | portal.                                            |
+-----------------+----------------------------------------------------+
| Flujo Principal | El sistema auto-clasifica la severidad con NLP.    |
|                 | Asigna prioridad. Inicia el SLA tracker. El        |
|                 | Developer Advocate investiga y corrige. Notifica   |
|                 | la resolución al reportante.                       |
+-----------------+----------------------------------------------------+
| Postcondición   | bug resuelto.                                      |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**            **Deseo\...**                                                         **Para\...**
  ---------- ----------------------- --------------------------------------------------------------------- ----------------------------------------------
  HU-O08.1   Desarrollador externo   reportar un bug con pasos para reproducirlo                           facilitar el diagnóstico
  HU-O08.2   Sistema                 auto-clasificar la severidad del bug con NLP                          priorizar los críticos
  HU-O08.3   Developer Advocate      ver el SLA tracker indicando el tiempo restante                       cumplir con la respuesta en menos de 4 horas
  HU-O08.4   Developer Advocate      linkear el commit de fix al ticket original                           mantener trazabilidad
  HU-O08.5   Sistema                 notificar al reportante automáticamente cuando el bug esté resuelto   cerrar el ciclo

------------------------------------------------------------------------

## CU-O09: Ejecutar Backup y Prueba de Restauración

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | SRE / DevOps                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Backup diario y prueba de restore semanal.         |
+-----------------+----------------------------------------------------+
| Precondición    | El sistema ejecuta pg_dump programado diariamente. |
+-----------------+----------------------------------------------------+
| Flujo Principal | Encripta el backup con KMS. Lo sube a cold storage |
|                 | (S3 Glacier). Semanalmente restaura el backup a    |
|                 | una instancia de prueba. Valida integridad de      |
|                 | datos. Loggea el resultado.                        |
+-----------------+----------------------------------------------------+
| Postcondición   | backup verificado.                                 |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                       **Para\...**
  ---------- -------------- --------------------------------------------------- --------------------------------------
  HU-O09.1   SRE            programar el backup diario a las 03:00 UTC          no impactar operaciones
  HU-O09.2   Sistema        encriptar el backup con KMS antes de almacenarlo    cumplir con requisitos de seguridad
  HU-O09.3   Sistema        subir el backup encriptado a cold storage           minimizar el costo de almacenamiento
  HU-O09.4   SRE            ejecutar una restauración de prueba semanal         validar que el backup es íntegro
  HU-O09.5   SRE            registrar un log de éxito o fallo de cada restore   auditar la efectividad del proceso

------------------------------------------------------------------------

## CU-O10: Revisar Error Budget y Congelar Deploys

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | SRE / DevOps                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Revisión semanal de SLI/SLO.                       |
+-----------------+----------------------------------------------------+
| Precondición    | El sistema calcula el SLI de uptime de los últimos |
|                 | 30 días.                                           |
+-----------------+----------------------------------------------------+
| Flujo Principal | Compara contra el SLO del 99.99%. Computa el error |
|                 | budget consumido. Si supera el 80% congela         |
|                 | automáticamente el pipeline CI/CD. Notifica al CTO |
|                 | y team leads.                                      |
+-----------------+----------------------------------------------------+
| Postcondición   | riesgo controlado.                                 |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                             **Para\...**
  ---------- -------------- --------------------------------------------------------- ----------------------------------------------
  HU-O10.1   SRE            calcular el SLI de uptime de los últimos 30 días          evaluar la confiabilidad real
  HU-O10.2   Sistema        computar el error budget consumido en minutos             compararlo contra el umbral
  HU-O10.3   SRE            comparar el consumo contra el umbral del 80%              decidir si se debe congelar
  HU-O10.4   Sistema        congelar automáticamente el pipeline de CI/CD             evitar nuevos deploys que aumenten el riesgo
  HU-O10.5   Sistema        notificar a todos los stakeholders sobre la congelación   coordinar las acciones de remediación

------------------------------------------------------------------------

## CU-O11: Publicar Changelog Semanal en Developer Portal

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Developer Advocate                                 |
+-----------------+----------------------------------------------------+
| Propósito       | Comunicar cambios de API a desarrolladores.        |
+-----------------+----------------------------------------------------+
| Precondición    | El sistema recolecta commits desde el último       |
|                 | release.                                           |
+-----------------+----------------------------------------------------+
| Flujo Principal | Categoriza cada cambio como feature, fix o         |
|                 | breaking. Genera un changelog con Semantic         |
|                 | Versioning. Publica en el portal. Envía email a    |
|                 | suscriptores.                                      |
+-----------------+----------------------------------------------------+
| Postcondición   | changelog publicado.                               |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**         **Deseo\...**                                                **Para\...**
  ---------- -------------------- ------------------------------------------------------------ ---------------------------------------
  HU-O11.1   Developer Advocate   recolectar commits automáticamente desde el último release   ahorrar tiempo manual
  HU-O11.2   Sistema              categorizar cada commit por tipo                             estructurar el changelog
  HU-O11.3   Developer Advocate   generar la nueva versión siguiendo Semantic Versioning       comunicar claramente el impacto
  HU-O11.4   Sistema              publicar el changelog en el Developer Portal                 que los desarrolladores lo consulten
  HU-O11.5   Sistema              enviar un email con el changelog a los suscriptores          mantenerlos informados proactivamente

------------------------------------------------------------------------

## CU-O12: Rotar Credenciales y Auditar Accesos IAM

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | SRE / DevOps                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Rotación mensual de secretos y auditoría           |
|                 | trimestral.                                        |
+-----------------+----------------------------------------------------+
| Precondición    | El sistema identifica credenciales próximas a      |
|                 | expirar.                                           |
+-----------------+----------------------------------------------------+
| Flujo Principal | Genera nuevas credenciales en el vault. Actualiza  |
|                 | los servicios con las nuevas. Verifica que todo    |
|                 | funcione. Desactiva las credenciales antiguas tras |
|                 | un período de gracia de 24 horas. Loggea toda la   |
|                 | operación.                                         |
+-----------------+----------------------------------------------------+
| Postcondición   | credenciales rotadas.                              |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                             **Para\...**
  ---------- -------------- ------------------------------------------------------------------------- -------------------------------------------
  HU-O12.1   SRE            rotar las API Keys de los clientes mensualmente                           reducir la ventana de exposición
  HU-O12.2   Sistema        actualizar los secrets en K8s automáticamente                             que los pods usen las nuevas credenciales
  HU-O12.3   SRE            verificar que todos los servicios funcionen con las nuevas credenciales   evitar disrupciones
  HU-O12.4   Sistema        desactivar las credenciales antiguas tras 24 horas                        completar la rotación
  HU-O12.5   CTO            generar una auditoría IAM trimestral con todos los accesos                revisar y revocar los innecesarios

------------------------------------------------------------------------

## CU-O13: Realizar Post-Mortem de Incidente

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | SRE / DevOps                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Análisis blameless post-incidente Sev1/Sev2.       |
+-----------------+----------------------------------------------------+
| Precondición    | Tras resolver un incidente, el SRE agenda una      |
|                 | reunión blameless.                                 |
+-----------------+----------------------------------------------------+
| Flujo Principal | El sistema genera automáticamente un timeline      |
|                 | completo. Se identifica la root cause con la       |
|                 | técnica de los 5 whys. Se documentan los           |
|                 | aprendizajes. Se crean tickets de acción. Se       |
|                 | publica el reporte en la wiki.                     |
+-----------------+----------------------------------------------------+
| Postcondición   | aprendizajes documentados.                         |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                   **Para\...**
  ---------- -------------- --------------------------------------------------------------- ---------------------------------------------------
  HU-O13.1   Sistema        generar un timeline automático del incidente                    reconstruir la secuencia exacta
  HU-O13.2   SRE            documentar qué funcionó bien y qué no durante la respuesta      mejorar los runbooks
  HU-O13.3   SRE            identificar la root cause utilizando la técnica de los 5 whys   prevenir recurrencia
  HU-O13.4   SRE            crear tickets de acción en Linear desde el post-mortem          asegurar seguimiento
  HU-O13.5   SRE            publicar el post-mortem en la wiki interna                      compartir el aprendizaje con toda la organización

------------------------------------------------------------------------

## CU-O14: Documentar FAQ en Base de Conocimientos del Chatbot

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Developer Advocate                                 |
+-----------------+----------------------------------------------------+
| Propósito       | Alimentar knowledge base desde tickets resueltos.  |
+-----------------+----------------------------------------------------+
| Precondición    | El sistema detecta un tema recurrente al           |
|                 | acumularse 3 o más tickets similares.              |
+-----------------+----------------------------------------------------+
| Flujo Principal | Sugiere un borrador de FAQ. El Developer Advocate  |
|                 | revisa, edita y publica con screenshots. Actualiza |
|                 | los embeddings del chatbot. Mide la tasa de        |
|                 | deflexión resultante.                              |
+-----------------+----------------------------------------------------+
| Postcondición   | KB enriquecida.                                    |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**         **Deseo\...**                                                          **Para\...**
  ---------- -------------------- ---------------------------------------------------------------------- ------------------------------------
  HU-O14.1   Sistema              detectar temas recurrentes cuando aparecen 3 o más tickets similares   proponer nueva documentación
  HU-O14.2   Sistema              generar un borrador de FAQ automáticamente                             agilizar la redacción
  HU-O14.3   Developer Advocate   revisar el borrador y publicarlo                                       garantizar calidad editorial
  HU-O14.4   Sistema              actualizar los embeddings del chatbot con la nueva FAQ                 mejorar la precisión de respuestas
  HU-O14.5   Developer Advocate   medir la tasa de deflexión después de publicar la FAQ                  evaluar su efectividad

------------------------------------------------------------------------

# Casos de Uso Operativos Adicionales

## CU-O15: Gestionar Sprint en Linear

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Todo el equipo de ingeniería                       |
+-----------------+----------------------------------------------------+
| Propósito       | Gestionar el backlog, planificar sprints y medir   |
|                 | la productividad del equipo.                       |
+-----------------+----------------------------------------------------+
| Precondición    | Los leads de equipo crean tickets de trabajo en    |
|                 | Linear desde el roadmap priorizado.                |
+-----------------+----------------------------------------------------+
| Flujo Principal | Cada sprint de 2 semanas inicia con planning       |
|                 | meeting para asignar estimaciones. Diariamente     |
|                 | cada miembro actualiza el estado de sus tickets en |
|                 | Slack standup. Al cierre del sprint se realiza     |
|                 | retrospectiva con revisión de velocity y burndown. |
|                 | Los aprendizajes se documentan y se ajusta el      |
|                 | backlog del siguiente sprint.                      |
+-----------------+----------------------------------------------------+
| Postcondición   | sprint cerrado con métricas y aprendizajes         |
|                 | documentados.                                      |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**    **Deseo\...**                                                       **Para\...**
  ---------- --------------- ------------------------------------------------------------------- --------------------------------------------------
  HU-O15.1   Tech Lead       crear tickets de trabajo con título, descripción y prioridad RICE   que el equipo tenga claridad sobre qué construir
  HU-O15.2   Desarrollador   actualizar el estado de mis tickets desde Slack sin abrir Linear    reducir el cambio de contexto
  HU-O15.3   Tech Lead       visualizar el burndown chart en tiempo real durante el sprint       identificar riesgos de entrega a tiempo
  HU-O15.4   Tech Lead       documentar los aprendizajes de la retrospectiva en la wiki          que el equipo no repita los mismos errores
  HU-O15.5   CTO             ver un dashboard de velocity y cycle time por equipo                evaluar la productividad y predecir entregables

------------------------------------------------------------------------

## CU-O16: Validar Especificaciones OpenAPI en CI/CD

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CTO / SRE                                          |
+-----------------+----------------------------------------------------+
| Propósito       | Asegurar que todas las especificaciones de API     |
|                 | cumplan el estándar OpenAPI 3.1.                   |
+-----------------+----------------------------------------------------+
| Precondición    | Al abrir un PR que modifique archivos .yaml de     |
|                 | especificación, el pipeline de CI/CD ejecuta       |
|                 | Spectral linter automáticamente.                   |
+-----------------+----------------------------------------------------+
| Flujo Principal | Verifica reglas: todos los endpoints tienen        |
|                 | descripción y ejemplos, no hay breaking changes    |
|                 | sin bump de versión major, los schemas de          |
|                 | request/response son válidos. Si hay errores, el   |
|                 | PR se bloquea hasta que se corrijan.               |
+-----------------+----------------------------------------------------+
| Postcondición   | spec validada y conforme al estándar.              |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**         **Deseo\...**                                                        **Para\...**
  ---------- -------------------- -------------------------------------------------------------------- ----------------------------------------------------
  HU-O16.1   CTO                  ejecutar un linter automático sobre cada spec OpenAPI en el PR       evitar que specs no conformes lleguen a producción
  HU-O16.2   Desarrollador        ver los errores de lint en el diff del PR                            corregirlos antes de pedir revisión
  HU-O16.3   Sistema              detectar automáticamente breaking changes comparando specs           exigir un bump de versión major
  HU-O16.4   Developer Advocate   verificar que todos los endpoints tengan ejemplos request/response   garantizar documentación completa
  HU-O16.5   CTO                  bloquear el merge si el linter encuentra errores                     mantener la calidad del contrato de API

------------------------------------------------------------------------

## CU-O17: Validar Data Contracts en Pipeline ETL

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | Data Engineer                                      |
+-----------------+----------------------------------------------------+
| Propósito       | Asegurar que los datos externos cumplan los        |
|                 | contratos de schema definidos.                     |
+-----------------+----------------------------------------------------+
| Precondición    | El Data Engineer define y versiona en Git los      |
|                 | schema contracts para cada fuente de datos         |
|                 | (proveedor aeronáutico, meteorología, etc.).       |
+-----------------+----------------------------------------------------+
| Flujo Principal | El pipeline de ingesta ejecuta validación          |
|                 | automática contra el contrato antes de cargar a    |
|                 | staging: tipos de datos, nulabilidad de columnas   |
|                 | críticas, rangos de valores plausibles y           |
|                 | estructura del archivo. Si hay schema drift del    |
|                 | proveedor, se alerta inmediatamente y se pausa la  |
|                 | ingesta.                                           |
+-----------------+----------------------------------------------------+
| Postcondición   | datos validados contra contrato o ingesta pausada  |
|                 | con alerta.                                        |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**    **Deseo\...**                                                                   **Para\...**
  ---------- --------------- ------------------------------------------------------------------------------- ----------------------------------------
  HU-O17.1   Data Engineer   definir el schema contract de cada fuente en un archivo YAML versionado         tener trazabilidad de cambios
  HU-O17.2   Sistema         validar que los datos entrantes cumplan el contrato antes de cargar a staging   evitar corrupción downstream
  HU-O17.3   Data Engineer   recibir una alerta si el proveedor cambió el schema sin notificar               actualizar el pipeline oportunamente
  HU-O17.4   Sistema         pausar la ingesta automáticamente si la validación de contrato falla            prevenir cascada de errores
  HU-O17.5   CTO             ver un dashboard de conformidad de data contracts por fuente                    monitorear la estabilidad del pipeline

------------------------------------------------------------------------

## CU-O18: Ejecutar Pipeline de Seguridad SAST/DAST en CI/CD

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | SRE / DevOps                                       |
+-----------------+----------------------------------------------------+
| Propósito       | Detectar vulnerabilidades de seguridad de forma    |
|                 | automática en cada cambio de código.               |
+-----------------+----------------------------------------------------+
| Precondición    | En cada PR, el pipeline de CI/CD ejecuta SonarQube |
|                 | para análisis estático de código (SAST) y lanza un |
|                 | escaneo con OWASP ZAP contra una instancia efímera |
|                 | del servicio modificado (DAST).                    |
+-----------------+----------------------------------------------------+
| Flujo Principal | Si se detectan vulnerabilidades con severidad      |
|                 | critical o high, el PR se bloquea y se notifica al |
|                 | autor. El reporte de seguridad se adjunta al       |
|                 | release.                                           |
+-----------------+----------------------------------------------------+
| Postcondición   | código validado sin vulnerabilidades críticas en   |
|                 | el diff.                                           |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**    **Deseo\...**                                                           **Para\...**
  ---------- --------------- ----------------------------------------------------------------------- ---------------------------------------------------
  HU-O18.1   SRE             ejecutar SonarQube automáticamente en cada PR                           detectar vulnerabilidades antes del merge
  HU-O18.2   SRE             lanzar un escaneo OWASP ZAP contra una instancia efímera del servicio   detectar vulnerabilidades en tiempo de ejecución
  HU-O18.3   Desarrollador   ver el resultado del escaneo directamente en el PR                      corregir issues antes de que se bloquee el merge
  HU-O18.4   Sistema         bloquear automáticamente el merge si hay vulnerabilidades críticas      evitar que el código inseguro llegue a producción
  HU-O18.5   CTO             generar un reporte de seguridad firmado por release                     presentarlo como evidencia en auditorías SOC 2

------------------------------------------------------------------------

## CU-O19: Analizar y Optimizar Costos Cloud

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | CTO / SRE                                          |
+-----------------+----------------------------------------------------+
| Propósito       | Monitorear, analizar y reducir el gasto en         |
|                 | infraestructura cloud.                             |
+-----------------+----------------------------------------------------+
| Precondición    | Semanalmente, el SRE audita la factura cloud       |
|                 | desglosada por servicio.                           |
+-----------------+----------------------------------------------------+
| Flujo Principal | El sistema compara el gasto real contra el         |
|                 | forecast mensual y detecta anomalías con un        |
|                 | algoritmo de desviación estándar. Identifica       |
|                 | recursos ociosos (instancias sin tráfico,          |
|                 | volúmenes no adjuntos, IPs no asignadas) y         |
|                 | recursos sobre-aprovisionados. Genera un reporte   |
|                 | con recomendaciones de rightsizing, reserved       |
|                 | instances y eliminación de waste. El CTO revisa y  |
|                 | aprueba las acciones.                              |
+-----------------+----------------------------------------------------+
| Postcondición   | gasto cloud optimizado y documentado.              |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                              **Para\...**
  ---------- -------------- -------------------------------------------------------------------------- --------------------------------------------------
  HU-O19.1   CTO            visualizar los costos desglosados por servicio cloud en tiempo real        identificar los mayores drivers de gasto
  HU-O19.2   SRE            recibir una alerta si el gasto diario se desvía más del 20% del forecast   investigar fugas a tiempo
  HU-O19.3   Sistema        detectar automáticamente recursos cloud ociosos                            proponer su eliminación o redimensionamiento
  HU-O19.4   SRE            generar recomendaciones de ahorro con estimación de impacto                priorizar las de mayor retorno
  HU-O19.5   CTO            comparar la tendencia mensual de costos contra el presupuesto              tomar decisiones de inversión en infraestructura

------------------------------------------------------------------------

## CU-O20: Ejecutar Experimentos de Deep Learning

+-----------------+----------------------------------------------------+
|                 |                                                    |
+:================+:===================================================+
| Actor Principal | ML Engineer                                        |
+-----------------+----------------------------------------------------+
| Propósito       | Explorar y validar técnicas de Deep Learning para  |
|                 | OCR documental y Speech-to-Text.                   |
+-----------------+----------------------------------------------------+
| Precondición    | El ML Engineer diseña experimentos de DL en        |
|                 | sprints de experimentación de 4 semanas.           |
+-----------------+----------------------------------------------------+
| Flujo Principal | Para OCR: entrena modelos con redes neuronales     |
|                 | (CRNN/TrOCR) sobre documentos de compliance,       |
|                 | facturas de proveedores y logs de auditoría        |
|                 | escaneados. Para Speech-to-Text: despliega modelos |
|                 | Whisper/DeepSpeech, integra con el pipeline de     |
|                 | grabación de entrevistas de feedback y mide Word   |
|                 | Error Rate. Todos los experimentos se registran en |
|                 | MLflow con hiperparámetros, métricas y artefactos. |
|                 | Se comparan contra baseline y se decide si         |
|                 | promover a desarrollo de producto.                 |
+-----------------+----------------------------------------------------+
| Postcondición   | experimentos documentados con recomendación        |
|                 | go/no-go.                                          |
+-----------------+----------------------------------------------------+

  **ID**     **Como\...**   **Deseo\...**                                                                  **Para\...**
  ---------- -------------- ------------------------------------------------------------------------------ ---------------------------------------------------
  HU-O20.1   ML Engineer    entrenar un modelo OCR sobre documentos de compliance escaneados               automatizar la extracción de datos para auditoría
  HU-O20.2   ML Engineer    comparar la precisión del OCR automático contra la entrada manual              decidir si es viable para producción
  HU-O20.3   ML Engineer    desplegar un modelo Whisper para transcripción de entrevistas de feedback      extraer texto de las grabaciones
  HU-O20.4   ML Engineer    medir el Word Error Rate del transcriptor contra transcripciones manuales      validar la calidad del modelo
  HU-O20.5   ML Engineer    loguear métricas, hiperparámetros y artefactos de cada experimento en MLflow   tener trazabilidad completa del proceso de I+D

------------------------------------------------------------------------

::: center
SkyAnalytics Inc. -- Perfil EstratÃ©gico Corporativo Â· Documento
Integral Â· 2026
:::
