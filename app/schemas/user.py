from sqlmodel import SQLModel, Field

class UserCreate(SQLModel):
    email: str
    password: str = Field(min_length=8, max_length=64)
    name: str
    age: int | None = None

class UserRead(SQLModel):
    id: int
    email: str
    name: str
    age: int | None = None