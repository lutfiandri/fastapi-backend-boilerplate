from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.dependency import db_session
from app.model.user import User
from app.rest.user_rest import (
    CreateUserRequest,
    UpdateUserRequest,
    UserResponse,
)

router = APIRouter(prefix="/api/users", tags=["users"])


@router.post("/", response_model=UserResponse)
async def create_user(
    request: CreateUserRequest, db_session: Session = db_session
) -> UserResponse:
    new_user = User(name=request.name)

    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)

    return UserResponse.model_validate(new_user)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int, db_session: Session = db_session
) -> UserResponse:
    user = db_session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse.model_validate(user)


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int, request: UpdateUserRequest, db_session: Session = db_session
) -> UserResponse:
    user = db_session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = request.name
    db_session.commit()
    db_session.refresh(user)

    return UserResponse.model_validate(user)


@router.delete("/{user_id}")
async def delete_user(user_id: int, db_session: Session = db_session):
    user = db_session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_session.delete(user)
    db_session.commit()
