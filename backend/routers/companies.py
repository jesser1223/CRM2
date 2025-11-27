from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Company
from database import engine

router = APIRouter()

@router.get('/')
def list_companies():
    with Session(engine) as session:
        return session.exec(select(Company)).all()

@router.post('/')
def create_company(company: Company):
    with Session(engine) as session:
        session.add(company)
        session.commit()
        session.refresh(company)
        return company

@router.get('/{company_id}')
def get_company(company_id: int):
    with Session(engine) as session:
        company = session.get(Company, company_id)
        if not company:
            raise HTTPException(status_code=404, detail='Not found')
        return company
