# Especificación de Caso de Uso: CU-O14

## 1. Nombre de la Funcionalidad
**Documentar FAQ en Base de Conocimientos del Chatbot**

## 2. Objetivo
Alimentar y mantener actualizada la base de conocimientos (Knowledge Base - KB) que utiliza el Agente Virtual / Chatbot basado en IA, con el fin de resolver de manera autónoma (Deflection Rate) consultas frecuentes (FAQ) y dudas de integración de Nivel 1.

## 3. Actores Involucrados
*   **Actor Principal:** Customer Success / Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** Motor de IA Conversacional (ej. OpenAI / LangChain), Base de Datos Vectorial (Pinecone / Weaviate).

## 4. Contexto del Problema
A medida que aumenta el número de Beta Testers y clientes B2B, las consultas repetitivas de Nivel 1 ("¿Cómo reinicio mi API Key?", "¿Cuál es el límite del plan Pro?") consumen tiempo valioso del equipo técnico. Un Chatbot basado en Modelos de Lenguaje Grande (LLMs) y Retrieval-Augmented Generation (RAG) puede responder esto automáticamente, pero necesita que el equipo le provea el contexto correcto.

## 5. Requisitos Funcionales
*   **RF-O14-001:** El sistema debe permitir a Customer Success ingresar artículos de FAQ en formato Markdown a través del CMS (Mintlify o interno).
*   **RF-O14-002:** El sistema debe procesar automáticamente cada nuevo artículo de FAQ, generar sus *Embeddings* vectoriales (vía OpenAI de text-embedding-ada-002) y almacenarlos en la base de datos vectorial (Pinecone).
*   **RF-O14-003:** El sistema debe proveer una métrica de "Deflection Rate" (Tasa de desviación): porcentaje de conversaciones que el Chatbot resolvió exitosamente sin requerir intervención de un agente humano.
*   **RF-O14-004:** El sistema debe alertar a Customer Success si el Chatbot responde frecuentemente "No tengo información sobre eso" sobre un tema particular, sugiriendo la creación de un nuevo FAQ.

## 6. Requisitos No Funcionales
*   **RNF-O14-001 (Frescura del Bot):** Cuando se añade o modifica un FAQ, los nuevos *embeddings* deben propagarse y estar disponibles para respuestas del Chatbot en menos de 5 minutos.
*   **RNF-O14-002 (Precisión / Alucinaciones):** El Chatbot debe operar con una temperatura baja (ej. 0.1) y bajo estricto modo RAG. Jamás debe inventar información sobre precios o SLAs que no esté explícitamente en la Base de Datos Vectorial.

## 7. Reglas de Negocio
*   **RN-O14-001 (Límite de la IA):** Si el Chatbot no logra resolver el problema tras 2 interacciones fallidas (o el usuario escribe "hablar con humano"), el ticket se transfiere inmediatamente al CU-O08 (Atender Ticket de Bug) y el bot se silencia.

## 8. Entradas
*   Texto Markdown del nuevo artículo de FAQ o resolución de un bug reciente.
*   Interacciones previas del usuario (Logs del chat).

## 9. Salidas
*   **Base Vectorial:** Nodos de contexto actualizados.
*   **Chat UI:** Respuesta en lenguaje natural generada por el Bot hacia el usuario.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Creación de FAQ y resolución automática
**Dado** que Customer Success nota 5 tickets preguntando cómo migrar de API REST a GraphQL
**Cuando** redacta y publica el artículo "Guía de Migración a GraphQL" en la base de conocimientos
**Entonces** el pipeline vectorial genera y guarda los embeddings
**Y** cuando el próximo usuario pregunta al Chatbot "How do I switch to GraphQL?"
**Y** el Chatbot lee la base vectorial y formula una respuesta técnica correcta y un enlace al nuevo FAQ, resolviendo la duda sin levantar ticket.

## 11. Criterios de Aceptación
*   **CA-O14-001:** Las respuestas del Chatbot siempre deben incluir una citación o hipervínculo a la fuente original del artículo del Developer Portal en la que basaron su respuesta.

## 12. Restricciones
*   El Bot de IA no tiene ni debe tener permisos de escritura sobre bases de datos transaccionales, ni puede modificar la cuenta de un usuario por su cuenta (Operaciones de solo lectura para soporte).

## 13. Fuera de Alcance
*   Atención y triage de bugs complejos (Si el usuario pega un *stack trace* con un error HTTP 500, el Bot debe escalar automáticamente el ticket, no intentar diagnosticarlo).
