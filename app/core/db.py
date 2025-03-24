from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

from app.core.config import settings

engine = create_engine(
    f"postgresql+psycopg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_PORT}:{settings.DB_PORT}/{settings.DB_NAME}"
)

Base = declarative_base()


def create_db_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
