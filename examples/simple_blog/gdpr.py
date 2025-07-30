from .models import User, Post
import json
import datetime

def export_user_data(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    posts = db.query(Post).filter(Post.author_id == user_id).all()
    if not user:
        return {"error": "User not found"}
    data = {
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "consent": user.consent
        },
        "posts": [
            {"id": p.id, "title": p.title, "content": p.content, "created_at": p.created_at.isoformat()} for p in posts
        ]
    }
    return data

def log_audit(user_id, action):
    with open("audit.log", "a") as f:
        f.write(f"{datetime.datetime.utcnow().isoformat()} | user_id={user_id} | {action}\n")
