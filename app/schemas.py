from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
