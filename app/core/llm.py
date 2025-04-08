from langchain_google_vertexai import VertexAI

from app.core.config import settings


def create_llm():
    """Create a language model instance."""
    return VertexAI(
        model=settings.DEFAULT_MODEL,
        temperature=settings.DEFAULT_TEMPERATURE,
    )
