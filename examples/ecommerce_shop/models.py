from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine
import datetime

Base = declarative_base()
engine = create_engine("sqlite:///shop.db")
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    consent = Column(String, default="accepted")
    orders = relationship("Order", back_populates="user")

    @staticmethod
    def create(db, user):
        db_user = User(email=user.email, name=user.name, consent=user.consent)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    price = Column(Float)

    @staticmethod
    def create(db, product):
        db_product = Product(name=product.name, description=product.description, price=product.price)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def list(db):
        return db.query(Product).all()

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="orders")
    product = relationship("Product")

    @staticmethod
    def create(db, order):
        db_order = Order(user_id=order.user_id, product_id=order.product_id, quantity=order.quantity)
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order

    @staticmethod
    def list(db):
        return db.query(Order).all()

Base.metadata.create_all(bind=engine)
