from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Base, User, Post, get_db
from .schemas import UserCreate, UserOut, PostCreate, PostOut
from .gdpr import export_user_data, log_audit
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Simple Blog Example", description="GDPR-compliant blog example.")

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

@app.post("/posts/", response_model=PostOut)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post.create(db, post)
    log_audit(db_post.author_id, "Post created")
    return db_post

@app.get("/posts/", response_model=list[PostOut])
def list_posts(db: Session = Depends(get_db)):
    return Post.list(db)

@app.get("/gdpr/export")
def gdpr_export(user_id: int, db: Session = Depends(get_db)):
    data = export_user_data(db, user_id)
    log_audit(user_id, "GDPR export")
    return data

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
