from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Activity
from database import engine

router = APIRouter()

@router.get('/')
def list_activities():
    with Session(engine) as session:
        return session.exec(select(Activity)).all()

@router.post('/')
def create_activity(activity: Activity):
    with Session(engine) as session:
        session.add(activity)
        session.commit()
        session.refresh(activity)
        return activity
