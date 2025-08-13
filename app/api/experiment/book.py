from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.book import Book
from database.init_db import get_db

router = APIRouter()

@router.get('')
def get_book(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return [{
        "id":b.id, 
        "name":b.name,
        "grade":b.grade,
        "static_file_path":b.static_file_path if b.static_file_path else None,
        "subject_id":b.subject_id,
        "bookset_id":b.bookset_id,
        } for b in books
    ]