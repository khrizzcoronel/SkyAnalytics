## Context
Necesitamos actualizar la "memoria" del Chatbot en cuanto se publica un FAQ.

## Decisions
- Crearemos `backend/src/support/faq_rag_indexer.py`.
- Generaremos un Hash del texto para simular un Vector/Embedding de OpenAI.
- Simular un almacenamiento en Base de Datos Vectorial.
- Simular una consulta de usuario donde el chatbot responde usando el texto indexado.
