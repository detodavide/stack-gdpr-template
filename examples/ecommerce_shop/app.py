from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Base, User, Product, Order, get_db
from .schemas import UserCreate, UserOut, ProductCreate, ProductOut, OrderCreate, OrderOut
from .gdpr import export_user_data, log_audit
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Ecommerce Shop Example", description="GDPR-compliant ecommerce example.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User.create(db, user)
    log_audit(db_user.id, "User registered")
    return db_user

@app.post("/products/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product.create(db, product)
    log_audit(db_product.id, "Product created")
    return db_product

@app.get("/products/", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return Product.list(db)

@app.post("/orders/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order.create(db, order)
    log_audit(db_order.user_id, "Order placed")
    return db_order

@app.get("/orders/", response_model=list[OrderOut])
def list_orders(db: Session = Depends(get_db)):
    return Order.list(db)

@app.get("/gdpr/export")
def gdpr_export(user_id: int, db: Session = Depends(get_db)):
    data = export_user_data(db, user_id)
    log_audit(user_id, "GDPR export")
    return data

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
