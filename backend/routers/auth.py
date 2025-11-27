from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from models import User, UserCreate
from database import get_session, engine
from security import verify_password, get_password_hash, create_access_token

router = APIRouter()

@router.post('/register')
def register(user: UserCreate):
    with Session(engine) as session:
        db_user = session.exec(select(User).where(User.email == user.email)).first()
        if db_user:
            raise HTTPException(status_code=400, detail='Email already registered')
        user_obj = User(name=user.name, email=user.email, role=user.role, password_hash=get_password_hash(user.password))
        session.add(user_obj)
        session.commit()
        session.refresh(user_obj)
        return {"id": user_obj.id, "email": user_obj.email}

@router.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.email == form_data.username)).first()
        if not user or not verify_password(form_data.password, user.password_hash):
            raise HTTPException(status_code=401, detail='Incorrect credentials')
        token = create_access_token({"sub": str(user.id), "email": user.email, "role": user.role})
        return {"access_token": token, "token_type": "bearer"}
