# Run once to create a sample user + data
from sqlmodel import Session
from database import engine
from models import User, Company, Contact, Deal, Task, Activity
from security import get_password_hash

with Session(engine) as session:
    u = User(name='Admin', email='admin@example.com', role='admin', password_hash=get_password_hash('password'))
    session.add(u)
    c1 = Company(name='ACME Corp', website='https://acme.example')
    session.add(c1)
    session.commit()
    session.refresh(u)
    session.refresh(c1)
    contact = Contact(company_id=c1.id, first_name='John', last_name='Doe', email='john@acme.example')
    session.add(contact)
    session.commit()
