from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError

from app.db.session import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserRead

from typing import List

router = APIRouter(
    prefix="/users",
    tags=["User"]
)

@router.post("/", response_model=UserRead)
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session)
):
    db_user = User(**user.dict())
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

@router.get("/", response_model=list[UserRead])
def list_user(
    session: Session = Depends(get_session)
):
    users = session.exec(select(User)).all()
    return users