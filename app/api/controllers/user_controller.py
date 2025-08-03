from sqlalchemy.orm import Session
from app.models.user import User

def is_username_available(username: str, db: Session) -> bool:
    return db.query(User.id).filter(User.username == username).first() is None
