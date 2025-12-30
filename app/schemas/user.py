from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=8, max_length=64)
    name: str
    age: int | None = None

class UserRead(BaseModel):
    id: int
    email: str
    name: str
    age: int | None = None