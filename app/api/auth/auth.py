from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.database.init_db import get_db
from app.schemas import LoginRequest

router = APIRouter()

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    username = request.username
    password = request.password

    existed_user = db.query(User).filter(User.username == username).first()
    if not existed_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    if existed_user.password != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    return {
        "id": existed_user.id,
        "role": existed_user.role,
    }


@router.get("/me")
def get_me(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": user.id,
        "username": user.username,
        "role": user.role,  
    }