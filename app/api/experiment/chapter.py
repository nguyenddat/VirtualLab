from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.chapter import Chapter
from app.database.init_db import get_db

router = APIRouter()

@router.get('')
def get_chapter(db: Session = Depends(get_db)):
    chapters = db.query(Chapter).all()
    return [{"id":c.id, "name":c.name, "book_id":c.book_id} for c in chapters]