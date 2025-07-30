from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine
import datetime

Base = declarative_base()
engine = create_engine("sqlite:///blog.db")
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
    posts = relationship("Post", back_populates="author")

    @staticmethod
    def create(db, user):
        db_user = User(email=user.email, name=user.name, consent=user.consent)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

    @staticmethod
    def create(db, post):
        db_post = Post(title=post.title, content=post.content, author_id=post.author_id)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    @staticmethod
    def list(db):
        return db.query(Post).all()

Base.metadata.create_all(bind=engine)
