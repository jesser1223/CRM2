from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Contact
from database import engine

router = APIRouter()

@router.get('/')
def list_contacts():
    with Session(engine) as session:
        return session.exec(select(Contact)).all()

@router.post('/')
def create_contact(contact: Contact):
    with Session(engine) as session:
        session.add(contact)
        session.commit()
        session.refresh(contact)
        return contact

@router.get('/{contact_id}')
def get_contact(contact_id: int):
    with Session(engine) as session:
        c = session.get(Contact, contact_id)
        if not c:
            raise HTTPException(status_code=404)
        return c
