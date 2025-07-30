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

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    created_at: str

    class Config:
        orm_mode = True
