from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import mapped_column

from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    created_at = mapped_column(DateTime, nullable=False)
    updated_at = mapped_column(DateTime, nullable=False)
