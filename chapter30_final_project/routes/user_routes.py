from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import SessionLocal
from schemas.user_schema import UserCreate
from crud.user_crud import create_user, get_users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def add_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


@router.get("/")
def read_users(
    db: Session = Depends(get_db)
):
    return get_users(db)