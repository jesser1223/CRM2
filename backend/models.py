from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime, date

class UserBase(SQLModel):
    name: str
    email: str
    role: str = 'sales'

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    deals: List['Deal'] = Relationship(back_populates='owner')

class UserCreate(UserBase):
    password: str

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    website: Optional[str] = None
    industry: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    contacts: List['Contact'] = Relationship(back_populates='company')
    deals: List['Deal'] = Relationship(back_populates='company')

class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_id: Optional[int] = Field(default=None, foreign_key='company.id')
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    title: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    company: Optional[Company] = Relationship(back_populates='contacts')

class Deal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_id: Optional[int] = Field(default=None, foreign_key='company.id')
    contact_id: Optional[int] = Field(default=None, foreign_key='contact.id')
    owner_id: Optional[int] = Field(default=None, foreign_key='user.id')
    name: Optional[str]
    value: Optional[float]
    currency: Optional[str] = 'USD'
    stage: Optional[str] = 'lead'
    close_date: Optional[date]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    company: Optional[Company] = Relationship(back_populates='deals')
    owner: Optional[User] = Relationship(back_populates='deals')

class Activity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    deal_id: Optional[int] = Field(default=None, foreign_key='deal.id')
    contact_id: Optional[int] = Field(default=None, foreign_key='contact.id')
    user_id: Optional[int] = Field(default=None, foreign_key='user.id')
    type: Optional[str]
    notes: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    assigned_to: Optional[int] = Field(default=None, foreign_key='user.id')
    due_date: Optional[date]
    status: str = 'open'
    related_type: Optional[str]
    related_id: Optional[int]
    description: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
