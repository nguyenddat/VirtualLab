from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.bookset import BookSet
from database.init_db import get_db

router = APIRouter()

@router.get('')
def get_bookset(db: Session = Depends(get_db)):
    booksets = db.query(BookSet).all()
    return [{
        "id":b.id, 
        "name":b.name, 
        } for b in booksets
    ]