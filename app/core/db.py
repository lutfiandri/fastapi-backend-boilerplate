from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

from app.core.config import settings

db_uri = f"postgresql+psycopg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_engine(db_uri)

Base = declarative_base()


def create_db_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
