---
module: 07-soporte
primary_user: CUSTOMER_SUCCESS
---
## ADDED Requirements

### Requirement: Indexación RAG
El sistema MUST convertir el texto del FAQ en vectores para habilitar búsqueda semántica por el Chatbot.

#### Scenario: Chatbot responde FAQ
- **WHEN** el usuario pregunta "Como migro a GraphQL"
- **THEN** el Chatbot recupera el artículo vectorial `Guía de Migración a GraphQL` y formula la respuesta sin abrir un ticket.
