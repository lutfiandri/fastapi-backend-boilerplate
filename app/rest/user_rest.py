from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class CreateUserRequest(UserBase):
    pass


class UpdateUserRequest(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Enables ORM mode
