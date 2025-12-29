from sqlmodel import SQLModel

class UserCreate(SQLModel):
    email: str
    password: str
    name: str
    age: str

class UserRead(SQLModel):
    id: str
    email: str
    name: str
    age: int