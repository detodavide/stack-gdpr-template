from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name: str
    consent: str = "accepted"

class UserOut(BaseModel):
    id: int
    email: str
    name: str
    consent: str

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    created_at: str

    class Config:
        orm_mode = True
