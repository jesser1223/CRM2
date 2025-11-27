from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Deal
from database import engine

router = APIRouter()

@router.get('/')
def list_deals():
    with Session(engine) as session:
        return session.exec(select(Deal)).all()

@router.post('/')
def create_deal(deal: Deal):
    with Session(engine) as session:
        session.add(deal)
        session.commit()
        session.refresh(deal)
        return deal

@router.put('/{deal_id}/move-stage')
def move_stage(deal_id: int, stage: str):
    with Session(engine) as session:
        deal = session.get(Deal, deal_id)
        if not deal:
            raise HTTPException(status_code=404)
        deal.stage = stage
        session.add(deal)
        session.commit()
        session.refresh(deal)
        return deal
