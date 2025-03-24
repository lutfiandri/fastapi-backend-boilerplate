from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from app.core.config import settings


def create_llm() -> BaseChatModel:
    """Create a language model instance."""
    return ChatOpenAI(
        model=settings.DEFAULT_MODEL,
        temperature=settings.DEFAULT_TEMPERATURE,
    )
