from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.controllers.user_controller import is_username_available
from app.db.session import get_db


router = APIRouter()

@router.get("/check-username")
def check_username(username: str, db: Session = Depends(get_db)):
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")

    available = is_username_available(username, db)
    return {"available": available}
