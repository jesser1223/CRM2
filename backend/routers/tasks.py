from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Task
from database import engine

router = APIRouter()

@router.get('/')
def list_tasks():
    with Session(engine) as session:
        return session.exec(select(Task)).all()

@router.post('/')
def create_task(task: Task):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
