from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from routers import auth, users, companies, contacts, deals, tasks, activities

app = FastAPI(title='CRM Starter')

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(auth.router, prefix='/api/auth')
app.include_router(users.router, prefix='/api/users')
app.include_router(companies.router, prefix='/api/companies')
app.include_router(contacts.router, prefix='/api/contacts')
app.include_router(deals.router, prefix='/api/deals')
app.include_router(tasks.router, prefix='/api/tasks')
app.include_router(activities.router, prefix='/api/activities')
