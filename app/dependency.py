from fastapi import Depends
from langchain_core.language_models import BaseChatModel
from sqlalchemy.orm import Session

from app.core.db import create_db_session
from app.core.llm import create_llm

db_session: Session = Depends(create_db_session)
llm: BaseChatModel = Depends(create_llm)
