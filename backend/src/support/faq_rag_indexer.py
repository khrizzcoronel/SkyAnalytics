import hashlib

class RAGIndexer:
    def __init__(self):
        self.vector_db = {}
        
    def index_article(self, title: str, content: str):
        print(f"\n[RAG INDEXER] Generando Embeddings (text-embedding-ada-002) para: '{title}'...")
        
        # Simulamos un embedding calculando un hash
        vector_id = hashlib.md5(title.encode()).hexdigest()
        
        # Guardamos en la base vectorial simulada
        self.vector_db[vector_id] = {
            "title": title,
            "content": content,
            "keywords": title.lower().split()
        }
        print(f"[RAG INDEXER] Articulo guardado en Base Vectorial. Pinecone ID: {vector_id}")

    def query_chatbot(self, question: str):
        print(f"\n--- USER CHAT: '{question}' ---")
        question_lower = question.lower()
        
        # Búsqueda semántica (Simulada por match de keywords)
        best_match = None
        for v_id, data in self.vector_db.items():
            if any(kw in question_lower for kw in data["keywords"]):
                best_match = data
                break
                
        if best_match:
            print(f"[AI BOT]: Segun nuestra base de conocimientos en '{best_match['title']}', la respuesta es:")
            print(f"   > {best_match['content']}")
            print(f"[METRICA] Deflection Rate: Resolucion autonoma exitosa (Evito creacion de ticket).")
        else:
            print(f"[AI BOT]: No tengo informacion sobre eso en mi contexto actual. Transfiriendo con un agente humano...")
            print(f"[METRICA] Escalamiento a Soporte L1 (CU-O08).")

if __name__ == "__main__":
    bot = RAGIndexer()
    
    # Customer Success publica un nuevo articulo
    bot.index_article("GraphQL", "Para migrar a GraphQL, cambia tu endpoint a /v2/graphql y envia un query { flights { id } }.")
    
    # Chatbot es capaz de responder preguntas relacionadas (Deflection)
    bot.query_chatbot("Como migro mi API a GraphQL?")
    
    # Chatbot falla si no tiene contexto (Alucinacion evitada)
    bot.query_chatbot("Como cancelo mi subscripcion de pago?")
