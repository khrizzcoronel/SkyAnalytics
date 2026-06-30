from src.support.faq_kb import FAQKnowledgeBase, FAQArticle, ChatbotInteraction


def test_faq_resolves_known_question():
    kb = FAQKnowledgeBase()
    kb.add_article(
        FAQArticle(
            article_id="faq-1",
            title="Reset API Key",
            markdown="To reset your API key, go to settings...",
            source_url="https://docs.skyanalytics.com/reset-api-key",
        )
    )
    answer = kb.answer("How do I reset my API key?")
    assert answer.resolved
    assert answer.source_url == "https://docs.skyanalytics.com/reset-api-key"


def test_unknown_query_returns_unresolved():
    kb = FAQKnowledgeBase()
    answer = kb.answer("What is the meaning of life?")
    assert not answer.resolved


def test_deflection_rate_calculation():
    kb = FAQKnowledgeBase()
    kb.record_interaction(ChatbotInteraction(query="q1", resolved=True))
    kb.record_interaction(ChatbotInteraction(query="q2", resolved=True))
    kb.record_interaction(ChatbotInteraction(query="q3", resolved=False))
    assert kb.deflection_rate() == (2 / 3) * 100


def test_knowledge_gap_detection():
    kb = FAQKnowledgeBase()
    for _ in range(3):
        kb.record_interaction(ChatbotInteraction(query="GraphQL migration", resolved=False))
    gaps = kb.knowledge_gaps(threshold=3)
    assert "GraphQL migration" in gaps
