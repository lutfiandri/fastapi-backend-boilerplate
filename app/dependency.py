from fastapi import Depends
from langchain_core.language_models import BaseChatModel

from app.core.llm import create_llm

llm: BaseChatModel = Depends(create_llm)
