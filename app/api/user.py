from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError

from app.db.session import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserRead

from typing import List

from app.core.security import hash_password, get_current_user

router = APIRouter(
    prefix="/users",
    tags=["User"]
)

@router.post("/", response_model=UserRead)
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session)
):
    db_user = User(
        email=user.email,
        name=user.name,
        age=user.age,
        hashed_password=hash_password(user.password),
    )

    session.add(db_user)
    
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )
    
    session.refresh(db_user)
    return db_user

@router.get("/me", response_model=UserRead)
def read_me(
    current_user: User = Depends(get_current_user)
):
    return current_user