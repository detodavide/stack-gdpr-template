# Simple Blog Example

This is a minimal example of a GDPR-compliant blog using the stack template. It demonstrates core features: user registration, post creation, GDPR data export, and plugin usage.

## Files
- app.py: FastAPI backend for blog
- models.py: SQLAlchemy models
- schemas.py: Pydantic schemas
- gdpr.py: GDPR export & audit
- requirements.txt: Dependencies
- README.md: Project info

---

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `uvicorn app:app --reload`
3. Access docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## GDPR Features
- Data export endpoint (`/gdpr/export`)
- Consent management
- Audit logging

---

## Example Endpoints
- `POST /users/` - Register user
- `POST /posts/` - Create post
- `GET /posts/` - List posts
- `GET /gdpr/export` - Export user data
