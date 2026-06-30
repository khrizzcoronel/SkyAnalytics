"""
FAQ Knowledge Base service for the AI chatbot.

Manages FAQ articles and computes a simple deflection metric. Embedding
storage is abstracted so a real vector DB (Pinecone/Weaviate) can be wired in.
"""
from dataclasses import dataclass, field
from typing import List, Optional, Protocol


class EmbeddingStore(Protocol):
    def add(self, article_id: str, text: str, embedding: List[float], source_url: str) -> None: ...
    def search(self, query_embedding: List[float], top_k: int = 3) -> List[dict]: ...


@dataclass
class FAQArticle:
    article_id: str
    title: str
    markdown: str
    source_url: str
    embedding: Optional[List[float]] = None


@dataclass
class ChatbotInteraction:
    query: str
    resolved: bool
    source_url: Optional[str] = None


class FAQKnowledgeBase:
    """In-memory FAQ knowledge base with optional vector store backend."""

    def __init__(self, embedding_store: Optional[EmbeddingStore] = None):
        self._articles: dict[str, FAQArticle] = {}
        self._store = embedding_store
        self._interactions: List[ChatbotInteraction] = []

    def add_article(
        self,
        article: FAQArticle,
        embedding: Optional[List[float]] = None,
    ) -> None:
        article.embedding = embedding or self._fake_embedding(article.markdown)
        self._articles[article.article_id] = article
        if self._store:
            self._store.add(
                article.article_id,
                article.markdown,
                article.embedding,
                article.source_url,
            )

    def answer(
        self,
        query: str,
        top_k: int = 3,
    ) -> ChatbotInteraction:
        """Simulated RAG response. Returns resolved if a matching article exists."""
        query_lower = query.lower()
        for article in self._articles.values():
            if any(word in query_lower for word in article.title.lower().split()):
                return ChatbotInteraction(
                    query=query, resolved=True, source_url=article.source_url
                )
        if self._store:
            results = self._store.search(self._fake_embedding(query), top_k=top_k)
            if results:
                return ChatbotInteraction(
                    query=query, resolved=True, source_url=results[0].get("source_url")
                )
        return ChatbotInteraction(query=query, resolved=False)

    def record_interaction(self, interaction: ChatbotInteraction) -> None:
        self._interactions.append(interaction)

    def deflection_rate(self) -> float:
        if not self._interactions:
            return 0.0
        resolved = sum(1 for i in self._interactions if i.resolved)
        return (resolved / len(self._interactions)) * 100

    def knowledge_gaps(self, threshold: int = 3) -> List[str]:
        """Return repeated unresolved queries that suggest a new FAQ is needed."""
        unresolved: dict[str, int] = {}
        for interaction in self._interactions:
            if not interaction.resolved:
                unresolved[interaction.query] = unresolved.get(interaction.query, 0) + 1
        return [query for query, count in unresolved.items() if count >= threshold]

    @staticmethod
    def _fake_embedding(text: str) -> List[float]:
        """Deterministic pseudo-embedding for tests and demos."""
        base = [ord(c) % 10 for c in text[:64].ljust(64, " ")]
        norm = sum(x * x for x in base) ** 0.5 or 1
        return [x / norm for x in base]
