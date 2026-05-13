from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.connection import SessionLocal, engine, Base
from models.user import User
from schemas.user_schema import UserCreate
from crud.user_crud import create_user, get_users

app = FastAPI()

Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "CRUD Operations Working"}


# Create User
@app.post("/users")
def add_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


# Get All Users
@app.get("/users")
def read_users(
    db: Session = Depends(get_db)
):
    return get_users(db)