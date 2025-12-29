from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    email: str = Field(
        sa_column=Column(String, unique=True, index=True, nullable=False)
    )

    hashed_password: str = Field(nullable=False)

    name: str
    age: int | None = None

    