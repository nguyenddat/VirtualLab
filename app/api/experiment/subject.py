from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.subject import Subject
from database.init_db import get_db
from schemas.experiment.subject import CreateSubjectRequest

router = APIRouter()


@router.get('')
def get_subject(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    return [{"id":s.id, "name":s.name} for s in subjects]


# @router.post('')
# def create_subject(body: CreateSubjectRequest, db: Session = Depends(get_db)):
#     subject = Subject(name=body.name)
#     if body.description: subject.description = body.description

#     db.add(subject)
#     db.commit()
#     db.refresh(subject)

#     return {"id": subject.id, "name": subject.name}


# @router.put('/{subject_id}')
# def update_subject(subject_id: int, body: CreateSubjectRequest, db: Session = Depends(get_db)):
#     subject = db.query(Subject).filter(Subject.id == subject_id).first()
#     if not subject:
#         raise HTTPException(status_code=404, detail="Subject not found")
    
#     subject.name = body.name
#     if body.description: subject.description = body.description

#     db.commit()
#     db.refresh(subject)

#     return {"id": subject.id, "name": subject.name}


# @router.delete('/{subject_id}')
# def delete_subject(subject_id: int, db: Session = Depends(get_db)):
#     subject = db.query(Subject).filter(Subject.id == subject_id).first()