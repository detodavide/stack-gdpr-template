from .models import User, Order, Product
import json
import datetime

def export_user_data(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    if not user:
        return {"error": "User not found"}
    data = {
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "consent": user.consent
        },
        "orders": [
            {"id": o.id, "product_id": o.product_id, "quantity": o.quantity, "created_at": o.created_at.isoformat()} for o in orders
        ]
    }
    return data

def log_audit(user_id, action):
    with open("audit.log", "a") as f:
        f.write(f"{datetime.datetime.utcnow().isoformat()} | user_id={user_id} | {action}\n")
