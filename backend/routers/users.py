from fastapi import APIRouter
from sqlmodel import Session, select
from models import User
from database import engine

router = APIRouter()

@router.get('/')
def list_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users
