from fastapi import FastAPI
from database.connection import engine, Base
from models.user import User

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "SQLAlchemy Database Connected"}